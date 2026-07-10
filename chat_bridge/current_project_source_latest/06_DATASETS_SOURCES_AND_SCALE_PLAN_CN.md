# 数据来源与规模计划

## 17 benchmark conditions 的含义

CAPPED_17 是 17 个 benchmark conditions / row-key scope，不等于 17 个完全独立来源。某些 Uploaded / compact / windowed / k15 / top500 / top5000 是格式或采样变体，必须带 source-family caveat。

## 主要来源族

- Microsoft CNR: BBS trio / clean IDS reference group。
- Binned Nanopore: BBS trio, 当前 large full-source primary。
- Oligo0: BBS trio, 当前 small full-source primary，也是 hard quality case。
- NBT17: projected NBT17 family，top500/top5000/all_available 等为不同 scope。
- NComms19: Space Shuttle / Vitruvian / 365 Dishes 等 projected family。
- TrellisBMA: projected trellis / TReconLM-related simulated family。
- Clover / Uploaded: source-gap exploratory，不作为 sole positive evidence。

## 为什么 capped 500/1000

Capped scope 用于横向公平比较、避免外部 baseline runtime 爆炸和快速审计；它保留，但不能替代 full-source scalability。

## Full-source small / medium / large

- small: `oligo0`, 1,466 clusters, 167,546 reads。
- medium: `ncomms19_365_dishes_full_strict_clean`, 2,038 clusters, 66,804 reads。
- large: `binned_nanopore`, 10,000 clusters, 213,740 reads。

当前未发现单一十万 cluster 来源，不能宣称十万 clusters。Clover 有 1,000,000 reads 但属于 source-gap/exploratory，不能作为主 claim 的 sole positive evidence。

## Source evidence

完整 inventory: `results/paper_restart_and_validation_20260710/FULL_DATASET_SCALE_INVENTORY.tsv`。
