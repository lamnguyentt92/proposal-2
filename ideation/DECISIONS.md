# DECISIONS — Nhật ký quyết định (2026-11-20)

| # | Quyết định | Lý do | Người quyết |
|---|---|---|---|
| D1 | Security lens: **on**; "red team" hiểu theo cả hai nghĩa (phản biện giả lập + cho phép đề tài bảo mật agent) | Tác giả trả lời "Cả hai" | Tác giả |
| D2 | Tài nguyên: API + 1–2 GPU; ≥ 2 annotator tiếng Việt; năng lực lý thuyết để coordinator chọn phương án tối ưu | Tác giả trả lời | Tác giả |
| D3 | Loại PROVENANCE-SUFFICIENT (IJCAI) | Audit: T1 và khung đã bị công bố; chưa có định lý | Coordinator (theo bằng chứng) |
| D4 | Loại REVOCATION-FEEDBACK (ICML) | Audit: nguy cơ cao là hệ quả của kết quả đã biết; không có bài toán mở được đặt tên | Coordinator |
| D5 | Giữ lõi SCOPE-INTERVENTIONS (ACL), viết lại | Audit: lõi ngôn ngữ học (lời thuật lại + quy chiếu ngôi tiếng Việt) chưa ai chiếm | Coordinator |
| D6 | Sinh 15 thẻ ý tưởng từ 5 góc nhìn độc lập; gộp 3 nhóm hội tụ (V1, F1, R1) | Quy trình Stage 4 | Coordinator |
| D7 | Shortlist tấn công novelty: L1, V1, F1, R1 (mỗi ý tưởng 2 hunter) | Xếp hạng gap; giới hạn chi phí — L2, T2, T3, H2, H3 để dự phòng, **chưa** tấn công | Coordinator |
| D8 | Một lần quay lại Stage 4: L1→L1R, F1→F1R, V1→V1R | Cả 4 ý tưởng bị xếp "incremental"; quy tắc cho phép một lần mài lại insight | Coordinator |
| D9 | Sau phản biện giả lập: thiết kế lại L1R→L1S, F1R→F1S | Referee: kết quả L1R đúng theo cấu tạo; devil's advocate: công cụ metamorphic của F1R bị gold-diff chi phối | Coordinator |
| D10 | Sau kill argument: sửa spec (K1–K3 thành điểm dừng thật; C2 của P2 thành kiểm định theo mode) | Atomiser: P1 1 đã trả lời/4 một phần/1 chưa; P2 1/4/1 | Coordinator |
| D11 | P1 (ACL) + P2 (ICML) là 2 proposal cuối; không đề xuất IJCAI | Điểm và gate ở `07_SELECTION.md` | **Tác giả xác nhận 2026-11-20** |
| D12 | P2 giữ đích ICML 2027 và **thêm AppWorld làm benchmark bắt buộc** (họ thứ hai) để claim tính tổng quát; không step-down lúc này | Tác giả quyết định; khuyến nghị của hai người chấm (NeurIPS E&D là "nhà" kỳ vọng) được ghi lại như một rủi ro, K2/K2b xác định khi nào step-down | **Tác giả, 2026-11-20** |
| D13 | Testbed của P2: máy tính chạy emulator + 3 điện thoại Android thật root bằng Magisk; thêm nhánh lặp lại trên máy thật (claim hỗ trợ C5) | Tác giả khai báo tài nguyên; máy thật cho phép kiểm tra kết quả không phải là artefact của emulator | Tác giả (tài nguyên) + coordinator (thiết kế) |

## Sai lệch so với quy trình chuẩn (ghi để minh bạch)
- **Chưa có review khác họ model.** Mọi verdict novelty và phản biện là same-family (provisional). File prompt cho đường thủ công đã chuẩn bị (`XMODEL_*`). Gate G2 và Stage 6 chỉ thực sự qua khi có review khác họ model hoặc tác giả ghi miễn trừ.
- **Devil's advocate cho L1R không chạy được** (lỗi khởi chạy); vai trò được bù bằng referee review, kill argument và atomiser.
- **Panel phản biện rút gọn:** V1R chỉ có một review gộp; R1 chưa qua Stage 6.
- **Nhánh AppWorld và nhánh máy thật của P2** được thêm sau lượt quét novelty và phản biện cuối; chưa bị tấn công. Số liệu AppWorld (9 app, 457 API, 750 tác vụ, đánh giá theo trạng thái có kiểm collateral damage) lấy từ bản ghi bài báo; việc AppWorld kèm lời giải tham chiếu là theo báo cáo audit khả thi, cần xác nhận ở commit được ghim.
- **Sau thiết kế lại lần cuối** (spec hiện tại), C1/C3 của P1 và C2 của P2 mới chỉ qua một drift scan/kill argument, chưa qua hai hunter độc lập.
- **Calibration venue** dựa trên tiêu đề và abstract, chưa đọc toàn văn 10–20 bài mỗi venue.
- **Chưa có `02_bibliography.bib`.** Danh mục tham khảo nằm trong các báo cáo `05_NOVELTY/` kèm mức kiểm chứng (toàn văn / abstract / chỉ mục). Tạo BibTeX từ identifier khi viết bài và đối chiếu từng mục với bản ghi gốc.
- **Giới hạn tìm kiếm:** Google Scholar, Semantic Scholar (giới hạn tần suất), OpenAlex, dblp, toàn văn ACM/IEEE, PDF và review trên OpenReview, bài ARR không công khai, venue tiếng Việt. Nhiều mục tháng 10–11/2026 là preprint chưa bình duyệt.
- **Không chạy thí nghiệm nào.** Mọi con số về hệ thống (cửa sổ 10 message của Mem0, 3 episode của Graphiti, regex chuẩn hoá tên, số template có nghịch đảo trong AndroidWorld) là đọc code tại commit được ghi trong báo cáo, không phải kết quả chạy.
