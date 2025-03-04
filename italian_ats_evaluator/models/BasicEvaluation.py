from typing import List, Set

from pydantic import BaseModel


class BasicEvaluation(BaseModel):
    tokens: List[str] = []
    tokens_all: List[str] = []
    chars: List[str] = []
    chars_all: List[str] = []
    syllables: List[str] = []
    words: Set[str] = set()
    lemmas: List[str] = []
    unique_lemmas: Set[str] = set()
    sentences: List[str] = []

    n_tokens: int = 0
    n_tokens_all: int = 0
    n_chars: int = 0
    n_chars_all: int = 0
    n_syllables: int = 0
    n_words: int = 0
    n_unique_lemmas: int = 0
    n_sentences: int = 0
