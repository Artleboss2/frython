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

## 5. Mots-clés

### Contrôle de flux

| Frython | Python | Exemple |
|---------|--------|---------|
| `si` | `if` | `si x > 0:` |
| `sinon` | `else` | `sinon:` |
| `sinonsi` | `elif` | `sinonsi x == 0:` |
| `tantque` | `while` | `tantque Vrai:` |
| `pour` | `for` | `pour i dans liste:` |
| `dans` | `in` | `pour x dans items:` |
| `pasdans` | `not in` | `si x pasdans liste:` |
| `casser` | `break` | `casser` |
| `continuer` | `continue` | `continuer` |
| `passer` | `pass` | `passer` |

### Définitions

| Frython | Python | Exemple |
|---------|--------|---------|
| `déf` | `def` | `déf ma_fonction():` |
| `retourner` | `return` | `retourner valeur` |
| `classe` | `class` | `classe MaClasse:` |
| `soi` | `self` | `soi.attribut` |
| `lambda` | `lambda` | `lambda x: x*2` |
| `rendement` | `yield` | `rendement valeur` |
| `asynchrone` | `async` | `asynchrone déf f():` |
| `attendre` | `await` | `attendre coroutine()` |

### Valeurs spéciales

| Frython | Python | Valeur |
|---------|--------|--------|
| `Vrai` | `True` | Booléen vrai |
| `Faux` | `False` | Booléen faux |
| `Rien` | `None` | Valeur nulle |

### Opérateurs logiques

| Frython | Python | Exemple |
|---------|--------|---------|
| `et` | `and` | `si a > 0 et b > 0:` |
| `ou` | `or` | `si a == 0 ou b == 0:` |
| `non` | `not` | `si non liste:` |
| `est` | `is` | `si x est Rien:` |

### Import

| Frython | Python | Exemple |
|---------|--------|---------|
| `importer` | `import` | `importer random` |
| `de` | `from` | `de math importer sqrt` |
| `comme` | `as` | `importer numpy comme np` |

### Exceptions

| Frython | Python | Exemple |
|---------|--------|---------|
| `essayer` | `try` | `essayer:` |
| `sauf` | `except` | `sauf ValueError:` |
| `enfin` | `finally` | `enfin:` |
| `lever` | `raise` | `lever ValueError("msg")` |
| `affirmer` | `assert` | `affirmer x > 0` |

### Divers

| Frython | Python | Exemple |
|---------|--------|---------|
| `avec` | `with` | `avec ouvrir("f") comme f:` |
| `global` | `global` | `global ma_var` |
| `nonlocal` | `nonlocal` | `nonlocal compteur` |
| `supprimer` | `del` | `supprimer ma_liste[0]` |

---

## 6. Fonctions intégrées

### Entrée/Sortie

| Frython | Python | Description |
|---------|--------|-------------|
| `afficher()` | `print()` | Affiche du texte |
| `saisir()` | `input()` | Lit une entrée utilisateur |

### Conversion de types

| Frython | Python | Description |
|---------|--------|-------------|
| `entier()` | `int()` | Convertit en entier |
| `decimal()` | `float()` | Convertit en décimal |
| `chaine()` | `str()` | Convertit en chaîne |
| `booleen()` | `bool()` | Convertit en booléen |
| `liste()` | `list()` | Convertit en liste |
| `tuple()` | `tuple()` | Convertit en tuple |
| `ensemble()` | `set()` | Convertit en ensemble |
| `dictionnaire()` | `dict()` | Crée un dictionnaire |
| `octets()` | `bytes()` | Convertit en octets |
| `complexe()` | `complex()` | Crée un nombre complexe |

### Itération

| Frython | Python | Description |
|---------|--------|-------------|
| `intervalle()` | `range()` | Génère une suite |
| `enumerer()` | `enumerate()` | Énumère avec indices |
| `zipper()` | `zip()` | Combine des itérables |
| `mapper()` | `map()` | Applique une fonction |
| `filtrer()` | `filter()` | Filtre des éléments |
| `inverser()` | `reversed()` | Inverse un itérable |
| `trier()` | `sorted()` | Trie un itérable |

### Mathématiques

| Frython | Python | Description |
|---------|--------|-------------|
| `somme()` | `sum()` | Somme des éléments |
| `maximum()` | `max()` | Valeur maximale |
| `minimum()` | `min()` | Valeur minimale |
| `absolu()` | `abs()` | Valeur absolue |
| `arrondir()` | `round()` | Arrondit un nombre |
| `puissance()` | `pow()` | Puissance |

### Introspection

| Frython | Python | Description |
|---------|--------|-------------|
| `type()` | `type()` | Type d'un objet |
| `longueur()` | `len()` | Longueur |
| `identifiant()` | `id()` | Identifiant unique |
| `repr()` | `repr()` | Représentation |
| `aide()` | `help()` | Aide |
| `sous_classe()` | `issubclass()` | Test sous-classe |
| `instance_de()` | `isinstance()` | Test instance |
| `appeler()` | `callable()` | Test callable |

### Fichiers

| Frython | Python | Description |
|---------|--------|-------------|
| `ouvrir()` | `open()` | Ouvre un fichier |
| `fermer()` | `close()` | Ferme un fichier |

---

## 7. Méthodes

### Méthodes de chaînes

| Frython | Python | Description |
|---------|--------|-------------|
| `.majuscule()` | `.upper()` | Met en majuscules |
| `.minuscule()` | `.lower()` | Met en minuscules |
| `.capitaliser()` | `.capitalize()` | Première lettre majuscule |
| `.titrer()` | `.title()` | Format titre |
| `.remplacer(a, b)` | `.replace(a, b)` | Remplace a par b |
| `.diviser()` | `.split()` | Divise en liste |
| `.diviser_droite()` | `.rsplit()` | Divise depuis la droite |
| `.diviser_lignes()` | `.splitlines()` | Divise par lignes |
| `.joindre(lst)` | `.join(lst)` | Joint une liste |
| `.supprimer_espaces()` | `.strip()` | Supprime les espaces |
| `.supprimer_espaces_gauche()` | `.lstrip()` | Supprime à gauche |
| `.supprimer_espaces_droite()` | `.rstrip()` | Supprime à droite |
| `.commencer_par()` | `.startswith()` | Commence par |
| `.finir_par()` | `.endswith()` | Finit par |
| `.trouver()` | `.find()` | Trouve une sous-chaîne |
| `.indice()` | `.index()` | Index d'une sous-chaîne |
| `.compter()` | `.count()` | Compte les occurrences |
| `.formater()` | `.format()` | Formate la chaîne |
| `.encoder()` | `.encode()` | Encode en bytes |
| `.est_alpha()` | `.isalpha()` | Test alphabétique |
| `.est_digit()` | `.isdigit()` | Test numérique |
| `.est_alphanum()` | `.isalnum()` | Test alphanumérique |
| `.est_espace()` | `.isspace()` | Test espace |
| `.est_majuscule()` | `.isupper()` | Test majuscule |
| `.est_minuscule()` | `.islower()` | Test minuscule |
| `.est_titre()` | `.istitle()` | Test titre |
| `.est_ascii()` | `.isascii()` | Test ASCII |
| `.centrer()` | `.center()` | Centre le texte |
| `.aligner_gauche()` | `.ljust()` | Aligne à gauche |
| `.aligner_droite()` | `.rjust()` | Aligne à droite |
| `.remplir_zeros()` | `.zfill()` | Remplit avec des zéros |
| `.partitionner()` | `.partition()` | Partitionne |
| `.supprimer_prefixe()` | `.removeprefix()` | Supprime le préfixe |
| `.supprimer_suffixe()` | `.removesuffix()` | Supprime le suffixe |
| `.traduire()` | `.translate()` | Traduit les caractères |

### Méthodes de listes

| Frython | Python | Description |
|---------|--------|-------------|
| `.ajouter(x)` | `.append(x)` | Ajoute un élément |
| `.inserer(i, x)` | `.insert(i, x)` | Insère à l'indice i |
| `.etendre(lst)` | `.extend(lst)` | Étend avec une liste |
| `.retirer(x)` | `.remove(x)` | Retire la première occurrence |
| `.extraire(i)` | `.pop(i)` | Extrait l'élément i |
| `.vider()` | `.clear()` | Vide la liste |
| `.trier()` | `.sort()` | Trie sur place |
| `.inverser()` | `.reverse()` | Inverse sur place |
| `.copier()` | `.copy()` | Copie superficielle |
| `.compter(x)` | `.count(x)` | Compte les occurrences |
| `.indice(x)` | `.index(x)` | Trouve l'indice |

### Méthodes de dictionnaires

| Frython | Python | Description |
|---------|--------|-------------|
| `.cles()` | `.keys()` | Retourne les clés |
| `.valeurs()` | `.values()` | Retourne les valeurs |
| `.elements()` | `.items()` | Retourne les paires |
| `.obtenir(k, d)` | `.get(k, d)` | Obtient avec défaut |
| `.mettre_a_jour(d)` | `.update(d)` | Met à jour |
| `.extraire(k)` | `.pop(k)` | Extrait une clé |
| `.extraire_dernier()` | `.popitem()` | Extrait le dernier |
| `.vider()` | `.clear()` | Vide le dictionnaire |
| `.copier()` | `.copy()` | Copie |
| `.depuis_cles(keys)` | `.fromkeys(keys)` | Crée depuis des clés |
| `.obtenir_ou_creer(k, d)` | `.setdefault(k, d)` | Obtient ou crée |

### Méthodes d'ensembles

| Frython | Python | Description |
|---------|--------|-------------|
| `.ajouter(x)` | `.add(x)` | Ajoute un élément |
| `.retirer(x)` | `.remove(x)` | Retire (erreur si absent) |
| `.ecarter(x)` | `.discard(x)` | Retire sans erreur |
| `.vider()` | `.clear()` | Vide l'ensemble |
| `.copier()` | `.copy()` | Copie |
| `.union(s)` | `.union(s)` | Union |
| `.intersection(s)` | `.intersection(s)` | Intersection |
| `.difference(s)` | `.difference(s)` | Différence |
| `.est_sous_ensemble(s)` | `.issubset(s)` | Test sous-ensemble |
| `.est_sur_ensemble(s)` | `.issuperset(s)` | Test sur-ensemble |
| `.est_disjoint(s)` | `.isdisjoint(s)` | Test disjonction |
| `.difference_symetrique(s)` | `.symmetric_difference(s)` | Différence symétrique |

---

## 8. Modules traduits

```python
# Mathématiques
importer mathématiques
mathématiques.sqrt(16)  # → math.sqrt(16)

# Aléatoire
importer aleatoire
aleatoire.randint(1, 10)

# Système
importer systeme
systeme.argv

# OS
importer systeme_exploitation

# Temps
importer temps
temps.time()

# Datetime
importer date

# JSON
importer json

# Collections
importer collections

# Itertools
importer iterateurs

# Functools
importer fonctionnel

# Pathlib
importer chemin_fichier

# Threading
importer fil

# Multiprocessing
importer multiprocessus

# Subprocess
importer sous_processus

# SQLite
importer base_donnees

# CSV
importer csv

# Statistics
importer statistiques

# Logging
importer journalisation

# Argparse
importer arguments

# Typing
importer types_donnees

# Dataclasses
importer dataclasse

# Enum
importer enum

# UUID
importer uuid

# Secrets
importer secret

# Hashlib
importer hachage

# Base64
importer encodage

# Requests (externe)
importer web

# NumPy (externe)
importer calcul

# Pandas (externe)
importer donnees

# Matplotlib (externe)
importer graphiques

# PIL (externe)
importer images

# Tkinter
importer interface

# Asyncio
importer async_io
```

---

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
