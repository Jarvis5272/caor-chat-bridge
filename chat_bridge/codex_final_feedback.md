# Codex Final Feedback

1. final label: `TPC_OCWP_REAL_SYNC_STOP_GLOBAL_SEARCH_REQUIRED`
2. output dir: `results/tpc_ocwp_real_data_validation_20260704`
3. completed stages: `本任务目的, Input scope, Global config, Sync summary, Constructive recovery, Sensitivity, Failure taxonomy, Go / Stop, Claim boundary, Protected/original source modified, stage0_gate_decision, stage9_gate_decision`
4. key metrics: `{'aggregate_summary': {'constructive_rate': '0.267742', 'dominant_status': 'global_search_risk', 'global_search_risk_rate': '0.560369', 'low_confidence_rate': '0.952074', 'num_constructive_residuals': '581', 'num_ocwp_recoveries': '380', 'num_pbrw_recoveries': '457', 'num_prefixes': '2170', 'output_length_abnormal_rate': '0.000461', 'profile_collapse_rate': '0.0', 'stable_or_recovery_or_low_confidence_rate': '0.047926'}, 'clusters_selected': 340, 'constructive_recovery_rows': 581, 'datasets': 17, 'high_confidence_wrong_rate': 0.005069, 'ocwp_pbrw_recovery_rows': 837, 'output_length_abnormal_rate': 0.000461, 'prefix_rows': 2170, 'prior_tpc_global_search_risk': 0.415513, 'stable_recovery_low_confidence_rate': 0.047926, 'tpc_ocwp_global_search_risk': 0.560369, 'valid_recovery_rate': 0.857143}`
5. gate decision: `SKIPPED: sync gate did not pass (TPC_OCWP_REAL_SYNC_STOP_GLOBAL_SEARCH_REQUIRED); small reconstruction smoke not allowed.`
6. claim boundary: `This is a BBS-free sync dry-run. It does not claim reconstruction benchmark quality. Low-confidence/refusal is not counted as decoder success.`
7. next recommendation: `Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.`
8. bridge status: `bridge_ok_with_nonblocking_missing`
9. chat_bridge_feedback_package path: `chat_bridge_feedback_package.zip`
10. bridge raw link if pushed: `see chat_bridge_export/CHATGPT_LINK_INSTRUCTIONS_CN.md`
11. protected files modified?: `no`
12. original BBS source modified?: `no`
