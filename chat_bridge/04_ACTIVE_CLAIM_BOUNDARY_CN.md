# Active Claim Boundary

## 可以说

- BAEPC 是一个值得进入 hand toy 的 baseline-aware original method-card candidate。
- BAEPC 的核心对象是 streaming edit-event posterior field。
- BAEPC 已定义自己的 `S_t / Update / Decode / Confidence / StopRule`。
- BAEPC 借鉴的 baseline module 已归属：medoid scaffold、bounded local DP/alignment、local edit-event posterior、posterior margin、confidence/stop rule。
- BAEPC 当前 final label 是 `BAEPC_METHOD_CARD_GO_TO_HAND_TOY`。

## 不能说

- 不能说 BAEPC 已经是有效 decoder。
- 不能说 BAEPC 已经超过 sampled_medoid 或接近 BBS。
- 不能说 BAEPC 是 BBS replacement、benchmark success、paper result 或 real-data proven method。
- 不能使用 BBS output、BBS full decoder wrapper、BBS score/beam/pruning/path likelihood 或 EPBSD kernel online。
- 不能把 refusal-only / low-confidence-only 写成 reconstruction success。

## 只能作为方法卡

- 当前只允许 hand toy。
- 不允许代码、真实数据 dry-run、small smoke、benchmark 或 formal integration。
- Hand toy 必须证明 bounded constructive correction，不是 medoid + refusal。

## 需要进一步验证

- Bounded insertion/deletion/substitution posterior 是否可手算；
- repeated context / homopolymer / long-range ambiguity 是否能诚实 low-confidence；
- `W/s/m` 三参数是否足够，不需要第 4 个核心参数。
