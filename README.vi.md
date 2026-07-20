# Theory of Change Agent

[English](README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · **Tiếng Việt**

Viết ma trận kết quả nhiều khi còn khó hơn chính việc thiết kế dự án. Bạn hiểu rõ vấn đề, các hoạt
động và kết quả mong muốn, nhưng chuyển tất cả thành một bản PDM mạch lạc lại là một việc khác.

**Theory of Change Agent đồng hành với bạn qua công việc đó bằng hội thoại.** Công cụ hỏi từng câu
một và ghép các câu trả lời thành chuỗi kết quả: vấn đề xã hội → hoạt động → đầu ra → kết quả →
tác động. Với dự án hợp tác phát triển quốc tế, nó tạo **PDM (Project Design Matrix) theo hướng dẫn
KOICA**; với startup tạo tác động, CSR và tổ chức phi lợi nhuận, nó tạo **sơ đồ Lý thuyết Thay đổi**.
Công cụ chạy trên các trợ lý AI như Claude và trả lời bằng ngôn ngữ bạn dùng.

Đây không chỉ là công cụ điền biểu mẫu. Nó chỉ ra những điểm yếu về logic, chẳng hạn một đầu ra
được viết như thể là kết quả. Và các phép kiểm đều có thể truy vết: cổng chất lượng xác định đạt
**18/18 trên benchmark phát hiện lỗi**, mỗi quy tắc đều dẫn **số trang trong hướng dẫn KOICA
(36 trang)**, và mô-đun ngân sách đã tái hiện tổng của hai bảng ngân sách KOICA thực **chính xác
đến từng won**.

**Công cụ này dành cho:**

- **Người viết PDM lần đầu** khi nộp hồ sơ cho KOICA hoặc chương trình tương tự
- **Người đã có bản nháp** và muốn đối chiếu với hướng dẫn trước khi thẩm định
- **Nhà sáng lập, đội CSR và tổ chức phi lợi nhuận** cần làm rõ mô hình tác động ban đầu

## Bắt đầu nhanh

1. Cài đặt skill. Mất khoảng 30 giây.
2. Nói: *"Tạo PDM bằng Theory of Change Agent"*. Bạn cũng có thể đính kèm kế hoạch kinh doanh hoặc báo cáo thường niên.
3. Trả lời các câu hỏi. Khi nội dung đã ổn, nói **"chốt" (finalize)**.
4. Mở kết quả trong `out/`: `pdm.md` cho hợp tác phát triển quốc tế, `toc.md` cho các trường hợp còn lại.

## Chọn lộ trình phù hợp

Cuộc phỏng vấn bắt đầu từ vấn đề, lần theo nguyên nhân, rồi đưa thay đổi mong muốn về dạng đo lường
được. Sản phẩm cuối cùng tùy theo mục đích sử dụng.

| Tình huống | Sản phẩm tạo ra | Tài liệu nên chuẩn bị |
|---|---|---|
| Dự án hợp tác phát triển quốc tế | PDM theo hướng dẫn KOICA | Ý tưởng, đề xuất, hoặc bản nháp PDM |
| Startup tạo tác động hoặc dự án mới | Sơ đồ Lý thuyết Thay đổi | Kế hoạch kinh doanh, hoặc vấn đề cần giải quyết |
| Dự án CSR hoặc ESG | Sơ đồ Lý thuyết Thay đổi | Bản mô tả chương trình hoặc đề xuất |
| Chương trình phi lợi nhuận, báo cáo thường niên | Sơ đồ Lý thuyết Thay đổi | Báo cáo thường niên; chọn xem toàn tổ chức hoặc một dự án |

PDM mới phải qua cổng chất lượng trước khi hoàn tất. Với PDM đã được phê duyệt, chế độ kiểm toán
sẽ rà soát và chỉ báo cáo các điểm khác với hướng dẫn, không chỉnh sửa tài liệu.

## Xem nó hoạt động

```
Bạn:    Tạo PDM bằng Theory of Change Agent.
Agent:  Bạn đang làm dự án gì?
        ① Hợp tác phát triển quốc tế (PDM)  ② Startup tạo tác động
        ③ CSR / ESG                         ④ Phi lợi nhuận
Bạn:    ①. Dự án sức khỏe bà mẹ ở Lào.
Agent:  [Câu 1 · vấn đề xã hội] Dự án này giải quyết vấn đề gì?
        Ai đang gặp khó khăn, và nguyên nhân là gì?
Bạn:    Bà mẹ ở nông thôn sinh con tại nhà. Trạm y tế thì xa,
        và người dân cũng không tin tưởng.
Agent:  Có thể xem đây là một vấn đề xã hội: mang tính cấu trúc, ảnh
        hưởng đến nhiều người, và gây tổn hại thực. Hiện tượng là tỷ lệ
        sinh tại nhà cao; nguyên nhân là khó tiếp cận và thiếu niềm tin
        vào cơ sở y tế. Vậy kết quả nên được đặt như một thay đổi trạng
        thái, ví dụ "nhiều bà mẹ sinh con tại cơ sở y tế hơn" — thay vì
        "tổ chức thêm nhiều buổi tập huấn". Điều này có đúng với thay
        đổi bạn muốn đạt được không?
        …
        [Agent hỏi lần lượt về hoạt động, đầu ra, chỉ số và giả định,
         và nối từng câu trả lời vào chuỗi kết quả.]
        …
Bạn:    chốt
Agent:  ✔ Cổng chất lượng đạt (8/8 quy tắc bắt buộc).
        ⚠ Kết quả 2 đang được viết như một đầu ra mở rộng. "Mở rộng
          đào tạo" đếm số buổi, chứ không phải thay đổi hành vi.
          Gợi ý sửa: …
        ◇ Gợi ý các chỉ số IRIS+ gần nhất cho chỉ số 1-1. Chỉ mang tính
          tham khảo, không phải ánh xạ chính thức.
        Kết quả: out/pdm.md
```

Cuộc phỏng vấn tách bạch hoạt động, đầu ra với thay đổi mà dự án hướng tới. Nhờ vậy, những vấn đề
hội đồng thẩm định thường nêu sẽ lộ ra trước khi nộp hồ sơ, chứ không phải sau.

## Cách hoạt động

**Phỏng vấn → Xây chuỗi kết quả → Kiểm chứng → Cổng chất lượng → Kết xuất.** Mỗi bước kế thừa
kết quả của bước trước.

Cuộc phỏng vấn đi theo phương pháp Lý thuyết Thay đổi. Nó bắt đầu bằng một **vấn đề xã hội** được
định nghĩa rõ: mang tính cấu trúc, ảnh hưởng đến nhiều người, và gây tổn hại thực. Sau đó nó nối
hiện tượng quan sát được với nguyên nhân, và định nghĩa kết quả là những thay đổi giải quyết được
các nguyên nhân đó. Đầu ra và những mô tả lợi ích chung chung không được xem là kết quả.

Với tài liệu cấp tổ chức, như báo cáo thường niên hoặc kế hoạch kinh doanh, agent kiểm tra trước
xem tài liệu nói về một hay nhiều dự án. Bạn có thể xem **toàn bộ tổ chức** như một sơ đồ nối sứ
mệnh với các dự án, hoặc đi sâu vào **một dự án** cụ thể.

| Sản phẩm | Nội dung |
|---|---|
| `pdm.md` | Ma trận PDM 4×4 chuẩn KOICA: Tác động/Kết quả/Đầu ra/Hoạt động × Tóm tắt/Chỉ số/Phương tiện kiểm chứng/Giả định |
| `toc.md` | Sơ đồ Lý thuyết Thay đổi, kèm bản văn bản cho trình xem không hỗ trợ Mermaid, và danh sách dữ liệu cần thu thập để đo tác động sau này |
| `details/monitoring.md` | Kế hoạch đo lường theo từng chỉ số: định nghĩa, công thức, giá trị cơ sở, mục tiêu, nguồn, thời điểm, đơn vị thu thập, phân tách |
| `budget.md` *(tùy chọn)* | Ngân sách gắn với PDM: hạng mục theo hoạt động, căn cứ tính (đơn giá × số lượng × số lần), phân bổ nguồn vốn, tổng theo năm |
| `details/pdm.json` | Dữ liệu nguồn dùng để kết xuất mọi bảng biểu ở trên |

Bạn có thể bắt đầu chỉ bằng hội thoại, hoặc đưa vào PDF và **tệp HWP tiếng Hàn (.hwp/.hwpx)**.
Bộ trích xuất đi kèm không cần thư viện ngoài, nên chạy được cả trong sandbox của ứng dụng.

## Kiểm chứng có thể tự xác nhận

Các phép kiểm được viết thành mã và lưu ngay trong repo này:

- **Cổng chất lượng xác định:** Python thuần thực thi 8 quy tắc bắt buộc của KOICA, gồm không đặt
  chỉ số cho Tác động, 3–4 đầu ra, giới hạn số chỉ số, bắt buộc phương tiện kiểm chứng, không có
  nút mồ côi, và đầu ra viết dạng danh từ. Đạt **độ chính xác phát hiện 18/18** trên
  [benchmark cài lỗi](./skills/theory-of-change-agent/benchmark/).
- **Quy tắc dẫn số trang:** Mọi quy tắc trong
  [`koica-rules.md`](./skills/theory-of-change-agent/rules/koica-rules.md) đều dẫn số trang tương
  ứng trong hướng dẫn PDM chính thức của KOICA.
- **Rà soát kết quả:** Một phép kiểm logic xét xem thay đổi dự kiến có giải quyết được nguyên nhân
  gốc hay không. Các chỉ số kết quả cũng được đối chiếu với chỉ số gần nhất trong **593 chỉ số tác
  động IRIS+**. Chỉ mang tính tham khảo, không phải ánh xạ chính thức.
- **Tính toán ngân sách bằng script:** Script tính và kiểm chứng mọi tổng, tỷ lệ, phân bổ nguồn vốn
  và trần chi phí quản lý chung. Qua ba vòng kiểm chứng với hai bảng ngân sách KOICA thực, nó tái
  hiện tổng chính xác đến từng won và phát hiện ba lỗi quy tắc, sau đó đã được sửa.
- **Quy tắc khuyến nghị:** SMART, CREAM và chỉ số phân tách theo giới chỉ được chấm điểm, không ép
  buộc. Bạn quyết định có áp dụng hay không.

## Cài đặt: 30 giây

**Yêu cầu:** Claude Code, Claude desktop hoặc claude.ai, cùng với `python3`. Sandbox thực thi mã
của bản desktop và web đã có sẵn Python.

### Claude Code (tự động cập nhật, khuyến nghị)

```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```

Cập nhật sau bằng `/plugin update theory-of-change-agent`.

### Claude desktop · Antigravity · claude.ai (tải lên zip)

1. Nén skill thành zip. Nếu đã có sẵn `theory-of-change-agent.zip` thì dùng luôn.
   ```bash
   cd skills && zip -r theory-of-change-agent.zip theory-of-change-agent \
     -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
   ```
2. Tải tệp lên: **Claude desktop** tại `Settings → Skills → Add → Upload`, **Antigravity** trong màn
   hình Skills, **claude.ai** tại `Settings → Capabilities → Skills → Upload`. Cần gói trả phí và
   bật tính năng thực thi mã.
3. Gõ vào chat: *"Tạo PDM KOICA bằng Theory of Change Agent"*.

> Skill tải lên ứng dụng không tự cập nhật. Khi có thay đổi, hãy tải lên tệp zip mới. Nếu sơ đồ
> Mermaid hiển thị như mã trong Antigravity, cài `bierner.markdown-mermaid` từ Open VSX, hoặc đọc
> bản văn bản đi kèm. Chi tiết:
> [`INSTALL-desktop.md`](./skills/theory-of-change-agent/INSTALL-desktop.md).

### Git (liên kết trực tiếp)

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

## Chính sách dữ liệu

- `docs/` chỉ chứa tài liệu công khai (hướng dẫn PDM KOICA, tài liệu Theory of Change).
- PDM trong `benchmark/` là dữ liệu hư cấu: giữ cấu trúc của bản gốc nhưng bỏ tên thật và số tiền thật.
- Bản gốc PDM và ngân sách của dự án thực không bao giờ được lưu trong repo này.

## Cấu trúc repo

```
theory-of-change-agent/
├── .claude-plugin/          cấu hình plugin
├── skills/theory-of-change-agent/
│   ├── SKILL.md             quy trình đầy đủ
│   ├── prompts/             prompt phỏng vấn và kết xuất
│   ├── rules/               quy tắc KOICA + bộ kiểm chứng xác định (cổng, ngân sách, HWP)
│   ├── schema/              schema pdm.json và ví dụ tham chiếu
│   └── benchmark/           fixture cài lỗi (18/18)
├── docs/                    tài liệu tham khảo công khai
└── README.md                README tiếng Anh (tài liệu này: README.vi.md)
```

## Trạng thái

Phiên bản 1.0 hỗ trợ hợp tác phát triển quốc tế, startup tạo tác động, CSR·ESG và tổ chức phi lợi
nhuận. Bao gồm ba chế độ tiến hành, cổng chất lượng xác định, mô-đun ngân sách, đầu vào HWP và phân
phối plugin. Chế độ thẩm định cho nhà đầu tư tác động đang được lên kế hoạch. Dự án đổi tên từ
"Impact Harness" vào tháng 6 năm 2026.

## Giấy phép

[MIT](./LICENSE) © 2026 IMPACT SQUARE.
