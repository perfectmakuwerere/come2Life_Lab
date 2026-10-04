"""Context compaction (paper section 4.3).

Rules to implement:
- retain in full: high-signal events (high rating) with richer metadata
- omit entirely: recent low-signal events
- summarize/compress: repeated behavior (e.g. runs of the same genre)
- elaborate selectively: cold-start or newly released items get extra metadata
- prioritize short/medium-term history at higher granularity; compress older
  history into a brief user-interest summary
"""


def compact_history(history, items, cfg: dict):
    raise NotImplementedError
