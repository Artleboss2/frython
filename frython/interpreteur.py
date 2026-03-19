"""
Frython - Interpréteur principal
Exécute les fichiers .fy et fournit une REPL interactive.
"""

import sys
import os
import traceback
import code
try:
    import readline  # Pour l'historique de la REPL (Linux/Mac)
except ImportError:
    pass  # Non disponible sur Windows, pas grave

from .transpileur import transpiler, PYTHON_VERS_MOTS_CLES


BANNIERE = r"""
 _____ _____     _   _
|  ___| ____|   | | | |
| |_  |  _| | | | |_| |_ | |__   ___  _ __
|  _| | |___ | | |  _  | | '_ \ / _ \| '_ \
| |   |_____|| |_| | | | | | | | (_) | | | |
|_|         \__, |_| |_|_|_| |_|\___/|_| |_|
             |___/

🐓 Frython v1.0.0 — Python en français, sacré bleu !
   Tapez 'aide()' pour de l'aide, 'quitter()' pour sortir.
   Tapez 'mots_cles()' pour voir les mots-clés Frython.
"""


def traduire_erreur(message: str) -> str:
    """Traduit les messages d'erreur Python en français."""
    traductions = {
        'SyntaxError': 'ErreurSyntaxe',
        'NameError': 'ErreurNom',
        'TypeError': 'ErreurType',
        'ValueError': 'ErreurValeur',
        'IndexError': 'ErreurIndice',
        'KeyError': 'ErreurCle',
        'AttributeError': 'ErreurAttribut',
        'ImportError': 'ErreurImport',
        'FileNotFoundError': 'ErreurFichierIntrouvable',
        'ZeroDivisionError': 'ErreurDivisionParZero',
        'RecursionError': 'ErreurRecursion',
        'MemoryError': 'ErreurMemoire',
        'OverflowError': 'ErreurDepassement',
        'RuntimeError': 'ErreurExecution',
        'StopIteration': 'ArreterIteration',
        'not defined': "n'est pas défini(e)",
        'is not defined': "n'est pas défini(e)",
        "name '": "nom '",
        'is not': "n'est pas",
        'unsupported operand': 'opérande non supporté',
        'cannot': 'ne peut pas',
        'expected': 'attendu',
        'invalid syntax': 'syntaxe invalide',
        'division by zero': 'division par zéro',
        'list index out of range': 'indice de liste hors limites',
        'string index out of range': 'indice de chaîne hors limites',
        'object has no attribute': "l'objet n'a pas l'attribut",
        'No module named': 'Module introuvable',
        'argument': 'argument',
        'positional arguments': 'arguments positionnels',
        'missing': 'manquant',
        'required': 'requis',
        'takes': 'prend',
        'but': 'mais',
        'given': 'donné(s)',
    }
    for en, fr in traductions.items():
        message = message.replace(en, fr)

    # Traduire les noms Python vers Frython dans les messages
    for py, fr in PYTHON_VERS_MOTS_CLES.items():
        message = message.replace(f"'{py}'", f"'{fr}'")

    return message


class InterpreteurFrython:
    """Interpréteur principal de Frython."""

    def __init__(self, verbeux: bool = False):
        self.verbeux = verbeux
        self.env_global = {
            '__name__': '__frython__',
            '__doc__': 'Espace de noms Frython',
            # Fonctions utilitaires Frython
            'quitter': self._quitter,
            'mots_cles': self._afficher_mots_cles,
        }
        self._injecter_builtins()

    def _injecter_builtins(self):
        """Injecte les builtins Python dans l'environnement Frython."""
        import builtins
        self.env_global['__builtins__'] = builtins

    def _quitter(self, code=0):
        """Quitte Frython."""
        print("Au revoir! 👋")
        sys.exit(code)

    def _afficher_mots_cles(self):
        """Affiche la liste des mots-clés Frython."""
        from .transpileur import MOTS_CLES_VERS_PYTHON
        print("\n📚 Mots-clés Frython → Python:\n")
        categories = {
            'Contrôle de flux': ['si', 'sinon', 'sinonsi', 'tantque', 'pour', 'dans', 'casser', 'continuer', 'passer'],
            'Fonctions': ['déf', 'retourner', 'lambda', 'rendement'],
            'Classes': ['classe', 'soi', 'super'],
            'Valeurs': ['Vrai', 'Faux', 'Rien'],
            'Logique': ['et', 'ou', 'non', 'est'],
            'Import': ['importer', 'de', 'comme'],
            'Exceptions': ['essayer', 'sauf', 'enfin', 'lever'],
            'Fonctions intégrées': ['afficher', 'saisir', 'longueur', 'intervalle', 'liste',
                                     'dictionnaire', 'ensemble', 'entier', 'decimal', 'chaine',
                                     'booleen', 'enumerer', 'zipper', 'trier', 'somme',
                                     'maximum', 'minimum', 'absolu', 'arrondir', 'type'],
        }
        for categorie, mots in categories.items():
            print(f"  {categorie}:")
            for mot in mots:
                py = MOTS_CLES_VERS_PYTHON.get(mot, mot)
                print(f"    {mot:<25} → {py}")
            print()

    def executer_fichier(self, chemin: str) -> int:
        """Exécute un fichier .fy"""
        try:
            with open(chemin, 'r', encoding='utf-8') as f:
                source = f.read()
        except FileNotFoundError:
            print(f"❌ Erreur: Fichier '{chemin}' introuvable.", file=sys.stderr)
            return 1
        except PermissionError:
            print(f"❌ Erreur: Permission refusée pour '{chemin}'.", file=sys.stderr)
            return 1

        return self.executer_source(source, nom_fichier=chemin)

    def executer_source(self, source: str, nom_fichier: str = '<frython>') -> int:
        """Exécute du code source Frython."""
        try:
            code_python = transpiler(source)
            if self.verbeux:
                print("--- Code Python généré ---")
                print(code_python)
                print("--------------------------")
            exec(compile(code_python, nom_fichier, 'exec'), self.env_global)
            return 0
        except SyntaxError as e:
            msg = traduire_erreur(str(e))
            print(f"❌ ErreurSyntaxe dans '{nom_fichier}': {msg}", file=sys.stderr)
            if e.lineno:
                print(f"   Ligne {e.lineno}: {e.text}", file=sys.stderr)
            return 1
        except SystemExit as e:
            return e.code if e.code else 0
        except Exception as e:
            type_erreur = type(e).__name__
            type_fr = traduire_erreur(type_erreur)
            msg = traduire_erreur(str(e))
            print(f"❌ {type_fr}: {msg}", file=sys.stderr)
            if self.verbeux:
                traceback.print_exc()
            return 1

    def repl(self):
        """Lance la REPL interactive Frython."""
        print(BANNIERE)

        env_repl = dict(self.env_global)
        buffer = []

        while True:
            try:
                if buffer:
                    prompt = "...  "
                else:
                    prompt = "🐓 >>> "

                ligne = input(prompt)

                # Commandes spéciales
                if ligne.strip() in ('quitter()', 'exit()', 'quit()'):
                    print("Au revoir! 👋")
                    break

                buffer.append(ligne)

                # Vérifier si le bloc est complet
                source_complete = '\n'.join(buffer)

                # Si la ligne est vide et on est dans un bloc, exécuter
                if ligne == '' and len(buffer) > 1:
                    self._executer_repl(source_complete, env_repl)
                    buffer = []
                    continue

                # Si la ligne ne termine pas avec ':', essayer d'exécuter
                if not ligne.rstrip().endswith(':') and not ligne.startswith(' ') and len(buffer) == 1:
                    succes = self._executer_repl(source_complete, env_repl)
                    buffer = []
                elif ligne == '' and buffer:
                    self._executer_repl(source_complete, env_repl)
                    buffer = []

            except KeyboardInterrupt:
                print("\n[Interrompez avec Ctrl+D ou tapez 'quitter()']")
                buffer = []
            except EOFError:
                print("\nAu revoir! 👋")
                break

    def _executer_repl(self, source: str, env: dict) -> bool:
        """Exécute une ligne/bloc dans la REPL."""
        if not source.strip():
            return True
        try:
            code_python = transpiler(source)
            # Essayer eval d'abord pour les expressions
            try:
                code_compile = compile(code_python.strip(), '<repl>', 'eval')
                resultat = eval(code_compile, env)
                if resultat is not None:
                    print(repr(resultat))
                return True
            except SyntaxError:
                pass
            # Sinon exec
            exec(compile(code_python, '<repl>', 'exec'), env)
            return True
        except SyntaxError as e:
            msg = traduire_erreur(str(e))
            print(f"❌ ErreurSyntaxe: {msg}")
        except SystemExit:
            raise
        except Exception as e:
            type_fr = traduire_erreur(type(e).__name__)
            msg = traduire_erreur(str(e))
            print(f"❌ {type_fr}: {msg}")
        return False