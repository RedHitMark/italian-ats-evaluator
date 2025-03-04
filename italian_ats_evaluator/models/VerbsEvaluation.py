from typing import List

from pydantic import BaseModel

from italian_ats_evaluator.models import Span


class VerbsEvaluation(BaseModel):
    active_verbs: List[Span] = []
    passive_verbs: List[Span] = []
    reflective_verbs: List[Span] = []

    n_active_verbs: int = 0
    n_passive_verbs: int = 0
    n_reflective_verbs: int = 0
