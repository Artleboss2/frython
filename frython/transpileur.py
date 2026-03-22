import re

MOTS_CLES_VERS_PYTHON = {
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
    'fermer': 'close',
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
    'toutca': 'any',
    'entier_long': 'int',
    'complexe': 'complex',
    'tableau': 'bytearray',
    'vrai_faux': 'bool',
    'fige': 'frozenset',
    'tranche': 'slice',
    'type_base': 'type',
    'sous_classe': 'issubclass',
    'instance_de': 'isinstance',
    'imprimer': 'print',
    'longueur_max': 'max',
    'longueur_min': 'min',
    'puissance': 'pow',
    'divmod': 'divmod',
    'hex': 'hex',
    'octal': 'oct',
    'binaire': 'bin',
    'caractere': 'chr',
    'ordinal': 'ord',
    'globals': 'globals',
    'locals': 'locals',
    'entree': 'input',
    'executer_fichier': 'execfile',
    'formater_chaine': 'format',
    'iter': 'iter',
    'prochain': 'next',
    'hash': 'hash',
    'taille': 'sizeof',
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
    'imprimer_erreur': 'sys.stderr.write',
    'geler': 'frozenset',
}

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
    'maketrans': 'maketrans',
    'rfind': 'rfind',
    'rindex': 'rindex',
    'rpartitionner': 'rpartition',
    'diviser_droite': 'rsplit',
    'diviser_lignes': 'splitlines',
    'formater_map': 'format_map',
    'compter_depuis': 'count',
    'compter_tout': 'count',
}

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
    'supprimer': 'remove',
    'effacer': 'clear',
    'annexer': 'append',
    'concatener': 'extend',
    'inserer_debut': 'insert',
    'premier': 'pop',
    'dernier': 'pop',
    'existe': '__contains__',
    'longueur': '__len__',
    'multiplier': '__mul__',
    'copie_profonde': 'copy',
    'remplir': 'fill',
}

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
    'effacer': 'clear',
    'fusionner': 'update',
    'extraire_defaut': 'setdefault',
    'extraire_dernier': 'popitem',
    'depuis_cles': 'fromkeys',
    'inverser': 'items',
    'longueur': '__len__',
    'contient': '__contains__',
    'obtenir_ou_creer': 'setdefault',
}

METHODES_ENSEMBLE = {
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
    'geler': 'frozenset',
    'union_sur_place': 'update',
    'intersection_sur_place': 'intersection_update',
    'difference_sur_place': 'difference_update',
    'diff_sym_sur_place': 'symmetric_difference_update',
    'supprimer_si_existe': 'discard',
    'extraire_aleatoire': 'pop',
    'est_vide': '__len__',
}

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
    'mathematiques': 'math',
    'chemin': 'os.path',
    'date': 'datetime',
    'expression_reguliere': 're',
    'iterateurs': 'itertools',
    'fonctionnel': 'functools',
    'chemin_fichier': 'pathlib',
    'entree_sortie': 'io',
    'copie_profonde': 'deepcopy',
    'hachage': 'hashlib',
    'encodage': 'base64',
    'reseau': 'urllib',
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
    'chiffrement': 'cryptography',
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
    'binaire_io': 'io',
    'uuid': 'uuid',
    'secret': 'secrets',
    'environnement': 'dotenv',
    'test_rapide': 'pytest',
    'tortue': 'turtle',
    'nombres': 'numbers',
}

PYTHON_VERS_MOTS_CLES = {v: k for k, v in MOTS_CLES_VERS_PYTHON.items()}


class Transpileur:

    def __init__(self, source: str):
        self.source = source
        self.lignes = source.splitlines(keepends=True)

    def transpiler(self) -> str:
        resultat = []
        for ligne in self.lignes:
            resultat.append(self._transpiler_ligne(ligne))
        return ''.join(resultat)

    def _transpiler_ligne(self, ligne: str) -> str:
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
                if est_fstring:
                    contenu = self._traduire_fstring(contenu)
                parties.append((True, contenu))
            else:
                j = i
                while j < n and code[j] not in ('"', "'"):
                    j += 1
                if j > i:
                    parties.append((False, code[i:j]))
                i = j
        return parties

    def _traduire_fstring(self, fstring: str) -> str:
        resultat = []
        i = 0
        n = len(fstring)
        while i < n:
            if fstring[i] == '{' and i + 1 < n and fstring[i+1] != '{':
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
        methodes_fusionnees = {}
        methodes_fusionnees.update(METHODES_ENSEMBLE)
        methodes_fusionnees.update(METHODES_DICT)
        methodes_fusionnees.update(METHODES_CHAINE)
        methodes_fusionnees.update(METHODES_LISTE)
        for fr, py in methodes_fusionnees.items():
            code = re.sub(r'\.' + re.escape(fr) + r'\b', '.' + py, code)
        for fr, py in MODULES_TRADUITS.items():
            code = re.sub(r'\b' + re.escape(fr) + r'\b', py, code)
        for fr, py in sorted(MOTS_CLES_VERS_PYTHON.items(), key=lambda x: -len(x[0])):
            code = re.sub(r'\b' + re.escape(fr) + r'\b', py, code)
        return code


def transpiler(source: str) -> str:
    t = Transpileur(source)
    return t.transpiler()
