from pydantic import BaseModel


class ReadabilityEvaluation(BaseModel):
    ttr: float = 0.0
    gulpease: float = 0.0
    flesch_vacca: float = 0.0
    lexical_density: float = 0.0
