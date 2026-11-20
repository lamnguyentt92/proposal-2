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
| D13 | Testbed của P2: MacBook + máy Windows chạy emulator, 3 điện thoại Android thật root bằng Magisk (`adb root` và `su` dùng được, theo tác giả); thêm nhánh lặp lại trên máy thật (claim hỗ trợ C5) | Tác giả khai báo tài nguyên; máy thật cho phép kiểm tra kết quả không phải là artefact của emulator | Tác giả (tài nguyên) + coordinator (thiết kế) |
| D14 | **Quy tắc ưu tiên khi không kịp cả hai:** dồn nguồn lực cho bài có khả năng được nhận và novelty cao nhất → **Proposal 1 trước, Proposal 2 sau** | Tác giả đặt quy tắc; theo hai người chấm P1 có novelty 3,5 so với 3,0, lõi được quét là *novel* so với *incremental*, và dải xác suất main track cao hơn | **Tác giả, 2026-11-20** (áp dụng quy tắc: coordinator) |
| D15 | Dựng bộ pilot của Proposal 1 trước (bản 0.1.0, thư mục `pilot/` và `impl/` trong repo proposal-1) | Tác giả chọn; khớp quy tắc ưu tiên D14 | **Tác giả, 2026-11-20** |
| D16 | Quy tắc dừng K1/K2 ở pilot chỉ kích hoạt khi có bằng chứng dương rằng hiệu ứng nhỏ; thêm trạng thái WARN (mở rộng pilot một lần) | Mô phỏng: với 60 family, "không vượt control" xảy ra thường xuyên ngay cả khi hiệu ứng thật là +15 điểm | Coordinator đề xuất — **chờ tác giả duyệt** (`impl/05_PREREG_PILOT.md` mục 4) |
| D17 | Nhận gần như toàn bộ điểm của 4 review GPT-6 sau khi kiểm chứng 30 trích dẫn; sửa đặc tả hai proposal | Xem `XMODEL_TRIAGE_P1.md`, `XMODEL_TRIAGE_P2.md` | Coordinator (theo bằng chứng) |
| D18 | P1: claim riêng của bộ nhớ là phần tăng do hợp nhất (C3); quy tắc đóng khung F1; thêm baseline bộ nhớ episodic; tách ba loại lỗi ở mức kho; Study 0 hai nhánh; thước đo cross-fitted (bộ pilot 0.1.1) | Reviewer: thiết kế cũ có thể cho kết quả có ý nghĩa thống kê mà không cô lập được cơ chế của bộ nhớ; ngưỡng 10% với 8 rater là 0 phiếu | Coordinator |
| D19 | P2: thêm hợp đồng đúng-sai theo tác vụ, audit hai pha có trọng số, hai estimand cho C2, bốn ước lượng trên agent giữ lại, baseline kiểu VeriCUA; đổi câu định vị | Reviewer: chân trị chưa độc lập với công cụ; C2 có thể chỉ đo lệch phân bố; tiêu chí "trong 2 điểm" đạt được mà không cần hiệu chỉnh | Coordinator |
| D20 | Gate G2 và Stage 6 của cả hai proposal: **WARN** sau review khác họ model | Verdict "incremental" và "weak reject ở giai đoạn ý tưởng" | **Chờ tác giả ký duyệt** |
| D21 | Mở vòng ý tưởng 2: bỏ hạn 4 Jan 2027, không giới hạn nhân lực/máy, security lens bật (red/blue), novelty là tiêu chí số một | Tác giả phê bình vòng 1 cho ra ý tưởng incremental; lời tác giả 2026-11-20 | Tác giả |
| D22 | Vòng 2: 4 ý tưởng vào vòng trong (M1, B1, E2, A2); cả 9 báo cáo săn tiền lệ đều "incremental"; không ý tưởng nào được trình là "novel" | `round2/05_NOVELTY/`, `round2/07_SELECTION_R2.md` | Coordinator (theo bằng chứng) |
| D23 | Sửa nhận định của chính coordinator: so sánh "tên Việt 24–27% vs tên Anh 0%" bị nhiễu thiết kế; khi đổi họ, tiếng Anh là 17,1% | Referee tự chạy lại probe (`round2/checks/m1_referee_probe.json`) | Coordinator |
| D24 | Bộ pilot 0.1.2: vá adapter Graphiti (driver Kuzu nhúng không chạy được) | Lỗi lộ ra khi chạy pipeline ingest đầy đủ offline | Coordinator |
| D25 | Hướng đi sau vòng 2 (gộp phát hiện về tên vào P1 / theo M1R như bài security / vòng 3 từ dữ liệu riêng của tác giả) | `round2/07_SELECTION_R2.md` mục 6 | **Chờ tác giả** |
| D26 | Dùng API key do tác giả cấp cho thí nghiệm, chỉ với hai model rẻ nhất (`claude-haiku-4-5-20251001`, `claude-haiku-5-5`); key lưu ngoài repo, không ghi vào file hay log | Lời tác giả 2026-11-20: "chọn model tiết kiệm" | Tác giả |
| D27 | Bộ pilot 0.1.3: cho phép bỏ tham số temperature và seed (model mới từ chối temperature); ghi token vào nhật ký | Lỗi 400 khi gọi `claude-haiku-5-5` | Coordinator |
| D28 | M1R: kế hoạch và cách đọc cho lượt chạy model thật được viết trước khi chạy; kết quả: C1 đứng vững trên Graphiti (12/13 ở cả hai model); phân loại chi tiết thêm sau được ghi là mô tả | `round2/checks/m1_real_model_PLAN.md`, `m1_real_model_RESULT.md` | Coordinator (theo bằng chứng) |
| D29 | Sai sót của coordinator: một lượt chạy bị mất kết quả do lỗi harness, lãng phí 221.206 token vào và 10.939 token ra | Ghi ở mục Deviations của kế hoạch | Coordinator |
| D30 | Tác giả cho phép thử model mới hơn và mạnh hơn; đồng ý đổi trọng tâm Proposal 1 sang tên riêng nếu hợp venue; muốn giữ hướng security (chuyên môn của tác giả) | Lời tác giả 2026-11-20, 21:46 | Tác giả |
| D31 | Bộ pilot 0.1.4: bảng chấm dạng Excel có hướng dẫn, ví dụ, danh sách chọn; sửa lỗi ô bắt đầu bằng "-" bị đọc thành công thức | Tác giả báo lỗi `#NAME?` khi mở file CSV | Coordinator |
| D32 | S1 (quyền theo người trong bộ nhớ dùng chung): kế hoạch viết trước; kết quả 4/4 cặp trùng khoá, 2/2 control; hai lượt săn tiền lệ: incremental, mô hình đe doạ còn là giả định với sản phẩm hiện nay | `round2/checks/s1_shared_graph_*`, `round2/05_NOVELTY/IDEA_S1_priorart_*` | Coordinator (theo bằng chứng) |
| D33 | Sửa phân loại ở lượt chạy model mạnh (node dẫn xuất bị đếm nhầm là người); ghi rõ là hậu kiểm. Với sonnet/opus, việc dữ kiện bị gắn nhầm chỉ thấy ở 3/12 và 4/13 | `round2/checks/m1_real_model_RESULT.md` | Coordinator |
| D34 | Một bài duy nhất về định danh người trong bộ nhớ agent; venue quyết định theo thí nghiệm trên hệ thống thật / agent thật | Tác giả đồng ý 2026-11-20, 22:14 | Tác giả |
| D35 | S2 (agent xoá dữ liệu người được nhắc tên): ngưỡng "làm hại người thứ ba" không đạt (1/8 lượt); "xoá không hết" không được ủng hộ. Theo quy tắc đã thống nhất, venue nghiêng về ACL/EMNLP | `round2/checks/s2_agent_erasure_PLAN.md`, `_RESULT.md` | Coordinator (theo bằng chứng) |
| D36 | Nhãn GPT-6 cho pilot thu nhỏ được lưu là "model chấm, tạm thời"; không dùng cho claim cho đến khi có nhãn của người | Tác giả: "Con người hiện tại chưa có, sẽ làm sau" | Tác giả / Coordinator |
| D37 | Chốt venue (ACL/EMNLP ngay, hay thử thêm kịch bản khó hơn cho hướng security trước) | `round2/07_SELECTION_R2.md` mục 9 | **Chờ tác giả** |

## Sai lệch so với quy trình chuẩn (ghi để minh bạch)
- **Review khác họ model đã có (GPT-6, 2026-11-20)** cho novelty và phản biện của cả hai proposal; các bản đặc tả gửi đi đã lược mục 13 và các câu dự đoán để reviewer tự đánh giá. Các sửa đổi sau review (D18, D19) **chưa** được review lại.
- **Devil's advocate cho L1R không chạy được** (lỗi khởi chạy); vai trò được bù bằng referee review, kill argument và atomiser.
- **Panel phản biện rút gọn:** V1R chỉ có một review gộp; R1 chưa qua Stage 6.
- **Nhánh AppWorld và nhánh máy thật của P2** được thêm sau lượt quét novelty và phản biện cuối; chưa bị tấn công. Số liệu AppWorld (9 app, 457 API, 750 tác vụ, đánh giá theo trạng thái có kiểm collateral damage) lấy từ bản ghi bài báo; việc AppWorld kèm lời giải tham chiếu là theo báo cáo audit khả thi, cần xác nhận ở commit được ghim.
- **Sau thiết kế lại lần cuối** (spec hiện tại), C1/C3 của P1 và C2 của P2 mới chỉ qua một drift scan/kill argument, chưa qua hai hunter độc lập.
- **Calibration venue** dựa trên tiêu đề và abstract, chưa đọc toàn văn 10–20 bài mỗi venue.
- **Chưa có `02_bibliography.bib`.** Danh mục tham khảo nằm trong các báo cáo `05_NOVELTY/` kèm mức kiểm chứng (toàn văn / abstract / chỉ mục). Tạo BibTeX từ identifier khi viết bài và đối chiếu từng mục với bản ghi gốc.
- **Giới hạn tìm kiếm:** Google Scholar, Semantic Scholar (giới hạn tần suất), OpenAlex, dblp, toàn văn ACM/IEEE, PDF và review trên OpenReview, bài ARR không công khai, venue tiếng Việt. Nhiều mục tháng 10–11/2026 là preprint chưa bình duyệt.
- **Không chạy thí nghiệm nào.** Mọi con số về hệ thống (cửa sổ 10 message của Mem0, 3 episode của Graphiti, regex chuẩn hoá tên, số template có nghịch đảo trong AndroidWorld) là đọc code tại commit được ghi trong báo cáo, không phải kết quả chạy.
