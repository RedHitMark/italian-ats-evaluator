from italian_ats_evaluator import TextAnalyzer, SimplificationAnalyzer

if __name__ == "__main__":
    result = TextAnalyzer(
        text="Il gatto mangia il topo",
        spacy_model_name="it_core_news_lg"
    )

    result = SimplificationAnalyzer(
        reference_text="Il felino mangia il roditore",
        simplified_text="Il gatto mangia il topo",
        spacy_model_name="it_core_news_lg",
        sentence_transformers_model_name="intfloat/multilingual-e5-base"
    )