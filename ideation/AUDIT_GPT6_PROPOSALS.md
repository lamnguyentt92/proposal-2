# Thẩm định 3 proposal của GPT-6 (bản v5) — 2026-11-20

Phương pháp: mỗi proposal được một luồng độc lập (a) kiểm chứng từng trích dẫn bằng bản ghi gốc, (b) săn prior-art
theo hướng "cố tìm cho ra ý tưởng đã được công bố". Ghi chú đầy đủ: `research_notes/…/*_audit.md`.
Giới hạn chung: chưa tìm trên OpenReview (bài đang review ở ICLR 2027), Google Scholar, Semantic Scholar; nhiều bài
tháng 10–11/2026 là preprint chưa bình duyệt. "Không tìm thấy" không chứng minh "không tồn tại".

## Kết luận nhanh

| Proposal | Trích dẫn | Novelty | Quyết định |
|---|---|---|---|
| IJCAI — PROVENANCE-SUFFICIENT | 8/8 có thật, khớp | **Incremental; khung và T1 đã bị công bố** | **BỎ** (ghi vào idea registry) |
| ICML — REVOCATION-FEEDBACK | 8/8 có thật, khớp (2 chỗ diễn đạt lỏng) | **Incremental; nguy cơ cao là hệ quả của kết quả đã biết** | **BỎ** (ghi vào idea registry) |
| ACL — SCOPE-INTERVENTIONS | 8/8 có thật, khớp | **Incremental như đang viết, nhưng còn một lõi chưa ai chiếm** | **GIỮ lõi, viết lại** |

Điểm tích cực: GPT-6 không bịa trích dẫn nào. Điểm yếu chung: cả ba **thiếu trích dẫn** đúng những bài đe doạ novelty nhất.

## 1. IJCAI 2027 — PROVENANCE-SUFFICIENT → BỎ

- **Định lý T1 đã có.** "Cùng tập fact và marginal, khác cấu trúc sao chép → quyết định đúng khác nhau" là Theorem 1 của
  *Replication or Corroboration?* (arXiv:2610.36151) và *Epistemic Sybil Resistance* (arXiv:2609.01873).
- **Tiêu chí ε-sufficiency gần trùng** tiêu chí distortion của DeMem (arXiv:2605.10870, NeurIPS 2026 poster) và
  approximate information state (Subramanian et al., JMLR 2022), chỉ thêm hành động truy vấn.
- **"Verification allocator" đã có** trong AMV-Guard (arXiv:2610.31446, chính proposal trích).
- **Referee planning/KR** sẽ mã hoá "ai chép ai" thành biến ẩn → bài toán thành phân tích width/relevance
  (Bonet & Geffner, JAIR 2014) và knowledge compilation.
- **Phần còn mở** (cần định lý thật): phụ thuộc có mức độ; độ bền khi nhãn lineage sai; tách biệt succinctness so với
  factored/compiled belief. Chưa có gì được chứng minh.
- **Ràng buộc venue:** IJCAI cấm nội dung do LLM sinh; 7 trang.
- Chính proposal tự xếp "NO-GO / small formal pilot" — đánh giá đó đúng.
- **Điều kiện hồi sinh:** chứng minh được một kết quả loại A (graded dependence) hoặc C (robustness to label errors) → nhắm KR/ICAPS/AAMAS.

## 2. ICML 2027 — REVOCATION-FEEDBACK → BỎ

- **Các thành phần đã được công bố riêng cho agent memory trong 5 tháng qua:**
  - Gating bộ nhớ = contextual apple tasting, phản hồi một phía có trễ, regret Õ(Tε ∧ d√T) — arXiv:2610.23812.
  - Định lý non-identifiability cho bộ nhớ không bao giờ được truy xuất + luật Bayes-tối ưu cho quên không đảo ngược — arXiv:2610.02070.
  - Mô hình censored-feedback cho context của agent, cận dưới tuyến tính hai-thế-giới — arXiv:2610.11007.
  - Caching có switching cost cho buffer truy xuất — arXiv:2607.00394.
  - Phân loại đầy đủ √T / T^{2/3} / T cho feedback graph có switching cost — arXiv:2606.03851.
  - Sleeping RL (ICML 2025); MemPrice (arXiv:2610.24955) đã có cận dưới tuyến tính khi nén không đảo ngược.
- **Ba phép quy dẫn khả dĩ** (suy luận của người thẩm định, chưa chứng minh): POMDP/Exo-MDP với động lực lưu trữ đã biết;
  apple tasting/bandit hai tay có switching cost + sleeping; restless bandit.
- **"Reachable same-information comparator" chưa phải là định nghĩa**: hoặc tầm thường, hoặc trùng benchmark informed-policy chuẩn.
- **Không tìm thấy bài toán mở được đặt tên** ở giao điểm này.
- **Phương án dự phòng T4** (bài evaluation) cũng trùng một phần với arXiv:2609.08258, 2610.18052, 2609.08279, 2610.00366.
- Chưa có định lý nào; tập trạng thái, lớp comparator, coupling và loại adversary còn chưa định nghĩa.
- **Điều kiện hồi sinh:** một tách biệt thật (cấu trúc phản hồi thay đổi theo trạng thái quyền, tốc độ không suy ra được từ việc ghép các hạng tử đã biết).

## 3. ACL 2027 — SCOPE-INTERVENTIONS → GIỮ LÕI, VIẾT LẠI

**Đã bị chiếm (phải cắt hoặc hạ thành baseline):**
- Nội dung hedged/suy đoán bị ghi thành fact: AgentMemGate (arXiv:2610.07707) — Mem0 35,2% và Graphiti 27,3% kế hoạch treo
  bị ghi thành hiện thực; có metric tương tự FUPR/LFRR; "cautious extractor" giảm xuống 2,5% trên bộ lõi.
- Ba nhánh can thiệp bộ nhớ (đúng / méo / vắng) với task cố định: DerivAudit (arXiv:2609.36130).
- Hạch toán lỗi theo giai đoạn: HaluMem (arXiv:2511.03506); MemGuard (arXiv:2605.28009).
- Attribution confusion mức thô từ dữ liệu người dùng thật: arXiv:2609.33623; MemAlign/ConMem (arXiv:2610.33432).
- So sánh no-memory / transcript / note tự viết: The Memory Trap (arXiv:2611.07554).
- Consent/contextual integrity: đông (CIMemories, PersistBench, GateMem, ConCI, SP-Mem) → **cắt RQ2 (permission ledger)**.
- PASB đã xoá lịch sử giữa pha ghi và pha hỏi; TimlMemBench đã đối chiếu pool sạch với session tự nạp.

**Chưa ai chiếm (lõi của proposal mới):**
- Lai ≥2 toán tử (lời thuật lại × điều kiện × phủ định × trích dẫn) với tổ hợp held-out.
- Khung mệnh đề gắn span, có trường người-nói-nhúng và mức cam kết, **gold do người gán**.
- Quy thuộc trích dẫn/lời thuật lại ở thời điểm ghi bộ nhớ.
- Tiếng Việt/VI–EN trong không gian memory: không thấy bài nào. "Thêm một ngôn ngữ" là lập luận yếu — phải dựa trên
  hiện tượng bản địa (từ thân tộc dùng như đại từ, chủ ngữ ẩn).
- Hội thoại do người viết hoàn toàn (các bài lân cận dùng dữ liệu LLM sinh + người duyệt).

**Cảnh báo quy mô:** pilot 40–60 family nhỏ hơn 1–2 bậc so với benchmark được nhận (1.000–5.000 mục, 5–30 cấu hình).
TWIST (arXiv:2609.28575): κ thô trên tương phản ngữ dụng chỉ 0,565, đạt 0,851 sau khi bỏ 39/200 mục.
