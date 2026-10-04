# GenRec prototype

Small-scale reproduction of **GenRec: An LLM-Backed Recommendation Ranker at Netflix**
(Li et al., arXiv [2608.10257](https://arxiv.org/abs/2608.10257)).

Netflix released no code or data, so this reproduces the Phase-2 recipe on a public
dataset (MovieLens-1M) with a small open LLM backbone.

## What is being reproduced

| Paper component | Module |
|---|---|
| Verbalizer `x = V(H, {M_i}, tau)` with event selection and compaction | `src/genrec/verbalize/` |
| Pooled hidden state `h` plus catalog-aware scoring head with item embeddings `e_i` | `src/genrec/model/` |
| Loss `L = a*L_rank + b*L_lm + g*L_misc` (a+b+g = 1) | `src/genrec/training/losses.py` |
| Reward-weighted ranking loss | `src/genrec/training/rewards.py` |
| Prefill-only full-catalog scoring | `src/genrec/serving/prefill_score.py` |
| MRR, Recall@K, NDCG@K | `src/genrec/eval/metrics.py` |

Not reproduced: Phase 1 (Netflix-specific foundation LLM), Netflix reward models, online A/B testing.

## Layout

```
genrec/
  configs/        YAML configs (data, model, loss weights, training)
  data/raw|processed   datasets (git-ignored)
  scripts/        entry points: prepare_data, train, evaluate, ablate_context
  src/genrec/
    data/         loading, temporal splits, conversation-style examples
    verbalize/    prompt construction and context compaction
    model/        backbone wrapper, scoring head
    training/     losses, reward weights, trainer
    eval/         ranking metrics
    serving/      prefill-only scoring
  tests/
  results/        tables and plots
  notebooks/      exploration
```

## Status

Skeleton only. Every module has a docstring and `NotImplementedError` stubs describing what to build.

## Roadmap

1. Baselines (popularity, SASRec) on a fixed temporal split
2. Data pipeline and verbalizer v1, then compaction rules
3. Model with scoring head; overfit a tiny batch
4. Reward weighting from MovieLens proxy signals
5. Ablations: context length, compaction, data scaling, backbone size, loss mix
6. Prefill-only latency benchmark (HF forward, then vLLM)
7. Write-up
"# come2Life_Lab" 
