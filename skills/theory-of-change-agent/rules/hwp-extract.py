#!/usr/bin/env python3
"""hwp-extract.py — extract plain text from .hwp / .hwpx, pure Python stdlib only.

Why this exists: mode-B inputs (사업계획서/기존 PDM) often arrive as 한글 .hwp files, which
Claude cannot read natively. This runs anywhere python3 runs — including the Claude
desktop / claude.ai / Antigravity code-execution sandbox where npm/hwpjs is unavailable.
(Richer conversion — tables/images to Markdown — is the @ohah/hwpjs route; see the skill's
HWP routing note. This script is the dependency-free fallback that always works.)

Usage:
  python3 rules/hwp-extract.py input.hwp            # text to stdout
  python3 rules/hwp-extract.py input.hwpx -o out.txt

Formats:
  .hwpx — HWP 2014+ OWPML: a zip of XML → full text via zipfile + ElementTree (stdlib).
  .hwp  — HWP 5.x binary: CFB(OLE) container → BodyText/Section* records (zlib-compressed),
          HWPTAG_PARA_TEXT(67) UTF-16LE runs. Falls back to the PrvText preview stream.

Exit codes: 0 ok · 1 error/corrupt · 2 usage · 3 unsupported (password-encrypted /
distribution-only document with no readable text) — caller should ask for a PDF instead.
"""
import io, struct, sys, zipfile, zlib
import xml.etree.ElementTree as ET

# ---------------------------------------------------------------- hwpx (zip+XML)

def extract_hwpx(path):
    out = []
    with zipfile.ZipFile(path) as z:
        sections = sorted(n for n in z.namelist()
                          if n.startswith("Contents/section") and n.endswith(".xml"))
        if not sections:
            raise ValueError("no Contents/section*.xml — not a valid hwpx?")
        for name in sections:
            root = ET.fromstring(z.read(name))
            for para in root.iter():
                if para.tag.split("}")[-1] != "p":  # <hp:p> paragraphs
                    continue
                runs = [t.text for t in para.iter()
                        if t.tag.split("}")[-1] == "t" and t.text]
                if runs:
                    out.append("".join(runs))
    return "\n".join(out)

# ---------------------------------------------------------------- hwp 5.x (CFB)

ENDOFCHAIN = 0xFFFFFFFE
FREESECT = 0xFFFFFFFF

class CFB:
    """Minimal read-only Compound File Binary parser (stdlib only)."""

    def __init__(self, data):
        if data[:8] != b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":
            raise ValueError("not a CFB/OLE file")
        self.data = data
        self.ssz = 1 << struct.unpack_from("<H", data, 30)[0]          # sector size
        self.mssz = 1 << struct.unpack_from("<H", data, 32)[0]         # mini sector
        self.first_dir = struct.unpack_from("<I", data, 48)[0]
        self.mini_cutoff = struct.unpack_from("<I", data, 56)[0]
        first_minifat = struct.unpack_from("<I", data, 60)[0]
        n_minifat = struct.unpack_from("<I", data, 64)[0]
        first_difat = struct.unpack_from("<I", data, 68)[0]
        n_difat = struct.unpack_from("<I", data, 72)[0]
        # FAT sector list: 109 in header + DIFAT chain
        fat_secs = [s for s in struct.unpack_from("<109I", data, 76) if s != FREESECT]
        sec = first_difat
        for _ in range(n_difat):
            if sec in (ENDOFCHAIN, FREESECT):
                break
            raw = self._sector(sec)
            entries = struct.unpack(f"<{self.ssz // 4}I", raw)
            fat_secs += [s for s in entries[:-1] if s != FREESECT]
            sec = entries[-1]
        fat = []
        for s in fat_secs:
            fat += struct.unpack(f"<{self.ssz // 4}I", self._sector(s))
        self.fat = fat
        # miniFAT
        minifat = []
        for s in self._chain(first_minifat) if n_minifat else []:
            minifat += struct.unpack(f"<{self.ssz // 4}I", self._sector(s))
        self.minifat = minifat
        # directory entries
        self.dir = []
        for s in self._chain(self.first_dir):
            raw = self._sector(s)
            for off in range(0, self.ssz, 128):
                e = raw[off:off + 128]
                nlen = struct.unpack_from("<H", e, 64)[0]
                name = e[:max(0, nlen - 2)].decode("utf-16-le", "ignore") if nlen >= 2 else ""
                self.dir.append({
                    "name": name, "type": e[66],
                    "left": struct.unpack_from("<I", e, 68)[0],
                    "right": struct.unpack_from("<I", e, 72)[0],
                    "child": struct.unpack_from("<I", e, 76)[0],
                    "start": struct.unpack_from("<I", e, 116)[0],
                    "size": struct.unpack_from("<Q", e, 120)[0],
                })
        root = self.dir[0]
        self.ministream = self._read_fat_chain(root["start"], root["size"])

    def _sector(self, n):
        return self.data[self.ssz * (n + 1): self.ssz * (n + 2)]

    def _chain(self, start, fat=None):
        fat = self.fat if fat is None else fat
        out, s, seen = [], start, set()
        while s not in (ENDOFCHAIN, FREESECT) and s < len(fat) and s not in seen:
            seen.add(s)
            out.append(s)
            s = fat[s]
        return out

    def _read_fat_chain(self, start, size):
        buf = b"".join(self._sector(s) for s in self._chain(start))
        return buf[:size]

    def read_stream(self, entry):
        if entry["size"] < self.mini_cutoff and entry is not self.dir[0]:
            secs = self._chain(entry["start"], self.minifat)
            buf = b"".join(self.ministream[self.mssz * s: self.mssz * (s + 1)] for s in secs)
            return buf[:entry["size"]]
        return self._read_fat_chain(entry["start"], entry["size"])

    def tree_children(self, entry_id):
        """All entries under a storage's child red-black tree."""
        out, stack = [], [self.dir[entry_id]["child"]]
        while stack:
            i = stack.pop()
            if i == FREESECT or i >= len(self.dir):
                continue
            e = self.dir[i]
            out.append(e)
            stack += [e["left"], e["right"]]
            if e["type"] == 1:  # nested storage
                stack.append(e["child"])
        return out

    def find(self, name, entries=None):
        for e in (entries if entries is not None else self.dir):
            if e["name"] == name:
                return e
        return None


# HWP 5.x control-character widths inside PARA_TEXT (code units, incl. the char itself)
_EXTENDED = {1, 2, 3, 11, 12, 14, 15, 16, 17, 18, 21, 22, 23}  # 8 units
_INLINE = {4, 5, 6, 7, 8, 9, 19, 20}                            # 8 units

def _para_text(payload):
    units = struct.unpack(f"<{len(payload) // 2}H", payload[:len(payload) // 2 * 2])
    chars, i = [], 0
    while i < len(units):
        u = units[i]
        if u == 13 or u == 10:
            chars.append("\n"); i += 1
        elif u < 32:
            i += 8 if (u in _EXTENDED or u in _INLINE) else 1
        else:
            chars.append(struct.pack("<H", u)); i += 1
    # join: decode UTF-16 runs (handles surrogate pairs), keep newlines
    out, run = [], []
    for c in chars:
        if c == "\n":
            if run:
                out.append(b"".join(run).decode("utf-16-le", "ignore")); run = []
            out.append("\n")
        else:
            run.append(c)
    if run:
        out.append(b"".join(run).decode("utf-16-le", "ignore"))
    return "".join(out)


def _records_text(data):
    """Walk HWP record stream; collect HWPTAG_PARA_TEXT (67) payloads."""
    texts, pos = [], 0
    while pos + 4 <= len(data):
        (hdr,) = struct.unpack_from("<I", data, pos)
        tag, size = hdr & 0x3FF, (hdr >> 20) & 0xFFF
        pos += 4
        if size == 0xFFF:
            (size,) = struct.unpack_from("<I", data, pos)
            pos += 4
        if tag == 67:  # HWPTAG_PARA_TEXT
            t = _para_text(data[pos:pos + size])
            if t.strip():
                texts.append(t.rstrip("\n"))
        pos += size
    return texts


def extract_hwp(path):
    cfb = CFB(open(path, "rb").read())
    fh = cfb.find("FileHeader")
    if fh is None:
        raise ValueError("no FileHeader stream — not an HWP 5.x file")
    header = cfb.read_stream(fh)
    if not header.startswith(b"HWP Document File"):
        raise ValueError("bad HWP signature")
    flags = struct.unpack_from("<I", header, 36)[0]
    compressed, encrypted, distribution = flags & 1, flags & 2, flags & 4
    if encrypted:
        print("password-encrypted HWP — cannot extract; ask for a PDF export instead",
              file=sys.stderr)
        sys.exit(3)

    texts = []
    body = cfb.find("BodyText")
    if body and not distribution:
        sections = sorted((e for e in cfb.tree_children(cfb.dir.index(body))
                           if e["name"].startswith("Section")),
                          key=lambda e: int(e["name"][7:] or 0))
        for sec in sections:
            raw = cfb.read_stream(sec)
            if compressed:
                try:
                    raw = zlib.decompress(raw, -15)
                except zlib.error:
                    continue
            texts += _records_text(raw)
    if not texts:  # distribution doc or empty body → PrvText preview fallback
        prv = cfb.find("PrvText")
        if prv is not None and prv["size"]:
            t = cfb.read_stream(prv).decode("utf-16-le", "ignore").strip("\x00").strip()
            if t:
                texts.append("[미리보기 텍스트(PrvText) — 전문이 아닐 수 있음]\n" + t)
    if not texts:
        print("no readable text (배포용/보호 문서?) — ask for a PDF export instead",
              file=sys.stderr)
        sys.exit(3)
    return "\n".join(texts)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    out_path = None
    if "-o" in sys.argv:
        out_path = sys.argv[sys.argv.index("-o") + 1]
        args = [a for a in args if a != out_path]
    if not args:
        print(__doc__, file=sys.stderr)
        return 2
    path = args[0]
    try:
        if zipfile.is_zipfile(path):
            text = extract_hwpx(path)
        else:
            text = extract_hwp(path)
    except SystemExit:
        raise
    except Exception as e:
        print(f"extract failed: {e}", file=sys.stderr)
        return 1
    if out_path:
        open(out_path, "w", encoding="utf-8").write(text)
        print(f"wrote {out_path} ({len(text)} chars)")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
