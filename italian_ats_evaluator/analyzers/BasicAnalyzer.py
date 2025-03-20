from typing import Dict

from ..models.BasicEvaluation import BasicEvaluation
from ..models.TextEvaluation import TextEvaluation
from ..utils import nlp_utils


class BasicAnalyzer:

    def analyze(self, text: str, processed_text: Dict, text_evaluation: TextEvaluation) -> BasicEvaluation:
        basic_evaluation = BasicEvaluation()

        for sentence in processed_text['sentences']:
            basic_evaluation.sentences.append(sentence['text'])
            for token in sentence['tokens']:
                basic_evaluation.tokens_all.append(token['text'])
                basic_evaluation.chars_all.extend([c for c in token['text']])

                if not token['upos'] == 'PUNCT':
                    basic_evaluation.tokens.append(token['text'])
                    basic_evaluation.chars.extend([c for c in token['text']])
                    basic_evaluation.syllables.extend(nlp_utils.eval_syllables(token['text']))
                    basic_evaluation.words.add(token['text'])
                    basic_evaluation.lemmas.append(token['lemma'])
                    basic_evaluation.unique_lemmas.add(token['lemma'])

        basic_evaluation.n_sentences = len(basic_evaluation.sentences)
        basic_evaluation.n_tokens = len(basic_evaluation.tokens)
        basic_evaluation.n_tokens_all = len(basic_evaluation.tokens_all)
        basic_evaluation.n_chars = len(basic_evaluation.chars)
        basic_evaluation.n_chars_all = len(basic_evaluation.chars_all)
        basic_evaluation.n_syllables = len(basic_evaluation.syllables)
        basic_evaluation.n_words = len(basic_evaluation.words)
        basic_evaluation.n_unique_lemmas = len(basic_evaluation.unique_lemmas)
        basic_evaluation.n_sentences = len(basic_evaluation.sentences)

        return basic_evaluation
