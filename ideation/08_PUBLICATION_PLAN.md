# 08_PUBLICATION_PLAN — Kế hoạch công bố (2026-11-20)

Nguyên tắc: thời hạn **không** quyết định ý tưởng. Nếu chưa qua pilot gate kịp một chu kỳ, chuyển sang chu kỳ kế tiếp.
Ngày tháng lấy từ `01_VENUES.md` (đã kiểm chứng từ CFP chính thức ngày 2026-11-20).

## Proposal 1 — ACL 2027 (qua ARR)

**Bài hội nghị (8 trang long paper).** Một đóng góp sắc: ghi bộ nhớ từ tiếng Việt đòi hỏi quy chiếu ngôi theo dyad, và
hệ thống bộ nhớ biến khó khăn đó thành lỗi bền vững.

| Phần | Trang (ước lượng) |
|---|---|
| Mở đầu + ví dụ xuyên suốt ("Mẹ bảo con về quê ăn Tết") | 1,0 |
| Hiện tượng ngôn ngữ + mô hình anchor/dyad ngắn | 1,0 |
| Study 0 (mức xuất hiện tự nhiên) | 0,75 |
| Benchmark, gold phân bố, độ đồng thuận | 1,5 |
| Thí nghiệm C1–C4 (+ C5 hỗ trợ) | 2,5 |
| Liên quan + giới hạn + đạo đức | 1,25 |

Artifact: benchmark (CC BY 4.0), script chấm, prompt/context đã log, bản vá can thiệp.

**Mốc (theo thứ tự, không theo ngày cứng):**
1. Người bản ngữ xác nhận ví dụ; cố định ngưỡng (đã ghi trong spec §5).
2. Pilot gate K1–K3: 60 family chẩn đoán + 40 lượt elicited; 3 backbone; ≥ 3 lượt end-to-end mỗi framework.
3. Review khác họ model (file `XMODEL_*_P1_*`) + quét novelty lại cho C1/C3.
4. Study 0 đầy đủ + sổ tay annotation → thu thập đầy đủ → thí nghiệm.
5. Viết (tác giả tự viết) → hai vòng review nội bộ (quy trình `research-paper-review`).

Chu kỳ: ARR **4 Jan 2027** (ACL 2027, Kyoto 17–22 Aug 2027). Nếu chưa qua mốc 2–4: các chu kỳ ARR kế tiếp → EMNLP 2027.
Điều kiện nộp ARR: cần một tác giả đủ chuẩn đóng góp review (mỗi người tối đa 2 bài), nếu không bài vào diện bốc thăm.
Khai báo AI trong Responsible NLP checklist.

**Bản mở rộng tạp chí:** *Computational Linguistics* (nhận bản mở rộng đáng kể; **không** dùng TACL — không nhận bản mở
rộng và cấm 9 tháng với bài đã gửi ARR). Nội dung mới: mô hình anchor/dyad tường minh; sổ tay annotation + phân tích bất
đồng; ngôn ngữ thứ hai có từ thân tộc/kính ngữ + một ngôn ngữ pro-drop đối chứng; code-switching VI–EN; nghiên cứu hậu quả
quy mô lớn hơn. Tiêu đề và tóm tắt mới; trích bài hội nghị. Quartile JCR: **chưa kiểm chứng** — tra JCR trước khi chốt.

## Proposal 2 — ICML 2027 (area Evaluation)

**Bài hội nghị (8 trang + phụ lục).** Một đóng góp sắc: tỉ lệ sót của bộ chấm đo bằng lỗi gieo có chuyển sang lỗi thật của
agent hay không, đo được nhờ chân trị mức trạng thái.

| Phần | Trang (ước lượng) |
|---|---|
| Mở đầu + ví dụ xuyên suốt (một template AndroidWorld có checker chỉ kiểm postcondition) | 1,0 |
| Định nghĩa lỗi phán quyết + phát biểu nhận dạng | 1,0 |
| Oracle vi sai với mask đa lộ trình; kiểm chứng | 1,5 |
| C1 (tỉ lệ sai hai chiều trên 3 benchmark, phần chỉ thấy ở mức trạng thái) | 1,25 |
| C2 (kiểm định transfer theo mode, đăng ký trước) | 1,75 |
| C3–C4, liên quan, giới hạn | 1,5 |

Artifact: state observer, script lộ trình tham chiếu, mask, kill matrix, nhãn audit, code phân tích (Apache-2.0).

**Mốc:**
1. Testbed đã được tác giả xác nhận (máy tính chạy emulator + 3 điện thoại root bằng Magisk). Kiểm tra ảo hoá trên máy tính (Linux: `/dev/kvm`).
2. Pilot (a) không cần agent: mask học trên một lộ trình đúng, đo báo động giả trên lộ trình đúng khác (K1).
3. Đăng ký trước C2: toán tử gieo lỗi (đóng băng), họ checker, margin, cỡ ô tối thiểu, agent giữ lại; **viết phân tích power**.
4. Pilot (b) với một agent rẻ trên ~30 template (K2).
5. Review khác họ model (file `XMODEL_*_P2_*`).
6. Dựng AppWorld và tái lập kết quả mutant đã công bố của arXiv:2610.09142; kiểm tra khả thi nhánh máy thật (`su -c` thay cho `adb root`).
7. Chạy đầy đủ trên **AndroidWorld + MobileWorld + AppWorld** (AppWorld là bắt buộc theo quyết định của tác giả) → audit mù → phân tích → lặp lại trên máy thật cho 10–15 template.
8. Viết → hai vòng review nội bộ.

Chu kỳ: ICML 2027 abstract **14 Jan**, full paper **22 Jan 2027** (Rio de Janeiro, 31 Jul – 6 Aug 2027). Nếu chưa qua mốc:
NeurIPS 2027. **Tác giả đã chọn giữ ICML** (2026-11-20); NeurIPS Evaluations & Datasets và
ISSTA/ICSE là phương án lùi khi K2/K2b kích hoạt. Điều kiện nộp ICML: một reciprocal reviewer mỗi bài; tác giả không đủ điều kiện review chỉ đứng tên ≤ 2 bài;
bắt buộc AI Disclosure Statement (khai cả ideation, tổng hợp tài liệu, thiết kế thí nghiệm).

**Bản mở rộng tạp chí:** JAIR hoặc AIJ (đều nhận bản mở rộng đáng kể). Nội dung mới: benchmark an toàn (chiều "bỏ sót tác
hại"), benchmark desktop/web, tổng hợp tự động lộ trình tham chiếu, phân tích nhận dạng đầy đủ, sửa checker từ lỗi sống sót.
Quartile JCR: **chưa kiểm chứng**.

## Quy tắc chung
- Không dual-submit: mỗi bản thảo chỉ một venue (ARR nêu đích danh IJCAI và ICML).
- Hai bài không chia chung một kết quả; không trùng claim.
- Quét novelty lại ở mỗi mốc lớn (sau pilot, trước khi viết, trước khi nộp tạp chí): cả hai vùng đều có 6–10 preprint mới mỗi quý.
