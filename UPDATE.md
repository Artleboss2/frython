# 📝 Historique des mises à jour — Frython

> Tous les changements notables du projet Frython, dans l'ordre chronologique.

---

## [1.0.3] — 2026-03-22


### Supprimé

- **Méthodes de dictionnaires** — 1 supprimé(s):
  - `supprimer` (était `__delitem__`)

---


## [1.0.2] — 2026-03-20

### Ajouté
- Fichier `DOCUMENTATION.md` — documentation complète du langage
- Fichier `UPDATE.md` — historique des changements
- Fichier `.gitattributes` — détection du langage Frython par GitHub
- Fichier `languages.yml` — définition officielle du langage pour GitHub Linguist
- Extension VS Code — coloration syntaxique pour les fichiers `.fy`
- Snippets VS Code — raccourcis pour écrire du Frython rapidement
- Fichier `CODE-OF-CONDUCT.md` — code de conduite de la communauté
- Fichier `CONTRIBUTING.md` — guide de contribution

### Amélioré
- Coloration syntaxique VS Code — ajout des appels de fonctions, méthodes, opérateurs, f-strings
- `interpreteur.py` — correction du module `readline` sur Windows (ImportError silencieux)
- `transpileur.py` — correction de la priorité des méthodes (`.ajouter()` → `.append()` au lieu de `.add()`)
- `transpileur.py` — traduction des expressions dans les f-strings (`{soi.nom}` → `{self.nom}`)
- `transpileur.py` — ajout de dizaines de mots-clés, méthodes et modules traduits

---

## [1.0.1] — 2026-03-19

### Ajouté
- Publication sur **PyPI** — `pip install frython` fonctionne mondialement
- Workflow GitHub Actions `.github/workflows/publish.yml` — publication automatique sur PyPI
- Exemples supplémentaires :
  - `calculatrice.fy` — calculatrice interactive
  - `devine_nombre.fy` — jeu de devinettes
  - `todo.fy` — gestionnaire de tâches
  - `carnet_contacts.fy` — carnet d'adresses
  - `pendu.fy` — jeu du pendu
  - `rpg.fy` — mini RPG complet
  - `algorithmes_tri.fy` — 5 algorithmes de tri avec benchmarks
  - `statistiques.fy` — statistiques et histogramme ASCII
  - `analyse_texte.fy` — analyseur de texte
  - `art_ascii.fy` — Mandelbrot, Pascal, spirale
  - `avance.fy` — décorateurs, générateurs, closures

### Corrigé
- `pyproject.toml` — correction du backend setuptools pour Python 3.14
- Compatibilité Windows — suppression de la dépendance `readline`

---

## [1.0.0] — 2026-03-19

### Ajouté — Version initiale

#### Cœur du langage
- `frython/transpileur.py` — transpileur Frython → Python
  - Dictionnaire `MOTS_CLES_VERS_PYTHON` — tous les mots-clés Python traduits en français
  - Dictionnaire `METHODES_CHAINE` — méthodes de chaînes traduites
  - Dictionnaire `METHODES_LISTE` — méthodes de listes traduites
  - Dictionnaire `METHODES_DICT` — méthodes de dictionnaires traduites
  - Dictionnaire `METHODES_ENSEMBLE` — méthodes d'ensembles traduites
  - Dictionnaire `MODULES_TRADUITS` — noms de modules traduits
  - Protection des chaînes de caractères (les strings ne sont pas modifiées)
  - Traduction des expressions dans les f-strings

- `frython/interpreteur.py` — interpréteur et REPL
  - REPL interactive avec prompt `🐓 >>>`
  - Exécution de fichiers `.fy`
  - Messages d'erreur traduits en français
  - Commandes spéciales : `quitter()`, `mots_cles()`
  - Bannière ASCII art au démarrage

- `frython/lexeur.py` — lexeur/tokenizer
  - Support des caractères accentués français
  - Gestion de l'indentation (INDENT/DEDENT)
  - Tous les types de tokens Python

- `frython/__init__.py` — point d'entrée du paquet
- `__main__.py` — interface en ligne de commande complète

#### Mots-clés supportés (version initiale)
- Contrôle de flux : `si`, `sinon`, `sinonsi`, `tantque`, `pour`, `dans`, `casser`, `continuer`, `passer`
- Définitions : `déf`, `retourner`, `classe`, `soi`, `lambda`, `rendement`, `asynchrone`, `attendre`
- Valeurs : `Vrai`, `Faux`, `Rien`
- Logique : `et`, `ou`, `non`, `est`, `pasdans`
- Import : `importer`, `de`, `comme`
- Exceptions : `essayer`, `sauf`, `enfin`, `lever`, `avec`, `affirmer`
- Fonctions : `afficher`, `saisir`, `longueur`, `intervalle`, `liste`, `dictionnaire`, `ensemble`, `tuple`, `entier`, `decimal`, `chaine`, `booleen`, `enumerer`, `zipper`, `mapper`, `filtrer`, `trier`, `inverser`, `somme`, `maximum`, `minimum`, `absolu`, `arrondir`, `aide`, `type`, `super`

#### Tests
- `tests/test_frython.py` — 48 tests unitaires
  - `TestsTranspileur` — 20 tests de transpilation
  - `TestsExecution` — 26 tests d'exécution complète
  - `TestsInterpreteur` — 2 tests de l'interpréteur

#### Exemples initiaux
- `exemples/bonjour_monde.fy` — Hello World
- `exemples/fibonacci.fy` — Suite de Fibonacci
- `exemples/classes.fy` — Programmation orientée objet
- `exemples/vitrine.fy` — Démonstration complète de toutes les fonctionnalités

#### Documentation et configuration
- `README.md` — documentation principale avec badges
- `LICENSE` — licence MIT
- `.gitignore` — fichiers ignorés par Git
- `setup.py` — configuration du paquet Python
- `pyproject.toml` — configuration moderne du build

---

## Roadmap — À venir

### [1.1.0] — Prévu

- [ ] Meilleurs messages d'erreur en français
- [ ] Support complet de `async`/`await`
- [ ] Plugin JetBrains (PyCharm)
- [ ] Documentation interactive en ligne
- [ ] Mode strict (refuse le Python non-traduit)
- [ ] `frython lint` — vérificateur de style

### [2.0.0] — Vision long terme

- [ ] Vrai parser AST (au lieu du transpileur regex)
- [ ] Débogueur intégré
- [ ] Support de la traduction vers d'autres langues
- [ ] Frython dans le navigateur (WebAssembly)
- [ ] Reconnaissance officielle par GitHub Linguist

---

## Format des versions

Ce projet suit [Semantic Versioning](https://semver.org/) :
- **MAJEUR** — changements incompatibles avec l'ancienne syntaxe
- **MINEUR** — nouvelles fonctionnalités rétrocompatibles
- **PATCH** — corrections de bugs

---

*🐓 Frython — Python en français, sacré bleu !*  
*github.com/Artleboss2/frython*
