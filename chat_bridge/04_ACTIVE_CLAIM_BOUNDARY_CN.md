# Active Claim Boundary

## 可以说

- 当前结果是 metadata-only 同步快照，latest result 为 `results/baepc_toy_only_prototype_20260704`。
- latest final label 是 `BAEPC_TOY_PASS_GO_TO_REAL_DATA_SYNC_DRYRUN`。
- 当前 claim boundary 是：Online state machine 只读取 observed reads。Hidden target 只在 offline toy audit 中用于 ED/exact。没有 BBS output、BBS score/beam/pruning/path likelihood、EPBSD kernel、STWC/CAOR core、dataset/source route、full alignment、POA 或 graph。

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
