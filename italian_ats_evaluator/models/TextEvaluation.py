from pydantic import BaseModel

from italian_ats_evaluator.models.BasicEvaluation import BasicEvaluation
from italian_ats_evaluator.models.LexiconEvaluation import LexiconEvaluation
from italian_ats_evaluator.models.PosEvaluation import PosEvaluation
from italian_ats_evaluator.models.ReadabilityEvaluation import ReadabilityEvaluation
from italian_ats_evaluator.models.VerbsEvaluation import VerbsEvaluation


class TextEvaluation(BaseModel):
    basic_evaluation: BasicEvaluation = None
    pos_evaluation: PosEvaluation = None
    verbs_evaluation: VerbsEvaluation = None
    lexicon_evaluation: LexiconEvaluation = None
    readability_evaluation: ReadabilityEvaluation = None
