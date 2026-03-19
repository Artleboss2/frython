"""
Frython - Transpileur
Convertit le code source Frython en Python valide.
"""

import re

# Table de correspondance Frython → Python (mots-clés)
MOTS_CLES_VERS_PYTHON = {
    # Structures de contrôle
    'si': 'if',
    'sinon': 'else',
    'sinonsi': 'elif',
    'tantque': 'while',
    'pour': 'for',
    'dans': 'in',
    'pasdans': 'not in',
    'casser': 'break',
    'continuer': 'continue',
    'passer': 'pass',

    # Fonctions et classes
    'déf': 'def',
    'retourner': 'return',
    'classe': 'class',
    'soi': 'self',
    'rendement': 'yield',
    'asynchrone': 'async',
    'attendre': 'await',

    # Valeurs spéciales
    'Vrai': 'True',
    'Faux': 'False',
    'Rien': 'None',

    # Opérateurs logiques
    'et': 'and',
    'ou': 'or',
    'non': 'not',
    'est': 'is',

    # Import
    'importer': 'import',
    'de': 'from',
    'comme': 'as',

    # Exceptions
    'essayer': 'try',
    'sauf': 'except',
    'enfin': 'finally',
    'lever': 'raise',

    # Divers
    'avec': 'with',
    'affirmer': 'assert',
    'global': 'global',
    'nonlocal': 'nonlocal',
    'supprimer': 'del',
    'lambda': 'lambda',

    # Fonctions intégrées
    'afficher': 'print',
    'saisir': 'input',
    'longueur': 'len',
    'intervalle': 'range',
    'liste': 'list',
    'dictionnaire': 'dict',
    'ensemble': 'set',
    'tuple': 'tuple',
    'entier': 'int',
    'decimal': 'float',
    'chaine': 'str',
    'booleen': 'bool',
    'enumerer': 'enumerate',
    'zipper': 'zip',
    'mapper': 'map',
    'filtrer': 'filter',
    'trier': 'sorted',
    'inverser': 'reversed',
    'somme': 'sum',
    'maximum': 'max',
    'minimum': 'min',
    'absolu': 'abs',
    'arrondir': 'round',
    'aide': 'help',
    'type': 'type',
    'super': 'super',
}

# Méthodes de chaînes
METHODES_CHAINE = {
    'majuscule': 'upper',
    'minuscule': 'lower',
    'capitaliser': 'capitalize',
    'titrer': 'title',
    'remplacer': 'replace',
    'diviser': 'split',
    'joindre': 'join',
    'supprimer_espaces': 'strip',
    'supprimer_espaces_gauche': 'lstrip',
    'supprimer_espaces_droite': 'rstrip',
    'commencer_par': 'startswith',
    'finir_par': 'endswith',
    'trouver': 'find',
    'contient': '__contains__',
    'formater': 'format',
    'encoder': 'encode',
    'decoder': 'decode',
    'est_alpha': 'isalpha',
    'est_digit': 'isdigit',
    'est_alphanum': 'isalnum',
    'est_espace': 'isspace',
    'est_majuscule': 'isupper',
    'est_minuscule': 'islower',
    'compter': 'count',
    'indice': 'index',
}

# Méthodes de listes
METHODES_LISTE = {
    'ajouter': 'append',
    'inserer': 'insert',
    'etendre': 'extend',
    'retirer': 'remove',
    'extraire': 'pop',
    'vider': 'clear',
    'copier': 'copy',
    'trier': 'sort',
    'inverser': 'reverse',
    'compter': 'count',
    'indice': 'index',
}

# Méthodes de dictionnaires
METHODES_DICT = {
    'cles': 'keys',
    'valeurs': 'values',
    'elements': 'items',
    'obtenir': 'get',
    'mettre_a_jour': 'update',
    'extraire': 'pop',
    'vider': 'clear',
    'copier': 'copy',
    'contient_cle': '__contains__',
}

# Méthodes d'ensembles
METHODES_ENSEMBLE = {
    'ajouter': 'add',
    'retirer': 'remove',
    'ecarter': 'discard',
    'union': 'union',
    'intersection': 'intersection',
    'difference': 'difference',
    'vider': 'clear',
    'copier': 'copy',
}

# Modules traduits → modules Python
MODULES_TRADUITS = {
    'mathématiques': 'math',
    'aleatoire': 'random',
    'systeme': 'sys',
    'systeme_exploitation': 'os',
    'temps': 'time',
    'datetime': 'datetime',
    'json': 'json',
    're': 're',
    'collections': 'collections',
    'itertools': 'itertools',
    'functools': 'functools',
    'pathlib': 'pathlib',
    'io': 'io',
    'copie': 'copy',
    'decimal_module': 'decimal',
    'fractions': 'fractions',
    'statistiques': 'statistics',
    'hashlib': 'hashlib',
    'base64': 'base64',
    'urllib': 'urllib',
    'http': 'http',
    'socket': 'socket',
    'threading': 'threading',
    'multiprocessing': 'multiprocessing',
    'subprocess': 'subprocess',
    'unittest': 'unittest',
    'logging': 'logging',
    'argparse': 'argparse',
    'configparser': 'configparser',
    'sqlite3': 'sqlite3',
}

# Table de correspondance Python → Frython (pour l'affichage des erreurs)
PYTHON_VERS_MOTS_CLES = {v: k for k, v in MOTS_CLES_VERS_PYTHON.items()}


class Transpileur:
    """Convertit le code Frython en code Python valide."""

    def __init__(self, source: str):
        self.source = source
        self.lignes = source.splitlines(keepends=True)

    def transpiler(self) -> str:
        """Transpile le code Frython complet en Python."""
        resultat = []
        for ligne in self.lignes:
            resultat.append(self._transpiler_ligne(ligne))
        code_python = ''.join(resultat)
        return code_python

    def _transpiler_ligne(self, ligne: str) -> str:
        """Transpile une ligne de code Frython en Python."""
        # Préserver l'indentation
        stripped = ligne.lstrip()
        indentation = ligne[:len(ligne) - len(stripped)]

        # Ligne vide ou commentaire
        if not stripped or stripped.startswith('#'):
            return ligne

        # Retirer le '\n' en fin si présent
        fin = '\n' if stripped.endswith('\n') else ''
        stripped = stripped.rstrip('\n')

        # Transpiler le contenu
        contenu = self._remplacer_tokens(stripped)

        return indentation + contenu + fin

    def _remplacer_tokens(self, code: str) -> str:
        """Remplace les tokens Frython par leurs équivalents Python."""
        # Traiter les chaînes de caractères séparément pour ne pas les modifier
        parties = self._separer_chaines(code)
        resultat = []

        for est_chaine, partie in parties:
            if est_chaine:
                resultat.append(partie)
            else:
                resultat.append(self._remplacer_mots_cles(partie))

        return ''.join(resultat)

    def _separer_chaines(self, code: str):
        """Sépare le code en parties chaînes et non-chaînes.
        Pour les f-strings, traduit les expressions dans {}.
        """
        parties = []
        i = 0
        n = len(code)

        while i < n:
            char = code[i]
            if char in ('"', "'"):
                # Détecter si c'est une f-string (précédé de f ou F)
                est_fstring = (i > 0 and code[i-1].lower() == 'f') or \
                              (i > 1 and code[i-2].lower() == 'f' and code[i-1] in 'rRbB')

                # Vérifier triple guillemet
                if code[i:i+3] in ('"""', "'''"):
                    delim = code[i:i+3]
                    fin = code.find(delim, i + 3)
                    if fin == -1:
                        contenu = code[i:]
                        i = n
                    else:
                        contenu = code[i:fin+3]
                        i = fin + 3
                else:
                    delim = char
                    j = i + 1
                    while j < n and code[j] != delim:
                        if code[j] == '\\':
                            j += 1
                        j += 1
                    contenu = code[i:j+1]
                    i = j + 1

                if est_fstring:
                    # Traduire les expressions {expr} dans la f-string
                    contenu = self._traduire_fstring(contenu)

                parties.append((True, contenu))
            else:
                # Trouver la prochaine chaîne
                j = i
                while j < n and code[j] not in ('"', "'"):
                    j += 1
                if j > i:
                    parties.append((False, code[i:j]))
                i = j

        return parties

    def _traduire_fstring(self, fstring: str) -> str:
        """Traduit les expressions Frython dans une f-string."""
        resultat = []
        i = 0
        n = len(fstring)
        while i < n:
            if fstring[i] == '{' and i + 1 < n and fstring[i+1] != '{':
                # Trouver la fermeture
                j = i + 1
                profondeur = 1
                while j < n and profondeur > 0:
                    if fstring[j] == '{':
                        profondeur += 1
                    elif fstring[j] == '}':
                        profondeur -= 1
                    j += 1
                expr = fstring[i+1:j-1]
                expr_traduit = self._remplacer_mots_cles(expr)
                resultat.append('{' + expr_traduit + '}')
                i = j
            else:
                resultat.append(fstring[i])
                i += 1
        return ''.join(resultat)

    def _remplacer_mots_cles(self, code: str) -> str:
        """Remplace les mots-clés Frython par Python en respectant les frontières de mots."""
        # Remplacer d'abord les méthodes (avec le point)
        # IMPORTANT: l'ordre compte — METHODES_LISTE avant METHODES_ENSEMBLE
        # pour que .ajouter → .append (liste) et non .add (ensemble)
        methodes_fusionnees = {}
        # Ensemble d'abord (priorité basse)
        methodes_fusionnees.update(METHODES_ENSEMBLE)
        # Puis dict, chaine, liste (priorité haute — écrasent ensemble)
        methodes_fusionnees.update(METHODES_DICT)
        methodes_fusionnees.update(METHODES_CHAINE)
        methodes_fusionnees.update(METHODES_LISTE)

        for fr, py in methodes_fusionnees.items():
            code = re.sub(r'\.' + re.escape(fr) + r'\b', '.' + py, code)

        # Remplacer les modules traduits
        for fr, py in MODULES_TRADUITS.items():
            code = re.sub(r'\b' + re.escape(fr) + r'\b', py, code)

        # Remplacer les mots-clés (ordre important: plus longs en premier)
        for fr, py in sorted(MOTS_CLES_VERS_PYTHON.items(), key=lambda x: -len(x[0])):
            code = re.sub(r'\b' + re.escape(fr) + r'\b', py, code)

        return code


def transpiler(source: str) -> str:
    """Fonction utilitaire pour transpiler du code Frython."""
    t = Transpileur(source)
    return t.transpiler()
