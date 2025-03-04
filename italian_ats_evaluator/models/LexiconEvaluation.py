from typing import List

from pydantic import BaseModel

from italian_ats_evaluator.models.Span import Span


class LexiconEvaluation(BaseModel):
    difficult_connectives: List[Span] = []
    latinisms: List[Span] = []
    easy_tokens: List[Span] = []
    easy_fo_tokens: List[Span] = []
    easy_au_tokens: List[Span] = []
    easy_ad_tokens: List[Span] = []

    n_difficult_connectives: int = 0
    n_latinisms: int = 0
    n_easy_tokens: int = 0
    n_easy_fo_tokens: int = 0
    n_easy_au_tokens: int = 0
    n_easy_ad_tokens: int = 0
