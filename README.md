<div align='center'>

```
  ______          _   _                 
 |  ____|        | | | |                
 | |__ _ __ _   _| |_| |__   ___  _ __  
 |  __| '__| | | | __| '_ \ / _ \| '_ \ 
 | |  | |  | |_| | |_| | | | (_) | | | |
 |_|  |_|   \__, |\__|_| |_|\___/|_| |_|
             __/ |                      
            |___/                       
```

# 🐓 Frython

### *Python en français, sacré bleu !*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Licence MIT](https://img.shields.io/badge/Licence-MIT-green?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange?style=for-the-badge)](https://github.com/Artleboss2/frython/releases)
[![Tests](https://img.shields.io/badge/Tests-✅%20Passés-brightgreen?style=for-the-badge)](tests/)
[![Blague?](https://img.shields.io/badge/Blague-Oui%20mais%20quand%20même-red?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHRleHQgeT0iMjAiIGZvbnQtc2l6ZT0iMjAiPvCfkI88L3RleHQ+PC9zdmc+)](https://github.com/Artleboss2/frython)

[![Fait avec amour](https://img.shields.io/badge/Fait_avec-❤️_et_beaucoup_de_baguettes-ff69b4?style=flat-square)](https://github.com/Artleboss2/frython)
[![Niveau de sérieux](https://img.shields.io/badge/Niveau_de_sérieux-Absolument_pas-yellow?style=flat-square)](https://github.com/Artleboss2/frython)
[![Compatible](https://img.shields.io/badge/Compatible-Python_100%25-blue?style=flat-square&logo=python)](https://python.org)

</div>

---

## 🥐 Qu'est-ce que c'est ?

**Frython** est un langage de programmation qui transpile du code Python écrit **entièrement en français** vers du Python standard. C'est un projet humoristique, mais **entièrement fonctionnel** — vous pouvez vraiment programmer en français !

Frython traduit les mots-clés Python (`if`, `while`, `for`, `print`, etc.) en leurs équivalents français (`si`, `tantque`, `pour`, `afficher`, etc.).

> *"Pourquoi programmer en anglais quand on peut le faire en français avec 3 fois plus de mots ?" — Victor Hugo, probablement*

---

## ⚡ Installation

### Depuis PyPI *(bientôt disponible)*

```bash
pip install frython
```

### Depuis les sources

```bash
git clone https://github.com/Artleboss2/frython.git
cd frython
pip install -e .
```

### Vérifier l'installation

```bash
frython --version
# Frython 1.0.0 — Python en français 🐓
```

---

## 🚀 Démarrage rapide

### Votre premier programme Frython

Créez un fichier `bonjour.fy` :

```python
# bonjour.fy
afficher("Bonjour le monde! 🐓")

prenom = "Marie"
age = 25

si age >= 18:
    afficher(f"Bienvenue, {prenom}! Vous êtes majeur(e).")
sinon:
    afficher(f"Bonjour, {prenom}! Vous êtes mineur(e).")
```

Exécutez-le :

```bash
frython bonjour.fy
```

```
Bonjour le monde! 🐓
Bienvenue, Marie! Vous êtes majeur(e).
```

### REPL Interactive

```bash
frython
```

```
 _____ _____     _   _
...

🐓 Frython v1.0.0 — Python en français, sacré bleu !
   Tapez 'aide()' pour de l'aide, 'quitter()' pour sortir.

🐓 >>> afficher("Ça marche!")
Ça marche!
🐓 >>> x = 42
🐓 >>> x * 2
84
🐓 >>> quitter()
Au revoir! 👋
```

---

## 📖 Référence du langage

### Structures de contrôle

| Frython | Python | Description |
|---------|--------|-------------|
| `si` | `if` | Condition |
| `sinon` | `else` | Sinon |
| `sinonsi` | `elif` | Sinon si |
| `tantque` | `while` | Boucle tant que |
| `pour` | `for` | Boucle pour |
| `dans` | `in` | Opérateur dans |
| `casser` | `break` | Sortir d'une boucle |
| `continuer` | `continue` | Itération suivante |
| `passer` | `pass` | Ne rien faire |

### Définitions

| Frython | Python | Description |
|---------|--------|-------------|
| `déf` | `def` | Définir une fonction |
| `retourner` | `return` | Retourner une valeur |
| `classe` | `class` | Définir une classe |
| `soi` | `self` | Instance courante |
| `lambda` | `lambda` | Fonction anonyme |
| `rendement` | `yield` | Générateur |

### Valeurs spéciales

| Frython | Python | Description |
|---------|--------|-------------|
| `Vrai` | `True` | Vrai |
| `Faux` | `False` | Faux |
| `Rien` | `None` | Nul |

### Opérateurs logiques

| Frython | Python | Description |
|---------|--------|-------------|
| `et` | `and` | Et logique |
| `ou` | `or` | Ou logique |
| `non` | `not` | Négation |
| `est` | `is` | Identité |
| `pasdans` | `not in` | Non présent dans |

### Imports et modules

| Frython | Python | Description |
|---------|--------|-------------|
| `importer` | `import` | Importer un module |
| `de` | `from` | Importer depuis |
| `comme` | `as` | Alias |

```python
# Importation en Frython
importer mathématiques
de collections importer defaultdict comme dd_fr
```

### Gestion des exceptions

| Frython | Python | Description |
|---------|--------|-------------|
| `essayer` | `try` | Bloc essai |
| `sauf` | `except` | Attraper une exception |
| `enfin` | `finally` | Toujours exécuter |
| `lever` | `raise` | Lever une exception |
| `affirmer` | `assert` | Assertion |

### Fonctions intégrées

| Frython | Python | Description |
|---------|--------|-------------|
| `afficher()` | `print()` | Afficher du texte |
| `saisir()` | `input()` | Lire une entrée |
| `longueur()` | `len()` | Longueur |
| `intervalle()` | `range()` | Suite de nombres |
| `liste()` | `list()` | Convertir en liste |
| `dictionnaire()` | `dict()` | Créer un dictionnaire |
| `ensemble()` | `set()` | Créer un ensemble |
| `tuple()` | `tuple()` | Créer un tuple |
| `entier()` | `int()` | Convertir en entier |
| `decimal()` | `float()` | Convertir en décimal |
| `chaine()` | `str()` | Convertir en chaîne |
| `booleen()` | `bool()` | Convertir en booléen |
| `enumerer()` | `enumerate()` | Énumérer |
| `zipper()` | `zip()` | Zipper |
| `mapper()` | `map()` | Mapper |
| `filtrer()` | `filter()` | Filtrer |
| `trier()` | `sorted()` | Trier |
| `inverser()` | `reversed()` | Inverser |
| `somme()` | `sum()` | Sommer |
| `maximum()` | `max()` | Maximum |
| `minimum()` | `min()` | Minimum |
| `absolu()` | `abs()` | Valeur absolue |
| `arrondir()` | `round()` | Arrondir |
| `type()` | `type()` | Type d'un objet |
| `aide()` | `help()` | Aide |

### Méthodes de chaînes

| Frython | Python | Description |
|---------|--------|-------------|
| `.majuscule()` | `.upper()` | Majuscules |
| `.minuscule()` | `.lower()` | Minuscules |
| `.capitaliser()` | `.capitalize()` | Première lettre majuscule |
| `.titrer()` | `.title()` | Format titre |
| `.remplacer()` | `.replace()` | Remplacer |
| `.diviser()` | `.split()` | Diviser |
| `.joindre()` | `.join()` | Joindre |
| `.supprimer_espaces()` | `.strip()` | Supprimer espaces |
| `.commencer_par()` | `.startswith()` | Commence par |
| `.finir_par()` | `.endswith()` | Finit par |
| `.trouver()` | `.find()` | Trouver |
| `.formater()` | `.format()` | Formater |
| `.compter()` | `.count()` | Compter |

### Méthodes de listes

| Frython | Python | Description |
|---------|--------|-------------|
| `.ajouter()` | `.append()` | Ajouter un élément |
| `.inserer()` | `.insert()` | Insérer à un indice |
| `.etendre()` | `.extend()` | Étendre avec une liste |
| `.retirer()` | `.remove()` | Retirer un élément |
| `.extraire()` | `.pop()` | Extraire un élément |
| `.vider()` | `.clear()` | Vider la liste |
| `.trier()` | `.sort()` | Trier sur place |
| `.inverser()` | `.reverse()` | Inverser sur place |
| `.copier()` | `.copy()` | Copier |
| `.compter()` | `.count()` | Compter les occurrences |

### Méthodes de dictionnaires

| Frython | Python | Description |
|---------|--------|-------------|
| `.cles()` | `.keys()` | Clés |
| `.valeurs()` | `.values()` | Valeurs |
| `.elements()` | `.items()` | Paires clé-valeur |
| `.obtenir()` | `.get()` | Obtenir avec défaut |
| `.mettre_a_jour()` | `.update()` | Mettre à jour |
| `.extraire()` | `.pop()` | Extraire |
| `.vider()` | `.clear()` | Vider |

---

## 💡 Exemples

### Fibonacci

```python
# fibonacci.fy
déf fibonacci(n):
    """Calcule la suite de Fibonacci."""
    si n <= 0:
        retourner []
    sinonsi n == 1:
        retourner [0]
    
    suite = [0, 1]
    tantque longueur(suite) < n:
        suivant = suite[-1] + suite[-2]
        suite.ajouter(suivant)
    
    retourner suite

nombres = fibonacci(10)
afficher(nombres)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Programmation orientée objet

```python
# classes.fy
classe Animal:
    def __init__(soi, nom, age):
        soi.nom = nom
        soi.age = age
    
    déf parler(soi):
        retourner "..."

classe Chien(Animal):
    déf parler(soi):
        retourner "Ouaf! 🐕"
    
    déf chercher(soi, objet):
        afficher(f"{soi.nom} cherche {objet}... trouvé!")

rex = Chien("Rex", 3)
afficher(rex.parler())   # Ouaf! 🐕
rex.chercher("la balle") # Rex cherche la balle... trouvé!
```

### Compréhensions de liste

```python
# comprehensions.fy
nombres = liste(intervalle(1, 11))

carres = [x**2 pour x dans nombres]
pairs = [x pour x dans nombres si x % 2 == 0]
cube_pairs = [x**3 pour x dans nombres si x % 2 == 0]

afficher(f"Carrés: {carres}")
afficher(f"Pairs: {pairs}")
afficher(f"Cubes des pairs: {cube_pairs}")
```

### Gestion des exceptions

```python
# exceptions.fy
déf diviser_securement(a, b):
    essayer:
        resultat = a / b
        retourner resultat
    sauf ZeroDivisionError:
        afficher("Erreur: Division par zéro!")
        retourner Rien
    enfin:
        afficher("Opération terminée.")

afficher(diviser_securement(10, 2))  # 5.0
afficher(diviser_securement(10, 0))  # Erreur + Rien
```

### Fonctions d'ordre supérieur

```python
# ordre_superieur.fy
nombres = liste(intervalle(1, 11))

# mapper, filtrer, trier
carres = liste(mapper(lambda x: x**2, nombres))
pairs = liste(filtrer(lambda x: x % 2 == 0, nombres))
desc = trier(nombres, reverse=Vrai)

afficher(f"Carrés: {carres}")
afficher(f"Pairs: {pairs}")
afficher(f"Décroissant: {desc}")

# Réduction manuelle
total = somme(nombres)
afficher(f"Total: {total}")
```

---

## 🛠️ Utilisation en ligne de commande

```bash
# Lancer la REPL interactive
frython

# Exécuter un fichier .fy
frython mon_programme.fy

# Voir le code Python généré (transpilation)
frython -t mon_programme.fy

# Mode verbeux (affiche le code Python avant exécution)
frython -v mon_programme.fy

# Exécuter une commande directe
frython -c "afficher('Bonjour depuis la ligne de commande!')"

# Voir tous les mots-clés disponibles
frython --mots-cles

# Voir la version
frython --version
```

---

## 🐍 API Python

Vous pouvez utiliser Frython directement dans vos scripts Python :

```python
from frython import transpiler, InterpreteurFrython

# Transpiler du code Frython en Python
code_frython = """
déf saluer(nom):
    retourner f"Bonjour, {nom}!"

afficher(saluer("Monde"))
"""

code_python = transpiler(code_frython)
print(code_python)
# def saluer(nom):
#     return f"Bonjour, {nom}!"
# print(saluer("Monde"))

# Exécuter directement
interp = InterpreteurFrython()
interp.executer_source(code_frython)
# Bonjour, Monde!
```

---

## 🗂️ Structure du projet

```
frython/
├── frython/
│   ├── __init__.py        # Point d'entrée du paquet
│   ├── lexeur.py          # Lexeur/Tokenizer Frython
│   ├── transpileur.py     # Transpileur Frython → Python
│   └── interpreteur.py    # Interpréteur et REPL
├── exemples/
│   ├── bonjour_monde.fy   # Hello World en Frython
│   ├── fibonacci.fy       # Suite de Fibonacci
│   ├── classes.fy         # POO en Frython
│   └── vitrine.fy         # Démonstration complète
├── tests/
│   └── test_frython.py    # Tests unitaires
├── __main__.py            # CLI principale
├── setup.py               # Configuration du paquet
├── pyproject.toml         # Configuration moderne
├── LICENSE                # Licence MIT
├── .gitignore             # Fichiers ignorés par Git
└── README.md              # Ce fichier
```

---

## 🧪 Tests

```bash
# Lancer tous les tests
python -m pytest tests/ -v

# Ou avec unittest
python -m unittest tests/test_frython.py -v

# Avec couverture de code
pip install pytest-cov
pytest tests/ --cov=frython --cov-report=html
```

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment participer :

1. **Forkez** le dépôt
2. Créez une **branche** pour votre fonctionnalité (`git checkout -b feature/ma-feature`)
3. **Committez** vos changements (`git commit -m 'Ajouter ma super feature'`)
4. **Poussez** la branche (`git push origin feature/ma-feature`)
5. Ouvrez une **Pull Request**

### Idées de contributions

- 🆕 Ajouter des mots-clés manquants
- 🐛 Corriger des bugs de transpilation
- 📚 Améliorer la documentation
- 🧪 Ajouter des tests
- 💡 Créer des exemples de programmes
- 🌍 Supporter d'autres langues ? (*Pythonisch ? Pythönen ?*)

---

## ❓ FAQ

**Q: Est-ce vraiment utilisable ?**  
R: Oui ! Frython transpile vers Python valide. Tout ce que Python peut faire, Frython peut le faire — en français.

**Q: Puis-je utiliser des bibliothèques Python normales ?**  
R: Absolument. `importer numpy comme np` fonctionne parfaitement.

**Q: Et les f-strings ?**  
R: Les f-strings Python fonctionnent directement : `f"Bonjour {nom}!"`.

**Q: Les accents dans les noms de variables ?**  
R: Frython supporte les caractères accentués pour les mots-clés et les méthodes.

**Q: Pourquoi ?**  
R: *Pourquoi pas ?* 🥐

**Q: Mon patron va-t-il accepter du code Frython en production ?**  
R: Nous ne pouvons pas garantir la santé de votre emploi.

---

## 📊 Compatibilité

| Python | Frython | Statut |
|--------|---------|--------|
| 3.8 | 1.0.0 | ✅ |
| 3.9 | 1.0.0 | ✅ |
| 3.10 | 1.0.0 | ✅ |
| 3.11 | 1.0.0 | ✅ |
| 3.12 | 1.0.0 | ✅ |
| 2.7 | — | ❌ On est en 2025 |

---

## 📜 Licence

Ce projet est sous licence [MIT](LICENSE). Vous êtes libre de l'utiliser, le modifier et le distribuer, même pour faire des blagues à vos collègues.

---

## 🙏 Remerciements

- **Guido van Rossum** — Pour avoir créé Python, sans lequel Frython n'existerait pas.
- **La langue française** — Pour être tellement plus élégante que l'anglais (opinion non biaisée).
- **Les baguettes** — Pour le support moral.
- **Codecrafters** — Pour l'inspiration via [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x).

---

<div align="center">

*Fait avec ❤️, du café ☕ et beaucoup de baguettes 🥖 en France 🇫🇷*

**⭐ Si ce projet vous a fait sourire, donnez-lui une étoile ! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/Artleboss2/frython?style=social)](https://github.com/Artleboss2/frython/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Artleboss2/frython?style=social)](https://github.com/Artleboss2/frython/network)

</div>
