"""
Frython — Python en français 🇫🇷🐓
=====================================
Un langage de programmation basé sur Python avec une syntaxe entièrement en français.

Usage:
    frython mon_programme.fy       # Exécuter un fichier
    frython                        # Lancer la REPL interactive
    frython -t mon_programme.fy    # Voir le code Python généré (transpilation)
"""

__version__ = '1.1.1'
__auteur__ = 'La Communauté Frython'
__licence__ = 'MIT'
__description__ = 'Python en français, sacré bleu ! 🐓'

from .transpileur import transpiler
from .interpreteur import InterpreteurFrython

__all__ = ['transpiler', 'InterpreteurFrython']
