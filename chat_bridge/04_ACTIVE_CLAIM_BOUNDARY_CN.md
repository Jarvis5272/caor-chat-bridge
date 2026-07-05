# Active Claim Boundary

## 可以说

- 当前结果是 metadata-only 同步快照，latest result 为 `results/scc_sparse_consistency_certificate_theory_note_20260705`。
- latest final label 是 `SCC_THEORY_READY_FOR_HAND_TOY`。
- 当前 claim boundary 是：An event `e` may be accepted only if:

1. paired witness unique；
2. bounded counterfactual delta over no-event and bounded competitors is at least `m`；
3. cross-read order consistency support exceeds `m`；
4. no competing certificate has comparable or stronger dominance；
5. independent support exceeds `m`；
6. all checks stay within `a/W` and the competitor registry remains sparse.

If any condition fails, SCC must output low-confidence/no correction or stop. It cannot widen W, add helper families, use graph/POA/full alignment, or call BBS/EPBSD semantics.


SCC is not guaranteed to cover all useful edits. It has coverage when true edits often have unique sparse identity and positive local counterfactual margin. It becomes refusal-only in repeats, homopolymers, low coverage, cost ties, competing certificate ties, and long-range ambiguity. These cases are not patched; they are reported.

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
