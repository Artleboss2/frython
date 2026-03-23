<div align="center">

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
[![Version](https://img.shields.io/badge/Version-1.1.2-orange?style=for-the-badge)](https://github.com/Artleboss2/frython/releases)
[![Tests](https://img.shields.io/badge/Tests-✅%20Passés-brightgreen?style=for-the-badge)](tests/)
[![PyPI](https://img.shields.io/badge/PyPI-frython-blue?style=for-the-badge&logo=pypi)](https://pypi.org/project/frython)

[![Fait avec amour](https://img.shields.io/badge/Fait_avec-❤️_et_beaucoup_de_baguettes-ff69b4?style=flat-square)](https://github.com/Artleboss2/frython)
[![Niveau de sérieux](https://img.shields.io/badge/Niveau_de_sérieux-Absolument_pas-yellow?style=flat-square)](https://github.com/Artleboss2/frython)
[![Compatible](https://img.shields.io/badge/Compatible-Python_100%25-blue?style=flat-square&logo=python)](https://python.org)

---

### 🌍 Languages / Langues

[🇫🇷 Français](assets/readme_fr.md) • [🇪🇸 Español](assets/readme_es.md) • [🇨🇳 中文](assets/readme_zh.md) • [🇮🇳 हिन्दी](assets/readme_hi.md) • [🇸🇦 العربية](assets/readme_ar.md) • [🇧🇷 Português](assets/readme_pt.md) • [🇷🇺 Русский](assets/readme_ru.md) • [🇯🇵 日本語](assets/readme_ja.md) • [🇩🇪 Deutsch](assets/readme_de.md) • [🇰🇷 한국어](assets/readme_ko.md)

</div>

---

## 🥐 What is it?

**Frython** is a programming language that transpiles Python code written **entirely in French** into standard Python. It's a humorous project, but **fully functional** — you can really program in French!

Frython translates Python keywords (`if`, `while`, `for`, `print`, etc.) into their French equivalents (`si`, `tantque`, `pour`, `afficher`, etc.).

> *"Why program in English when you can do it in French with 3 times more words?" — Victor Hugo, probably*

---

## ⚡ Installation

```bash
pip install frython
```

### From source

```bash
git clone https://github.com/Artleboss2/frython.git
cd frython
pip install .
```

### Verify installation

```bash
python -m frython --version
# Frython 1.0.2 — Python en français 🐓
```

### Windows (multiple Python versions)

```bash
C:\Python314\python.exe -m frython mon_fichier.fy
```

Or create a permanent PowerShell alias:
```powershell
function frython { C:\Python314\python.exe -m frython $args }
```

---

## 🚀 Quick Start

Create a file `bonjour.fy`:

```python
afficher("Bonjour le monde! 🐓")

prenom = "Marie"
age = 25

si age >= 18:
    afficher(f"Bienvenue, {prenom}! Vous êtes majeur(e).")
sinon:
    afficher(f"Bonjour, {prenom}! Vous êtes mineur(e).")
```

Run it:

```bash
python -m frython bonjour.fy
```

```
Bonjour le monde! 🐓
Bienvenue, Marie! Vous êtes majeur(e).
```

### Interactive REPL

```bash
python -m frython
```

```
🐓 Frython v1.0.2 — Python en français, sacré bleu !

🐓 >>> afficher("Ça marche!")
Ça marche!
🐓 >>> quitter()
Au revoir! 👋
```

---

## 📖 Language Reference

### Control Flow

| Frython | Python | Description |
|---------|--------|-------------|
| `si` | `if` | Condition |
| `sinon` | `else` | Else |
| `sinonsi` | `elif` | Else if |
| `tantque` | `while` | While loop |
| `pour` | `for` | For loop |
| `dans` | `in` | In operator |
| `casser` | `break` | Break |
| `continuer` | `continue` | Continue |
| `passer` | `pass` | Pass |

### Definitions

| Frython | Python | Description |
|---------|--------|-------------|
| `déf` | `def` | Define function |
| `retourner` | `return` | Return value |
| `classe` | `class` | Define class |
| `soi` | `self` | Current instance |
| `lambda` | `lambda` | Anonymous function |

### Special Values

| Frython | Python |
|---------|--------|
| `Vrai` | `True` |
| `Faux` | `False` |
| `Rien` | `None` |

### Built-in Functions

| Frython | Python |
|---------|--------|
| `afficher()` | `print()` |
| `saisir()` | `input()` |
| `longueur()` | `len()` |
| `intervalle()` | `range()` |
| `trier()` | `sorted()` |
| `somme()` | `sum()` |
| `maximum()` | `max()` |
| `minimum()` | `min()` |

---

## 🛠️ CLI Usage

```bash
python -m frython fichier.fy          # Run a file
python -m frython                      # Interactive REPL
python -m frython -t fichier.fy        # Show transpiled Python
python -m frython -v fichier.fy        # Verbose mode
python -m frython -c "afficher('Hi')"  # Run direct code
python -m frython --mots-cles          # List all keywords
python -m frython --version            # Show version
```

---

## 💡 Examples

### Fibonacci

```python
déf fibonacci(n):
    si n <= 1:
        retourner n
    retourner fibonacci(n-1) + fibonacci(n-2)

pour i dans intervalle(10):
    afficher(f"F({i}) = {fibonacci(i)}")
```

### Classes

```python
classe Animal:
    def __init__(soi, nom):
        soi.nom = nom

    déf parler(soi):
        retourner "..."

classe Chien(Animal):
    déf parler(soi):
        retourner "Ouaf! 🐕"

rex = Chien("Rex")
afficher(rex.parler())
```

### List Comprehensions

```python
carres = [x**2 pour x dans intervalle(1, 11)]
pairs = [x pour x dans intervalle(20) si x % 2 == 0]
afficher(carres)
afficher(pairs)
```

---

## 🗂️ Project Structure

```
frython/
├── frython/
│   ├── __init__.py
│   ├── lexeur.py
│   ├── transpileur.py
│   └── interpreteur.py
├── examples/
├── tests/
├── assets/
│   ├── readme_fr.md
│   ├── readme_es.md
│   ├── readme_zh.md
│   ├── readme_hi.md
│   ├── readme_ar.md
│   ├── readme_pt.md
│   ├── readme_ru.md
│   ├── readme_ja.md
│   ├── readme_de.md
│   └── readme_ko.md
├── README.md
├── DOCUMENTATION.md
├── UPDATE.md
└── LICENSE
```

---

## ❓ FAQ

**Q: Is it actually usable?**
A: Yes! Frython transpiles to valid Python. Everything Python can do, Frython can do — in French.

**Q: Can I use external Python libraries?**
A: Absolutely. `importer numpy comme np` works perfectly.

**Q: Do f-strings work?**
A: Yes, and expressions inside `{}` are also translated.

**Q: Why does this exist?**
A: *Pourquoi pas?* 🥐

**Q: Will my boss accept Frython in production?**
A: We cannot guarantee the health of your employment.

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Run tests: `python -m unittest tests/test_frython.py -v`
4. Commit and push
5. Open a Pull Request

---

## 📜 License

[MIT](LICENSE) — Free to use, modify and distribute. Even for pranking colleagues.

---

<div align="center">

*Made with ❤️, coffee ☕ and lots of baguettes 🥖*

**⭐ If this project made you smile, give it a star! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/Artleboss2/frython?style=social)](https://github.com/Artleboss2/frython/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Artleboss2/frython?style=social)](https://github.com/Artleboss2/frython/network)

</div>
