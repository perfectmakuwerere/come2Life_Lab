"""Ranking metrics over full-catalog scores.

Inputs: scores [N, |C|] and target item indices [N].
Exclude items already in the user's history from the ranking before computing metrics.
"""


def mrr(scores, targets):
    raise NotImplementedError


def recall_at_k(scores, targets, k: int = 10):
    raise NotImplementedError


def ndcg_at_k(scores, targets, k: int = 10):
    raise NotImplementedError
