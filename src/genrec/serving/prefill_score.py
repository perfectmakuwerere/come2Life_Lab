"""Prefill-only inference: one forward pass scores the whole catalog.

TODO:
- HF version: model.forward on the prompt, take pooled h, scoring_head -> all item scores
- benchmark latency/throughput vs autoregressive title generation
- optional vLLM version (Linux/WSL2) with prefix caching
"""


def score_catalog(model, tokenizer, prompts):
    raise NotImplementedError
