# Proposal 2 — ICML 2027

## Are the Passes Real? A State-Level Audit of Mobile-Agent Benchmark Verdicts and a Test of Whether Verifier Mutation Scores Transfer to Real Agent Failures

**Trạng thái (2026-11-20): CONDITIONAL GO — phải qua pilot gate (không cần agent) trước.** Chưa xây gì, chưa chạy thí nghiệm, chưa có kết quả nào.

**Quyết định của tác giả (2026-11-20):** chốt proposal này; giữ đích **ICML 2027** và thêm **AppWorld** làm benchmark bắt buộc
để claim tính tổng quát; testbed gồm MacBook, máy Windows và **3 điện thoại Android thật đã root (Magisk, có `adb root`)**.

Đây là **ý tưởng mới**, thay cho hai proposal của GPT-6 đã bị loại (`PROVENANCE-SUFFICIENT` cho IJCAI và
`REVOCATION-FEEDBACK` cho ICML — lý do ở `ideation/AUDIT_GPT6_PROPOSALS.md`). Đặc tả đầy đủ: [`PROPOSAL.md`](PROPOSAL.md).

## Ý tưởng trong một đoạn

Benchmark agent có trạng thái (AndroidWorld, MobileWorld trên Android; AppWorld ở thế giới API) chấm một lượt chạy bằng đoạn code kiểm tra trạng thái. Năm 2026
có cả một làn sóng bài "audit bộ chấm" bằng cách gieo lỗi vào lượt chạy mẫu rồi đếm xem bộ chấm bỏ sót bao nhiêu — đó là
kết quả về **tồn tại**. Nhưng một PASS sai cần hai thứ trùng nhau: điểm mù của bộ chấm **và** một lỗi thật của agent rơi
đúng vào đó. Câu hỏi đúng vì thế là theo từng loại lỗi: *bộ chấm bỏ sót lỗi thật của agent có nhiều như bỏ sót lỗi gieo
không?* — phiên bản "mutant có đại diện cho lỗi thật không" (Just et al., FSE 2014) cho bộ chấm agent, chưa ai kiểm định.
Kiểm định được vì với benchmark có trạng thái, **chân trị mức trạng thái lấy được mà không cần gán nhãn từng lượt**: chạy
script tham chiếu từ cùng trạng thái đầu cho ra trạng thái cuối chuẩn; trở ngại duy nhất (các lộ trình đúng khác nhau, trường
không tất định) thì **đo** được bằng cách chạy nhiều lộ trình đúng.

## Các claim

| | Claim | Bị bác bỏ / không kết luận khi |
|---|---|---|
| C1 | Tỉ lệ PASS sai và FAIL sai ở **mức trạng thái**, kèm khoảng tin cậy; phần PASS sai chỉ thấy được ở mức trạng thái (thay đổi ngoài yêu cầu, không hiện trên ảnh màn hình) | Phần "chỉ thấy ở mức trạng thái" ≈ 0 |
| C2 | **Transfer theo mode:** với từng họ checker × loại lỗi, tỉ lệ sót trên lỗi thật của agent bằng tỉ lệ sót trên lỗi gieo theo công thức gieo đã công bố (kiểm định tương đương, đăng ký trước) | Đúng → hiệu chỉnh được điểm agent mới không cần audit; Sai → đo được độ lệch của mutation audit; Không kết luận ở > ½ số ô → K2 |
| C3 | Lỗi phán quyết khác nhau giữa các agent; có đổi thứ hạng hay không (kỳ vọng: null) | Báo cáo cả hai chiều |
| C4 | Oracle vi sai với mask đa lộ trình: precision ≥ 0,8 so với audit mù, recall cao hơn LLM verifier, rẻ hơn audit toàn bộ | Precision < 0,8 |
| C5 | (hỗ trợ) Kết quả không phải artefact của emulator: lặp lại 10–15 template trên 3 điện thoại thật đã root | Mask không chuyển được sang máy thật → chỉ phát biểu cho cấu hình emulator |

**Ba benchmark, hai họ.** Họ Android GUI (AndroidWorld, MobileWorld) và họ thế giới API (AppWorld — 9 app, 457 API, 750 tác vụ;
bộ chấm theo trạng thái có kiểm "collateral damage" ngay từ thiết kế). AppWorld cho hai thứ: một đối chứng về thiết kế bộ
chấm, và phép thử C2 sạch nhất vì dùng **nguyên vẹn** các mutant đã công bố của arXiv:2610.09142, không phải port. Claim tổng
quát chỉ được đưa ra nếu C2 có kết luận ở **cả hai** họ.

**Điểm dừng:** K1 — mask báo động giả > 10% trên lộ trình đúng → oracle không dùng được → dừng; K2 — các ô của C2 không đủ
cỡ ở cả hai họ → không có claim tổng quát → **không nộp ICML**; K2b — chỉ có kết luận ở một họ → chỉ claim họ đó, bạn quyết định lại venue; K3 — có bài công bố kiểm định này trước → quay lại phản biện.

## Mức độ mới và độ phù hợp venue — nói thẳng

- Hai lượt săn prior-art và một lượt quét lại: ***incremental***, với **một lõi còn sạch là C2**. Phần oracle, phần "thứ hạng
  đổi sau khi sửa bộ chấm", và công thức Mills/Rogan–Gladen đều **không** được claim.
- Đã biết trước: MobileJudgeBench (arXiv:2608.11434) cho thấy khoảng 1,4% PASS của AndroidWorld sai và ~13% thành công thật
  bị từ chối — nhưng chỉ từ ảnh màn hình, 52/116 template, không khoảng tin cậy.
- Điểm rubric: **3,08 / 3,23** trên 5. **Chưa vượt ngưỡng A\* trên giấy.** Venue fit ICML được chấm 3/5.
- Cả hai người chấm khuyên coi NeurIPS Evaluations & Datasets là "nhà" kỳ vọng và ICML là mục tiêu vươn tới. **Bạn đã chọn giữ
  ICML và thêm AppWorld**; khuyến nghị kia được ghi lại như một rủi ro, và K2/K2b xác định khi nào lùi.
- Phương án thay thế cho slot ICML: ý tưởng R1 (red-teaming như lấy mẫu "loài chưa thấy") có điểm ngang, nhưng chưa qua phản
  biện giả lập — xem `ideation/07_SELECTION.md`.
- Mọi review là cùng họ model (provisional).

## Việc cần làm ngay (theo thứ tự)

1. **Cài môi trường:** AndroidWorld trên MacBook (Mac arm64 dùng AVD arm64) hoặc máy Windows; MobileWorld ghi tài liệu cho Linux/KVM và WSL2 nên máy Windows là ứng viên. Emulator không cần GPU.
2. **Pilot (a), không cần agent:** ~15 template AndroidWorld; viết ≥ 2 lộ trình UIAutomator đúng mỗi template; học mask trên một lộ trình, đo báo động giả trên lộ trình còn lại (K1).
3. **Dựng AppWorld** (không cần emulator) và tái lập kết quả mutant đã công bố của arXiv:2610.09142; xác nhận ở commit được ghim rằng AppWorld có kèm lời giải tham chiếu.
4. **Đăng ký trước C2** — và **viết phân tích power** (điểm còn mở trong bảng atom): toán tử gieo lỗi đóng băng, danh sách họ checker, margin, cỡ ô tối thiểu, agent giữ lại.
5. **Pilot (b) ở cả hai họ:** một agent rẻ trên ~30 template AndroidWorld và một tập con AppWorld; đếm lỗi thật theo từng loại (K2).
6. **Kiểm tra khả thi nhánh máy thật:** bạn cho biết `adb root` và `su` dùng được trên 3 máy; còn phải thử các bước setup riêng của emulator (đặt lại đồng hồ, khôi phục snapshot app, bộ APK cho API 33) trên từng dòng máy. Dùng máy không chứa dữ liệu cá nhân.
7. **Review khác họ model:** chạy `ideation/XMODEL_NOVELTY_P2_PROMPT.md` và `ideation/XMODEL_REDTEAM_P2_PROMPT.md` trên GPT/Gemini — nhánh AppWorld và nhánh máy thật **chưa** qua phản biện nào.

## Venue

ICML 2027 — abstract **14 Jan 2027**, full paper **22 Jan 2027** (AoE), 8 trang + phụ lục; area *Evaluation*; loại đóng góp
*Datasets, Evaluations and Benchmarks* hoặc *Negative Results*. Bắt buộc **AI Disclosure Statement** (khai cả ideation, tổng
hợp tài liệu, thiết kế thí nghiệm — tức là cả bộ hồ sơ này). Mỗi bài cần một reciprocal reviewer. Nếu chưa qua pilot kịp:
NeurIPS 2027. Chi tiết: `ideation/01_VENUES.md`, `ideation/08_PUBLICATION_PLAN.md`.

## Cấu trúc repo

| Đường dẫn | Nội dung |
|---|---|
| `PROPOSAL.md` | Đặc tả ý tưởng đầy đủ (13 mục) — đầu vào cho giai đoạn implement |
| `ideation/00_CONSTRAINTS.md` … `08_PUBLICATION_PLAN.md` | Hồ sơ quy trình: ràng buộc, venue, gap, chọn lựa, kế hoạch công bố |
| `ideation/AUDIT_GPT6_PROPOSALS.md` | Kết quả thẩm định 3 proposal gốc |
| `ideation/04_IDEAS/` | 15 thẻ ý tưởng + các bản sửa (T1 + M2 → F1 → F1R → F1S) |
| `ideation/05_NOVELTY/` | Báo cáo săn prior-art (kèm mức kiểm chứng từng tài liệu) |
| `ideation/06_REDTEAM/` | Phản biện giả lập (referee, devil's advocate, feasibility), kill argument, bảng atom |
| `ideation/DECISIONS.md`, `IDEA_REGISTRY.md` | Nhật ký quyết định; sổ ý tưởng đã loại/dự phòng |
| `sota/` | Ghi chú nghiên cứu gốc (SOTA bảo mật/đánh giá agent, chủ đề nóng, venue, audit) |
| `original/` | Hai proposal gốc của GPT-6 đã bị loại |

Proposal còn lại: repo `proposal-1` (ACL 2027).
