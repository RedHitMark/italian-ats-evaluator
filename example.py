from italian_ats_evaluator import TextAnalyzer, SimplificationAnalyzer

if __name__ == "__main__":
    text_analyzer = TextAnalyzer()

#     TEXT = """"Il documento individua le esigenze di sviluppo necessarie per assicurare che i principi delineati dalla Legge Regionale 23 dicembre 2004, n. 29 e dai successivi atti normativi, sulla essenziale funzione della ricerca e innovazione nelle Aziende Sanitarie della Regione Emilia-Romagna, si traducano in azioni concrete nel Servizio Sanitario Regionale.
#
# Alla luce delle evidenze della letteratura internazionale, delle indicazioni della normativa nazionale e della valutazione di quanto già attuato a livello regionale negli anni passati, vengono individuati gli obiettivi di sviluppo e le linee per il raggiungimento dei suddetti obiettivi.
#
# Tali linee si sostanziano in interventi di carattere generale mirati a promuovere la programmazione e il coordinamento delle attività: a tale scopo viene identificato un nuovo strumento di programmazione, il “Piano regionale triennale della ricerca sanitaria” e vengono indicate le iniziative mirate a coordinare, a livello regionale le attività di ricerca sanitaria, ricerca industriale, innovazione e trasferimento tecnologico. Viene, inoltre, individuato un nuovo meccanismo di finanziamento diretto della ricerca per il sistema sanitario regionale.
#
# Vengono poi identificati azioni/attori/strumenti per promuovere la ricerca e l’innovazione. Alcune azioni sono già in corso, altre richiedono invece ulteriori approfondimenti tecnici e la loro attuazione viene, quindi, rinviata a successivi documenti regionali di indirizzo, in grado di dettagliare meglio gli obiettivi operativi e individuare le soluzioni più opportune.
#
# Vengono, infine, indicati gli assetti istituzionali a livello regionale ed aziendale ritenuti necessari al governo del sistema della ricerca."""
#
#     text_evaluation = text_analyzer.analyze(text=TEXT)
#     print(text_evaluation.verbs_evaluation)


    text_evaluation = text_analyzer.analyze(text="Il gatto è bello. Il gatto è mangiato dal topo.")
    print(text_evaluation.verbs_evaluation)

    # text_evaluation = text_analyzer.analyze(text="Il gatto mangia il topo.")
    # print(text_evaluation.verbs_evaluation)
    #
    # text_evaluation = text_analyzer.analyze(text="Il gatto ha mangiato il topo.")
    # print(text_evaluation.verbs_evaluation)
    #
    # text_evaluation = text_analyzer.analyze(text="Il gatto è mangiato dal topo.")
    # print(text_evaluation.verbs_evaluation)

    # simplification_analyzer = SimplificationAnalyzer(
    #     spacy_model_name="italian",
    #     sentence_transformers_model_name="intfloat/multilingual-e5-base"
    # )
    # simplification_evaluation = simplification_analyzer.analyze(
    #     reference_text="Il felino mangia il roditore",
    #     simplified_text="Il gatto mangia il topo"
    # )
    # print(simplification_evaluation)
