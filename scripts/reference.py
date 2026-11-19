"""Calcul de référence des indicateurs, indépendant de l'application.

Sert d'arbitre : chaque valeur affichée par l'application (avec ou sans
filtre) doit être identique à celle produite ici.

Usage :
    python3 scripts/reference.py docs/data [pays=FR] [annee=2016] [contrat=S]
"""
import json
import statistics
import sys


def load(path):
    d = json.load(open(path, encoding="utf-8"))
    n, c, dic = d["n"], d["cols"], d["dicts"]
    rows = []
    for i in range(n):
        r = {k: c[k][i] for k in ("id", "year", "lots", "offers", "value", "poids")}
        for k in dic:
            code = c[k][i]
            r[k] = dic[k][code] if code >= 0 else None
        rows.append(r)
    return rows


def kpis(rows, pays=None, annee=None, contrat=None):
    f = [r for r in rows if (pays is None or r["pays"] == pays)
         and (contrat is None or r["contrat"] == contrat)]
    fa = [r for r in f if annee is None or r["year"] == annee]
    out = {"lignes": len(fa)}
    # KPI 1 et 2 : procédure ouverte, au moins une offre renseignée
    ope = [r for r in fa if r["proc"] == "OPE" and r["offers"] is not None and r["offers"] >= 1]
    num1 = sum(1 for r in ope if r["offers"] == 1)
    out["kpi1"] = (num1, len(ope), num1 / len(ope) if ope else None)
    out["kpi2_mediane_offres"] = (statistics.median([r["offers"] for r in ope]) if ope else None, len(ope))
    # KPI 3 : fenêtre 2016-2017 verrouillée (ignore le filtre année)
    w = [r for r in f if r["year"] in (2016, 2017)]
    ren = [r for r in w if r["pme"] is not None]
    num3 = sum(1 for r in ren if r["pme"] == "Y")
    out["kpi3"] = (num3, len(ren), num3 / len(ren) if ren else None)
    out["kpi3_taux_renseignement"] = (len(ren), len(w), len(ren) / len(w) if w else None)
    # KPI 5 : montant total pondéré, et médiane des montants (non pondérée)
    v = [r for r in fa if r["value"] is not None]
    out["kpi5_md_eur"] = (sum(r["value"] * r["poids"] for r in v) / 1e9, len(v))
    out["mediane_montant"] = (statistics.median([r["value"] for r in v]) if v else None, len(v))
    return out


if __name__ == "__main__":
    base = sys.argv[1]
    args = dict(a.split("=") for a in sys.argv[2:])
    if "annee" in args:
        args["annee"] = int(args["annee"])
    rows = load(f"{base}/principal.json")
    for k, v in kpis(rows, **args).items():
        print(f"{k:28s} {v}")
