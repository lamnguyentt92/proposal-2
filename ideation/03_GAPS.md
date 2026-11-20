# 03_GAPS — Bản đồ khoảng trống (2026-11-20)

Nguồn bằng chứng: các file ghi chú trong `research_notes/Thẩm định proposal IJCAI ICML ACL 2027/`
(`acl_scope_interventions_audit.md`, `icml_revocation_feedback_audit.md`, `ijcai_provenance_sufficient_audit.md`,
`hot_topics.md`, `agent_security_sota.md`). Mọi arXiv ID dưới đây lấy từ các ghi chú đó (đã được fetch trong phiên);
mục nào chỉ thấy ở mức abstract/listing được ghi rõ trong ghi chú gốc. "Không tìm thấy" ≠ "không tồn tại".

| ID | Khoảng trống | Loại | Bằng chứng còn mở | Công trình gần nhất | Ai quan tâm | Vì sao còn mở |
|---|---|---|---|---|---|---|
| G1 | Lỗi ghi bộ nhớ do **toán tử ngữ dụng lồng nhau** (lời thuật lại × điều kiện × phủ định × trích dẫn) và **quy chiếu ngôi tiếng Việt** (đại từ–từ thân tộc, chủ ngữ ẩn); gold do người gán | Vấn đề chưa xử lý + thiếu đánh giá | Không bài nào lai ≥2 toán tử với tổ hợp held-out; không có bộ nhớ hội thoại tiếng Việt/VI–EN | AgentMemGate 2610.07707 (1 họ toán tử, dữ liệu LLM sinh, tiếng Anh); DerivAudit 2609.36130 (3 nhánh correct/distorted/absent, nhãn do model); HaluMem 2511.03506 (stage-wise); MemAlign/ConMem 2610.33432 (15 ca attribution confusion) | ACL: Discourse & Pragmatics, Dialogue, Multilinguality; nhà phát triển memory framework | Cần annotator bản ngữ + thiết kế ngôn ngữ học; các nhóm memory dùng dữ liệu LLM sinh |
| G2 | **Ngôn ngữ là một biến số** trong độ tin cậy/an toàn của agent (ngôn ngữ người dùng, UI, nội dung bị chèn biến thiên độc lập; code-switching) | Setting chưa phủ | Chỉ 3 nghiên cứu nhỏ 2026: 2610.22244, 2610.23093, 2608.15392; không có GUI/mobile, memory, tiếng Việt | 2609.23490 (lỗi ở ngôn ngữ ít tài nguyên chuyển sang tool-use/control-flow) | ACL (kể cả special theme về ngôn ngữ ít tài nguyên), cộng đồng agent safety | Benchmark agent gần như chỉ tiếng Anh/Trung |
| G3 | **Tính hợp lệ của benchmark/thước đo an toàn agent**, đặc biệt mobile: không có audit nào cho benchmark an toàn mobile hay benchmark memory; không báo CI | Đánh giá yếu | Bảng xếp hạng không nhất quán, baseline tầm thường thắng model thật (2607.28685); 76–80% tấn công "thất bại" là bị bỏ qua chứ không phải từ chối, system prompt đổi ASR 0.2%→43% (2610.23254); ≥5/25 tool AgentDojo lệch spec (2609.37315) | Audit benchmark năng lực: 2507.02825, 2609.34262, 2611.04399, 2610.16067; 2607.22368 (shortcut ~67% trace) | ICML area "Evaluation" (loại bài Negative Results / Datasets-Benchmarks); mọi nhóm báo cáo ASR | Audit tốn công, ít "hào nhoáng"; cần kỹ năng kiểm thử phần mềm |
| G4 | **Memory poisoning xuyên app / xuyên phiên cho mobile–GUI agent** | Setting chưa phủ | Không tìm thấy bài nào; 4 bài an toàn mobile không nhắc memory poisoning | ZoneClaw 2610.00450; plan injection web agent 2506.17318; Trojan Hippo 2605.01970 | Cộng đồng security + agent | Mobile agent có memory mới xuất hiện; nhưng dòng memory poisoning đang rất đông (≥8 benchmark 2026) → rủi ro bị scoop |
| G5 | **Đánh giá thích nghi độc lập cho các defence bộ nhớ** | Đánh giá yếu | A-MemGuard không có đánh giá adaptive, bị FARMA 2607.05029 vượt; PipePoison 2609.00523 hiệu quả dưới 8 defence; MemoryDojo 2611.09721 hoãn đánh giá defence | "12 defence bị phá" 2510.09023 (cho prompt injection) | ICML/security | Rủi ro scoop cao nhất |
| G6 | **False positive/negative trong chấm điểm computer-use/mobile agent**; chấm theo quá trình | Đánh giá yếu | 15.3% phán quyết FAIL sai, chưa ước lượng FP trong các ca "thành công" (2607.28367); AndroidWorld gần bão hoà (2602.07787) | 2607.28367 | Cộng đồng agent evaluation; người làm kiểm thử app | Cần oracle trạng thái hệ thống — đúng chuyên môn kiểm thử Android |
| G7 | **Evaluation awareness** làm lệch điểm an toàn/bảo mật | Giả định chưa kiểm | Chỉ đo khi model nói ra (2605.23055); confound được ghi nhận (2505.23836, 2608.10669) nhưng chưa ai định lượng tác động lên ASR | — | ICML/safety | Khó đo nếu không có white-box |
| G8 | So sánh **red-teamer tự động chuẩn hoá theo ngân sách** | Đánh giá yếu | Ngân sách không so được (10 vs 800 lượt vs RL công nghiệp 2607.26115); kết quả transfer mâu thuẫn (2606.10525 vs 2609.33628); attacker mất đa dạng (2611.19680) | — | ICML/security | Lab công nghiệp áp đảo về compute |
| G9 | Lý thuyết provenance: **phụ thuộc có mức độ** và giao diện đủ yếu nhất; độ bền khi nhãn lineage sai | Thiếu bảo đảm | Được nêu là mở trong 2610.36151 và 2609.01873 | DeMem 2605.10870 (NeurIPS 2026); 2606.09858 | IJCAI KR/planning | Cần định lý thật; khung và T1 đã bị chiếm |
| G10 | Online learning khi **cấu trúc phản hồi đổi theo trạng thái quyền** | Thiếu bảo đảm | Không thấy bài toán mở được đặt tên; 3 phép quy dẫn khả dĩ về kết quả đã biết | 2610.23812, 2610.02070, 2610.11007, 2606.03851, Sleeping RL (ICML 2025) | ICML theory | Nguy cơ là hệ quả của kết quả đã có |
| G11 | Phục hồi/sửa chữa sau khi bộ nhớ hoặc hệ đa agent bị xâm hại | Vấn đề chưa xử lý | 42/44 đánh giá giả định thành viên cố định, 1 ghi provenance (2609.00595) | — | IJCAI agents/MAS | Mới |
| G12 | ACL 2027 special theme "homogenization & knowledge collapse" × bộ nhớ agent: memory writer **đồng nhất hoá** cấu trúc ngôn ngữ riêng (hệ xưng hô tiếng Việt) về khung "user/I" kiểu tiếng Anh | Technology shift / "why now" | Theme nêu rõ ngôn ngữ ít tài nguyên; số bài multilingual ở ACL 2026 đi ngang (54→52) trong khi agent tăng 142→366 | — | ACL theme track | Chưa ai nối hai dòng này |

## Xếp hạng (ý nghĩa × phù hợp ràng buộc)
1. **G1 (+G12)** — lõi chưa ai chiếm, đúng nguồn lực (≥2 annotator Việt), đúng ACL.
2. **G3 (+G6)** — rủi ro scoop thấp nhất, đúng chuyên môn kiểm thử Android/khung đánh giá tự động, đúng area "Evaluation" của ICML.
3. **G2** — phù hợp ACL; có thể ghép với G1 hoặc G4.
4. **G4** — mới nhưng dòng đang rất đông.
5. **G7, G8** — có giá trị, bị giới hạn bởi compute/white-box.
6. **G5** — rủi ro scoop cao.
7. **G9, G10** — chỉ khả thi nếu có định lý thật; khung đã bị chiếm.
8. **G11** — còn sớm, khó định hình trong một bài.
