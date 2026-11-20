# Proposal 2 — ICML 2027

## Are the Passes Real? A State-Level Audit of Mobile-Agent Benchmark Verdicts and a Test of Whether Verifier Mutation Scores Transfer to Real Agent Failures

**Trạng thái (2026-11-20): CONDITIONAL GO — phải qua pilot gate (không cần agent) trước.** Chưa xây gì, chưa chạy thí nghiệm, chưa có kết quả nào.

Đây là **ý tưởng mới**, thay cho hai proposal của GPT-6 đã bị loại (`PROVENANCE-SUFFICIENT` cho IJCAI và
`REVOCATION-FEEDBACK` cho ICML — lý do ở `ideation/AUDIT_GPT6_PROPOSALS.md`). Đặc tả đầy đủ: [`PROPOSAL.md`](PROPOSAL.md).

## Ý tưởng trong một đoạn

Benchmark mobile agent (AndroidWorld, MobileWorld) chấm một lượt chạy bằng đoạn code kiểm tra trạng thái thiết bị. Năm 2026
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

**Điểm dừng:** K1 — mask báo động giả > 10% trên lộ trình đúng → oracle không dùng được → dừng; K2 — các ô của C2 không đủ
cỡ → không có claim tổng quát → **không nộp ICML**; K3 — có bài công bố kiểm định này trước → quay lại phản biện.

## Mức độ mới và độ phù hợp venue — nói thẳng

- Hai lượt săn prior-art và một lượt quét lại: ***incremental***, với **một lõi còn sạch là C2**. Phần oracle, phần "thứ hạng
  đổi sau khi sửa bộ chấm", và công thức Mills/Rogan–Gladen đều **không** được claim.
- Đã biết trước: MobileJudgeBench (arXiv:2608.11434) cho thấy khoảng 1,4% PASS của AndroidWorld sai và ~13% thành công thật
  bị từ chối — nhưng chỉ từ ảnh màn hình, 52/116 template, không khoảng tin cậy.
- Điểm rubric: **3,08 / 3,23** trên 5. **Chưa vượt ngưỡng A\* trên giấy.** Venue fit ICML được chấm 3/5.
- **Cả hai người chấm khuyên coi NeurIPS Evaluations & Datasets là "nhà" kỳ vọng và ICML là mục tiêu vươn tới** (lựa chọn
  khác: ISSTA/ICSE). **Quyết định step-down là của bạn.**
- Phương án thay thế cho slot ICML: ý tưởng R1 (red-teaming như lấy mẫu "loài chưa thấy") có điểm ngang, nhưng chưa qua phản
  biện giả lập — xem `ideation/07_SELECTION.md`.
- Mọi review là cùng họ model (provisional).

## Việc cần làm ngay (theo thứ tự)

1. **Xác nhận máy chạy emulator:** Linux x86 có KVM (hoặc Mac arm64). Emulator không cần GPU. Môi trường cloud dùng để lập hồ sơ này **không** chạy được emulator.
2. **Pilot (a), không cần agent:** ~15 template AndroidWorld; viết ≥ 2 lộ trình UIAutomator đúng mỗi template; học mask trên một lộ trình, đo báo động giả trên lộ trình còn lại (K1).
3. **Đăng ký trước C2** — và **viết phân tích power** (đây là điểm còn mở duy nhất trong bảng atom): toán tử gieo lỗi đóng băng, danh sách họ checker, margin, cỡ ô tối thiểu, agent giữ lại.
4. **Pilot (b):** một agent rẻ trên ~30 template; đếm lỗi thật theo từng loại (K2).
5. **Review khác họ model:** chạy `ideation/XMODEL_NOVELTY_P2_PROMPT.md` và `ideation/XMODEL_REDTEAM_P2_PROMPT.md` trên GPT/Gemini.
6. Quyết định venue (ICML hay step-down) sau pilot (b).

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
