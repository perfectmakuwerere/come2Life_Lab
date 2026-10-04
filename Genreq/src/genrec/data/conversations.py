"""Conversation-style training examples (paper section 4.2).

Each example pairs a user message (context + profile/history + item detail + task)
with an assistant message (the user's actual next engagement).

TODO: build_examples returns dicts with
  - prompt_text: verbalized user message (from verbalize.Verbalizer)
  - target_item_idx: catalog index of the engaged item (ranking label)
  - target_text: title text for the language-modeling loss
  - reward_weight: scalar from training.rewards
"""


def build_examples(split, items, verbalizer, reward_fn=None):
    raise NotImplementedError
