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
    'entree_erreur': 'stderr',
    'afficher_format': 'format',
    'memoire': 'memoryview',
    'aiter': 'aiter',
	'prochain_async': 'anext',
	'ascii': 'ascii',
	'compiler': 'compile',
	'supprimer_attribut': 'delattr',
	'repertoire': 'dir',
	'obtenir_attribut': 'getattr',
	'a_attribut': 'hasattr',
	'index': '__index__',
	'vue_memoire': 'memoryview',
	'definir_attribut': 'setattr',
	'variables': 'vars',
	'importer_module': '__import__',
	'__construire_classe__': 'NATIVE.__build_class__',
	'__importer__': 'NATIVE.__import__',
	'abs': 'NATIVE.abs',
	'aiter': 'NATIVE.aiter',
	'tous': 'NATIVE.all',
	'anext': 'NATIVE.anext',
	'asuivant': 'NATIVE.anext',
	'suivant_async': 'NATIVE.anext',
	'certains': 'NATIVE.any',
	'n_importe_quel': 'NATIVE.any',
	'appendStr': 'NATIVE.appendStr',
	'ajouterStr': 'NATIVE.appendStr',
	'ascii': 'NATIVE.ascii',
	'bin': 'NATIVE.bin',
	'binaire': 'NATIVE.bin',
	'bound': 'NATIVE.bound',
	'lien': 'NATIVE.bound',
	'limite': 'NATIVE.bound',
	'breakpoint': 'NATIVE.breakpoint',
	'point_de_rupture': 'NATIVE.breakpoint',
	'pointderupture': 'NATIVE.breakpoint',
	'callable': 'NATIVE.callable',
	'appelable': 'NATIVE.callable',
	'chr': 'NATIVE.chr',
	'clamp': 'NATIVE.clamp',
	'pince': 'NATIVE.clamp',
	'serrer': 'NATIVE.clamp',
	'compile': 'NATIVE.compile',
	'compiler': 'NATIVE.compile',
	'configIsToday': 'NATIVE.configIsToday',
	'configurationEstAujourdhui': 'NATIVE.configIsToday',
	'typeprofond': 'NATIVE.deeptype',
	'type_profond': 'NATIVE.deeptype',
	'rep': 'NATIVE.dir',
	'div_reste': 'NATIVE.divmod',
	'divreste': 'NATIVE.divmod',
	'erreur_enregistree': 'NATIVE.exceptionLogged',
	'exception_enregistree': 'NATIVE.exceptionLogged',
	'exception_journalisee': 'NATIVE.exceptionLogged',
	'repr_rapide': 'NATIVE.fastRepr',
	'representation_rapide': 'NATIVE.fastRepr',
	'volant_inertie': 'NATIVE.flywheel',
	'regulateur': 'NATIVE.flywheel',
	'accumulateur': 'NATIVE.flywheel',
	'formater': 'NATIVE.format',
    'obtenir_base': 'NATIVE.getBase',
    'obtenir_depot': 'NATIVE.getRepository',
    'dictionnaire_histogramme': 'NATIVE.histogramDict',
    'inverser_dictionnaire': 'NATIVE.invertDict',
    'inverser_dictionnaire_sans_perte': 'NATIVE.invertDictLossless',
    'type_itérateur': 'NATIVE.itype',
    'interpolation_linéaire': 'NATIVE.lerp',
    'lerp': 'NATIVE.lerp',
    'journaliser_bloc': 'NATIVE.logBlock',
    'generateur_boucle': 'NATIVE.loopGen',
    'creer_liste': 'NATIVE.makeList',
    'creer_tuple': 'NATIVE.makeTuple',
    'generateur_nul': 'NATIVE.nullGen',
    'afficher_pile_inverse': 'NATIVE.printReverseStack',
    'afficher_pile': 'NATIVE.printStack',
    'afficher_pile_verbeuse': 'NATIVE.printVerboseStack',
    'profile': 'NATIVE.profiled',
    'collecte_pstat': 'NATIVE.pstatcollect',
    'rapport': 'NATIVE.report',
    'repr_securise': 'NATIVE.safeRepr',
    'nom_type_securise': 'NATIVE.safeTypeName',
    'numero_serie': 'NATIVE.serialNum',
    'nom_type': 'NATIVE.typeName',
    'nom_unique': 'NATIVE.uniqueName',
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
    'en_liste': 'split',
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
    'remplir_avec': 'extend',
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
    'a_cle': 'has_key',
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
    'couleur': 'colorsys',
    'decimal_precision': 'decimal',
	'ast_module': 'ast',
	'debogueur': 'pdb',
	'code_module': 'code',
	'collections_abc': 'collections.abc',
	'concurrent': 'concurrent.futures',
	'cryptographie': 'cryptography',
	'curses': 'curses',
	'difflib': 'difflib',
	'dis': 'dis',
	'doctest': 'doctest',
	'fichier_entree': 'fileinput',
	'fnmatch': 'fnmatch',	
	'formateur': 'formatter',
	'fractions': 'fractions',
	'ftplib': 'ftplib',
	'futur': '__future__',
	'gestionnaire_contexte': 'contextlib',
	'glob': 'glob',
	'grp': 'grp',
	'gzip': 'gzip',
	'heapq': 'heapq',
	'hmac': 'hmac',
	'html_analyse': 'html.parser',
	'http_client': 'http.client',
	'http_serveur': 'http.server',
	'imaplib': 'imaplib',
	'importlib': 'importlib',
	'ipaddress': 'ipaddress',
	'locale': 'locale',
	'lzma': 'lzma',
	'mailbox': 'mailbox',
	'marshal': 'marshal',
	'math': 'math',
	'mimetypes': 'mimetypes',
	'mmap': 'mmap',
	'msvcrt': 'msvcrt',
	'netrc': 'netrc',
	'nis': 'nis',
	'nntplib': 'nntplib',
	'nombres': 'numbers',
	'operateur': 'operator',
	'optparse': 'optparse',
	'os_chemin': 'os.path',
	'pickle': 'pickle',
	'pickletools': 'pickletools',
	'pipes': 'pipes',
	'pkgutil': 'pkgutil',
	'poplib': 'poplib',
	'pprint': 'pprint',
	'profil': 'cProfile',
	'pty': 'pty',
	'pwd': 'pwd',
	'py_compile': 'py_compile',
	'pydoc': 'pydoc',
	'queue': 'queue',
	'quopri': 'quopri',
	'readline': 'readline',
	'reprlib': 'reprlib',
	'rlcompleter': 'rlcompleter',
	'runpy': 'runpy',
	'sched': 'sched',
	'secrets': 'secrets',
	'select': 'select',
	'selectors': 'selectors',
	'shelve': 'shelve',
	'shlex': 'shlex',
	'shutil': 'shutil',
	'smtplib': 'smtplib',
	'sndhdr': 'sndhdr',
	'spwd': 'spwd',
	'sqlite': 'sqlite3',
	'ssl': 'ssl',
	'stat': 'stat',
	'statistiques_module': 'statistics',
	'string_module': 'string',
	'stringprep': 'stringprep',
	'tableau_module': 'array',
	'telnetlib': 'telnetlib',
	'tempfichier': 'tempfile',
	'terminal': 'tty',
	'textwrap': 'textwrap',
	'timeit': 'timeit',
	'tkinter_module': 'tkinter',
	'token': 'token',
	'tokenize': 'tokenize',
	'tomllib': 'tomllib',
	'trace': 'trace',
	'turtle_module': 'turtle',
	'turtledemo': 'turtledemo',
	'types_module': 'types',
	'unicodedata': 'unicodedata',
	'urllib_analyse': 'urllib.parse',
	'urllib_requete': 'urllib.request',
	'urllib_erreur': 'urllib.error',
	'uu': 'uu',
	'venv': 'venv',
	'wave': 'wave',
	'webbrowser': 'webbrowser',
	'winreg': 'winreg',
	'winsound': 'winsound',
	'wsgiref': 'wsgiref',
	'xdrlib': 'xdrlib',
	'xmlrpc': 'xmlrpc',
	'zipapp': 'zipapp',
	'zipimport': 'zipimport',
	'zlib': 'zlib',
	'zoneinfo': 'zoneinfo',
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
