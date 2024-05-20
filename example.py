import italian_ats_evaluator


a = italian_ats_evaluator.compare(
    ref_text="Il felino mangia il roditore",
    simplified_text="Il gatto mangia il topo",
)

print(a)