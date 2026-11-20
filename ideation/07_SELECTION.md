# 07_SELECTION — Chấm điểm, gate và quyết định (2026-11-20)

Hai người chấm độc lập (không thấy điểm của nhau): **selector** (`07_SELECTION_scores_selector.md`) và **referee phản biện**
(`07_SELECTION_scores_referee.md`). Cả hai là cùng họ model với coordinator → kết quả **tạm thời (same-family, provisional)**
cho tới khi có review khác họ model (xem các file `XMODEL_*`). Mọi điểm số là đánh giá trên **kế hoạch**, chưa có dữ liệu hay pilot.

## 1. Điểm theo rubric (1–5)

| Tiêu chí (trọng số) | P1 ACL (selector / referee) | P2 ICML | V1R ACL | R1 ICML |
|---|---|---|---|---|
| Novelty (0,35) | 3,5 / 3,5 | 3,0 / 3,0 | 3,0 / 3,0 | 2,5 / 2,5 |
| Venue fit & bar (0,25) | 3,5 / 4,0 | 2,5 / 3,0 | 3,0 / 3,0 | 3,0 / 3,5 |
| Significance (0,15) | 3,0 / 3,0 | 3,0 / 3,0 | 2,0 / 2,0 | 3,5 / 3,5 |
| Evaluation clarity (0,10) | 3,5 / 3,5 | 4,0 / 4,0 | 2,5 / 2,5 | 3,0 / 3,5 |
| Mở rộng lên journal (0,05) | 4,0 / 4,0 | 3,5 / 3,5 | 3,0 / 3,0 | 3,5 / 4,0 |
| Khả thi kỹ thuật (0,05) | 4,0 / 4,0 | 3,0 / 3,5 | 3,5 / 3,0 | 3,0 / 3,0 |
| Rủi ro đạo đức, đảo (0,05) | 4,0 / 4,0 | 4,5 / 4,5 | 3,0 / 3,0 | 3,5 / 3,5 |
| **Tổng có trọng số** | **3,50 / 3,625** | **3,075 / 3,225** | **2,825 / 2,80** | **2,95 / 3,15** |

Không có tiêu chí nào lệch ≥ 2 điểm giữa hai người chấm. Khoảng cách P1–P2 bền vững với mọi thay đổi nửa điểm đơn lẻ;
P2 và R1 **không tách được** về điểm (chênh 0,075–0,125, nằm trong nhiễu chấm).

Dải xác suất được nhận main track (đánh giá của referee, **không phải phép đo**, điều kiện là thực thi tốt):
P1 10–25% (đầu trên của dải; tính cả Findings: 25–40%); P2 10–25% (nửa dưới); R1 10–25% (cận dưới, sau khi viết lại); V1R < 10%.

## 2. Gate (theo selector)

| Gate | P1 | P2 | V1R | R1 |
|---|---|---|---|---|
| G1 venue fit | Có điều kiện (phụ thuộc pilot) | Có điều kiện (fit 3/5; "audit một hệ sinh thái") | Có điều kiện (dự đoán Findings) | Có điều kiện |
| G2 novelty | Có điều kiện (lõi dyad chưa bị anticipate; C1/C3 bản mới chưa được quét lại) | Có điều kiện (chỉ C2 sạch) | Có điều kiện (delta hẹp) | Có điều kiện (delta ghi trong thẻ đã lỗi thời) |
| G3 significance | Có điều kiện (chưa đo mức xuất hiện tự nhiên) | Có điều kiện | **Trượt** (attacker né được miễn phí) | Đạt |
| G4 khả thi | Đạt | Có điều kiện (chưa xác nhận máy KVM; chưa biết mask khả thi) | Có điều kiện | Có điều kiện (chưa audit) |
| G5 falsifiability | Đạt | Đạt | **Trượt** (2/4 claim không thể sai) | Có điều kiện |
| G6 integrity | Đạt | Đạt | Có điều kiện (tranh tài nguyên và slot với P1) | Có điều kiện (chưa qua Stage 6) |

## 3. Kết luận trung thực

**Chưa finalist nào vượt mức chuẩn A\* trên giấy.** P1 gần nhất (3,50–3,63 so với ngưỡng 4,0). Đây là bức tranh thật của
vùng chủ đề agent/memory/đánh giá agent cuối 2026: mọi ý tưởng đưa vào tấn công novelty đều ra "incremental với một lõi hẹp
còn mới". Sự khác biệt giữa các finalist nằm ở việc lõi đó có được bảo vệ bởi nguồn lực riêng của nhóm hay không.

Điều kiện để P1 chạm ngưỡng (selector chấm lại ≈ 3,95 nếu đủ 1–3):
1. Pilot: format gap trên item từ thân tộc vượt control (C1), hoặc extractor mạnh nhất lệch khỏi phân bố đọc của người bản ngữ (C2).
2. Chạy end-to-end trên Mem0 và Graphiti: lỗi gộp/nhầm người vẫn còn sau khi thêm một dòng prompt tiếng Việt (C3).
3. Study 0 vượt ngưỡng 5% đã cố định, ở hơn một vùng miền.
4. Quét novelty lại cho C1/C3 bản mới + review khác họ model.
5. Người bản ngữ xác nhận các ví dụ tiếng Việt.

## 4. Quyết định của tác giả (2026-11-20)

- **Chốt cặp proposal:** P1 (ACL 2027) và P2 (ICML 2027).
- **P2 giữ đích ICML** và thêm **AppWorld** làm benchmark bắt buộc để tăng tính tổng quát (không step-down lúc này).
- **Testbed P2:** máy tính chạy emulator + 3 điện thoại Android thật đã root (Magisk).

Phần dưới đây là đề xuất gốc của coordinator, giữ lại để đối chiếu.

## 4b. Đề xuất ban đầu cho tác giả

| Slot | Đề xuất | Venue | Trạng thái |
|---|---|---|---|
| **Proposal 1** → repo `proposal-1` | **P1 — Who Is "con"? Dyad-anchored person reference khi agent ghi bộ nhớ tiếng Việt** (phát triển tiếp từ SCOPE-INTERVENTIONS) | ACL 2027 (ARR), area Discourse & Pragmatics | CONDITIONAL GO — qua pilot gate K1–K3 |
| **Proposal 2** → repo `proposal-2` | **P2 — Are the Passes Real? Audit mức trạng thái cho phán quyết của benchmark mobile agent + kiểm định transfer của mutation score** (ý tưởng mới) | ICML 2027, area Evaluation | CONDITIONAL GO — qua pilot gate K1–K2 |

**Về step-down cho P2:** cả hai người chấm khuyên trình bày **NeurIPS Evaluations & Datasets là "nhà" kỳ vọng và ICML là mục
tiêu vươn tới** (lựa chọn khác: ISSTA/ICSE). Lý do: novelty incremental theo chính drift scan, venue fit 3/5. Quyết định
step-down chỉ có hiệu lực khi tác giả xác nhận.

**Phương án thay thế cho slot ICML:** R1 (red-teaming như lấy mẫu "loài chưa thấy") có điểm ngang P2 nhưng **chưa qua phản
biện giả lập, chưa audit khả thi**, phương pháp vay mượn toàn bộ, và có đối thủ có lý thuyết mới 9 ngày tuổi
(arXiv:2611.15835). P2 được chọn vì đã bị tấn công và sửa, và khớp chuyên môn kiểm thử Android. Nếu tác giả ưu tiên xác suất
ở ICML, bước rẻ nhất tiếp theo là viết lại và phản biện R1.

**IJCAI 2027:** không đề xuất proposal. Proposal gốc bị loại; không ý tưởng dự phòng nào hợp IJCAI hơn hai lựa chọn trên; và
IJCAI chỉ cho dùng LLM để trau chuốt văn bản do tác giả tự viết, nên hồ sơ AI hỗ trợ này không dùng trực tiếp được ở đó.

## 5. Phương án bị loại và lý do
Xem `IDEA_REGISTRY.md`.
