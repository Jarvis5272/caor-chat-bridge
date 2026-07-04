# Active Claim Boundary

## 可以说

- 当前原创性目标已更新为 **baseline-aware original CleanIDS algorithm**。
- 可以说新边界允许借鉴通用 baseline 模块，例如 k-mer/minimizer features、bounded local DP/alignment、local POA-like micro-consensus、medoid scaffold、edit sketches、local posterior/edit-event posterior、run-length normalization、confidence/margin。
- 可以说更精确的独立性边界是 **BBS-semantics-independent**，而不是把所有 baseline 技术都排除在外。
- 可以说 latest result 为 `results/originality_boundary_baseline_aware_update_20260704`，latest final label 为 `ORIGINALITY_BOUNDARY_BASELINE_AWARE_UPDATED`。

## 不能说

- 不能说已经找到 BBS-semantics-independent CleanIDS decoder。
- 不能说 EPBSD / BBS fork 是 independent decoder；它只能作为 BBS-compatible exact-equivalent acceleration。
- 不能把 BBS output、BBS full decoder wrapper、BBS path-likelihood / beam / pruning semantics 用作在线核心。
- 不能把 reference/truth/ED/exact/accuracy 用作在线决策。
- 不能使用 dataset name / source family route。
- 不能把 refusal-only、fallback-only 或 low-confidence-only 写成 reconstruction success。
- 不能把 TPC+OCWP 写成成功；它是 toy pass、real-data sync stop。

## 只能作为工程或算法工程结果

- EPBSD / optimized BBS fork 可以作为 BBS-compatible engineering / algorithm-engineering acceleration 结果。
- baseline-aware module reuse 可以作为设计许可，但不能自动构成算法贡献。
- bridge package 只是 ChatGPT-Codex 状态同步层，不是实验结果。

## 只能作为负证据

- TPC+OCWP、MDFC/EISC/LCPC/R3C 等停止线只能作为当前边界下的负证据。
- broad candidate sea 失败说明候选数量不是进展，不能作为发现算法的证据。

## 需要进一步验证

- 若要继续算法创新，需要先写少量深理论 method-card，明确自身 state / update / decode / confidence / stop rule。
- 若要借鉴 baseline 模块，需要逐项说明“借鉴的模块”和“原创的决策机制”。
- 任何 toy、dry-run、smoke 或 benchmark 都需要用户另行批准并保留新的 result dir。
