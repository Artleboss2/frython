# 📚 Documentation Frython

> Documentation complète du langage de programmation Frython — Python en français 🐓

---

## Table des matières

1. [Introduction](#1-introduction)
2. [Installation](#2-installation)
3. [Utilisation](#3-utilisation)
4. [Syntaxe complète](#4-syntaxe-complète)
5. [Mots-clés](#5-mots-clés)
6. [Fonctions intégrées](#6-fonctions-intégrées)
7. [Méthodes](#7-méthodes)
8. [Modules traduits](#8-modules-traduits)
9. [Exceptions et erreurs](#9-exceptions-et-erreurs)
10. [Exemples complets](#10-exemples-complets)
11. [API Python](#11-api-python)
12. [Architecture interne](#12-architecture-interne)
13. [Extension VS Code](#13-extension-vs-code)
14. [FAQ](#14-faq)
15. [Contribuer](#15-contribuer)

---

## 1. Introduction

**Frython** est un langage de programmation transpilé basé sur Python. Il permet d'écrire du code Python en utilisant des mots-clés et des fonctions entièrement en français.

### Comment ça fonctionne

```
Code Frython (.fy)
       ↓
  [TRANSPILEUR]
       ↓
  Code Python valide
       ↓
  [INTERPRÉTEUR Python]
       ↓
     Résultat
```

Frython ne réinvente pas la roue — il traduit simplement le code français vers Python standard, puis laisse Python faire le reste. Tout ce que Python peut faire, Frython peut le faire.

### Pourquoi Frython ?

- 🎭 C'est un projet humoristique mais entièrement fonctionnel
- 🎓 Excellent pour apprendre la programmation en français
- 🔧 100% compatible avec toutes les bibliothèques Python
- 🐓 Le coq est une mascotte parfaite

---

## 2. Installation

### Prérequis

- Python 3.8 ou supérieur
- pip

### Depuis PyPI (recommandé)

```bash
pip install frython
```

### Depuis les sources

```bash
git clone https://github.com/Artleboss2/frython.git
cd frython
pip install .
```

### Vérifier l'installation

```bash
python -m frython --version
# Frython 1.0.0 — Python en français 🐓
```

### Sur Windows avec plusieurs versions de Python

Si vous avez plusieurs versions de Python installées :

```bash
C:\Python314\python.exe -m frython mon_fichier.fy
```

Ou créez un alias PowerShell permanent :

```powershell
# Dans votre $PROFILE PowerShell
function frython { C:\Python314\python.exe -m frython $args }
```

---

## 3. Utilisation

### Exécuter un fichier

```bash
python -m frython mon_programme.fy
```

### REPL interactive

```bash
python -m frython
```

```
🐓 Frython v1.0.0 — Python en français, sacré bleu !

🐓 >>> afficher("Bonjour!")
Bonjour!
🐓 >>> x = 42
🐓 >>> x * 2
84
🐓 >>> quitter()
Au revoir! 👋
```

### Options de la ligne de commande

| Option | Description |
|--------|-------------|
| `python -m frython fichier.fy` | Exécuter un fichier |
| `python -m frython` | Lancer la REPL |
| `python -m frython -t fichier.fy` | Afficher le code Python transpilé |
| `python -m frython -v fichier.fy` | Mode verbeux |
| `python -m frython -c "code"` | Exécuter du code direct |
| `python -m frython --mots-cles` | Lister tous les mots-clés |
| `python -m frython --version` | Afficher la version |

### Voir le code Python généré

```bash
python -m frython -t mon_programme.fy
```

Utile pour déboguer ou comprendre comment Frython transpile votre code.

---

## 4. Syntaxe complète

### Variables et types

```python
# Entiers
age = 25
annee = 2026

# Décimaux
taille = 1.75
pi = 3.14159

# Chaînes
prenom = "Marie"
message = 'Bonjour le monde!'
multiligne = """
Ceci est un texte
sur plusieurs lignes
"""

# f-strings
afficher(f"Bonjour, {prenom}! Tu as {age} ans.")

# Booléens
est_majeur = Vrai
est_mineur = Faux

# Nul
valeur = Rien
```

### Structures de données

```python
# Listes
nombres = [1, 2, 3, 4, 5]
mixte = ["texte", 42, Vrai, Rien]

# Dictionnaires
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris"
}

# Ensembles
couleurs = {"rouge", "vert", "bleu"}

# Tuples
coordonnees = (48.8566, 2.3522)
```

### Conditions

```python
# Si simple
si age >= 18:
    afficher("Majeur")

# Si / Sinon
si temperature > 30:
    afficher("Il fait chaud!")
sinon:
    afficher("Il fait frais.")

# Si / Sinonsi / Sinon
si note >= 16:
    mention = "Très bien"
sinonsi note >= 14:
    mention = "Bien"
sinonsi note >= 12:
    mention = "Assez bien"
sinonsi note >= 10:
    mention = "Passable"
sinon:
    mention = "Insuffisant"
```

### Boucles

```python
# Boucle pour
pour i dans intervalle(5):
    afficher(i)

# Boucle pour avec liste
fruits = ["pomme", "banane", "cerise"]
pour fruit dans fruits:
    afficher(fruit)

# Boucle pour avec enumerer
pour i, fruit dans enumerer(fruits):
    afficher(f"{i}: {fruit}")

# Boucle tantque
compteur = 0
tantque compteur < 10:
    afficher(compteur)
    compteur += 1

# Casser et continuer
pour i dans intervalle(10):
    si i == 5:
        casser
    si i % 2 == 0:
        continuer
    afficher(i)
```

### Fonctions

```python
# Fonction simple
déf saluer(nom):
    afficher(f"Bonjour, {nom}!")

# Fonction avec retour
déf additionner(a, b):
    retourner a + b

# Valeurs par défaut
déf saluer(nom, salutation="Bonjour"):
    retourner f"{salutation}, {nom}!"

# *args et **kwargs
déf afficher_tout(*args, **kwargs):
    pour arg dans args:
        afficher(arg)
    pour cle, valeur dans kwargs.elements():
        afficher(f"{cle}: {valeur}")

# Fonction récursive
déf factorielle(n):
    si n <= 1:
        retourner 1
    retourner n * factorielle(n - 1)

# Lambda
doubler = lambda x: x * 2
```

### Classes

```python
classe Animal:
    """Classe de base pour les animaux."""
    
    def __init__(soi, nom, age):
        soi.nom = nom
        soi.age = age
    
    déf parler(soi):
        retourner "..."
    
    déf __str__(soi):
        retourner f"{soi.nom} ({soi.age} ans)"


classe Chien(Animal):
    """Un chien."""
    
    def __init__(soi, nom, age, race):
        super().__init__(nom, age)
        soi.race = race
    
    déf parler(soi):
        retourner "Ouaf!"


# Utilisation
rex = Chien("Rex", 3, "Berger")
afficher(rex)          # Rex (3 ans)
afficher(rex.parler()) # Ouaf!
```

### Compréhensions

```python
# Compréhension de liste
carres = [x**2 pour x dans intervalle(1, 11)]

# Avec condition
pairs = [x pour x dans intervalle(20) si x % 2 == 0]

# Compréhension de dictionnaire
carres_dict = {n: n**2 pour n dans intervalle(1, 6)}

# Compréhension d'ensemble
lettres = {c pour c dans "frython" si c != "o"}
```

### Exceptions

```python
essayer:
    resultat = 10 / 0
sauf ZeroDivisionError:
    afficher("Division par zéro!")
sauf (ValueError, TypeError) comme e:
    afficher(f"Erreur: {e}")
enfin:
    afficher("Toujours exécuté.")

# Lever une exception
déf diviser(a, b):
    si b == 0:
        lever ErreurValeur("Le diviseur ne peut pas être zéro!")
    retourner a / b
```

### Générateurs

```python
déf compter(n):
    i = 0
    tantque i < n:
        rendement i
        i += 1

pour nombre dans compter(5):
    afficher(nombre)
```

### Gestionnaires de contexte

```python
avec ouvrir("fichier.txt", "r") comme f:
    contenu = f.lire()
    afficher(contenu)
```

### Décorateurs

```python
importer functools

déf minuteur(fonction):
    @functools.wraps(fonction)
    déf enveloppe(*args, **kwargs):
        importer time
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        afficher(f"Durée: {time.time() - debut:.3f}s")
        retourner resultat
    retourner enveloppe

@minuteur
déf calcul_lent():
    retourner somme(intervalle(1000000))
```

---

<!-- MOTS_CLES_START -->

### Mots-clés et fonctions intégrées

| Frython | Python |
|---------|--------|
| `Avertissement` | `Warning` |
| `AvertissementDepreciation` | `DeprecationWarning` |
| `AvertissementFutur` | `FutureWarning` |
| `AvertissementRuntime` | `RuntimeWarning` |
| `AvertissementSyntaxe` | `SyntaxWarning` |
| `AvertissementUtilisateur` | `UserWarning` |
| `Ellipsis` | `Ellipsis` |
| `ErreurArret` | `StopIteration` |
| `ErreurAssertion` | `AssertionError` |
| `ErreurAttribut` | `AttributeError` |
| `ErreurCle` | `KeyError` |
| `ErreurConnexion` | `ConnectionError` |
| `ErreurDebordement` | `OverflowError` |
| `ErreurDivisionZero` | `ZeroDivisionError` |
| `ErreurES` | `IOError` |
| `ErreurFichier` | `FileNotFoundError` |
| `ErreurImport` | `ImportError` |
| `ErreurIndentation` | `IndentationError` |
| `ErreurIndex` | `IndexError` |
| `ErreurInterruption` | `KeyboardInterrupt` |
| `ErreurMemoire` | `MemoryError` |
| `ErreurNom` | `NameError` |
| `ErreurNotImplemented` | `NotImplementedError` |
| `ErreurOS` | `OSError` |
| `ErreurPermission` | `PermissionError` |
| `ErreurRecursion` | `RecursionError` |
| `ErreurRuntime` | `RuntimeError` |
| `ErreurSyntaxe` | `SyntaxError` |
| `ErreurSysteme` | `SystemError` |
| `ErreurTabulation` | `TabError` |
| `ErreurTimeout` | `TimeoutError` |
| `ErreurType` | `TypeError` |
| `ErreurUnicode` | `UnicodeError` |
| `ErreurValeur` | `ValueError` |
| `Faux` | `False` |
| `NotImplemented` | `NotImplemented` |
| `Rien` | `None` |
| `Vrai` | `True` |
| `absolu` | `abs` |
| `afficher` | `print` |
| `afficher_format` | `format` |
| `affirmer` | `assert` |
| `aide` | `help` |
| `appeler` | `callable` |
| `arrondir` | `round` |
| `asynchrone` | `async` |
| `attendre` | `await` |
| `aucun` | `any` |
| `avec` | `with` |
| `binaire` | `bin` |
| `booleen` | `bool` |
| `breakpoint` | `breakpoint` |
| `caractere` | `chr` |
| `casser` | `break` |
| `chaine` | `str` |
| `classe` | `class` |
| `classique` | `classmethod` |
| `comme` | `as` |
| `complexe` | `complex` |
| `continuer` | `continue` |
| `dans` | `in` |
| `de` | `from` |
| `decimal` | `float` |
| `dictionnaire` | `dict` |
| `divmod` | `divmod` |
| `déf` | `def` |
| `enfin` | `finally` |
| `ensemble` | `set` |
| `entier` | `int` |
| `entier_long` | `int` |
| `entree` | `input` |
| `entree_erreur` | `stderr` |
| `entree_standard` | `stdin` |
| `enumerer` | `enumerate` |
| `essayer` | `try` |
| `est` | `is` |
| `et` | `and` |
| `evaluer` | `eval` |
| `executer` | `exec` |
| `executer_fichier` | `execfile` |
| `fermer` | `close` |
| `fige` | `frozenset` |
| `filtrer` | `filter` |
| `formater_chaine` | `format` |
| `geler` | `frozenset` |
| `global` | `global` |
| `globals` | `globals` |
| `hash` | `hash` |
| `hex` | `hex` |
| `identifiant` | `id` |
| `importer` | `import` |
| `imprimer` | `print` |
| `imprimer_erreur` | `sys.stderr.write` |
| `instance_de` | `isinstance` |
| `intervalle` | `range` |
| `inverser` | `reversed` |
| `iter` | `iter` |
| `lambda` | `lambda` |
| `lever` | `raise` |
| `liste` | `list` |
| `locals` | `locals` |
| `longueur` | `len` |
| `longueur_max` | `max` |
| `longueur_min` | `min` |
| `mapper` | `map` |
| `maximum` | `max` |
| `memoire` | `memoryview` |
| `minimum` | `min` |
| `non` | `not` |
| `nonlocal` | `nonlocal` |
| `objet` | `object` |
| `octal` | `oct` |
| `octets` | `bytes` |
| `ordinal` | `ord` |
| `ou` | `or` |
| `ouvrir` | `open` |
| `pasdans` | `not in` |
| `passer` | `pass` |
| `pour` | `for` |
| `prochain` | `next` |
| `propriete` | `property` |
| `puissance` | `pow` |
| `rendement` | `yield` |
| `repr` | `repr` |
| `retourner` | `return` |
| `saisir` | `input` |
| `sauf` | `except` |
| `si` | `if` |
| `sinon` | `else` |
| `sinonsi` | `elif` |
| `soi` | `self` |
| `somme` | `sum` |
| `sortie_standard` | `stdout` |
| `sous_classe` | `issubclass` |
| `statique` | `staticmethod` |
| `super` | `super` |
| `supprimer` | `del` |
| `tableau` | `bytearray` |
| `taille` | `sizeof` |
| `tantque` | `while` |
| `tous` | `all` |
| `toutca` | `any` |
| `tranche` | `slice` |
| `trier` | `sorted` |
| `tuple` | `tuple` |
| `type` | `type` |
| `type_base` | `type` |
| `vrai_faux` | `bool` |
| `zipper` | `zip` |


### Méthodes de chaînes

| Frython | Python |
|---------|--------|
| `aligner_droite` | `rjust` |
| `aligner_gauche` | `ljust` |
| `capitaliser` | `capitalize` |
| `centrer` | `center` |
| `commencer_par` | `startswith` |
| `compter` | `count` |
| `compter_depuis` | `count` |
| `compter_tout` | `count` |
| `contient` | `__contains__` |
| `decoder` | `decode` |
| `diviser` | `split` |
| `diviser_droite` | `rsplit` |
| `diviser_lignes` | `splitlines` |
| `en_liste` | `split` |
| `encoder` | `encode` |
| `est_alpha` | `isalpha` |
| `est_alphanum` | `isalnum` |
| `est_ascii` | `isascii` |
| `est_decimal` | `isdecimal` |
| `est_digit` | `isdigit` |
| `est_espace` | `isspace` |
| `est_identifiant` | `isidentifier` |
| `est_imprimable` | `isprintable` |
| `est_majuscule` | `isupper` |
| `est_minuscule` | `islower` |
| `est_numerique` | `isnumeric` |
| `est_titre` | `istitle` |
| `expandre_tabs` | `expandtabs` |
| `finir_par` | `endswith` |
| `formater` | `format` |
| `formater_map` | `format_map` |
| `indice` | `index` |
| `joindre` | `join` |
| `majuscule` | `upper` |
| `maketrans` | `maketrans` |
| `minuscule` | `lower` |
| `partitionner` | `partition` |
| `remplacer` | `replace` |
| `remplir_zeros` | `zfill` |
| `rfind` | `rfind` |
| `rindex` | `rindex` |
| `rpartitionner` | `rpartition` |
| `supprimer_espaces` | `strip` |
| `supprimer_espaces_droite` | `rstrip` |
| `supprimer_espaces_gauche` | `lstrip` |
| `supprimer_prefixe` | `removeprefix` |
| `supprimer_suffixe` | `removesuffix` |
| `titrer` | `title` |
| `traduire` | `translate` |
| `trouver` | `find` |


### Méthodes de listes

| Frython | Python |
|---------|--------|
| `ajouter` | `append` |
| `annexer` | `append` |
| `compter` | `count` |
| `concatener` | `extend` |
| `copie_profonde` | `copy` |
| `copier` | `copy` |
| `dernier` | `pop` |
| `effacer` | `clear` |
| `etendre` | `extend` |
| `existe` | `__contains__` |
| `extraire` | `pop` |
| `indice` | `index` |
| `inserer` | `insert` |
| `inserer_debut` | `insert` |
| `inverser` | `reverse` |
| `longueur` | `__len__` |
| `multiplier` | `__mul__` |
| `premier` | `pop` |
| `remplir` | `fill` |
| `remplir_avec` | `extend` |
| `retirer` | `remove` |
| `supprimer` | `remove` |
| `trier` | `sort` |
| `vider` | `clear` |


### Méthodes de dictionnaires

| Frython | Python |
|---------|--------|
| `a_cle` | `has_key` |
| `cles` | `keys` |
| `contient` | `__contains__` |
| `contient_cle` | `__contains__` |
| `copier` | `copy` |
| `depuis_cles` | `fromkeys` |
| `effacer` | `clear` |
| `elements` | `items` |
| `extraire` | `pop` |
| `extraire_defaut` | `setdefault` |
| `extraire_dernier` | `popitem` |
| `fusionner` | `update` |
| `inverser` | `items` |
| `longueur` | `__len__` |
| `mettre_a_jour` | `update` |
| `obtenir` | `get` |
| `obtenir_ou_creer` | `setdefault` |
| `valeurs` | `values` |
| `vider` | `clear` |


### Méthodes d'ensembles

| Frython | Python |
|---------|--------|
| `ajouter` | `add` |
| `copier` | `copy` |
| `diff_sym_sur_place` | `symmetric_difference_update` |
| `difference` | `difference` |
| `difference_sur_place` | `difference_update` |
| `difference_symetrique` | `symmetric_difference` |
| `ecarter` | `discard` |
| `est_disjoint` | `isdisjoint` |
| `est_sous_ensemble` | `issubset` |
| `est_sur_ensemble` | `issuperset` |
| `est_vide` | `__len__` |
| `extraire_aleatoire` | `pop` |
| `geler` | `frozenset` |
| `intersection` | `intersection` |
| `intersection_sur_place` | `intersection_update` |
| `mettre_a_jour` | `update` |
| `retirer` | `remove` |
| `supprimer_si_existe` | `discard` |
| `union` | `union` |
| `union_sur_place` | `update` |
| `vider` | `clear` |


### Modules traduits

| Frython | Python |
|---------|--------|
| `abstrait` | `abc` |
| `aleatoire` | `random` |
| `archive` | `tarfile` |
| `argparse` | `argparse` |
| `arguments` | `argparse` |
| `async_io` | `asyncio` |
| `base64` | `base64` |
| `base_donnees` | `sqlite3` |
| `binaire_io` | `io` |
| `calcul` | `numpy` |
| `chemin` | `os.path` |
| `chemin_fichier` | `pathlib` |
| `chiffrement` | `cryptography` |
| `collections` | `collections` |
| `compression` | `zipfile` |
| `configparser` | `configparser` |
| `configuration` | `configparser` |
| `contextlib` | `contextlib` |
| `copie` | `copy` |
| `copie_profonde` | `deepcopy` |
| `couleur` | `colorsys` |
| `csv` | `csv` |
| `dataclasse` | `dataclasses` |
| `date` | `datetime` |
| `datetime` | `datetime` |
| `decimal_module` | `decimal` |
| `decimal_precision` | `decimal` |
| `donnees` | `pandas` |
| `email` | `email` |
| `encodage` | `base64` |
| `entree_sortie` | `io` |
| `enum` | `enum` |
| `environnement` | `dotenv` |
| `expression_reguliere` | `re` |
| `fil` | `threading` |
| `fonctionnel` | `functools` |
| `fractions` | `fractions` |
| `functools` | `functools` |
| `garbage` | `gc` |
| `graphiques` | `matplotlib` |
| `hachage` | `hashlib` |
| `hashlib` | `hashlib` |
| `html` | `html` |
| `http` | `http` |
| `images` | `PIL` |
| `inspection` | `inspect` |
| `interface` | `tkinter` |
| `io` | `io` |
| `iterateurs` | `itertools` |
| `itertools` | `itertools` |
| `journalisation` | `logging` |
| `json` | `json` |
| `logging` | `logging` |
| `mathematiques` | `math` |
| `mathématiques` | `math` |
| `multiprocessing` | `multiprocessing` |
| `multiprocessus` | `multiprocessing` |
| `nombres` | `numbers` |
| `pathlib` | `pathlib` |
| `plateforme` | `platform` |
| `re` | `re` |
| `reseau` | `urllib` |
| `secret` | `secrets` |
| `signal` | `signal` |
| `socket` | `socket` |
| `sous_processus` | `subprocess` |
| `sqlite3` | `sqlite3` |
| `statistiques` | `statistics` |
| `struct` | `struct` |
| `subprocess` | `subprocess` |
| `systeme` | `sys` |
| `systeme_exploitation` | `os` |
| `temps` | `time` |
| `test_rapide` | `pytest` |
| `tests` | `unittest` |
| `threading` | `threading` |
| `tortue` | `turtle` |
| `traceback` | `traceback` |
| `types_donnees` | `typing` |
| `unittest` | `unittest` |
| `urllib` | `urllib` |
| `uuid` | `uuid` |
| `warnings` | `warnings` |
| `weakref` | `weakref` |
| `web` | `requests` |
| `xml` | `xml` |

<!-- MOTS_CLES_END -->

## 9. Exceptions et erreurs

### Exceptions Frython

| Frython | Python | Description |
|---------|--------|-------------|
| `ErreurValeur` | `ValueError` | Valeur incorrecte |
| `ErreurType` | `TypeError` | Mauvais type |
| `ErreurNom` | `NameError` | Nom non défini |
| `ErreurIndex` | `IndexError` | Indice hors limites |
| `ErreurCle` | `KeyError` | Clé inexistante |
| `ErreurAttribut` | `AttributeError` | Attribut inexistant |
| `ErreurImport` | `ImportError` | Import impossible |
| `ErreurMemoire` | `MemoryError` | Mémoire insuffisante |
| `ErreurRecursion` | `RecursionError` | Récursion infinie |
| `ErreurSyntaxe` | `SyntaxError` | Erreur de syntaxe |
| `ErreurDivisionZero` | `ZeroDivisionError` | Division par zéro |
| `ErreurFichier` | `FileNotFoundError` | Fichier introuvable |
| `ErreurPermission` | `PermissionError` | Permission refusée |
| `ErreurArret` | `StopIteration` | Arrêt d'itération |
| `ErreurOS` | `OSError` | Erreur système |
| `ErreurConnexion` | `ConnectionError` | Erreur de connexion |
| `ErreurDebordement` | `OverflowError` | Dépassement |
| `ErreurRuntime` | `RuntimeError` | Erreur d'exécution |
| `ErreurTimeout` | `TimeoutError` | Délai dépassé |
| `ErreurInterruption` | `KeyboardInterrupt` | Interruption clavier |
| `ErreurAssertion` | `AssertionError` | Assertion échouée |

### Avertissements

| Frython | Python |
|---------|--------|
| `Avertissement` | `Warning` |
| `AvertissementDepreciation` | `DeprecationWarning` |
| `AvertissementRuntime` | `RuntimeWarning` |
| `AvertissementSyntaxe` | `SyntaxWarning` |
| `AvertissementUtilisateur` | `UserWarning` |
| `AvertissementFutur` | `FutureWarning` |

### Exemple de gestion complète

```python
déf lire_fichier(chemin):
    essayer:
        avec ouvrir(chemin, "r") comme f:
            retourner f.lire()
    sauf ErreurFichier:
        afficher(f"Fichier '{chemin}' introuvable!")
        retourner Rien
    sauf ErreurPermission:
        afficher(f"Permission refusée pour '{chemin}'!")
        retourner Rien
    sauf Exception comme e:
        lever ErreurRuntime(f"Erreur inattendue: {e}")
    enfin:
        afficher("Tentative de lecture terminée.")
```

---

## 10. Exemples complets

### Calculatrice

```python
# calculatrice.fy
tantque Vrai:
    essayer:
        entree = saisir(">>> ")
        si entree dans ("quitter", "q"):
            casser
        afficher(f"= {eval(entree)}")
    sauf ZeroDivisionError:
        afficher("Division par zéro!")
    sauf Exception:
        afficher("Expression invalide.")
```

### Fibonacci

```python
# fibonacci.fy
déf fibonacci(n):
    si n <= 1:
        retourner n
    retourner fibonacci(n-1) + fibonacci(n-2)

pour i dans intervalle(15):
    afficher(f"F({i}) = {fibonacci(i)}")
```

### Tri à bulles

```python
# tri_bulles.fy
déf tri_bulles(lst):
    arr = liste(lst)
    n = longueur(arr)
    pour i dans intervalle(n):
        pour j dans intervalle(0, n - i - 1):
            si arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    retourner arr

nombres = [64, 34, 25, 12, 22, 11, 90]
afficher(tri_bulles(nombres))
```

---

## 11. API Python

Vous pouvez utiliser Frython comme bibliothèque Python :

```python
from frython import transpiler, InterpreteurFrython

# Transpiler uniquement
code_python = transpiler("""
déf bonjour(nom):
    afficher(f"Bonjour, {nom}!")
bonjour("Monde")
""")
print(code_python)

# Exécuter
interp = InterpreteurFrython()
interp.executer_source(code_frython)

# Exécuter un fichier
interp.executer_fichier("mon_programme.fy")
```

---

## 12. Architecture interne

### Fichiers principaux

```
frython/
├── __init__.py      # Point d'entrée, exports publics
├── lexeur.py        # Tokenizer (analyse lexicale)
├── transpileur.py   # Cœur : traduit Frython → Python
└── interpreteur.py  # REPL et exécution
```

### Le transpileur

Le transpileur fonctionne en plusieurs étapes :

1. **Séparation des chaînes** — protège le contenu des strings
2. **Traduction des méthodes** — `.ajouter()` → `.append()`
3. **Traduction des modules** — `mathématiques` → `math`
4. **Traduction des mots-clés** — `si` → `if`, `afficher` → `print`
5. **Traduction des f-strings** — traduit les expressions à l'intérieur des `{}`

### Dictionnaires de traduction

- `MOTS_CLES_VERS_PYTHON` — mots-clés et fonctions globales
- `METHODES_CHAINE` — méthodes de chaînes
- `METHODES_LISTE` — méthodes de listes
- `METHODES_DICT` — méthodes de dictionnaires
- `METHODES_ENSEMBLE` — méthodes d'ensembles
- `MODULES_TRADUITS` — noms de modules

---

## 13. Extension VS Code

Une extension VS Code est disponible pour Frython avec :

- **Coloration syntaxique** complète pour les fichiers `.fy`
- **Snippets** pour écrire du Frython rapidement
- **Auto-indentation** après `:`
- **Auto-fermeture** des paires de caractères

### Snippets disponibles

| Préfixe | Description |
|---------|-------------|
| `aff` | `afficher()` |
| `afff` | `afficher()` avec f-string |
| `si` | Bloc si/sinon |
| `sisi` | Bloc si/sinonsi/sinon |
| `def` | Définir une fonction |
| `defr` | Fonction avec retour |
| `cls` | Définir une classe |
| `clsh` | Classe avec héritage |
| `tq` | Boucle tantque |
| `pour` | Boucle pour/dans |
| `pouri` | Boucle pour avec intervalle |
| `poure` | Boucle pour avec enumerer |
| `ess` | Bloc essayer/sauf |
| `esse` | Bloc essayer/sauf/enfin |
| `imp` | Importer |
| `impd` | Importer depuis |
| `lev` | Lever une erreur |
| `comp` | Compréhension de liste |
| `compc` | Compréhension avec condition |
| `lam` | Lambda |
| `avec` | Gestionnaire de contexte |
| `main` | Garde principale |
| `doc` | Docstring complète |

---

## 14. FAQ

**Q: Frython est-il vraiment utilisable en production ?**  
R: Techniquement oui — le code transpilé est du Python valide. En pratique, votre équipe va vous regarder bizarrement.

**Q: Puis-je utiliser des bibliothèques Python externes ?**  
R: Oui, toutes. `importer numpy comme np` fonctionne parfaitement.

**Q: Les f-strings fonctionnent-elles ?**  
R: Oui, et les expressions à l'intérieur des `{}` sont aussi traduites.

**Q: Puis-je mixer Frython et Python dans le même fichier ?**  
R: Oui — `def` et `déf` sont tous les deux supportés, `True` et `Vrai` aussi.

**Q: Frython supporte-t-il async/await ?**  
R: Oui — `asynchrone` et `attendre`.

**Q: Les accents dans les noms de variables sont-ils supportés ?**  
R: Pour les mots-clés et méthodes oui. Pour les noms de variables, ça dépend de votre version de Python.

**Q: Pourquoi ce projet existe-t-il ?**  
R: *Pourquoi pas ?* 🥐

---

## 15. Contribuer

### Comment contribuer

1. Forkez le repo : `https://github.com/Artleboss2/frython`
2. Créez une branche : `git checkout -b feature/ma-feature`
3. Faites vos changements
4. Lancez les tests : `python -m unittest tests/test_frython.py -v`
5. Committez : `git commit -m "feat: ma feature"`
6. Push : `git push origin feature/ma-feature`
7. Ouvrez une Pull Request

### Idées de contributions

- Ajouter de nouveaux mots-clés français
- Améliorer les messages d'erreur en français
- Créer des exemples de programmes
- Ajouter des tests
- Améliorer la documentation
- Créer des tutoriels
- Traduire dans d'autres langues (*Pythonisch ? Pythönen ?*)

### Standards de code

- Tests requis pour toute nouvelle fonctionnalité
- Docstrings en français
- Messages de commit en anglais ou français

---

*Documentation générée pour Frython v1.0.2 — 🐓 Python en français, sacré bleu !*
