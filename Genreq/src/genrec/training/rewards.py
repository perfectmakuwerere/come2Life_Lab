"""Reward weights (paper section 4.6).

Netflix uses separate reward models; here, build MovieLens proxies:
- long-term satisfaction proxy: e.g. rating level, whether the user kept engaging later
- behavior rebalancing: e.g. upweight under-exposed genres or newer releases

Each training example gets one scalar weight that scales its ranking loss.
"""


def reward_weight(example, user_stats, item_stats) -> float:
    raise NotImplementedError
