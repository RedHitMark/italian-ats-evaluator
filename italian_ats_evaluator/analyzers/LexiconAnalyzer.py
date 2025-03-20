import re
from typing import Dict

from italian_ats_evaluator.models.LexiconEvaluation import LexiconEvaluation
from italian_ats_evaluator.models.Span import Span
from italian_ats_evaluator.models.TextEvaluation import TextEvaluation
from italian_ats_evaluator.utils import nlp_utils


class LexiconAnalyzer:

    def __init__(self):
        self.juridical_expressions = nlp_utils.get_juridical_expressions()
        self.difficult_connectives = nlp_utils.get_difficult_connectives()
        self.latinisms = nlp_utils.get_latinisms()

    def analyze(self, text: str, processed_text: Dict, text_evaluation: TextEvaluation) -> LexiconEvaluation:
        lexicon_evaluation = LexiconEvaluation()

        for jur in self.juridical_expressions:
            for found in re.finditer(jur, text, re.IGNORECASE):
                span = Span(start=found.start(), end=found.end(), text=found.group())
                lexicon_evaluation.n_juridical_expressions += 1
                lexicon_evaluation.juridical_expressions.append(span)

        for conn in self.difficult_connectives:
            for found in re.finditer(conn, text, re.IGNORECASE):
                span = Span(start=found.start(), end=found.end(), text=found.group())
                lexicon_evaluation.n_difficult_connectives += 1
                lexicon_evaluation.difficult_connectives.append(span)

        for lat in self.latinisms:
            for found in re.finditer(lat, text, re.IGNORECASE):
                span = Span(start=found.start(), end=found.end(), text=found.group())
                lexicon_evaluation.n_latinisms += 1
                lexicon_evaluation.latinisms.append(span)

        for sentence in processed_text['sentences']:
            for token in sentence['tokens']:
                if not token['upos'] == 'PUNCT':
                    span = Span(start=token['dspan'][0], end=token['dspan'][1], text=token['text'])
                    if nlp_utils.is_vdb(token['lemma']):
                        lexicon_evaluation.n_easy_tokens += 1
                        lexicon_evaluation.easy_tokens.append(span)
                    if nlp_utils.is_vdb_fo(token['lemma']):
                        lexicon_evaluation.n_easy_fo_tokens += 1
                        lexicon_evaluation.easy_fo_tokens.append(span)
                    if nlp_utils.is_vdb_au(token['lemma']):
                        lexicon_evaluation.n_easy_au_tokens += 1
                        lexicon_evaluation.easy_au_tokens.append(span)
                    if nlp_utils.is_vdb_ad(token['lemma']):
                        lexicon_evaluation.n_easy_ad_tokens += 1
                        lexicon_evaluation.easy_ad_tokens.append(span)

        return lexicon_evaluation
