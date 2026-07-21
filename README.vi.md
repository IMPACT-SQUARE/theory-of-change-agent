# Theory of Change Agent

[English](README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · **Tiếng Việt**

Bạn có thể hiểu rõ dự án của mình nhưng vẫn khó chuyển nó thành PDM với câu chữ, chỉ số và giả định
rõ ràng. Theory of Change Agent hỗ trợ công việc đó bằng một cuộc trao đổi có cấu trúc.

Mỗi lần công cụ chỉ hỏi một việc. Từ câu trả lời của bạn, nó kết nối vấn đề xã hội, hoạt động, đầu ra,
kết quả và tác động thành một chuỗi kết quả. Dự án hợp tác phát triển quốc tế nhận **PDM theo hướng dẫn
PDM**. Startup tạo tác động, CSR và tổ chức phi lợi nhuận nhận **sơ đồ Theory of Change**. Công cụ
hoạt động trên các môi trường AI như Claude và trả lời bằng ngôn ngữ bạn đang dùng.

## Phù hợp khi nào

- Bạn lần đầu lập PDM cho dự án hợp tác phát triển quốc tế
- Bạn muốn kiểm tra bản nháp trước khi gửi thẩm định
- Bạn muốn sắp xếp ý tưởng dự án thành một logic tác động rõ ràng

## Bắt đầu nhanh

1. Cài skill theo hướng dẫn bên dưới.
2. Nhập *"Tạo PDM bằng Theory of Change Agent"*. Bạn cũng có thể đính kèm kế hoạch kinh doanh hoặc báo cáo thường niên.
3. Trả lời câu hỏi và nói **"chốt"** khi nội dung đã đúng.
4. Mở `out/`. Dự án hợp tác phát triển quốc tế tạo `pdm.md`; các trường hợp khác tạo `toc.md`.

## Chọn đúng đầu ra

| Tình huống | Kết quả | Tài liệu để bắt đầu |
|---|---|---|
| Hợp tác phát triển quốc tế | PDM | Ý tưởng, đề xuất hoặc PDM hiện có |
| Startup tạo tác động, dự án mới | Sơ đồ Theory of Change | Kế hoạch kinh doanh hoặc vấn đề cần giải quyết |
| CSR, ESG | Sơ đồ Theory of Change | Mô tả chương trình hoặc đề xuất |
| Chương trình phi lợi nhuận | Sơ đồ Theory of Change | Báo cáo thường niên hoặc tài liệu chương trình |

PDM mới được kiểm tra cấu trúc trước khi chốt. Với PDM đã phê duyệt, chế độ kiểm toán chỉ báo các điểm
khác hướng dẫn và không thay đổi tài liệu.

## Ví dụ hội thoại

```
Bạn:    Tạo PDM bằng Theory of Change Agent.
Agent:  Dự án của bạn thuộc loại nào?
        ① Hợp tác phát triển quốc tế  ② Startup tạo tác động
        ③ CSR, ESG                   ④ Phi lợi nhuận
Bạn:    ① Dự án sức khỏe bà mẹ ở Lào.
Agent:  Dự án muốn giải quyết vấn đề gì? Ai đang gặp khó khăn và vì sao?
Bạn:    Phụ nữ nông thôn sinh con tại nhà. Trạm y tế xa và người dân không tin tưởng.
Agent:  Vấn đề trực tiếp là tỷ lệ sinh tại nhà cao. Nguyên nhân có thể là khả năng tiếp cận
        và niềm tin vào cơ sở y tế. Kết quả có thể viết là "nhiều phụ nữ sinh tại cơ sở y tế hơn".
        "Tăng số buổi đào tạo" phù hợp hơn với hoạt động hoặc đầu ra. Có đúng hướng không?
        …
Bạn:    chốt
Agent:  ✔ Đã qua 8 quy tắc bắt buộc.
        ⚠ "Mở rộng đào tạo" ở kết quả 2 đang mô tả số lượng hoạt động. Hãy nêu thay đổi hành vi.
        Kết quả: out/pdm.md
```

## Cách hoạt động

Quy trình gồm **phỏng vấn → xây chuỗi kết quả → rà soát → kiểm tra → xuất tài liệu**.

Công cụ bắt đầu bằng việc xác định vấn đề xã hội có tính cấu trúc, ảnh hưởng đến nhiều người và gây tổn
hại thực. Sau đó nó phân biệt hiện tượng với nguyên nhân, rồi xác định kết quả là thay đổi có thể tác
động vào nguyên nhân. Mở rộng hoạt động hoặc lợi ích chung chung không được xem là kết quả.

Với tài liệu cấp tổ chức như báo cáo thường niên, bạn có thể chọn sơ đồ cho toàn bộ tổ chức hoặc đi sâu
vào một dự án cụ thể.

| Tệp | Nội dung |
|---|---|
| `pdm.md` | Ma trận PDM 4×4 |
| `toc.md` | Sơ đồ Theory of Change kèm phiên bản văn bản cho nơi không hỗ trợ Mermaid |
| `details/monitoring.md` | Kế hoạch đo lường: định nghĩa, công thức, cơ sở, mục tiêu, nguồn, thời điểm và người thu thập |
| `budget.md` | Ngân sách theo hoạt động, căn cứ tính, phân bổ vốn và tổng theo năm. Tùy chọn |
| `details/toc.json` | Dữ liệu gốc dùng để tạo các tệp trên |

Bạn có thể bắt đầu bằng hội thoại, PDF hoặc tệp HWP tiếng Hàn (`.hwp`, `.hwpx`). Bộ trích xuất HWP
không cần thư viện ngoài nên dùng được trong môi trường thực thi mã của ứng dụng.

## Các kiểm tra có thể xác nhận

- **Cổng chất lượng xác định:** Python thuần kiểm tra 8 quy tắc cấu trúc quan trọng, gồm chỉ số tác động, số đầu ra, phương tiện kiểm chứng và nút mồ côi. [Benchmark](./skills/theory-of-change-agent/benchmark/) phát hiện đủ 18 vi phạm.
- **Rà soát kết quả:** Công cụ kiểm tra kết quả có xử lý nguyên nhân hay không và gợi ý chỉ số gần với 593 chỉ số IRIS+ để tham khảo. Đây không phải ánh xạ chính thức.
- **Tính ngân sách:** Script tính và kiểm tra tổng, tỷ lệ, phân bổ vốn và trần chi phí quản lý, đã được kiểm chứng với các bảng ngân sách thực tế.
- **Quy tắc khuyến nghị:** SMART, CREAM và chỉ số phân tách giới tính chỉ được chấm điểm. Bạn tự quyết định có dùng hay không.

## Cài đặt

**Cần có:** Claude Code, Claude desktop hoặc claude.ai cùng với `python3`. Môi trường thực thi mã trên desktop và web đã có Python.

### Claude Code

```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```

Cập nhật bằng `/plugin update theory-of-change-agent`.

### Claude desktop, Antigravity, claude.ai

1. Nén skill thành zip hoặc dùng `theory-of-change-agent.zip` có sẵn.
   ```bash
   cd skills && zip -r theory-of-change-agent.zip theory-of-change-agent \
     -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
   ```
2. Tải lên tại `Settings → Skills → Add → Upload` trên Claude desktop, màn hình Skills của Antigravity, hoặc `Settings → Capabilities → Skills → Upload` trên claude.ai. Cần gói trả phí có thực thi mã.
3. Nhập *"Tạo PDM bằng Theory of Change Agent"* vào chat.

> Skill tải lên ứng dụng không tự cập nhật. Hãy tải lại zip sau khi thay đổi. Nếu Mermaid hiện thành mã trong Antigravity, cài `bierner.markdown-mermaid` từ Open VSX hoặc đọc phiên bản văn bản. Xem [INSTALL-desktop.md](./skills/theory-of-change-agent/INSTALL-desktop.md).

### Git

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

## Chính sách dữ liệu

- `docs/` chỉ chứa tài liệu công khai, gồm tài liệu tham khảo Theory of Change.
- PDM trong `benchmark/` là tình huống hư cấu, không có tên hoặc số tiền thật.
- PDM và ngân sách của dự án thực không được lưu trong kho này.

## Trạng thái

Phiên bản 1.0 hỗ trợ hợp tác phát triển quốc tế, startup tạo tác động, CSR, ESG và tổ chức phi lợi nhuận. Phần mềm có ba cách thực hiện, cổng chất lượng, mô-đun ngân sách, đầu vào HWP và phân phối dưới dạng plugin. Chức năng thẩm định đầu tư tác động đang được chuẩn bị.

## Giấy phép

[MIT](./LICENSE) © 2026 IMPACT SQUARE.
