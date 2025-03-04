from pydantic import BaseModel

from italian_ats_evaluator.models.DiffEvaluation import DiffEvaluation
from italian_ats_evaluator.models.SimilarityEvaluation import SimilarityEvaluation
from italian_ats_evaluator.models.TextEvaluation import TextEvaluation


class SimplificationEvaluation(BaseModel):
    reference_text_evaluation: TextEvaluation = None
    simplified_text_evaluation: TextEvaluation = None

    similarity_evaluation: SimilarityEvaluation = None
    diff_evaluation: DiffEvaluation = None
