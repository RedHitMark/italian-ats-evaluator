from italian_ats_evaluator import TextAnalyzer, SimplificationAnalyzer

if __name__ == "__main__":
    result = TextAnalyzer(
      text="Il gatto mangia il topo"
    )

    result = SimplificationAnalyzer(
        reference_text="Il felino mangia il roditore",
        simplified_text="Il gatto mangia il topo"
    )