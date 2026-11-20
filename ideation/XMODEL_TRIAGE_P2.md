# Phân loại review khác họ model — Proposal 2 (2026-11-20)

Nguồn: `XMODEL_NOVELTY_P2_RESPONSE.md`, `XMODEL_REDTEAM_P2_RESPONSE.md` (GPT-6, nguyên văn). Kiểm chứng trích dẫn:
`XMODEL_VERIFY_P2.md` — cả 18 tài liệu đều có thật; 17 mô tả chính xác, 1 tiêu đề lỗi thời.

## Kết luận của reviewer
| | Kết luận |
|---|---|
| Novelty (prior-art) | **Incremental** — C2 "không tìm thấy" (khoảng trống mạnh nhất); C1, C3, C4, C5 "đã bị chiếm một phần" |
| Referee | **Borderline / Weak Reject ở giai đoạn ý tưởng**; significance 4/5, soundness potential 2/5, trung bình 3,29/5; dải 10–25% (25–40% nếu có chân trị độc lập và các ô C2 đủ dữ liệu) |

So với đánh giá cùng họ model: **trùng** cả verdict novelty lẫn dải xác suất.
Gate G2 và Stage 6: đã có review → trạng thái **WARN**, cần tác giả ký duyệt để đi tiếp.

## Từng điểm
| # | Điểm của reviewer | Kiểm chứng | Phân loại | Hành động |
|---|---|---|---|---|
| R1 | Chân trị không độc lập: lộ trình tham chiếu + mask không mô tả hết các trạng thái cuối hợp lệ; mask có thể che lỗi thật | Lập luận thiết kế | **Nhận — điểm nặng nhất** | Thêm **hợp đồng đúng-sai theo tác vụ** (bắt buộc / cấm / chấp nhận được / mơ hồ), viết từ đề bài trước khi xem lượt chạy; báo cáo theo cả định nghĩa chặt và định nghĩa theo tác vụ |
| R2 | C2 có thể chỉ đo lệch phân bố giữa lỗi gieo và lỗi thật, kể cả trong cùng template và cùng mode | Lập luận + ví dụ số đúng | **Nhận** | Hai estimand: phân bố lỗi quan sát được, và tập hỗ trợ chung khớp template; phân loại lỗi mịn hơn (trường trạng thái, mức độ, phạm vi); ô không có hỗ trợ chung = không nhận dạng được |
| R3 | Chỉ audit mẫu các lượt không bị gắn cờ thì không "thấy mọi lỗi thật" | Đúng — câu trong đặc tả mục 2 nói quá | **Nhận** | Audit hai pha có xác suất chọn biết trước; ước lượng có trọng số; bất định gồm cả lấy mẫu và cụm template |
| R4 | Tiêu chí "trong 2 điểm" có thể đạt mà không cần hiệu chỉnh; cần cả tỉ lệ nhận nhầm α và từ chối nhầm β | Công thức đúng | **Nhận** | Kiểm chứng trên agent giữ lại phải **thắng điểm gốc** và thắng hiệu chỉnh từ lỗi thật; ước lượng α và β kèm bất định |
| R5 | Kiểm định tương đương dễ thiếu power ở từng ô | Lập luận | **Đã có một phần** | Chỉ vài ô chính được định trước, power tính theo cụm template; còn lại là thăm dò |
| R6 | Công cụ là tích hợp các cơ chế đã có; VerifierBench | Có thật (4.993 test; đối tượng là verifier do agent sinh) | **Nhận** | C4 không phải đóng góp độc lập |
| R7 | Tính tổng quát hẹp hơn mô tả; "toàn trạng thái" phải gồm backend của MobileWorld | MobileWorld: 201 tác vụ, 4 kiểu kiểm, backend tự host — chính xác | **Nhận** | Observer đọc cả cơ sở dữ liệu backend và callback; chỉ claim tổng quát có điều kiện |
| R8 | Thay đổi phụ vô hại (cache, lịch sử) không nên tính là thất bại | Lập luận | **Nhận** | Như R1 |
| B1 | Thiếu baseline: hiệu chỉnh từ **lỗi thật** của các agent nguồn rồi dự đoán agent giữ lại | Lập luận | **Nhận** | So 4 ước lượng: điểm gốc / hiệu chỉnh bằng mutant / hiệu chỉnh bằng lỗi thật / audit phân tầng |
| N1 | Dự đoán: C2 sẽ không đạt tương đương ở cả hai họ; lo nhất là "phần lớn ô không kết luận được" | Dự đoán | **Đã có** (K2) | Giữ |
| KILL | Chân trị không đủ độc lập nên mẫu số của C2 không tin được | Như R1, R3 | **Nhận** | Như R1, R3 |
| P1 | arXiv:2610.16067 (τ-bench): gieo 7 loại lỗi evaluator, phát lại 4.320 episode thật, điểm 94,3% → 65,5%, thứ hạng đổi, khoảng tin cậy theo cụm | Chính xác (toàn văn) | **Nhận** | C3 chỉ là lặp lại ngoài lĩnh vực; trích đầy đủ |
| P2 | VeriCUA (arXiv:2610.40578) đã đánh giá verifier đọc trạng thái trên AndroidWorld | Có thật; **nhưng dùng checker gốc làm chuẩn**, nên "false positive" ở đó là lệch với checker, không phải với chân trị; không thấy code | **Nhận, kèm lưu ý** | Baseline của C4 phải là verifier kiểu VeriCUA (tự dựng lại, ghi rõ là dựng lại), không phải LLM đọc dump trạng thái |
| P3 | Sauron (arXiv:2610.17724): dùng cả bộ lỗi gieo và lỗi thật để đánh giá verifier | Chính xác | **Nhận** | Điểm mới của C2 là phép **so sánh theo mode giữa hai loại**, không phải việc có cả hai |
| P4 | Interactive Reward Agent; State Field Coverage (ASE 2025); ROUTE (TOSEM 2023); SWE-Mutation | Đều có thật | **Nhận** | Trích; thêm "độ phủ trường trạng thái của checker" làm biến dự báo rẻ để so với kill rate |
| P5 | AndroidWorld đã chạy trên Pixel 7 thật (arXiv:2602.07787v2) | Có thật, **hẹp hơn reviewer nói**: 16/116 tác vụ, máy không root, không so cùng tác vụ giữa emulator và máy thật | **Nhận một phần** | C5 vẫn là claim hỗ trợ hẹp; trích tiền lệ |
| P6 | MobileJudgeBench: 1,4% là trên các lượt checker cho PASS, không phải trên mọi lượt | Chính xác | **Nhận** | Sửa cách viết |
| P7 | Người gán nhãn AgentRewardBench được xem môi trường khi ảnh màn hình không đủ | Chính xác — ghi chú drift scan của ta sai | **Nhận** | Sửa đặc tả |
| P8 | Ba ranh giới của C2: khớp mode ≠ khớp phân bố; lựa chọn nội sinh; lợi ích "hiệu chỉnh điểm" có thể vòng quanh | Lập luận | **Nhận** | Như R2; tính cả chi phí thông tin cần có khi áp dụng cho agent mới |
| P9 | Định vị: "kiểm định tính hợp lệ ngoài của mutation score, có audit trạng thái hỗ trợ" | — | **Nhận** | Đổi câu định vị |

## Điểm không đồng ý hoặc cần lưu ý
- "Silent Instrument Errors" (arXiv:2611.04399) là về lỗi harness (episode không được chấm, đếm trùng chi phí), không phải checker nhận nhầm trạng thái sai; không có benchmark mobile.
- Tiền lệ máy thật (P5) và VeriCUA (P2) yếu hơn cách reviewer trình bày — xem cột kiểm chứng.
- Bản review phản biện dùng tiêu đề cũ (v2) của arXiv:2610.09142.
- OpenReview vẫn là điểm mù của cả hai phía; hai bài `zh33pqlBjf` và `GWFSBzaPNd` chưa ai mở được.
