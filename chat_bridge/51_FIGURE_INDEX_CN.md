# Figure Index for ChatGPT

## 生成的图 (2026-07-09)

### fig1_accuracy_runtime_tradeoff.png
- **路径**: [chat_bridge/fig1_accuracy_runtime_tradeoff.png](fig1_accuracy_runtime_tradeoff.png)
- **类型**: Accuracy-Runtime scatter plot (log x-axis)
- **表达结论**: OUR C++ single 在接近 BBS 准确度 (0.9660 vs 0.9688) 下快 10.8×
- **Claim**: 单进程公平比较

### fig2_runtime_speedup_bar.png
- **路径**: [chat_bridge/fig2_runtime_speedup_bar.png](fig2_runtime_speedup_bar.png)
- **类型**: Horizontal runtime bar chart (log x-axis)
- **表达结论**: Parallel-16 5.3s (129×), Single 63.2s (10.8×), BBS 684s (1.0×)
- **Claim**: Single = fair, parallel hatched = deployment

### fig3_engineering_scaling.png
- **路径**: [chat_bridge/fig3_engineering_scaling.png](fig3_engineering_scaling.png)
- **类型**: Worker scaling line chart
- **表达结论**: 从 w=1 的 63s 缩放到 w=16 的 5.3s; 24 workers 饱和
- **Claim**: Deployment throughput scaling

### fig3b_acceleration_pipeline.png
- **路径**: [chat_bridge/fig3b_acceleration_pipeline.png](fig3b_acceleration_pipeline.png)
- **类型**: Waterfall/pipeline chart
- **表达结论**: Python 103.5s → C++ 63.2s → Parallel 5.3s
- **Claim**: 工程加速流水线 (supplementary)

### fig4_key_result_card.png
- **路径**: [chat_bridge/fig4_key_result_card.png](fig4_key_result_card.png)
- **类型**: Summary card
- **表达结论**: 左右面板: single-process fair + deployment throughput
- **Claim**: 适合开场/结论页

## 数据来源
- `results/v1_cpp_parallel_engineering_limit_20260709/CPP_PARALLEL_SCALING_SUMMARY.tsv`
- `results/final_full_17dataset_baseline_benchmark_20260707/CAPPED_17_main_comparison.tsv`

## SVG / PDF
完整矢量图在:
`results/final_presentation_figures_20260709/fig*_*.{svg,pdf}`

## Claim Boundary
- C++ single = fair single-thread result (63.2s)
- C++ parallel-16 = deployment throughput (5.3s, 16 workers)
- 两者都保持 100% output identity vs Python V1 reference
