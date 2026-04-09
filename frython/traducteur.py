import re

PYTHON_VERS_FRYTHON = {v: k for k, v in {
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
    'déf': 'def',
    'retourner': 'return',
    'classe': 'class',
    'soi': 'self',
    'rendement': 'yield',
    'asynchrone': 'async',
    'attendre': 'await',
    'Vrai': 'True',
    'Faux': 'False',
    'Rien': 'None',
    'et': 'and',
    'ou': 'or',
    'non': 'not',
    'est': 'is',
    'importer': 'import',
    'de': 'from',
    'comme': 'as',
    'essayer': 'try',
    'sauf': 'except',
    'enfin': 'finally',
    'lever': 'raise',
    'avec': 'with',
    'affirmer': 'assert',
    'global': 'global',
    'nonlocal': 'nonlocal',
    'supprimer': 'del',
    'lambda': 'lambda',
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
    'ouvrir': 'open',
    'identifiant': 'id',
    'repr': 'repr',
    'appeler': 'callable',
    'executer': 'exec',
    'evaluer': 'eval',
    'octets': 'bytes',
    'objet': 'object',
    'propriete': 'property',
    'statique': 'staticmethod',
    'classique': 'classmethod',
    'ErreurValeur': 'ValueError',
    'ErreurType': 'TypeError',
    'ErreurNom': 'NameError',
    'ErreurIndex': 'IndexError',
    'ErreurCle': 'KeyError',
    'ErreurAttribut': 'AttributeError',
    'ErreurImport': 'ImportError',
    'ErreurMemoire': 'MemoryError',
    'ErreurRecursion': 'RecursionError',
    'ErreurSyntaxe': 'SyntaxError',
    'ErreurDivisionZero': 'ZeroDivisionError',
    'ErreurFichier': 'FileNotFoundError',
    'ErreurPermission': 'PermissionError',
    'ErreurArret': 'StopIteration',
    'entree_standard': 'stdin',
    'sortie_standard': 'stdout',
    'tous': 'all',
    'aucun': 'any',
    'instance_de': 'isinstance',
    'sous_classe': 'issubclass',
    'puissance': 'pow',
    'hex': 'hex',
    'octal': 'oct',
    'binaire': 'bin',
    'caractere': 'chr',
    'ordinal': 'ord',
    'globals': 'globals',
    'locals': 'locals',
    'prochain': 'next',
    'hash': 'hash',
    'breakpoint': 'breakpoint',
    'NotImplemented': 'NotImplemented',
    'Ellipsis': 'Ellipsis',
    'ErreurOS': 'OSError',
    'ErreurES': 'IOError',
    'ErreurConnexion': 'ConnectionError',
    'ErreurDebordement': 'OverflowError',
    'ErreurUnicode': 'UnicodeError',
    'ErreurIndentation': 'IndentationError',
    'ErreurTabulation': 'TabError',
    'ErreurSysteme': 'SystemError',
    'ErreurRuntime': 'RuntimeError',
    'ErreurNotImplemented': 'NotImplementedError',
    'ErreurTimeout': 'TimeoutError',
    'ErreurInterruption': 'KeyboardInterrupt',
    'ErreurAssertion': 'AssertionError',
    'Avertissement': 'Warning',
    'AvertissementDepreciation': 'DeprecationWarning',
    'AvertissementRuntime': 'RuntimeWarning',
    'AvertissementSyntaxe': 'SyntaxWarning',
    'AvertissementUtilisateur': 'UserWarning',
    'AvertissementFutur': 'FutureWarning',
}.items()}

METHODES_CHAINE_INVERSEES = {v: k for k, v in {
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
    'est_numerique': 'isnumeric',
    'est_decimal': 'isdecimal',
    'est_titre': 'istitle',
    'centrer': 'center',
    'aligner_gauche': 'ljust',
    'aligner_droite': 'rjust',
    'remplir_zeros': 'zfill',
    'partitionner': 'partition',
    'expandre_tabs': 'expandtabs',
    'supprimer_prefixe': 'removeprefix',
    'supprimer_suffixe': 'removesuffix',
    'est_ascii': 'isascii',
    'est_identifiant': 'isidentifier',
    'est_imprimable': 'isprintable',
    'traduire': 'translate',
    'rpartitionner': 'rpartition',
    'diviser_droite': 'rsplit',
    'diviser_lignes': 'splitlines',
    'formater_map': 'format_map',
}.items()}

METHODES_LISTE_INVERSEES = {v: k for k, v in {
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
}.items()}

METHODES_DICT_INVERSEES = {v: k for k, v in {
    'cles': 'keys',
    'valeurs': 'values',
    'elements': 'items',
    'obtenir': 'get',
    'mettre_a_jour': 'update',
    'extraire': 'pop',
    'vider': 'clear',
    'copier': 'copy',
    'extraire_defaut': 'setdefault',
    'extraire_dernier': 'popitem',
    'depuis_cles': 'fromkeys',
}.items()}

METHODES_ENSEMBLE_INVERSEES = {v: k for k, v in {
    'ajouter': 'add',
    'retirer': 'remove',
    'ecarter': 'discard',
    'union': 'union',
    'intersection': 'intersection',
    'difference': 'difference',
    'vider': 'clear',
    'copier': 'copy',
    'est_sous_ensemble': 'issubset',
    'est_sur_ensemble': 'issuperset',
    'difference_symetrique': 'symmetric_difference',
    'est_disjoint': 'isdisjoint',
    'mettre_a_jour': 'update',
    'intersection_sur_place': 'intersection_update',
    'difference_sur_place': 'difference_update',
    'diff_sym_sur_place': 'symmetric_difference_update',
    'extraire_aleatoire': 'pop',
}.items()}

MODULES_TRADUITS_INVERSES = {v: k for k, v in {
    'mathématiques': 'math',
    'aleatoire': 'random',
    'systeme': 'sys',
    'systeme_exploitation': 'os',
    'temps': 'time',
    'json': 'json',
    'collections': 'collections',
    'itertools': 'itertools',
    'functools': 'functools',
    'pathlib': 'pathlib',
    'io': 'io',
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
    'chemin': 'os.path',
    'expression_reguliere': 're',
    'iterateurs': 'itertools',
    'fil': 'threading',
    'multiprocessus': 'multiprocessing',
    'sous_processus': 'subprocess',
    'tests': 'unittest',
    'journalisation': 'logging',
    'arguments': 'argparse',
    'configuration': 'configparser',
    'base_donnees': 'sqlite3',
    'csv': 'csv',
    'xml': 'xml',
    'html': 'html',
    'email': 'email',
    'compression': 'zipfile',
    'archive': 'tarfile',
    'interface': 'tkinter',
    'graphiques': 'matplotlib',
    'donnees': 'pandas',
    'calcul': 'numpy',
    'images': 'PIL',
    'web': 'requests',
    'async_io': 'asyncio',
    'signal': 'signal',
    'plateforme': 'platform',
    'inspection': 'inspect',
    'abstrait': 'abc',
    'types_donnees': 'typing',
    'enum': 'enum',
    'dataclasse': 'dataclasses',
    'contextlib': 'contextlib',
    'warnings': 'warnings',
    'traceback': 'traceback',
    'garbage': 'gc',
    'weakref': 'weakref',
    'struct': 'struct',
    'uuid': 'uuid',
    'secret': 'secrets',
    'test_rapide': 'pytest',
    'tortue': 'turtle',
    'nombres': 'numbers',
    'couleur': 'colorsys',
    'ast_module': 'ast',
    'debogueur': 'pdb',
    'glob': 'glob',
    'gzip': 'gzip',
    'sqlite': 'sqlite3',
    'math': 'math',
    'pickle': 'pickle',
    'queue': 'queue',
    'shutil': 'shutil',
    'ssl': 'ssl',
    'stat': 'stat',
    'zlib': 'zlib',
    'zoneinfo': 'zoneinfo',
}.items()}


class Traducteur:

    def __init__(self, source: str):
        self.source = source
        self.lignes = source.splitlines(keepends=True)

    def traduire(self) -> str:
        resultat = []
        for ligne in self.lignes:
            resultat.append(self._traduire_ligne(ligne))
        return ''.join(resultat)

    def _traduire_ligne(self, ligne: str) -> str:
        stripped = ligne.lstrip()
        indentation = ligne[:len(ligne) - len(stripped)]
        if not stripped or stripped.startswith('#'):
            return ligne
        fin = '\n' if stripped.endswith('\n') else ''
        stripped = stripped.rstrip('\n')
        contenu = self._remplacer_tokens(stripped)
        return indentation + contenu + fin

    def _remplacer_tokens(self, code: str) -> str:
        parties = self._separer_chaines(code)
        resultat = []
        for est_chaine, partie in parties:
            if est_chaine:
                resultat.append(partie)
            else:
                resultat.append(self._remplacer_mots_cles(partie))
        return ''.join(resultat)

    def _separer_chaines(self, code: str):
        parties = []
        i = 0
        n = len(code)
        while i < n:
            char = code[i]
            if char in ('"', "'"):
                est_fstring = (i > 0 and code[i-1].lower() == 'f') or \
                              (i > 1 and code[i-2].lower() == 'f' and code[i-1] in 'rRbB')
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
                parties.append((True, contenu))
            else:
                j = i
                while j < n and code[j] not in ('"', "'"):
                    j += 1
                if j > i:
                    parties.append((False, code[i:j]))
                i = j
        return parties

    def _remplacer_mots_cles(self, code: str) -> str:
        methodes_fusionnees = {}
        methodes_fusionnees.update(METHODES_ENSEMBLE_INVERSEES)
        methodes_fusionnees.update(METHODES_DICT_INVERSEES)
        methodes_fusionnees.update(METHODES_CHAINE_INVERSEES)
        methodes_fusionnees.update(METHODES_LISTE_INVERSEES)
        for py, fr in methodes_fusionnees.items():
            code = re.sub(r'\.' + re.escape(py) + r'\b', '.' + fr, code)
        for py, fr in MODULES_TRADUITS_INVERSES.items():
            code = re.sub(r'\b' + re.escape(py) + r'\b', fr, code)
        for py, fr in sorted(PYTHON_VERS_FRYTHON.items(), key=lambda x: -len(x[0])):
            code = re.sub(r'\b' + re.escape(py) + r'\b', fr, code)
        return code


def traduire(source: str) -> str:
    t = Traducteur(source)
    return t.traduire()


def traduire_fichier(chemin_entree: str, chemin_sortie: str = None) -> str:
    if not chemin_entree.endswith('.py'):
        raise ValueError(f"Le fichier doit être un .py, reçu: {chemin_entree}")
    if chemin_sortie is None:
        chemin_sortie = chemin_entree[:-3] + '.fy'
    with open(chemin_entree, 'r', encoding='utf-8') as f:
        source = f.read()
    resultat = traduire(source)
    with open(chemin_sortie, 'w', encoding='utf-8') as f:
        f.write(resultat)
    return chemin_sortie
