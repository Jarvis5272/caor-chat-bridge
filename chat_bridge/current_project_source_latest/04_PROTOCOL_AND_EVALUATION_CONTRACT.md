# Protocol and Evaluation Contract

## Dataset / cluster / prefix

- Dataset: neutral-format benchmark condition with dataset_key and source_family.
- Cluster: one reconstruction unit with reads and reference available for offline evaluation.
- Prefix: first t reads in file_order; current checkpoints are 1, 2, 3, 5, 10, 20 unless a full-prefix study is explicitly declared.

## Row key

Canonical key: `dataset_key, cluster_id, prefix_t, prefix_mode, arrival_order_mode, method_key`。CAPPED_17 row-key hash must remain fixed when comparing methods.

## File order

Primary arrival order is file_order. Shuffle/order robustness is separate and cannot be mixed into main row-key claims.

## Reference boundary

Reference/truth are forbidden online. They are used only for offline ED/Accuracy/Exact and hash/evaluator audits.

## Metrics

- ED: Levenshtein edit distance to reference under current evaluator definition.
- Accuracy: evaluator-defined normalized edit accuracy, usually `1 - ED / reference_len` unless evaluator records another definition.
- Exact: output sequence exactly equals reference under evaluator normalization.
- Macro/micro: must be explicitly reported; do not silently mix dataset macro with row micro.

## Runtime

- Runtime(s): wall-clock runtime for declared method/scope.
- Prefix/s: prefix rows divided by runtime.
- Raw reads/s: only if actual `num_reads_seen` or `num_reads_used` is summed and recorded.
- Worker count: implementation/deployment setting; not an algorithm parameter.

## Fairness

- Single-process / single-thread current method result is the fair primary comparison to baselines.
- 8/16/24 worker results are deployment throughput and must be separated.
- External baselines do not need to be reimplemented by us in multi-thread mode.

## Failure handling

Timeout, failed, missing, parser failure, and hidden failure rows must be retained. Do not exclude failed rows to improve averages.

## Full-source vs capped benchmark

CAPPED_17_MATCHED is a horizontal fair benchmark, not large-scale scalability evidence. Full-source claims require actual full small/medium/large runs.
