# 01_VENUES — Hồ sơ venue (kiểm chứng ngày 2026-11-20)

Mọi số liệu dưới đây lấy từ trang chính thức được đọc trong phiên này; chi tiết, trích nguồn từng dòng và danh sách
bài calibration nằm ở `../sota/venues.md`. Mục ghi **CHƯA KIỂM CHỨNG** là trang chưa công bố hoặc không đọc được —
không điền từ trí nhớ.

## 1. Bảng tổng hợp

| | IJCAI 2027 Main Track | ICML 2027 | ACL 2027 (qua ARR) |
|---|---|---|---|
| Hạn abstract | 4 Jan 2027 (còn 45 ngày) | 14 Jan 2027 (còn 55 ngày) | không có |
| Hạn full paper | 11 Jan 2027 (còn 52 ngày) | 22 Jan 2027 (còn 63 ngày) | ARR 4 Jan 2027 (còn 45 ngày) |
| Múi giờ | 23:59 AoE | 11:59 PM AoE | 11:59 PM AoE |
| Loại sớm | 25 Feb 2027 | trước 23 Feb 2027 (vòng 1 do AC) | — |
| Rebuttal | 30 Mar – 2 Apr 2027 | CHƯA KIỂM CHỨNG | CHƯA KIỂM CHỨNG |
| Thông báo | 21 Apr 2027 | 3 May 2027 | CHƯA CÔNG BỐ (commitment TBD) |
| Hội nghị | Kyoto 7–13 Aug 2027 (+ Hengqin 15–17 Aug) | Rio de Janeiro 31 Jul – 6 Aug 2027 | Kyoto 17–22 Aug 2027 |
| Số trang | 7 nội dung + 2 tài liệu tham khảo | 8 + phụ lục/tham khảo không giới hạn | 8 (long) / 4 (short) + tham khảo |
| Giới hạn/tác giả | 8 bài; phí USD 100/bài trừ khi mọi tác giả chỉ có đúng bài này | 20 bài | 20 bài, tối đa 5 bài là tác giả đầu mỗi chu kỳ ARR |
| Xếp hạng CORE (ICORE2026) | A* | A* | A* |
| Tỉ lệ nhận 2025 | CHƯA KIỂM CHỨNG | 27% (3.260 bài) | 20,3% main + 16,7% Findings |
| Tỉ lệ nhận 2026 | CHƯA KIỂM CHỨNG | 6.552 / 24.661 (~26,6%) | 18,9% main + 17,8% Findings |

Nguồn: [IJCAI 2027 CFP](https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/) ·
[IJCAI submission process](https://2027.ijcai.org/ijcai-2027-submission-process/) ·
[ICML 2027 CFP](https://icml.cc/Conferences/2027/CallForPapers) · [ICML 2027 Dates](https://icml.cc/Conferences/2027/Dates) ·
[ACL 2027 call](https://2027.aclweb.org/calls/main/) · [ARR dates](https://aclrollingreview.org/dates) ·
[ARR CFP](https://aclrollingreview.org/cfp) · [CORE portal](https://portal.core.edu.au/conf-ranks/).
Lưu ý: các trang ICML 2027 được đọc qua bản tóm tắt của công cụ fetch, nên cần mở lại trang gốc trước khi nộp.

## 2. Các điểm quyết định việc chọn venue

1. **Một bản thảo – một venue.** Hạn abstract IJCAI trùng ngày hạn ARR (4 Jan); cả ba cấm dual submission; ARR nêu đích danh IJCAI và ICML.
2. **Chính sách dùng LLM khác nhau rõ rệt.**
   - IJCAI: chỉ được dùng LLM để trau chuốt văn bản do tác giả viết; không được sinh nội dung mới ([chính sách](https://ijcai.org/generative_ai_policy/), cập nhật 11 Nov 2026).
   - ICML: được dùng nếu khai báo; bắt buộc có **AI Disclosure Statement** (gồm cả ideation, tổng hợp tài liệu, thiết kế thí nghiệm, code, phân tích) ([chính sách](https://icml.cc/Conferences/2027/UseOfGenerativeAIByAuthors)).
   - ACL/ARR: công cụ AI không được là tác giả; khai báo trong Responsible NLP checklist.
   - Cả ba loại bài có prompt injection ẩn.
   - **Hệ quả cho dự án này:** bộ hồ sơ ideation do AI hỗ trợ phù hợp với ICML và ACL (khai báo đầy đủ); với IJCAI, tác giả phải tự viết toàn bộ nội dung và không được chép từ tài liệu này.
3. **Yêu cầu reviewer là điều kiện bắt buộc.**
   - IJCAI: mỗi bài một reciprocal reviewer đủ chuẩn (≥5 bài ở các venue liệt kê); miễn nếu không tác giả nào đủ chuẩn.
   - ICML: mỗi bài một reciprocal reviewer; tác giả không đủ điều kiện review chỉ được đứng tên tối đa 2 bài.
   - ARR: thiếu người đóng góp review đủ chuẩn (mỗi người tối đa 2 bài) thì bài vào diện bốc thăm theo năng lực review và có thể bị desk-reject ([chính sách](https://aclrollingreview.org/sustainable-reviewing-2026)).
4. **ICML 2027 có hai điểm mới:** review hai vòng (AC loại ở vòng 1) và 6 loại đóng góp, trong đó có *Datasets, Evaluations and Benchmarks* và *Negative Results*; "Evaluation" là area cấp cao nhất. Không bắt buộc dự trực tiếp. IJCAI bắt buộc trình bày trực tiếp.
5. **ACL 2027:** special theme *"Homogenization and knowledge collapse in LLMs"* (nêu ngôn ngữ ít tài nguyên); có area *LLM Agents for NLP*.

## 3. Calibration (mức chuẩn bài được nhận)

- Cụm chủ đề agent/memory/an toàn agent: đông ở ACL 2026 (45+ tiêu đề long paper) và ICML 2026 (100+ tiêu đề), thưa ở IJCAI.
- Bài điển hình: phương pháp, tấn công/phòng thủ hoặc benchmark (thường benchmark + phương pháp), đánh giá trên benchmark agent công khai, so với baseline SOTA có tên, công bố code. Kết quả hình thức chủ yếu ở ICML.
- Benchmark bộ nhớ hội thoại họ ACL (từ audit ACL): khoảng 1.000–5.000 mục chấm điểm, 5–30 cấu hình hệ thống, 2–12 annotator, κ 0,69–0,90.
  Ví dụ đã kiểm chứng: TimlMemBench (Findings EMNLP 2026: 208 mẫu/1.821 ca, 12 hệ thống), OP-Bench (EMNLP 2026 main: 1.700 mẫu, 12 annotator, 30 cấu hình), LOCOMO-CONV (Findings EMNLP 2026: ~6.600 truy vấn, 5 hệ thống).
- Lý thuyết ICML 2025–2026 (từ audit ICML): một mô hình gọn, cận trên chặt, thường có cận dưới khớp, 20–60 trang proceedings, thí nghiệm ít hoặc không có.
- Giải thưởng 2025–2026 nghiêng về lý thuyết, nghiên cứu "nghĩ lại"/kết quả âm tính, và đánh giá chặt chẽ — không phải bài agent số đông.

## 4. Tạp chí cho bản mở rộng

| Tạp chí | Nhận bản mở rộng từ hội nghị? | Ghi chú |
|---|---|---|
| JAIR | Có (mở rộng đáng kể) | Quartile: CHƯA KIỂM CHỨNG |
| Artificial Intelligence (AIJ) | Có | Quartile: CHƯA KIỂM CHỨNG |
| JMLR | Có | Quartile: CHƯA KIỂM CHỨNG |
| Computational Linguistics | Có | Quartile: CHƯA KIỂM CHỨNG |
| TACL | **Không**; cấm 9 tháng với bài đã gửi ARR | Không dùng làm đích mở rộng |
| Computers & Security | Đang tạm ngừng nhận bài AI/ML; LLM security ngoài phạm vi ([trang Elsevier](https://shop.elsevier.com/journals/computers-and-security/0167-4048)) | Không dùng |
| IEEE TDSC / TIFS, ACM TOSEM | CHƯA KIỂM CHỨNG | Cần kiểm tra lại |

Quartile JCR chưa kiểm chứng được trong phiên (Scimago chặn) — phải tra JCR trước khi chốt tạp chí.
