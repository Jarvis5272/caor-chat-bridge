# P0 结果交叉验证计划与状态

当前只完成计划，尚未执行审计；所有主结果数值仍为 provisional。

| item | audit | status |
|---|---|---|
| input_hash | 输入 manifest / row-key hash freeze | not_started |
| output_hash | 当前方法和 baseline output hash audit | not_started |
| independent_evaluator | ED/Accuracy/Exact independent recomputation | not_started |
| runtime_repeat_1worker | 1-thread runtime repeat | not_started |
| runtime_repeat_8_16worker | 8/16 worker repeat and throughput audit | not_started |
| reference_blind | online reference/truth isolation audit | not_started |
| future_read_isolation | prefix reads[1:t] isolation audit | not_started |
| baseline_isolation | no BBS/CPL/VS/MUSCLE/BMALA online dependency | not_started |
| manual_inspection | manual output examples and failure rows | not_started |
| number_lock | final number lock after all pass | not_started |

## 必须验证

- 输入 hash 与 row keys 是否一致。
- 输出 hash 是否来自实际 output sequence。
- 独立 evaluator 是否复现 ED / accuracy / exact。
- 1/8/16 thread runtime 是否可重复。
- current method 是否 reference-blind / future-read-blind。
- baseline outputs 是否只作为 offline comparator。

## 状态词

`not_started`, `running`, `passed`, `failed`, `blocked`。目前全部为 `not_started`，不得写成 passed。
