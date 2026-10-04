"""GenRec model: decoder-only LLM backbone + catalog-aware scoring head.

TODO:
- load backbone (HF AutoModelForCausalLM) and optional LoRA via peft
- pooled representation h = hidden state at the pooling position (last token)
- ranking logits = scoring_head(h)
- LM logits from the backbone for the language-modeling loss
- forward returns both so training.losses can combine them
"""


class GenRecModel:  # becomes nn.Module when implemented
    def __init__(self, cfg: dict, num_items: int):
        raise NotImplementedError

    def forward(self, input_ids, attention_mask, labels=None):
        raise NotImplementedError
