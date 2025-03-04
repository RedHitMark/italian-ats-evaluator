from pydantic import BaseModel


class SimilarityEvaluation(BaseModel):
    semantic_similarity: float = 0.0
