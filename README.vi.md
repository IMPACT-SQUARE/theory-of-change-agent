# Theory of Change Agent (Tác nhân Lý thuyết Thay đổi)

[한국어](README.md) · [English](README.en.md) · [日本語](README.ja.md) · **Tiếng Việt**

Đây là công cụ giúp xây dựng cấu trúc kết quả của dự án theo **Lý thuyết Thay đổi (Theory of Change)**.
Chỉ cần trả lời các câu hỏi như đang trò chuyện: với dự án hợp tác phát triển quốc tế, công cụ sẽ tạo
**PDM (Project Design Matrix — Ma trận Thiết kế Dự án)**; với startup tạo tác động xã hội, hoạt động
trách nhiệm xã hội của doanh nghiệp (CSR) hoặc tổ chức phi lợi nhuận, công cụ sẽ tạo **sơ đồ Lý thuyết
Thay đổi**. Công cụ chạy trên các trợ lý AI như Claude.

Mục tiêu là xóa bỏ cảm giác bối rối khi ngồi trước một bảng trống mà không biết bắt đầu từ đâu. Trả lời
từng câu hỏi một, bạn sẽ có một bảng ma trận phù hợp với hướng dẫn PDM của KOICA (Cơ quan Hợp tác Quốc
tế Hàn Quốc). Trả lời bằng ngôn ngữ nào, kết quả sẽ được xuất ra bằng ngôn ngữ đó.

---

## Công cụ giúp gì cho bạn

- Đặt câu hỏi theo dòng chảy của **Lý thuyết Thay đổi** (Đầu vào → Hoạt động → Đầu ra → Kết quả →
  Tác động) và cùng bạn xây dựng chuỗi kết quả.
- Khi hoàn thành, công cụ tạo hai tài liệu: **bảng PDM** và **bảng giám sát (monitoring)**.
- **Kiểm chứng hai lớp xem Kết quả (Outcome) có phải là kết quả thực sự hay không** — ① **kiểm chứng
  logic**: sự thay đổi của đối tượng có khắc phục được nguyên nhân của vấn đề hay không, và ② **đối
  chiếu chỉ số gần nhất** trong **593 chỉ số của IRIS+**, thư viện chỉ số tác động toàn cầu, để tham khảo.
- Trước khi kết thúc, công cụ **tự động kiểm tra** kết quả theo các quy tắc cốt lõi của hướng dẫn
  KOICA, giúp bạn tránh trước những lỗi thường bị nhắc trong thẩm định.

Công cụ hữu ích cho:

- Người lần đầu viết PDM để nộp hồ sơ dự án KOICA
- Người đã có bản nháp và muốn kiểm tra xem có đúng hướng dẫn không
- Người mới chỉ có ý tưởng, chưa định hình cấu trúc kết quả

---

## Bắt đầu như thế nào

Công cụ sẽ hỏi bạn ba điều theo thứ tự.

**(1) Bạn muốn làm gì?** Chọn một trong bốn — **Hợp tác phát triển quốc tế (PDM)** sẽ tạo bảng PDM;
**Startup tạo tác động (phát triển kinh doanh mới)** · **Đóng góp xã hội của doanh nghiệp (CSR, ESG)** ·
**Phi lợi nhuận** sẽ tạo sơ đồ Lý thuyết Thay đổi. Logic bên dưới là như nhau; chỉ khác hình thức của
sản phẩm cuối cùng. (Lựa chọn thứ năm, **Nhà đầu tư tác động (thẩm định đầu tư)**, đang được phát triển.)

Khi bạn đưa vào **tài liệu cấp tổ chức** (kế hoạch kinh doanh, báo cáo thường niên) — thường gặp ở tổ
chức phi lợi nhuận và startup tạo tác động — và công cụ phát hiện nhiều dự án, nó sẽ hỏi bạn muốn xem
**toàn bộ dự án** (sơ đồ kết nối giữa sứ mệnh và các dự án) hay đi sâu vào **một dự án cụ thể**.

**(2) Bạn đang ở giai đoạn nào?**

- **Tôi mới chỉ có ý tưởng** — đã có hình dung về dự án nhưng chưa có tài liệu.
- **Tôi có tài liệu — kế hoạch kinh doanh, bản nháp, PDM sẵn có** — công cụ sẽ đọc và tận dụng chúng.
  (Nếu PDM đã được phê duyệt, bạn có thể chỉ yêu cầu rà soát mà không chỉnh sửa gì.)

**(3) Bạn muốn tiến hành như thế nào?**

- **Trả lời từng câu hỏi một cách kỹ lưỡng** — chi tiết nhất. (Khoảng 10–20 phút từ ý tưởng, 5–10 phút
  từ tài liệu)
- **Tạo bản nháp trước rồi chỉnh sửa** — nhanh nhất (khoảng 2–5 phút). Công cụ tạo ngay một bản nháp
  hoàn chỉnh, bạn sửa những chỗ chưa ưng ý, và khi nói "chốt" (finalize) thì bản nháp sẽ qua bước kiểm
  tra chất lượng để hoàn thành.

---

## Bạn nhận được gì

Khi kết thúc, kết quả được lưu thành các tệp.

- **Bảng PDM (`pdm.md`)**: đúng theo mẫu KOICA — Tác động / Kết quả / Đầu ra / Hoạt động trong bốn cột
  (Tóm tắt, Chỉ số kiểm chứng, Phương tiện kiểm chứng, Giả định quan trọng). Đây là sản phẩm mặc định
  cho dự án hợp tác phát triển quốc tế.
- **Sơ đồ Lý thuyết Thay đổi (`toc.md`)**: sơ đồ nút (node diagram) thể hiện kết nối từ hoạt động đến
  đầu ra, từ đầu ra đến kết quả. Với startup tạo tác động, CSR và phi lợi nhuận, đây là sản phẩm mặc
  định — kèm theo gợi ý về những dữ liệu bạn cần tự thu thập để đo lường tác động sau này.
- **Bảng giám sát (`monitoring.md`)**: với mỗi chỉ số — định nghĩa, công thức tính, giá trị cơ sở, mục
  tiêu, căn cứ, nguồn dữ liệu, thời điểm đo, đơn vị thu thập và tiêu chí phân tách.
- **Dự toán ngân sách (`budget.md`, tùy chọn)**: với dự án hợp tác phát triển quốc tế (PDM), công cụ có
  thể lập thêm bản nháp ngân sách gắn với PDM — hạng mục chi theo từng hoạt động, căn cứ tính toán
  (đơn giá × số lượng × số lần), phân bổ nguồn vốn và chi phí quản lý chung. Mọi phép cộng đều do
  script tính toán và kiểm chứng một cách xác định.

Giá trị cơ sở (baseline) và mục tiêu thường được xác định sau khảo sát thực địa, nên ban đầu được để
trống là "xác định sau (추후 확정)" và có thể điền vào sau.

Các tệp được sắp xếp sao cho **sản phẩm chính (`pdm.md` hoặc `toc.md`) nằm ngay trong `out/`**, còn
bảng giám sát và dữ liệu nguồn nằm trong `out/details/`:

```
out/
├── pdm.md          (hoặc toc.md)   ← sản phẩm chính
└── details/
    ├── monitoring.md
    └── pdm.json    (dữ liệu nguồn để tạo ra các bảng trên)
```

---

## Kiểm tra chất lượng như thế nào

Ngay trước khi hoàn tất, công cụ tự kiểm tra PDM theo các quy tắc cốt lõi của hướng dẫn KOICA. Ví dụ:

- Tác động (Impact) không có chỉ số riêng.
- Đầu ra (Output) được gom lại thành 3–4 mục.
- Mỗi kết quả có 1–2 chỉ số (tối đa 3).
- Mọi chỉ số đều ghi rõ cách đo lường (phương tiện kiểm chứng).
- Mọi hoạt động phải kết nối với một đầu ra, mọi đầu ra phải kết nối với một kết quả — không có nút mồ côi.
- Kết quả được diễn đạt bằng **sự thay đổi hành vi** của đối tượng, không phải mở rộng số lượng.

Các quy tắc bắt buộc sẽ được cùng chỉnh sửa cho đến khi đạt; các quy tắc khuyến nghị (SMART, CREAM,
chỉ số phân tách theo giới, v.v.) được báo cáo dưới dạng điểm số. Danh sách đầy đủ các quy tắc kèm
trích dẫn trang hướng dẫn nằm tại
[`skills/theory-of-change-agent/rules/koica-rules.md`](./skills/theory-of-change-agent/rules/koica-rules.md).

---

## Cài đặt

Nếu bạn thường dùng **ứng dụng Claude desktop hoặc claude.ai**, xem **Cách 3**.
Nếu quen với công cụ dòng lệnh **Claude Code**, **Cách 1** là tiện nhất.

### Cách 1. Plugin Claude Code (tự động cập nhật, khuyến nghị)

Gõ hai dòng sau trong Claude Code:

```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```

Để cập nhật sau này:

```
/plugin marketplace update impact-square
/plugin update theory-of-change-agent
```

### Cách 2. Liên kết trực tiếp (cài nhanh)

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

Cập nhật bằng `git pull`. Để gỡ liên kết, chạy `rm ~/.claude/skills/theory-of-change-agent` — thư mục
gốc vẫn được giữ nguyên.

### Cách 3. Tải lên tệp zip (Claude desktop · Antigravity · claude.ai)

Để dùng **trực tiếp trong ứng dụng** thay vì Claude Code, hãy nén skill thành tệp zip và tải lên.

1. **Tạo tệp zip**: trong thư mục `skills` của repo đã tải về, chạy:
   ```bash
   cd skills
   zip -r theory-of-change-agent.zip theory-of-change-agent \
     -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
   ```
   (Nếu repo đã có sẵn `theory-of-change-agent.zip`, bạn có thể dùng luôn.)

2. **Tải lên** — tùy ứng dụng bạn dùng:
   - **Claude desktop**: `Settings → Skills → Add → Upload`, chọn `theory-of-change-agent.zip` → Bật (Enable).
   - **Antigravity**: tải `theory-of-change-agent.zip` lên trong màn hình Skills.
   - **claude.ai (web)**: `Settings → Capabilities → Skills → Upload`.

   > Điều kiện: ứng dụng Claude cần **gói trả phí + bật tính năng thực thi mã (code execution)**
   > (bước kiểm tra chất lượng chạy bằng python3). Tên menu có thể khác đôi chút tùy phiên bản.

3. **Sử dụng**: gõ vào khung chat, ví dụ "Tạo PDM KOICA bằng Theory of Change Agent".

#### Khi sơ đồ Lý thuyết Thay đổi (Mermaid) không hiển thị trong Antigravity

Sơ đồ trong `out/toc.md` được vẽ bằng **Mermaid `flowchart`**. Antigravity (và VS Code chưa có tiện ích
xem trước Mermaid) mặc định **không kết xuất** khối ```mermaid``` thành hình, nên nó có thể trông như
mã nguồn. Hai cách khắc phục:

- **(Khuyến nghị) Cài tiện ích xem trước Mermaid** — Antigravity thuộc họ VS Code, nên cài
  **`Markdown Preview Mermaid Support`** (nhà phát hành `bierner`, id `bierner.markdown-mermaid`) từ
  chợ tiện ích **Open VSX**, và `toc.md` sẽ hiển thị thành hình. *(Tiện ích phải do bạn tự cài trong
  ứng dụng — skill không thể tự động cài.)*
- **Đọc trực tiếp, không cần cài** — skill luôn xuất **dòng chảy nhân quả dạng văn bản (mũi tên →)**
  với nội dung y hệt ngay bên dưới khối Mermaid, nên logic của dự án vẫn đọc được mà không cần tiện ích.
   Sản phẩm hoàn chỉnh được nhận qua liên kết tải xuống trong chat.

> Skill đã tải lên ứng dụng **không tự động cập nhật**. Khi nội dung thay đổi, hãy tải lên tệp zip mới.
> Nếu cần tự động cập nhật, dùng **Cách 1 (plugin Claude Code)**.

Hướng dẫn chi tiết hơn tại
[`skills/theory-of-change-agent/INSTALL-desktop.md`](./skills/theory-of-change-agent/INSTALL-desktop.md).

### Yêu cầu

- **Claude** (Claude Code, ứng dụng desktop, hoặc web đều được)
- **`python3`**: dùng để chạy kiểm tra chất lượng. Có sẵn mặc định trong môi trường thực thi mã của
  desktop/web.

---

## Chính sách dữ liệu

- Các tệp PDF trong `docs/` của kho lưu trữ này đều là tài liệu công khai (hướng dẫn PDM KOICA, tài
  liệu Theory of Change).
- Dữ liệu mẫu cho kiểm tra chất lượng (`benchmark/`) là các PDM hư cấu đã xóa toàn bộ tên thật và số
  tiền thật — chỉ giữ lại cấu trúc.
- Bản gốc PDM của các dự án thực không được lưu trong kho này; chúng được bảo quản riêng, không công khai.

---

## Cấu trúc thư mục

```
theory-of-change-agent/
├── .claude-plugin/      tệp cấu hình plugin
├── skills/
│   └── theory-of-change-agent/
│       ├── SKILL.md         mô tả toàn bộ quy trình
│       ├── README.md        hướng dẫn sử dụng cấp skill
│       ├── INSTALL-desktop.md  hướng dẫn cài đặt desktop/web
│       ├── prompts/         prompt phỏng vấn và tạo tài liệu
│       ├── rules/           quy tắc KOICA và công cụ kiểm tra tự động
│       ├── schema/          định dạng dữ liệu PDM và ví dụ
│       └── benchmark/       ví dụ hư cấu để kiểm tra chất lượng
├── docs/                tài liệu tham khảo công khai
├── README.md            tài liệu này (tiếng Hàn)
└── LICENSE              giấy phép (MIT)
```

---

## Trạng thái

Phiên bản 1.0 — ba chế độ tiến hành, kiểm tra chất lượng tự động, và phân phối plugin Claude Code.
Tên cũ là "Impact Harness"; đổi tên thành "Theory of Change Agent (변화이론 에이전트)" vào tháng 6 năm 2026.

---

## Giấy phép

[MIT](./LICENSE) © 2026 IMPACT SQUARE
