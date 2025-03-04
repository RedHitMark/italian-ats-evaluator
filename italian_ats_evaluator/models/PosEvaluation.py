from typing import List

from pydantic import BaseModel

from italian_ats_evaluator.models.Span import Span


class PosEvaluation(BaseModel):
    other: List[Span] = []
    nouns: List[Span] = []
    verbs: List[Span] = []
    number: List[Span] = []
    symbols: List[Span] = []
    adverbs: List[Span] = []
    articles: List[Span] = []
    pronouns: List[Span] = []
    particles: List[Span] = []
    adjectives: List[Span] = []
    prepositions: List[Span] = []
    proper_nouns: List[Span] = []
    punctuations: List[Span] = []
    interjections: List[Span] = []
    coordinating_conjunctions: List[Span] = []
    subordinating_conjunctions: List[Span] = []
    n_other: int = 0
    n_nouns: int = 0
    n_verbs: int = 0
    n_number: int = 0
    n_symbols: int = 0
    n_adverbs: int = 0
    n_articles: int = 0
    n_pronouns: int = 0
    n_particles: int = 0
    n_adjectives: int = 0
    n_prepositions: int = 0
    n_proper_nouns: int = 0
    n_punctuations: int = 0
    n_interjections: int = 0
    n_coordinating_conjunctions: int = 0
    n_subordinating_conjunctions: int = 0
