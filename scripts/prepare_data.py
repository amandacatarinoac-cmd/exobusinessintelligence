"""Préparation des données de l'application (séance 5).

Lit les deux fichiers FINAL de la séance 3 et écrit deux fichiers JSON
séparés pour l'application. Les deux sources ne sont JAMAIS empilées
(erreur sanctionnée n° 11 du cours).

Usage :
    python3 scripts/prepare_data.py <principal.xlsx> <rares.xlsx> <dossier_sortie>

Règles appliquées en plus du nettoyage de la séance 3 (déjà dans les FINAL) :
  R-S5-1  ID_AW 164662498 présent 3 fois (seul le poids du prix diffère :
          60, 50, 40). Grain = une attribution : on garde la première ligne.
  R-S5-2  NUMBER_OFFERS = 999 (3 lignes, BG 2014, même acheteur, 45 lots) :
          traité comme la sentinelle 940, mis à vide et signalé.
Chaque règle est consignée dans le registre des écarts.
"""
import json
import sys

import pandas as pd

ID_TRIPLE = 164662498
SENTINELLE_999 = 999


def encode_cat(series):
    """Encodage par dictionnaire : renvoie (modalités, codes ; -1 = vide)."""
    s = series.astype("string")
    cats = sorted(s.dropna().unique().tolist())
    idx = {c: i for i, c in enumerate(cats)}
    codes = [idx[v] if v is not pd.NA and v in idx else -1 for v in s.tolist()]
    return cats, codes


def num(series, nd=None):
    out = []
    for v in series.tolist():
        if pd.isna(v):
            out.append(None)
        elif nd is None:
            out.append(int(v))
        else:
            out.append(round(float(v), nd))
    return out


def build(df, cats_cols, journal):
    cols, dicts = {}, {}
    cols["id"] = num(df["ID_AW"])
    cols["year"] = num(df["YEAR"])
    cols["lots"] = num(df["LOTS_NUMBER"])
    cols["offers"] = num(df["NUMBER_OFFERS"])
    cols["awards"] = num(df["NUMBER_AWARDS"])
    cols["value"] = num(df["AWARD_VALUE_EURO"], 2)
    cols["poids"] = num(df["POIDS"], 2)
    cols["cpv"] = [None if pd.isna(c) else str(c).replace("CPV", "") for c in df["CPV"].tolist()]
    for key, col in cats_cols.items():
        dicts[key], cols[key] = encode_cat(df[col])
    return {"n": len(df), "dicts": dicts, "cols": cols, "journal": journal}


def main(p_path, r_path, out_dir):
    cats = {
        "pays": "ISO_COUNTRY_CODE", "contrat": "TYPE_OF_CONTRACT", "proc": "TOP_TYPE",
        "pme": "B_CONTRACTOR_SME", "enchere": "B_ELECTRONIC_AUCTION", "crit": "CRIT_CODE",
        "acheteur": "CAE_TYPE",
    }

    p = pd.read_excel(p_path, sheet_name=0)
    n_final = len(p)
    dup_mask = p["ID_AW"].eq(ID_TRIPLE) & p.duplicated("ID_AW", keep="first")
    n_dup = int(dup_mask.sum())
    p = p[~dup_mask].copy()
    m999 = p["NUMBER_OFFERS"].eq(SENTINELLE_999)
    n999 = int(m999.sum())
    p.loc[m999, "NUMBER_OFFERS"] = pd.NA
    journal_p = {
        "lignes_brutes": 150147, "doublons_stricts_s3": 334, "lignes_final": n_final,
        "id_triple_retire": n_dup, "sentinelle_999_mise_a_vide": n999,
        "sentinelle_940_deja_isolee": int(p["NUMBER_OFFERS_SENTINELLE"].sum()),
        "lignes_application": len(p),
    }
    r = pd.read_excel(r_path, sheet_name=0)
    journal_r = {"lignes_brutes": 6024, "doublons_stricts_s3": 2, "lignes_final": len(r),
                 "lignes_application": len(r)}

    for name, df, jr in (("principal", p, journal_p), ("rares", r, journal_r)):
        data = build(df, cats, jr)
        with open(f"{out_dir}/{name}.json", "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
        print(name, jr)


if __name__ == "__main__":
    main(*sys.argv[1:4])
