# Phân loại review khác họ model — Proposal 1 (2026-11-20)

Nguồn: `XMODEL_NOVELTY_P1_RESPONSE.md`, `XMODEL_REDTEAM_P1_RESPONSE.md` (GPT-6, nguyên văn). Kiểm chứng trích dẫn:
`XMODEL_VERIFY_P1.md` — cả 12 tài liệu ưu tiên đều có thật; 9 mô tả chính xác, 3 chính xác kèm lưu ý.

## Kết luận của reviewer
| | Kết luận |
|---|---|
| Novelty (prior-art) | **Incremental** — không tìm thấy công trình nào làm toàn bộ; C0, C1, C4 "không tìm thấy"; C2, C3, C5 "đã bị chiếm một phần" |
| Referee | **Weak Reject ở giai đoạn ý tưởng**; novelty 4/5, soundness potential 2/5, trung bình 3,29/5; dải main track 10–25% |

So với đánh giá cùng họ model: dải xác suất **trùng** (10–25%); verdict novelty **thấp hơn** ("novel core" → "incremental").
Gate G2 và Stage 6 (yêu cầu review khác họ model): đã có review → trạng thái **WARN**, cần tác giả ký duyệt để đi tiếp.

## Từng điểm
| # | Điểm của reviewer | Kiểm chứng | Phân loại | Hành động |
|---|---|---|---|---|
| R1 | Chưa cô lập được hiện tượng riêng của bộ nhớ: nếu summary sai ngang memory extraction thì C1 chỉ là chi phí viết lại sang ngôi thứ ba | Lập luận thiết kế; DIAL-SUMMER có thật (chỉ SPEAKER MISATTRIBUTION là lỗi sai người) | **Nhận** | Đặc tả: phân rã E = hiểu + Δ viết lại + Δ hợp nhất; claim riêng của bộ nhớ là **Δ hợp nhất**; quy tắc đóng khung F1 cố định trước |
| R2 | Ngưỡng "< 10% rater" với 8 rater = 0 phiếu; so sánh writer với phân bố trong mẫu là lệch; phải tách "không thể" / "thiểu số" / "không xác định được" | Số học đúng (1/8 = 12,5%) | **Nhận — lỗi thật trong code phân tích** | Bộ pilot 0.1.1: điểm cross-fitted (bỏ từng rater ra), bản ghi UNRESOLVED chấm như CANNOT_TELL, thêm mức nhạy 20% |
| R3 | Study 0 theo kịch bản gia đình/công việc tự kéo ra từ thân tộc | Lập luận thiết kế | **Nhận** | Thêm nhánh chủ đề mở; K3 đọc trên nhánh "làm giàu", nhánh mở báo cáo kèm, không gọi là tần suất tự nhiên |
| R4 | Extractor mạnh + một dòng prompt có thể xoá hiệu ứng | Manufactured Confidence có can thiệp giữ hedge (có thật) | **Đã có** (K2) | Giữ |
| R5 | C3 gộp hai cơ chế: quy chiếu sai và va chạm tên do chuẩn hoá | PR Graphiti #1357, #1850 có thật, còn mở, không nhắc tiếng Việt | **Nhận** | Tách 3 kết quả: sai người / gộp do từ quan hệ / gộp do tên; cái thứ ba báo cáo riêng, không tính vào C3 |
| R6 | Né lỗi bằng cách không ghi gì | Lập luận thiết kế | **Nhận** | Báo cáo đường risk–coverage (sai người so với giữ đúng) cho mọi điều kiện |
| R7 | Lớp tự nhiên và lớp chẩn đoán khác độ khó; control tiếng Anh không giữ được nghĩa xã hội của từ thân tộc; 8 rater/item là ít | Lập luận thiết kế | **Nhận một phần** | Ghi vào giới hạn; control khớp độ khó đã cam kết; số rater mỗi item là tham số của phân tích power |
| B1 | Thiếu baseline: bộ nhớ episodic giữ nguyên lời, truy xuất rồi mới giải quy chiếu, khớp ngân sách | Control "raw-vector" trong Manufactured Confidence có thật nhưng nhỏ và **không** khớp ngân sách — "budget-matched" là thêm của reviewer | **Nhận** | Thêm baseline episodic vào nghiên cứu chính (không phải pilot) |
| N1 | Thí nghiệm dễ âm nhất: C4 (dịch có thể *giảm* lỗi) | Dự đoán | **Đã có** | Giữ quy tắc: C4 bị bác thì dịch là biện pháp giảm thiểu |
| CE-A | Tham chiếu thật sự không xác định được: giữ nguyên từ không phải lỗi | Lập luận | **Nhận** | Như R2 |
| CE-B | Giải đúng quy chiếu nhưng Graphiti gộp tên: lỗi hợp nhất, không phải lỗi ngôn ngữ | Lập luận | **Nhận** | Như R5 |
| CE-C | Hệ lưu nguyên lời không buộc phải chốt người sớm → claim là về kiến trúc ghi *phi ngữ cảnh hoá*, không phải mọi bộ nhớ | Lập luận | **Nhận** | Sửa phạm vi claim trong đặc tả |
| C5 | Câu hỏi phiên sau chỉ lặp lại bản ghi cài sẵn thì kết quả là tất yếu | Lập luận | **Nhận** | Câu hỏi phiên sau phải trả lời được từ hội thoại gốc; so với baseline episodic |
| P1 | CogMem (EMNLP 2026) đã có schema Person–Event–Concept–Claim–Fact giữ nguồn và đích của phát ngôn | Chính xác (toàn văn); chỉ đánh giá tiếng Anh; không nhắc từ thân tộc | **Nhận** | Không claim schema có provenance là mới; đóng góp schema thu hẹp thành "neo từ quan hệ chỉ người"; CogMem là baseline nếu lấy được code |
| P2 | SpeakerMem-R1 (arXiv:2609.26780) | Chính xác | **Nhận** | Trích; phân biệt danh tính người nói với quy chiếu trong sự kiện lời nói lồng |
| P3 | Nghiên cứu bộ nhớ đa phiên tiếng Hàn (Applied Sciences 2026) bác câu "gần như chỉ Anh/Trung" | Có thật; chủ yếu là nghiên cứu fine-tune, mở rộng bộ dữ liệu có sẵn | **Nhận** | Sửa câu định vị: có nghiên cứu bộ nhớ đa phiên ngoài Anh/Trung; chưa có nghiên cứu lỗi ghi về quy chiếu ngôi |
| P4 | Nguyen & Sim (Language Variation and Change, 2026) | Có thật; "hiệu ứng theo ngôi" là nói quá — bài về lược tân ngữ ở tiếng Việt di sản | **Nhận một phần** | Trích làm nền ngôn ngữ học; không claim hiện tượng là mới |
| P5 | Tạp chí Ngân hàng 2024 đã thử chatbot với câu hỏi đổi cách xưng hô | Có thật: 2 chatbot, 65 câu trong đó 20 câu đổi xưng hô; không có số liệu cho tiêu chí này | **Nhận** | Thu hẹp câu "chưa có nghiên cứu thực nghiệm nào": chưa có đo đạc về cách *người dùng* xưng hô và thuật lời |
| P6 | KinshipQA; He Said, She Said | Có thật | **Nhận** | Trích |
| P7 | Kết quả Graphiti mới là "cơ chế khả dĩ", chưa phải gộp end-to-end | Đúng với thời điểm reviewer viết | **Nhận, kèm cập nhật** | Đã chạy thật ở **mức hàm** trên bản 0.31.2 (4/6 cặp bị gộp); end-to-end vẫn chưa chạy |
| P8 | Không cần ngôn ngữ thứ hai cho main track (hướng dẫn reviewer ARR, mục H10) | Chính xác | **Nhận** | Bỏ khỏi danh sách rủi ro; giữ cho bản tạp chí |

## Điểm không đồng ý hoặc cần lưu ý
- Reviewer novelty viết FACTWASH có đánh giá LangMem: theo abstract thì LangMem chỉ có ở Manufactured Confidence.
- "Budget-matched" cho baseline episodic là yêu cầu của reviewer, không phải tiền lệ đã công bố.
- OpenReview vẫn là điểm mù của cả hai phía.
