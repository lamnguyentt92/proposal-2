# 00_CONSTRAINTS — Ràng buộc và bối cảnh

Ngày lập: 2026-11-20. Nguồn: câu trả lời trực tiếp của tác giả trong phiên làm việc + hồ sơ đã có.

## Idea registry
- `research/IDEA_REGISTRY.md` chưa tồn tại trước phiên này → tạo mới ở cuối quy trình.
- Ba proposal đầu vào (GPT-6, bản v5) được coi là ứng viên ban đầu:
  - IJCAI 2027 — PROVENANCE-SUFFICIENT (kế thừa v4 `EPISTEMIC-COMMIT`)
  - ICML 2027 — REVOCATION-FEEDBACK (kế thừa v4 `REVSHIFT-POM`)
  - ACL 2027 — SCOPE-INTERVENTIONS (kế thừa v4 `SCOPE-TRACE`)

## Nhà nghiên cứu
- Chuyên môn đã công bố/đang làm: kiểm thử tự động ứng dụng Android và khung đánh giá tự động; bảo mật IoT/smart-home (kiến trúc broker-less, RBAC).
- Ngôn ngữ: tiếng Việt bản ngữ, tiếng Anh học thuật.
- Năng lực lý thuyết: tác giả để coordinator chọn phương án tối ưu → không giả định có chuyên gia online-learning theory; ý tưởng thuần định lý phải tự chứng minh được tính khả thi kỹ thuật.

## Tài nguyên
- Tính toán: API thương mại (GPT/Claude/Gemini) + 1–2 GPU (chạy được model mở cỡ vừa, không huấn luyện quy mô lớn).
- Con người cho dữ liệu: ≥ 2 annotator bản ngữ tiếng Việt, thạo tiếng Anh, annotate độc lập được.
- Thiết bị/testbed (tác giả xác nhận 2026-11-20): **MacBook, máy Windows** (chạy emulator Android) và **3 điện thoại Android thật đã root bằng Magisk** — tác giả cho biết `adb root` dùng được và `su` vào được root. Còn phải kiểm tra khi cài đặt: benchmark nào chạy trên máy nào (Mac arm64 dùng AVD arm64; MobileWorld ghi tài liệu cho Linux/KVM và WSL2).

## Venue mục tiêu (do tác giả chỉ định)
- IJCAI 2027 Main Track, ICML 2027, ACL 2027 (qua ARR). Chỉ cần **2 proposal cuối** cho 3 venue này.
- Cộng đồng: AI tổng quát (IJCAI), ML (ICML), NLP (ACL).

## Security lens: **on**
- Lý do: tác giả trả lời "Cả hai" — vừa phản biện giả lập ý tưởng, vừa cho phép đề tài thuộc hướng red-teaming / bảo mật AI agent.
- Hệ quả: dùng thêm generator góc nhìn adversarial/security (Stage 4) và security referee (Stage 6). Phản biện giả lập (Stage 6) chạy cho mọi finalist bất kể lens.

## Chu kỳ nộp (chỉ là thông tin, không dùng để chọn ý tưởng)
- Đợt gần nhất: tháng 1/2027 (ngày chính xác xem `01_VENUES.md`, đã kiểm chứng từ CFP chính thức).
- Nếu trượt chu kỳ: chuyển sang chu kỳ kế tiếp (ARR hàng tháng; NeurIPS/EMNLP 2027; IJCAI/ICML/ACL 2028).

## Đạo đức, dữ liệu, pháp lý
- Không dùng hội thoại thật có danh tính; dữ liệu hư cấu hoặc có đồng thuận.
- Nghiên cứu tấn công chỉ trong sandbox tổng hợp; tuân thủ responsible disclosure nếu phát hiện lỗi ở sản phẩm thật.
- Chính sách dùng LLM của từng venue: xem `01_VENUES.md`. Tài liệu ideation này do AI hỗ trợ; **không** chép vào bản thảo ở venue cấm nội dung do LLM sinh.

## Loại trừ cứng
- Không trùng nội dung với các bài khác của tác giả đang được bình duyệt.
- Không dual-submit nội dung trùng lặp giữa các venue.

## Trạng thái xác nhận
- Tác giả đã trả lời 4 câu hỏi ràng buộc trong phiên. Các giả định còn lại được đánh dấu "(chưa khai báo)".
