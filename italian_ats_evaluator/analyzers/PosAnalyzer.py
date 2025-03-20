from typing import Dict

from italian_ats_evaluator.models.PosEvaluation import PosEvaluation
from italian_ats_evaluator.models.Span import Span
from italian_ats_evaluator.models.TextEvaluation import TextEvaluation


class PosAnalyzer:

    def analyze(self, text: str, processed_text: Dict, text_evaluation: TextEvaluation) -> PosEvaluation:
        pos_evaluation = PosEvaluation()

        for sentence in processed_text['sentences']:
            for token in sentence['tokens']:
                span = Span(start=token['dspan'][0], end=token['dspan'][1], text=token['text'])
                if token['upos'] == "X":
                    pos_evaluation.n_other += 1
                    pos_evaluation.other.append(span)
                if token['upos'] == "NOUN":
                    pos_evaluation.n_nouns += 1
                    pos_evaluation.nouns.append(span)
                if token['upos'] == "AUX":
                    pos_evaluation.n_verbs += 1
                    pos_evaluation.verbs.append(span)
                if token['upos'] == "VERB":
                    pos_evaluation.n_verbs += 1
                    pos_evaluation.verbs.append(span)
                if token['upos'] == "NUM":
                    pos_evaluation.n_number += 1
                    pos_evaluation.number.append(span)
                if token['upos'] == "SYM":
                    pos_evaluation.n_symbols += 1
                    pos_evaluation.symbols.append(span)
                if token['upos'] == "ADV":
                    pos_evaluation.n_adverbs += 1
                    pos_evaluation.adverbs.append(span)
                if token['upos'] == "DET":
                    pos_evaluation.n_articles += 1
                    pos_evaluation.articles.append(span)
                if token['upos'] == "PRON":
                    pos_evaluation.n_pronouns += 1
                    pos_evaluation.pronouns.append(span)
                if token['upos'] == "PART":
                    pos_evaluation.n_particles += 1
                    pos_evaluation.particles.append(span)
                if token['upos'] == "ADJ":
                    pos_evaluation.n_adjectives += 1
                    pos_evaluation.adjectives.append(span)
                if token['upos'] == "ADP":
                    pos_evaluation.n_prepositions += 1
                    pos_evaluation.prepositions.append(span)
                if token['upos'] == "PROPN":
                    pos_evaluation.n_proper_nouns += 1
                    pos_evaluation.proper_nouns.append(span)
                if token['upos'] == "PUNCT":
                    pos_evaluation.n_punctuations += 1
                    pos_evaluation.punctuations.append(span)
                if token['upos'] == "INTJ":
                    pos_evaluation.n_interjections += 1
                    pos_evaluation.interjections.append(span)
                if token['upos'] == "CCONJ":
                    pos_evaluation.n_coordinating_conjunctions += 1
                    pos_evaluation.coordinating_conjunctions.append(span)
                if token['upos'] == "SCONJ":
                    pos_evaluation.n_subordinating_conjunctions += 1
                    pos_evaluation.subordinating_conjunctions.append(span)

        return pos_evaluation
