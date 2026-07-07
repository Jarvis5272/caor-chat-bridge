# Active Claim Boundary

## 可以说

- 当前结果是 metadata-only 同步快照，latest result 为 `results/final_full_17dataset_baseline_benchmark_20260707`。
- latest final label 是 `FINAL_BENCHMARK_PARTIAL_EXTERNAL_COMPLETE_PENDING`。
- 当前 claim boundary 是：### Can claim:
- OUR_REALTIME_METHOD accuracy 0.9660 on CAPPED_17_MATCHED (82,462 rows)
- Wall-clock runtime 103.53s, 796 prefix/s, BBS-free online decode
- Row keys verified (SHA256: 7ac2b177...)
- CAPPED_17_MATCHED is the defined fair comparison scope for ALL methods

### Cannot claim:
- Cannot claim speedup vs BBS/CGBAPC/kmer_medoid until they are rerun on same keys
- Cannot claim position vs MUSCLE/VS/BMALA/ITR/CPL until they complete
- Cannot claim FULL_17 (495K) scope completion
- Cannot use historical 495K metrics for direct comparison with 82K scope

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
