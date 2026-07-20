# Theory of Change Agent

[English](README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · **Tiếng Việt**

Bất kỳ người làm tác động xã hội nào cũng biết khoảnh khắc ấy: một ma trận kết quả trống trên màn
hình, hạn nộp hồ sơ trước mắt — và không biết bắt đầu từ ô nào. Logic nằm trong đầu bạn, nhưng biểu
mẫu không chịu tiếp nhận nó.

**Theory of Change Agent là một AI phỏng vấn giúp rút logic đó ra.** Trả lời từng câu hỏi một, bằng
ngôn ngữ tự nhiên, và nó xây dựng chuỗi kết quả — vấn đề xã hội → hoạt động → đầu ra → kết quả →
tác động — rồi kết xuất thành **PDM (Project Design Matrix) theo hướng dẫn KOICA** cho dự án hợp
tác phát triển quốc tế, hoặc **sơ đồ Lý thuyết Thay đổi** cho startup tạo tác động, CSR và tổ chức
phi lợi nhuận. Công cụ chạy trên các trợ lý AI như Claude và trả lời bằng ngôn ngữ bạn dùng.

Nó không chỉ điền ô. Nó phản biện — "đó là đầu ra được mở rộng, không phải kết quả" — và nó chứng
minh công việc của mình: cổng chất lượng xác định đạt **18/18 trên benchmark phát hiện lỗi**, mọi
quy tắc đều kèm **trích dẫn số trang từ hướng dẫn KOICA 36 trang**, và mô-đun ngân sách đã tái hiện
hai bảng ngân sách KOICA thực **chính xác đến từng won**.

**Dành cho ai:**

- **Người viết PDM lần đầu** nộp hồ sơ KOICA hoặc chương trình tương tự — câu hỏi có cấu trúc thay vì biểu mẫu trống
- **Người đã có bản nháp** muốn đối chiếu với hướng dẫn trước khi hội đồng thẩm định nhìn thấy
- **Nhà sáng lập và đội CSR/phi lợi nhuận** mới chỉ có ý tưởng, cần logic tác động trên một trang

## Bắt đầu nhanh

1. Cài đặt (30 giây — xem bên dưới)
2. Nói: *"Tạo PDM bằng Theory of Change Agent"* — hoặc đính kèm kế hoạch kinh doanh / báo cáo thường niên
3. Trả lời các câu hỏi. Nói **"chốt" (finalize)** khi đã ưng ý.
4. Mở `out/pdm.md`. Bạn sẽ biết ngay công cụ này có dành cho mình không.

## Xem nó hoạt động

```
Bạn:    Tạo PDM bằng Theory of Change Agent.
Agent:  Bạn đang làm dự án gì?
        ① Hợp tác phát triển quốc tế (PDM)  ② Startup tạo tác động
        ③ CSR / ESG                         ④ Phi lợi nhuận
Bạn:    ① — dự án sức khỏe bà mẹ ở Lào.
Agent:  [Câu 1 · vấn đề xã hội] Dự án này giải quyết vấn đề gì —
        ai đang chịu thiệt, và nguyên nhân là gì?
Bạn:    Bà mẹ nông thôn sinh con tại nhà. Trạm y tế thì xa,
        và người dân không tin tưởng.
Agent:  Đây đúng là một vấn đề xã hội (mang tính cấu trúc · ảnh hưởng
        số đông · gây tổn hại thực). Hiện tượng: tỷ lệ sinh tại nhà cao.
        Nguyên nhân: thiếu tiếp cận và niềm tin vào cơ sở y tế. Vậy kết
        quả cần nhắm tới là một thay đổi trạng thái: "thực hành sinh tại
        cơ sở y tế được duy trì" — chứ không phải "tăng số buổi tập
        huấn." Giữ khung này chứ?
        …
        [từng câu một: hoạt động → đầu ra → chỉ số → giả định —
         mỗi câu trả lời được nối vào chuỗi kết quả]
        …
Bạn:    chốt
Agent:  ✔ Cổng chất lượng đạt (8/8 quy tắc bắt buộc).
        ⚠ Kết quả 2 đọc như đầu ra được mở rộng — "mở rộng đào tạo"
          đếm số buổi, không phải thay đổi hành vi. Gợi ý sửa: …
        ◇ Gợi ý chỉ số IRIS+ gần nhất cho chỉ số 1-1
          (chỉ để tham khảo, không phải ánh xạ chính thức).
        Kết quả cuối: out/pdm.md
```

Agent lắng nghe *nỗi đau*, gọi tên nguyên nhân, và từ chối để đầu ra giả dạng kết quả. Đúng cái
chỉnh sửa mà hội đồng thẩm định luôn yêu cầu — nhưng xảy ra trước khi nộp, không phải sau.

## Cách hoạt động

**Phỏng vấn → Xây chuỗi kết quả → Kiểm chứng → Cổng chất lượng → Kết xuất.** Mỗi bước nối tiếp
bước sau.

Cuộc phỏng vấn đi theo Lý thuyết Thay đổi: neo vào một **vấn đề xã hội** được định nghĩa đúng
(mang tính cấu trúc · ảnh hưởng số đông · gây tổn hại thực), truy vết hiện tượng → nguyên nhân, và
yêu cầu mọi kết quả phải là **thay đổi trạng thái khắc phục nguyên nhân** — không phải đầu ra mở
rộng, không phải lợi ích chung chung. Tài liệu cấp tổ chức (báo cáo thường niên của tổ chức phi lợi
nhuận, kế hoạch kinh doanh của startup) đi qua bước phát hiện dự án: xem **toàn bộ dự án** (sơ đồ
kết nối sứ mệnh ↔ các dự án) hoặc đi sâu vào **một dự án cụ thể**.

| Sản phẩm | Nội dung |
|---|---|
| `pdm.md` | Ma trận PDM 4×4 chuẩn KOICA — Tác động/Kết quả/Đầu ra/Hoạt động × Tóm tắt/Chỉ số/Phương tiện kiểm chứng/Giả định |
| `toc.md` | Sơ đồ nút Lý thuyết Thay đổi (kèm dòng chảy nhân quả dạng văn bản cho trình xem không hỗ trợ Mermaid) + dữ liệu bạn cần bắt đầu thu thập ngay để đo tác động sau này |
| `monitoring.md` | Kế hoạch đo lường theo từng chỉ số: định nghĩa, công thức, cơ sở, mục tiêu, nguồn, thời điểm, đơn vị thu thập, phân tách |
| `budget.md` *(tùy chọn)* | Ngân sách gắn với PDM: hạng mục theo hoạt động, căn cứ tính (đơn giá × số lượng × số lần), phân bổ nguồn vốn, tổng theo năm |
| `details/pdm.json` | Nguồn dữ liệu duy nhất — mọi bảng trên đều được kết xuất từ đây |

Đầu vào: hội thoại thường, PDF, và **tệp HWP tiếng Hàn (.hwp/.hwpx)** — bộ trích xuất đi kèm không
cần thư viện ngoài, nên chạy được cả trong sandbox của ứng dụng.

## Kiểm chứng bạn có thể tự xác nhận

Không có chuyện "hãy tin AI." Các phép kiểm là mã nguồn, và bằng chứng nằm trong repo:

- **Cổng chất lượng xác định** — 8 quy tắc bắt buộc của KOICA (Tác động không có chỉ số riêng, 3–4
  đầu ra, giới hạn số chỉ số, bắt buộc phương tiện kiểm chứng, không nút mồ côi, đầu ra dạng danh
  từ…) được thực thi bằng Python thuần. **Độ chính xác phát hiện 18/18** trên benchmark cài lỗi tại
  [`benchmark/`](./skills/theory-of-change-agent/benchmark/).
- **Quy tắc kèm trích dẫn trang** — mọi quy tắc trong
  [`koica-rules.md`](./skills/theory-of-change-agent/rules/koica-rules.md) đều trích dẫn số trang
  trong hướng dẫn PDM chính thức của KOICA — hãy tranh luận với nguồn gốc, không phải với chúng tôi.
- **Kiểm chứng kết quả hai lớp** — kiểm tra logic (thay đổi có khắc phục nguyên nhân không?) + đối
  chiếu chỉ số gần nhất trong **593 chỉ số IRIS+**, thư viện chỉ số tác động toàn cầu (tham khảo,
  © GIIN).
- **Tính toán ngân sách do script làm, AI không bao giờ** — mọi tổng, tỷ lệ, phân bổ và trần chi phí
  quản lý chung được tính và kiểm chứng một cách xác định. Đã kiểm chứng 3 vòng với 2 bảng ngân
  sách KOICA thực: tái hiện tổng **chính xác đến từng won**, và quá trình này còn phát hiện (và
  sửa) 3 lỗi quy tắc thật.
- Quy tắc khuyến nghị (SMART, CREAM, chỉ số phân tách theo giới) chỉ được chấm điểm, không ép buộc —
  quyền quyết định vẫn ở bạn.

## Cài đặt — 30 giây

**Yêu cầu:** Claude (Claude Code, ứng dụng desktop, hoặc claude.ai) · `python3` (có sẵn trong
sandbox thực thi mã của desktop/web)

### Claude Code (tự động cập nhật, khuyến nghị)

```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```

Cập nhật sau bằng `/plugin update theory-of-change-agent`.

### Claude desktop · Antigravity · claude.ai (tải lên zip)

1. Nén skill thành zip (hoặc dùng `theory-of-change-agent.zip` có sẵn):
   ```bash
   cd skills && zip -r theory-of-change-agent.zip theory-of-change-agent \
     -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
   ```
2. Tải lên: **Claude desktop** `Settings → Skills → Add → Upload` · **Antigravity** màn hình Skills ·
   **claude.ai** `Settings → Capabilities → Skills → Upload`. Cần gói trả phí + bật thực thi mã.
3. Gõ vào chat: *"Tạo PDM KOICA bằng Theory of Change Agent"*.

> Skill tải lên ứng dụng không tự cập nhật — tải lại zip mới khi có thay đổi. Chi tiết, gồm cách
> khắc phục khi sơ đồ Mermaid hiển thị như mã trong Antigravity (cài `bierner.markdown-mermaid` từ
> Open VSX, hoặc đọc dòng chảy văn bản đi kèm):
> [`INSTALL-desktop.md`](./skills/theory-of-change-agent/INSTALL-desktop.md).

### Git (liên kết trực tiếp)

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

## Chính sách dữ liệu

- `docs/` chỉ chứa tài liệu công khai (hướng dẫn PDM KOICA, tài liệu Theory of Change).
- PDM trong `benchmark/` là hư cấu — đã xóa tên thật và số tiền thật, chỉ giữ cấu trúc.
- Bản gốc PDM và ngân sách của dự án thực không bao giờ được lưu trong repo này.

## Cấu trúc repo

```
theory-of-change-agent/
├── .claude-plugin/          cấu hình plugin
├── skills/theory-of-change-agent/
│   ├── SKILL.md             quy trình đầy đủ
│   ├── prompts/             prompt phỏng vấn & kết xuất
│   ├── rules/               quy tắc KOICA + bộ kiểm chứng xác định (cổng, ngân sách, HWP)
│   ├── schema/              schema pdm.json và ví dụ tham chiếu
│   └── benchmark/           fixture cài lỗi (18/18)
├── docs/                    tài liệu tham khảo công khai
└── README.md                README tiếng Anh (tài liệu này: README.vi.md)
```

## Trạng thái

v1.0 — 4 trường hợp sử dụng (hợp tác phát triển quốc tế / startup tạo tác động / CSR·ESG / phi lợi
nhuận), 3 chế độ tiến hành, cổng chất lượng xác định, mô-đun ngân sách, đầu vào HWP, phân phối
plugin. Chế độ nhà đầu tư tác động (thẩm định) đang được phát triển. Tên cũ: "Impact Harness"
(đổi tên tháng 6/2026).

## Giấy phép

[MIT](./LICENSE) © 2026 IMPACT SQUARE. Miễn phí mãi mãi. Hãy xây dựng lý thuyết thay đổi của bạn.
