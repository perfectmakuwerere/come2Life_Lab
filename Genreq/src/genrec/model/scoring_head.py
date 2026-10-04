"""Catalog-aware scoring head phi (paper section 4.5).

score(i) = phi(h, e_i) with learned item embeddings e_i in R^d.
Softmax over the catalog gives a distribution; ranking pi comes from the scores.

TODO:
- nn.Embedding(|C|, d) for items
- dot-product scoring first, optional small MLP variant
- full softmax and a sampled-softmax option for large catalogs
- forward(h) -> logits of shape [batch, |C|]
"""


class CatalogScoringHead:  # becomes nn.Module when implemented
    def __init__(self, num_items: int, hidden_dim: int, scoring: str = "dot"):
        raise NotImplementedError

    def forward(self, h):
        raise NotImplementedError
