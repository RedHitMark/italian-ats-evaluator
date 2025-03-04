from italian_ats_evaluator import TextAnalyzer, SimplificationAnalyzer

if __name__ == "__main__":
    analyzer = TextAnalyzer(
        spacy_model_name="it_core_news_lg"
    )
    text_evaluation = analyzer.analyze(text="Il gatto mangia il topo")
    print(text_evaluation)

    analyzer = SimplificationAnalyzer(
        spacy_model_name="it_core_news_lg",
        sentence_transformers_model_name="intfloat/multilingual-e5-base"
    )
    simplification_evaluation = analyzer.analyze(
        reference_text="Il felino mangia il roditore",
        simplified_text="Il gatto mangia il topo"
    )
    print(simplification_evaluation)
