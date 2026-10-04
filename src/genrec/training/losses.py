"""Multi-objective loss (paper section 4.4).

L = alpha * L_ranking + beta * L_language + gamma * L_misc,  alpha + beta + gamma = 1

- L_ranking: cross-entropy over the catalog (or sampled softmax), scaled per example
  by the reward weight
- L_language: next-token loss over verbalized inputs/targets (titles)
- L_misc: placeholder
"""


def genrec_loss(rank_logits, target_idx, lm_loss, reward_weights, alpha, beta, gamma):
    raise NotImplementedError
