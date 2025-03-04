from sentence_transformers import util

from ..models.SimilarityEvaluation import SimilarityEvaluation


class SimilarityAnalyzer:

    def __init__(self, sentence_transformers_model):
        self.sentence_transformers_model = sentence_transformers_model

    def analyze(self, reference_text: str, simplified_text: str) -> SimilarityEvaluation:
        similarity_evaluation = SimilarityEvaluation()

        embeddings1 = self.sentence_transformers_model.encode([reference_text], convert_to_numpy=True)
        embeddings2 = self.sentence_transformers_model.encode([simplified_text], convert_to_numpy=True)
        cosine_scores = util.cos_sim(embeddings1, embeddings2)

        similarity_evaluation.semantic_similarity = float(cosine_scores[0][0]) * 100.0
        return similarity_evaluation
