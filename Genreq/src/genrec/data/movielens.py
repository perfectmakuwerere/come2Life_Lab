"""MovieLens-1M loading.

TODO:
- download/unzip ml-1m into data/raw
- return ratings (user_id, item_id, rating, timestamp), items (item_id, title, genres), users
- filter users/items below `min_interactions`
- map item_id -> contiguous catalog index 0..|C|-1 (used by the scoring head)
"""


def load_movielens(raw_dir: str, min_interactions: int = 5):
    raise NotImplementedError
