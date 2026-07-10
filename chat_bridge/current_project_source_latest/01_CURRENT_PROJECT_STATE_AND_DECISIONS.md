# 当前项目状态与决策

## 已完成

- CAPPED_17_MATCHED fair benchmark 形成：17 benchmark conditions / 82,462 prefix rows / same row-key SHA256。
- 当前 runner 与参数已从真实代码冻结：`scripts/pareto_run_to_completion_controller_20260706/run_cecc_bounded.py`。
- Latest bridge active task: `paper_restart_and_validation_20260710`，label `PAPER_RESTART_VALIDATION_AND_SCALE_PLAN_READY`。
- presentation 表格和 runtime figure 数据已生成：`results/final_presentation_tables_20260710_v3` 与 `results/final_presentation_runtime_bars_20260710_v3`。
- 数据规模 inventory 已生成：`results/paper_restart_and_validation_20260710/FULL_DATASET_SCALE_INVENTORY.tsv`。
- 旧 STWC source files 已从当前迁移包退役，只作为历史归档。

## 正在进行

- P0 result cross-validation 计划已完成，但审计尚未运行。
- 新论文 skeleton 已生成，可开始撰写 problem/method/experiment shell。
- small/medium/large full-source plan 已确定，但实际 full-source 运行尚未启动。

## 尚未开始

- independent metric recomputation。
- output hash / input hash freeze。
- runtime 1/8/16 thread repeats。
- no-leakage static/dynamic audit。
- oligo0 / NComms19 365 Dishes / binned_nanopore full-source pilots。
- parameter sensitivity、ablation、confidence calibration。
- final paper locked tables。

## 不可再做

- 不再把 STWC / FPCR / SGR / MGCS / CECC / DICEC / BAPC / CGBAPC 旧候选池叙事作为当前论文主线。
- 不再继续增加相似小数据源来代替规模深度。
- 不再把 thread / C++ / wrapper 当算法贡献。
- 不再将 capped 500/1000 cluster benchmark 作为 scalability 证据。
- 不再修改当前方法主结构，直到 P0 cross-validation 完成。

## 当前 open blockers

1. 主结果数字尚未 independent cross-validated。
2. full-source large validation 尚未运行。
3. 方法正式命名未定。
4. confidence 是否作为正式算法模块需在校准后决定。
5. INFOCOM claim 仍 conditional。
