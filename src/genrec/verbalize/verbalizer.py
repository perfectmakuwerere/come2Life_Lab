"""Verbalizer V: x = V(H, {M_i}, tau).

Turns context (time, device-like fields), profile, history and item metadata
into a single text sequence for the LLM.

TODO:
- v1: verbose prompt listing every history event with title, genres, rating
- v2: compact prompt using compaction.compact_history
- report token count per prompt (needed for the context-length ablation)
"""


class Verbalizer:
    def __init__(self, cfg: dict, tokenizer=None):
        self.cfg = cfg
        self.tokenizer = tokenizer

    def __call__(self, history, context, items) -> str:
        raise NotImplementedError

    def count_tokens(self, text: str) -> int:
        raise NotImplementedError
