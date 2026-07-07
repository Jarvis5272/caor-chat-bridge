# Active Claim Boundary

## 可以说

- 当前结果是 metadata-only 同步快照，latest result 为 `results/final_full_17dataset_baseline_benchmark_20260707`。
- latest final label 是 `FINAL_FULL_17DATASET_BASELINE_COMPLETE`。
- 当前 claim boundary 是：### 可以说 (Can claim):
- On 17 datasets same-scope, our BBS-free realtime method achieves accuracy 0.9660 (between kmer_medoid 0.9663 and BBS 0.9698)
- Our method is 7.6× faster than BBS and 5.5× faster than CGBAPC (796 vs 105 vs 146 prefix/s)
- Our method is BBS-free, reference-free, online-only decode
- 10 of 17 target baselines have same-scope results; 5 external baselines and 2 MSA tools are unavailable

### 不能说 (Cannot claim):
- Cannot claim our method exceeds BBS in quality (Δacc = -0.0038)
- Cannot claim our method exceeds CGBAPC in quality (Δacc = -0.0061)
- Cannot claim our method outperforms MUSCLE/VS/BMALA/ITR/CPL (no same-scope results)
- Cannot claim BBS trio harmful is solved (11.1% harmful in BBS trio rows)
- Cannot claim final algorithm success (harmful 6.9% > 5% gate)
- Cannot use historical 4-dataset results for same-scope comparison

## 不能说

- 不能说当前结果证明 reconstruction benchmark 质量成功。
- 不能把 low-confidence/refusal 计为 decoder success。
- 不能把 method-card 或 hand-toy gate 写成 real-data proven decoder。
- 不能声称 protected code、原始数据或 original BBS source 在本轮被修改。

## 只能作为工程结果

- `chat_bridge/` 是 ChatGPT-Codex 状态同步层。
- 大文件、raw data、secret-like 文件不会被复制进 bridge。

## 只能作为负证据

- gate fail / stop label 只能作为当前路线需要修正的证据。
- missing expected files 只能作为上下文缺失，不能补写结论。
- BAEPC+FEIW 已冻结为 `full_alignment_information_required` 负证据，不得恢复为 active latest 或继续 patch。

## 需要进一步验证

- 若要继续实验、修改候选机制或进入 reconstruction smoke，需要另行批准并保留新的 result dir。
- 对 latest result 的 claim 应由 ChatGPT 审查 `chat_bridge/06_FILES_FOR_REVIEW.tsv` 中列出的源文件。
