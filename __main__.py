"""
Frython - Point d'entrée en ligne de commande
"""

import sys
import os
import argparse

def main():
    analyseur = argparse.ArgumentParser(
        prog='frython',
        description='🐓 Frython — Python en français, sacré bleu !',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  frython                         Lance la REPL interactive
  frython programme.fy            Exécute un fichier Frython
  frython -t programme.fy         Affiche le code Python transpilé
  frython -v programme.fy         Mode verbeux (affiche le code Python)
  frython -c "afficher('Bonjour')"  Exécute une commande directe
  frython --version               Affiche la version

Syntaxe Frython (exemples):
  afficher("Bonjour le monde!")
  si x > 0:
      afficher("positif")
  sinon:
      afficher("négatif")
        """
    )

    analyseur.add_argument(
        'fichier',
        nargs='?',
        help='Fichier Frython à exécuter (.fy)'
    )
    analyseur.add_argument(
        '-t', '--transpiler',
        action='store_true',
        help='Afficher le code Python généré sans exécuter'
    )
    analyseur.add_argument(
        '-v', '--verbeux',
        action='store_true',
        help='Mode verbeux: afficher le code Python avant exécution'
    )
    analyseur.add_argument(
        '-c', '--commande',
        metavar='CODE',
        help='Exécuter une commande Frython directement'
    )
    analyseur.add_argument(
        '--version',
        action='version',
        version='Frython 1.0.0 — Python en français 🐓'
    )
    analyseur.add_argument(
        '--mots-cles',
        action='store_true',
        help='Afficher tous les mots-clés Frython'
    )

    args = analyseur.parse_args()

    # Ajouter le dossier courant au chemin Python
    sys.path.insert(0, os.getcwd())

    from frython.interpreteur import InterpreteurFrython
    from frython.transpileur import transpiler

    # Afficher les mots-clés
    if args.mots_cles:
        interp = InterpreteurFrython()
        interp._afficher_mots_cles()
        return

    # Mode transpilation seule
    if args.transpiler and args.fichier:
        try:
            with open(args.fichier, 'r', encoding='utf-8') as f:
                source = f.read()
            code_python = transpiler(source)
            print("# Code Python généré par Frython")
            print("# Source:", args.fichier)
            print()
            print(code_python)
        except FileNotFoundError:
            print(f"❌ Fichier '{args.fichier}' introuvable.", file=sys.stderr)
            sys.exit(1)
        return

    interp = InterpreteurFrython(verbeux=args.verbeux)

    # Exécuter une commande directe
    if args.commande:
        code_sortie = interp.executer_source(args.commande, nom_fichier='<commande>')
        sys.exit(code_sortie)

    # Exécuter un fichier
    if args.fichier:
        if not args.fichier.endswith('.fy'):
            print(f"⚠️  Attention: '{args.fichier}' n'a pas l'extension .fy", file=sys.stderr)
        code_sortie = interp.executer_fichier(args.fichier)
        sys.exit(code_sortie)

    # REPL interactive
    interp.repl()


if __name__ == '__main__':
    main()
