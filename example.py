from italian_ats_evaluator import TextAnalyzer, SimplificationAnalyzer

if __name__ == "__main__":
    text_analyzer = TextAnalyzer(
        spacy_model_name="it_core_news_lg"
    )
    text_evaluation = text_analyzer.analyze(text="Il gatto mangia il topo")
    print(text_evaluation)

    simplification_analyzer = SimplificationAnalyzer(
        spacy_model_name="it_core_news_lg",
        sentence_transformers_model_name="intfloat/multilingual-e5-base"
    )
    simplification_evaluation = simplification_analyzer.analyze(
        reference_text="Il felino mangia il roditore",
        simplified_text="Il gatto mangia il topo"
    )
    print(simplification_evaluation)
