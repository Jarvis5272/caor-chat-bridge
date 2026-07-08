# Fixed Rendered Table Index

## Part1 — Datasets 1–6
- 18_RENDERED_TABLE_PART1.html — standalone HTML
- 18_RENDERED_TABLE_PART1.png — PNG with CJK font
- Datasets: binned_nanopore, clover, clover_clusters, microsoft_cnr, nbt17_id20_m2m_top500, nbt17_id20_m2m_top5000

## Part2 — Datasets 7–12
- 19_RENDERED_TABLE_PART2.html — standalone HTML
- 19_RENDERED_TABLE_PART2.png — PNG with CJK font
- Datasets: nbt17_id20_m2m_top500_k15, ncomms19_365_dishes_full_strict_clean, ncomms19_space_shuttle_k15_min5, ncomms19_space_shuttle_min5, ncomms19_space_shuttle_min5_windowed, ncomms19_vitruvian_min5_windowed

## Part3 — Datasets 13–17
- 20_RENDERED_TABLE_PART3.html — standalone HTML
- 20_RENDERED_TABLE_PART3.png — PNG with CJK font
- Datasets: oligo0, trellisbma_datatoprocess_sim, uploaded_compact, uploaded_real_clusters, uploaded_real_clusters_compact

## Verification
- **total datasets = 17** — all shown across 3 parts
- **total rows = 119** (17 × 7 methods)
- **runtime fields filled = yes** — wall_clock_runtime_seconds from raw data
- **speedup fields filled = yes** — BBS_runtime / method_runtime per dataset
- **time_per_cluster filled = yes** — runtime_seconds / clusters
- **CJK font readable = yes** — Noto Sans CJK SC
- **ITR status = failed/unusable** — excluded from best-value selection
- **best values bolded** = yes — within each dataset-metric, HTML `<strong>`
