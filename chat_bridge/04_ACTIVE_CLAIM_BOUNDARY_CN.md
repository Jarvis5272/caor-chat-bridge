# Active Claim Boundary

## 可以说

- 当前结果是 metadata-only 同步快照，latest result 为 `results/adaptive_quality_speed_pareto_explorer_wave4_20260706`。
- latest final label 是 `PARETO_WAVE4_CONTINUE_REQUIRED_WITH_UNTESTED_FRONTIER`。
- 当前 claim boundary 是：可以说：Wave4 必测 frontier CPES/RDIS/SWMC 已完成，且 Wave4 失败后自动验证了 Wave5 候选 PSEC/ISPC/WRMC；所有 tested candidates 都保持 observed-only selector、no BBS/EPBSD online、no reference online、no dataset route。可以说这些候选在 aggregate quality 上相对 best simple baseline 有小幅正信号。

不能说：不能 claim target success、不能 claim clean IDS realtime reconstruction algorithm found、不能 claim BBS replacement、不能把 source-gap/projected 正信号覆盖 BBS trio collapse、不能把 fallback/refusal 或 posterior-heavy replay 当作成功。当前 blocking reason 是 BBS trio group gate 与 safety gate 未通过，部分候选同时未达到 speed gate。

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

## 需要进一步验证

- 若要继续实验、修改候选机制或进入 reconstruction smoke，需要另行批准并保留新的 result dir。
- 对 latest result 的 claim 应由 ChatGPT 审查 `chat_bridge/06_FILES_FOR_REVIEW.tsv` 中列出的源文件。
