italian_vdb_fo = {a for a in open('./nvdb/FO.txt', 'r').read().split('\n')}
italian_vdb_au = {a for a in open('./nvdb/AU.txt', 'r').read().split('\n')}
italian_vdb_ad = {a for a in open('./nvdb/AD.txt', 'r').read().split('\n')}
italian_vdb = italian_vdb_fo.union(italian_vdb_au).union(italian_vdb_ad)


def is_vdb(lemma: str):
    return lemma in italian_vdb


def is_vdb_fo(lemma: str):
    return lemma in italian_vdb_fo


def is_vdb_au(lemma: str):
    return lemma in italian_vdb_au


def is_vdb_ad(lemma: str):
    return lemma in italian_vdb_ad


def do_vdb_analysis(lemmas: list[str]):
    return {
        "all": [lemma for lemma in lemmas if is_vdb(lemma)],
        "fo": [lemma for lemma in lemmas if is_vdb_fo(lemma)],
        "au": [lemma for lemma in lemmas if is_vdb_au(lemma)],
        "ad": [lemma for lemma in lemmas if is_vdb_ad(lemma)]
    }
