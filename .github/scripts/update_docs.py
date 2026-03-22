"""
Script de mise à jour automatique de la documentation Frython.
Détecte les nouveaux mots-clés dans transpileur.py et met à jour
DOCUMENTATION.md et UPDATE.md automatiquement.
Supporte les espaces ET les tabulations dans les dictionnaires.
"""

import subprocess
import sys
import re
from datetime import datetime

# ── Chemins ────────────────────────────────────────────────────────────────
TRANSPILEUR   = "frython/transpileur.py"
DOCUMENTATION = "DOCUMENTATION.md"
UPDATE        = "UPDATE.md"

NOMS_LISIBLES = {
    "MOTS_CLES_VERS_PYTHON": "Mots-clés et fonctions",
    "METHODES_CHAINE":       "Méthodes de chaînes",
    "METHODES_LISTE":        "Méthodes de listes",
    "METHODES_DICT":         "Méthodes de dictionnaires",
    "METHODES_ENSEMBLE":     "Méthodes d'ensembles",
    "MODULES_TRADUITS":      "Modules traduits",
}


# ── Extraction robuste ─────────────────────────────────────────────────────

def extraire_dictionnaire(contenu, nom_dict):
    """
    Extrait toutes les paires clé:valeur d'un dictionnaire Python.
    Fonctionne avec espaces ET tabulations (mélangés ou non).
    """
    pattern = nom_dict + r"\s*=\s*\{"
    debut = re.search(pattern, contenu)
    if not debut:
        return {}

    # Trouver la fermeture du dictionnaire en comptant les accolades
    pos = debut.end()
    profondeur = 1
    while pos < len(contenu) and profondeur > 0:
        if contenu[pos] == '{':
            profondeur += 1
        elif contenu[pos] == '}':
            profondeur -= 1
        pos += 1

    bloc = contenu[debut.start():pos]

    # Extraire toutes les paires — supporte ' et " et espaces/tabs
    paires = re.findall(r"""['"]((?:[^'"\\]|\\.)+)['"]\s*:\s*['"]((?:[^'"\\]|\\.)+)['"]""", bloc)
    return dict(paires)


def extraire_tous_les_mots(contenu):
    """Extrait tous les dictionnaires de traduction."""
    return {nom: extraire_dictionnaire(contenu, nom) for nom in NOMS_LISIBLES}


# ── Git ────────────────────────────────────────────────────────────────────

def get_contenu_precedent():
    """Récupère le contenu de transpileur.py au commit précédent."""
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD~1:{TRANSPILEUR}"],
            capture_output=True, text=True
        )
        return result.stdout if result.returncode == 0 else ""
    except Exception:
        return ""


# ── Détection des nouveaux mots ────────────────────────────────────────────

def trouver_nouveaux_mots(anciens_dicts, nouveaux_dicts):
    """Compare les deux versions et retourne les nouveaux mots par catégorie."""
    nouveautes = {}
    for nom_dict, nouveau in nouveaux_dicts.items():
        ancien = anciens_dicts.get(nom_dict, {})
        nouveaux = {k: v for k, v in nouveau.items() if k not in ancien}
        if nouveaux:
            nom_lisible = NOMS_LISIBLES.get(nom_dict, nom_dict)
            nouveautes[nom_lisible] = nouveaux
    return nouveautes


def trouver_mots_supprimes(anciens_dicts, nouveaux_dicts):
    """Détecte les mots supprimés."""
    supprimes = {}
    for nom_dict, ancien in anciens_dicts.items():
        nouveau = nouveaux_dicts.get(nom_dict, {})
        retires = {k: v for k, v in ancien.items() if k not in nouveau}
        if retires:
            nom_lisible = NOMS_LISIBLES.get(nom_dict, nom_dict)
            supprimes[nom_lisible] = retires
    return supprimes


# ── Version ────────────────────────────────────────────────────────────────

def determiner_version():
    """Lit la version actuelle dans UPDATE.md et incrémente le patch (avec rollover mineur)."""
    try:
        with open(UPDATE, "r", encoding="utf-8") as f:
            contenu = f.read()
        versions = re.findall(r"\[(\d+\.\d+\.\d+)\]", contenu)
        if not versions:
            return "1.0.1"
        derniere = versions[0]
        majeur, mineur, patch = derniere.split(".")
        majeur, mineur, patch = int(majeur), int(mineur), int(patch)

        if patch >= 9:
            patch = 0
            mineur += 1
            if mineur >= 10:
                mineur = 0
                majeur += 1
        else:
            patch += 1

        return f"{majeur}.{mineur}.{patch}"
    except FileNotFoundError:
        return "1.0.1"


# ── Mise à jour de UPDATE.md ───────────────────────────────────────────────

def mettre_a_jour_update_md(nouveautes, supprimes, version):
    """Ajoute une nouvelle section dans UPDATE.md."""
    date = datetime.now().strftime("%Y-%m-%d")

    lignes = [f"## [{version}] — {date}\n"]

    if nouveautes:
        lignes.append("\n### Ajouté\n")
        for categorie, mots in nouveautes.items():
            lignes.append(f"- **{categorie}** — {len(mots)} nouveau(x):")
            for fr, py in sorted(mots.items()):
                lignes.append(f"  - `{fr}` → `{py}`")
        lignes.append("")

    if supprimes:
        lignes.append("\n### Supprimé\n")
        for categorie, mots in supprimes.items():
            lignes.append(f"- **{categorie}** — {len(mots)} supprimé(s):")
            for fr, py in sorted(mots.items()):
                lignes.append(f"  - `{fr}` (était `{py}`)")
        lignes.append("")

    nouvelle_section = "\n".join(lignes) + "\n---\n\n"

    try:
        with open(UPDATE, "r", encoding="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        contenu = "# 📝 Historique des mises à jour — Frython\n\n---\n\n"

    # Insérer après le premier "---"
    insertion = contenu.find("---\n")
    if insertion != -1:
        contenu = contenu[:insertion + 4] + "\n" + nouvelle_section + contenu[insertion + 4:]
    else:
        contenu += nouvelle_section

    with open(UPDATE, "w", encoding="utf-8") as f:
        f.write(contenu)

    print(f"✅ UPDATE.md mis à jour — version {version}")


# ── Mise à jour de DOCUMENTATION.md ───────────────────────────────────────

def generer_tableaux(dicts):
    """Génère les tableaux markdown complets pour tous les dictionnaires."""
    sections = [
        ("MOTS_CLES_VERS_PYTHON", "### Mots-clés et fonctions intégrées"),
        ("METHODES_CHAINE",       "### Méthodes de chaînes"),
        ("METHODES_LISTE",        "### Méthodes de listes"),
        ("METHODES_DICT",         "### Méthodes de dictionnaires"),
        ("METHODES_ENSEMBLE",     "### Méthodes d'ensembles"),
        ("MODULES_TRADUITS",      "### Modules traduits"),
    ]

    lignes = []
    for nom_dict, titre in sections:
        d = dicts.get(nom_dict, {})
        if not d:
            continue
        # Dédupliquer (garder uniquement la première occurrence de chaque clé)
        d_unique = {}
        for k, v in d.items():
            if k not in d_unique:
                d_unique[k] = v

        lignes.append(f"\n{titre}\n")
        lignes.append("| Frython | Python |")
        lignes.append("|---------|--------|")
        for fr, py in sorted(d_unique.items()):
            lignes.append(f"| `{fr}` | `{py}` |")
        lignes.append("")

    return "\n".join(lignes)


def mettre_a_jour_documentation_md(nouveaux_dicts):
    """Met à jour la section des mots-clés dans DOCUMENTATION.md."""
    try:
        with open(DOCUMENTATION, "r", encoding="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        print("⚠️  DOCUMENTATION.md introuvable.")
        return

    nouveau_tableau = generer_tableaux(nouveaux_dicts)

    debut = "<!-- MOTS_CLES_START -->"
    fin   = "<!-- MOTS_CLES_END -->"

    if debut in contenu and fin in contenu:
        avant = contenu[:contenu.index(debut) + len(debut)]
        apres = contenu[contenu.index(fin):]
        contenu = avant + "\n" + nouveau_tableau + "\n" + apres
    else:
        print("⚠️  Balises <!-- MOTS_CLES_START --> / <!-- MOTS_CLES_END --> introuvables dans DOCUMENTATION.md")
        contenu += f"\n\n{debut}\n{nouveau_tableau}\n{fin}\n"

    # Mettre à jour la date
    date = datetime.now().strftime("%Y-%m-%d")
    contenu = re.sub(
        r"_Documentation.*?mise à jour.*?_",
        f"_Documentation mise à jour le {date} — 🐓 Python en français, sacré bleu !_",
        contenu
    )

    with open(DOCUMENTATION, "w", encoding="utf-8") as f:
        f.write(contenu)

    print("✅ DOCUMENTATION.md mis à jour")


# ── Résumé console ─────────────────────────────────────────────────────────

def afficher_resume(nouveautes, supprimes):
    print("\n" + "=" * 55)
    print("🐓 FRYTHON — Détection des changements de mots-clés")
    print("=" * 55)

    if not nouveautes and not supprimes:
        print("✅ Aucun changement détecté.")
        print("=" * 55 + "\n")
        return

    if nouveautes:
        total = sum(len(m) for m in nouveautes.values())
        print(f"\n🆕 {total} nouveau(x) mot(s):\n")
        for categorie, mots in nouveautes.items():
            print(f"  📂 {categorie} ({len(mots)}):")
            for fr, py in sorted(mots.items()):
                print(f"     '{fr}' → '{py}'")

    if supprimes:
        total = sum(len(m) for m in supprimes.values())
        print(f"\n🗑️  {total} mot(s) supprimé(s):\n")
        for categorie, mots in supprimes.items():
            print(f"  📂 {categorie} ({len(mots)}):")
            for fr, py in sorted(mots.items()):
                print(f"     '{fr}' (était '{py}')")

    print("\n" + "=" * 55 + "\n")


# ── Mise à jour de la version dans setup.py et pyproject.toml ──────────────

def mettre_a_jour_version_fichiers(version):
    """Met à jour la version dans setup.py et pyproject.toml."""

    # setup.py
    try:
        with open("setup.py", "r", encoding="utf-8") as f:
            contenu = f.read()
        contenu = re.sub(r"version='[\d\.]+'", f"version='{version}'", contenu)
        with open("setup.py", "w", encoding="utf-8") as f:
            f.write(contenu)
        print(f"✅ setup.py → version {version}")
    except FileNotFoundError:
        print("⚠️  setup.py introuvable")

    # pyproject.toml
    try:
        with open("pyproject.toml", "r", encoding="utf-8") as f:
            contenu = f.read()
        contenu = re.sub(r'version = "[\d\.]+"', f'version = "{version}"', contenu)
        with open("pyproject.toml", "w", encoding="utf-8") as f:
            f.write(contenu)
        print(f"✅ pyproject.toml → version {version}")
    except FileNotFoundError:
        print("⚠️  pyproject.toml introuvable")

    # frython/__init__.py
    try:
        with open("frython/__init__.py", "r", encoding="utf-8") as f:
            contenu = f.read()
        contenu = re.sub(r"__version__ = '[\d\.]+'", f"__version__ = '{version}'", contenu)
        with open("frython/__init__.py", "w", encoding="utf-8") as f:
            f.write(contenu)
        print(f"✅ frython/__init__.py → version {version}")
    except FileNotFoundError:
        print("⚠️  frython/__init__.py introuvable")


# ── Point d'entrée ─────────────────────────────────────────────────────────

def main():
    try:
        with open(TRANSPILEUR, "r", encoding="utf-8") as f:
            contenu_actuel = f.read()
    except FileNotFoundError:
        print(f"❌ Impossible de lire {TRANSPILEUR}")
        sys.exit(1)

    contenu_precedent = get_contenu_precedent()

    nouveaux_dicts = extraire_tous_les_mots(contenu_actuel)
    anciens_dicts  = extraire_tous_les_mots(contenu_precedent) if contenu_precedent else {}

    nouveautes = trouver_nouveaux_mots(anciens_dicts, nouveaux_dicts)
    supprimes  = trouver_mots_supprimes(anciens_dicts, nouveaux_dicts)

    afficher_resume(nouveautes, supprimes)

    if nouveautes or supprimes:
        version = determiner_version()
        mettre_a_jour_update_md(nouveautes, supprimes, version)
        mettre_a_jour_documentation_md(nouveaux_dicts)
        mettre_a_jour_version_fichiers(version)
        print(f"📦 Nouvelle version: {version}")
    else:
        mettre_a_jour_documentation_md(nouveaux_dicts)
        print("📄 Tableaux rafraîchis — pas de nouvelle version.")

    print("✅ Terminé!\n")


if __name__ == "__main__":
    main()
