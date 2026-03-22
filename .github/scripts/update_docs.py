import subprocess
import sys
import os
import re
from datetime import datetime
TRANSPILEUR = "frython/transpileur.py"
DOCUMENTATION = "DOCUMENTATION.md"
UPDATE = "UPDATE.md"


def extraire_dictionnaire(contenu, nom_dict):
    """Extrait toutes les paires clé:valeur d'un dictionnaire Python dans un fichier."""
    pattern = rf"{nom_dict}\s*=\s*\{{(.*?)\}}"
    bloc = re.search(pattern, contenu, re.DOTALL)
    if not bloc:
        return {}
    paires = re.findall(r"'([^']+)'\s*:\s*'([^']+)'", bloc.group(1))
    return dict(paires)


def extraire_tous_les_mots(contenu):
    """Extrait tous les dictionnaires de traduction du transpileur."""
    dicts = {
        "MOTS_CLES_VERS_PYTHON": extraire_dictionnaire(contenu, "MOTS_CLES_VERS_PYTHON"),
        "METHODES_CHAINE":       extraire_dictionnaire(contenu, "METHODES_CHAINE"),
        "METHODES_LISTE":        extraire_dictionnaire(contenu, "METHODES_LISTE"),
        "METHODES_DICT":         extraire_dictionnaire(contenu, "METHODES_DICT"),
        "METHODES_ENSEMBLE":     extraire_dictionnaire(contenu, "METHODES_ENSEMBLE"),
        "MODULES_TRADUITS":      extraire_dictionnaire(contenu, "MODULES_TRADUITS"),
    }
    return dicts


def get_contenu_precedent():
    """Récupère le contenu de transpileur.py au commit précédent via git."""
    try:
        result = subprocess.run(
            ["git", "show", "HEAD~1:" + TRANSPILEUR],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return result.stdout
        return ""
    except Exception:
        return ""


def trouver_nouveaux_mots(anciens_dicts, nouveaux_dicts):
    """Compare les deux versions et retourne les nouveaux mots par catégorie."""
    nouveautes = {}

    noms_lisibles = {
        "MOTS_CLES_VERS_PYTHON": "Mots-clés et fonctions",
        "METHODES_CHAINE":       "Méthodes de chaînes",
        "METHODES_LISTE":        "Méthodes de listes",
        "METHODES_DICT":         "Méthodes de dictionnaires",
        "METHODES_ENSEMBLE":     "Méthodes d'ensembles",
        "MODULES_TRADUITS":      "Modules traduits",
    }

    for nom_dict, nouveau in nouveaux_dicts.items():
        ancien = anciens_dicts.get(nom_dict, {})
        nouveaux = {k: v for k, v in nouveau.items() if k not in ancien}
        if nouveaux:
            nom_lisible = noms_lisibles.get(nom_dict, nom_dict)
            nouveautes[nom_lisible] = nouveaux

    return nouveautes


def determiner_version():
    """Lit la version actuelle dans UPDATE.md et incrémente le patch."""
    try:
        with open(UPDATE, "r", encoding="utf-8") as f:
            contenu = f.read()
        versions = re.findall(r"\[(\d+\.\d+\.\d+)\]", contenu)
        if not versions:
            return "1.0.1"
        derniere = versions[0]
        majeur, mineur, patch = derniere.split(".")
        return f"{majeur}.{mineur}.{int(patch) + 1}"
    except FileNotFoundError:
        return "1.0.1"


def mettre_a_jour_update_md(nouveautes, version):
    """Ajoute une nouvelle section dans UPDATE.md."""
    date = datetime.now().strftime("%Y-%m-%d")

    lignes = [f"## [{version}] — {date}\n\n### Ajouté\n"]

    for categorie, mots in nouveautes.items():
        lignes.append(f"- **{categorie}** — {len(mots)} nouveau(x) mot(s):")
        for fr, py in mots.items():
            lignes.append(f"  - `{fr}` → `{py}`")
        lignes.append("")

    nouvelle_section = "\n".join(lignes) + "\n---\n\n"

    try:
        with open(UPDATE, "r", encoding="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        contenu = "# 📝 Historique des mises à jour — Frython\n\n---\n\n"

    insertion = contenu.find("---\n")
    if insertion != -1:
        contenu = contenu[:insertion + 4] + "\n" + nouvelle_section + contenu[insertion + 4:]
    else:
        contenu += nouvelle_section

    with open(UPDATE, "w", encoding="utf-8") as f:
        f.write(contenu)

    print(f"✅ UPDATE.md mis à jour avec la version {version}")


def generer_tableau_mots_cles(dicts):
    """Génère les tableaux markdown pour la documentation."""
    
    sections = {
        "MOTS_CLES_VERS_PYTHON": ("### Mots-clés et fonctions intégrées", "Frython", "Python", "Description"),
        "METHODES_CHAINE":       ("### Méthodes de chaînes", "Frython", "Python", "Description"),
        "METHODES_LISTE":        ("### Méthodes de listes", "Frython", "Python", "Description"),
        "METHODES_DICT":         ("### Méthodes de dictionnaires", "Frython", "Python", "Description"),
        "METHODES_ENSEMBLE":     ("### Méthodes d'ensembles", "Frython", "Python", "Description"),
        "MODULES_TRADUITS":      ("### Modules traduits", "Frython", "Python", "Description"),
    }

    lignes = []
    for nom_dict, (titre, col1, col2, col3) in sections.items():
        d = dicts.get(nom_dict, {})
        if not d:
            continue
        lignes.append(f"\n{titre}\n")
        lignes.append(f"| {col1} | {col2} |")
        lignes.append("|--------|--------|")
        for fr, py in sorted(d.items()):
            lignes.append(f"| `{fr}` | `{py}` |")
        lignes.append("")

    return "\n".join(lignes)


def mettre_a_jour_documentation_md(nouveaux_dicts, nouveautes):
    """Met à jour la section des mots-clés dans DOCUMENTATION.md."""
    try:
        with open(DOCUMENTATION, "r", encoding="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        print("⚠️  DOCUMENTATION.md introuvable, création d'un nouveau fichier.")
        contenu = "# 📚 Documentation Frython\n\n## Référence complète\n\n<!-- MOTS_CLES_START -->\n<!-- MOTS_CLES_END -->\n"

    nouveau_tableau = generer_tableau_mots_cles(nouveaux_dicts)

    debut = "<!-- MOTS_CLES_START -->"
    fin = "<!-- MOTS_CLES_END -->"

    if debut in contenu and fin in contenu:
        avant = contenu[:contenu.index(debut) + len(debut)]
        apres = contenu[contenu.index(fin):]
        contenu = avant + "\n" + nouveau_tableau + "\n" + apres
    else:

        contenu += f"\n\n{debut}\n{nouveau_tableau}\n{fin}\n"

    date = datetime.now().strftime("%Y-%m-%d")
    contenu = re.sub(
        r"_Documentation générée pour Frython v[\d\.]+ — .*_",
        f"_Documentation mise à jour le {date} — 🐓 Python en français, sacré bleu !_",
        contenu
    )

    with open(DOCUMENTATION, "w", encoding="utf-8") as f:
        f.write(contenu)

    print(f"✅ DOCUMENTATION.md mis à jour")

def afficher_resume(nouveautes):
    """Affiche un résumé des changements détectés."""
    print("\n" + "=" * 50)
    print("🐓 FRYTHON — Détection de nouveaux mots-clés")
    print("=" * 50)

    if not nouveautes:
        print("✅ Aucun nouveau mot-clé détecté.")
        print("=" * 50 + "\n")
        return

    total = sum(len(m) for m in nouveautes.values())
    print(f"🆕 {total} nouveau(x) mot(s) détecté(s) !\n")

    for categorie, mots in nouveautes.items():
        print(f"  📂 {categorie} ({len(mots)}):")
        for fr, py in mots.items():
            print(f"     '{fr}' → '{py}'")
        print()

    print("=" * 50 + "\n")

def main():
    try:
        with open(TRANSPILEUR, "r", encoding="utf-8") as f:
            contenu_actuel = f.read()
    except FileNotFoundError:
        print(f"❌ Impossible de lire {TRANSPILEUR}")
        sys.exit(1)

    contenu_precedent = get_contenu_precedent()

    nouveaux_dicts = extraire_tous_les_mots(contenu_actuel)
    anciens_dicts = extraire_tous_les_mots(contenu_precedent) if contenu_precedent else {}

    nouveautes = trouver_nouveaux_mots(anciens_dicts, nouveaux_dicts)

    afficher_resume(nouveautes)

    if nouveautes:
        version = determiner_version()
        mettre_a_jour_update_md(nouveautes, version)
        mettre_a_jour_documentation_md(nouveaux_dicts, nouveautes)
        print(f"📦 Version documentée: {version}")
    else:
        mettre_a_jour_documentation_md(nouveaux_dicts, {})
        print("📄 Tableaux DOCUMENTATION.md rafraîchis.")

    print("✅ Terminé!")


if __name__ == "__main__":
    main()
