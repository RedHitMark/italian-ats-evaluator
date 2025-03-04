from typing import List

from pydantic import BaseModel


class DiffEvaluation(BaseModel):
    editdistance: int = 0

    added_tokens: List[str] = []
    deleted_tokens: List[str] = []
    added_vdb_tokens: List[str] = []
    deleted_vdb_tokens: List[str] = []

    n_added_tokens: int = 0
    n_deleted_tokens: int = 0
    n_added_vdb_tokens: int = 0
    n_deleted_vdb_tokens: int = 0
