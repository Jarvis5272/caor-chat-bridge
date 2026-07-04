# Active Claim Boundary

## 可以说

- 当前结果是 metadata-only 同步快照，latest result 为 `results/spwic_identity_certificate_hand_toy_20260704`。
- latest final label 是 `SPWIC_HAND_TOY_PASS_GO_TO_TOY_ONLY_PROTOTYPE`。
- 当前 claim boundary 是：可以说：

- SPWIC hand toy 规则具体；
- hand toy 上有 9 个 constructive recovery；
- S/I/D 都有；
- harmful residual traps 被拒绝；
- 非唯一 witness low-confidence；
- no full alignment / graph / BBS / EPBSD semantics。

不能说：

- 不能说 SPWIC 是算法成功；
- 不能说 toy prototype 已通过；
- 不能说 real-data 成功；
- 不能说 smoke/benchmark 允许；
- 不能把 low-confidence 当 success。

下一步只允许 toy-only prototype，并且需要用户明确批准。

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
