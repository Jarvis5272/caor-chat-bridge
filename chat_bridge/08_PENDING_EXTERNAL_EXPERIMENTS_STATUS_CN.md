# Pending External Experiments Status

## ITR — ACTIVE BACKGROUND RUN

| Item | Value |
|------|-------|
| Binary | /home/hanlinxuan/research/TestBBS/tools/Reconstruction/Iterative/main |
| PID | 86030 (RUNNING) |
| Status | **Background running — producing valid output** |
| Rows completed | 11,510 / 82,462 (14%) |
| Datasets completed | binned_nanopore (5,542 rows), clover (5,968 rows) |
| Partial accuracy | **0.9996** |
| Partial exact | **0.9837** |
| Partial ED | 0.0559 |
| Log | logs/itr_background.log |
| Background script | scripts/.../run_itr_background.py |
| Estimated total time | ~7-8 hours at current rate |
| Resume command | `nohup python scripts/.../run_itr_background.py >> logs/itr_background.log 2>&1 &` |
| Can claim OUR vs ITR? | **Not yet** — ITR must complete 82,462 rows first |

## ITR Partial Results (2 of 17 datasets)

| Dataset | Rows | Non-empty | ED | Accuracy | Exact |
|--------|------|-----------|-----|----------|-------|
| binned_nanopore | 5,542 | 5,542 | 0.1160 | 0.9992 | 0.9661 |
| clover | 5,968 | 5,968 | 0.0000 | 1.0000 | 1.0000 |
| **Combined** | **11,510** | **11,510** | **0.0559** | **0.9996** | **0.9837** |

## All Completed External Baselines

BBS (acc=0.9688), MUSCLE (acc=0.9292), VS (acc=0.9450), BMALA (acc=0.5378), CPL (acc=0.9972), OUR_REALTIME_METHOD (acc=0.9660)

## Excluded

CGBAPC, BAPC, ACDC, DICEC, TICEC, GLICE, CECC, all Pareto candidates
