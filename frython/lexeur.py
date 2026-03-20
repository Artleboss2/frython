"""
Frython - Lexeur (Tokenizer)
Transforme le code source Frython en tokens.
"""

MOTS_CLES = {
    'si': 'SI',
    'sinon': 'SINON',
    'sinonsi': 'SINONSI',
    'tantque': 'TANTQUE',
    'pour': 'POUR',
    'dans': 'DANS',
    'intervalle': 'INTERVALLE',
    'casser': 'CASSER',
    'continuer': 'CONTINUER',
    'passer': 'PASSER',

    'def': 'DEF',           
    'déf': 'DEF',
    'retourner': 'RETOURNER',
    'lambda': 'LAMBDA',

    'classe': 'CLASSE',
    'soi': 'SOI',
    'super': 'SUPER',
    'héritage': 'HERITAGE',

    'Vrai': 'VRAI',
    'Faux': 'FAUX',
    'Rien': 'RIEN',

    'et': 'ET',
    'ou': 'OU',
    'non': 'NON',
    'dans': 'DANS',
    'pasdans': 'PASDANS',
    'est': 'EST',

    'importer': 'IMPORTER',
    'de': 'DE',
    'comme': 'COMME',

    'essayer': 'ESSAYER',
    'sauf': 'SAUF',
    'enfin': 'ENFIN',
    'lever': 'LEVER',

    'avec': 'AVEC',

    'affirmer': 'AFFIRMER',

    'afficher': 'AFFICHER',
    'saisir': 'SAISIR',
    'type': 'TYPE',
    'longueur': 'LONGUEUR',
    'intervalle': 'INTERVALLE',
    'liste': 'LISTE',
    'dictionnaire': 'DICTIONNAIRE',
    'ensemble': 'ENSEMBLE',
    'tuple': 'TUPLE',
    'entier': 'ENTIER',
    'decimal': 'DECIMAL',
    'chaine': 'CHAINE',
    'booleen': 'BOOLEEN',
    'enumerer': 'ENUMERER',
    'zipper': 'ZIPPER',
    'mapper': 'MAPPER',
    'filtrer': 'FILTRER',
    'trier': 'TRIER',
    'inverser': 'INVERSER',
    'somme': 'SOMME',
    'maximum': 'MAXIMUM',
    'minimum': 'MINIMUM',
    'absolu': 'ABSOLU',
    'arrondir': 'ARRONDIR',
    'aide': 'AIDE',
    'dir': 'DIR',
    'vars': 'VARS',
    'hasattr': 'HASATTR',
    'getattr': 'GETATTR',
    'setattr': 'SETATTR',
    'global': 'GLOBAL',
    'nonlocal': 'NONLOCAL',
    'del': 'DEL',
    'supprimer': 'SUPPRIMER',
    'rendement': 'RENDEMENT',  
    'asynchrone': 'ASYNCHRONE', 
    'attendre': 'ATTENDRE',  
}

TYPES_TOKENS = [
    'NOMBRE',
    'DECIMAL_LIT',
    'CHAINE_LIT',
    'VRAI', 'FAUX', 'RIEN',

    'IDENT',

    'SI', 'SINON', 'SINONSI',
    'TANTQUE', 'POUR', 'DANS', 'PASDANS',
    'CASSER', 'CONTINUER', 'PASSER',
    'RETOURNER', 'LAMBDA', 'EST',

    'DEF', 'CLASSE', 'SOI', 'SUPER', 'HERITAGE',

    'IMPORTER', 'DE', 'COMME',

    'ESSAYER', 'SAUF', 'ENFIN', 'LEVER',

    'AVEC',

    'AFFIRMER',

    'AFFICHER', 'SAISIR', 'TYPE', 'LONGUEUR',
    'INTERVALLE', 'LISTE', 'DICTIONNAIRE', 'ENSEMBLE',
    'TUPLE', 'ENTIER', 'DECIMAL', 'CHAINE', 'BOOLEEN',
    'ENUMERER', 'ZIPPER', 'MAPPER', 'FILTRER',
    'TRIER', 'INVERSER', 'SOMME', 'MAXIMUM', 'MINIMUM',
    'ABSOLU', 'ARRONDIR', 'AIDE',
    'DIR', 'VARS', 'HASATTR', 'GETATTR', 'SETATTR',
    'GLOBAL', 'NONLOCAL', 'DEL', 'SUPPRIMER',
    'RENDEMENT', 'ASYNCHRONE', 'ATTENDRE',

    'ET', 'OU', 'NON',

    'PLUS', 'MOINS', 'ETOILE', 'SLASH', 'DOUBLEETOILE', 'DOUBLESLASH', 'MODULO',

    'EG', 'NEG', 'LT', 'GT', 'LTE', 'GTE',

    'ASSIGNER', 'PLUSEG', 'MOINSEG', 'ETOILEEG', 'SLASHEG', 'MODEG',

    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'VIRGULE', 'DEUXPOINTS', 'POINTVIRGULE', 'POINT',
    'FLECHE', 'AROBASE', 'TILDE',

    'WALRUS',

    'INDENT', 'DEDENT', 'NEWLINE', 'EOF',
]


class Token:
    def __init__(self, type, valeur, ligne=0, colonne=0):
        self.type = type
        self.valeur = valeur
        self.ligne = ligne
        self.colonne = colonne

    def __repr__(self):
        return f"Token({self.type}, {repr(self.valeur)}, L{self.ligne}:C{self.colonne})"


class ErreurLexicale(Exception):
    def __init__(self, message, ligne=0, colonne=0):
        self.ligne = ligne
        self.colonne = colonne
        super().__init__(f"Ligne {ligne}, Colonne {colonne}: {message}")


class Lexeur:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.ligne = 1
        self.colonne = 1
        self.tokens = []
        self.pile_indentation = [0]

    def char_actuel(self):
        if self.pos < len(self.source):
            return self.source[self.pos]
        return None

    def regarder(self, decalage=1):
        pos = self.pos + decalage
        if pos < len(self.source):
            return self.source[pos]
        return None

    def avancer(self):
        char = self.source[self.pos]
        self.pos += 1
        if char == '\n':
            self.ligne += 1
            self.colonne = 1
        else:
            self.colonne += 1
        return char

    def sauter_commentaire(self):
        while self.char_actuel() and self.char_actuel() != '\n':
            self.avancer()

    def lire_nombre(self):
        debut_ligne = self.ligne
        debut_col = self.colonne
        resultat = ''
        while self.char_actuel() and self.char_actuel().isdigit():
            resultat += self.avancer()
        if self.char_actuel() == '.' and self.regarder() and self.regarder().isdigit():
            resultat += self.avancer()
            while self.char_actuel() and self.char_actuel().isdigit():
                resultat += self.avancer()
            return Token('DECIMAL_LIT', float(resultat), debut_ligne, debut_col)
        return Token('NOMBRE', int(resultat), debut_ligne, debut_col)

    def lire_chaine(self, guillemet):
        debut_ligne = self.ligne
        debut_col = self.colonne
        self.avancer()
        triple = False
        if self.char_actuel() == guillemet and self.regarder() == guillemet:
            self.avancer()
            self.avancer()
            triple = True

        resultat = ''
        while self.char_actuel():
            char = self.char_actuel()
            if triple:
                if char == guillemet and self.regarder() == guillemet and self.regarder(2) == guillemet:
                    self.avancer(); self.avancer(); self.avancer()
                    break
            else:
                if char == guillemet:
                    self.avancer()
                    break
                if char == '\n':
                    raise ErreurLexicale("Chaîne non terminée", self.ligne, self.colonne)
            if char == '\\':
                self.avancer()
                escapes = {'n': '\n', 't': '\t', 'r': '\r', '\\': '\\',
                           '"': '"', "'": "'", '0': '\0', 'a': '\a', 'b': '\b'}
                c = self.char_actuel()
                resultat += escapes.get(c, c)
                self.avancer()
            else:
                resultat += self.avancer()
        return Token('CHAINE_LIT', resultat, debut_ligne, debut_col)

    def lire_identifiant(self):
        debut_ligne = self.ligne
        debut_col = self.colonne
        resultat = ''
        while self.char_actuel() and (self.char_actuel().isalnum() or self.char_actuel() in ('_', 'é', 'è', 'ê', 'ë', 'à', 'â', 'ù', 'û', 'î', 'ï', 'ô', 'ç', 'É', 'È', 'Ê', 'À', 'Â', 'Ù', 'Û', 'Î', 'Ï', 'Ô', 'Ç')):
            resultat += self.avancer()
        type_token = MOTS_CLES.get(resultat, 'IDENT')
        return Token(type_token, resultat, debut_ligne, debut_col)

    def gerer_indentation(self, niveau):
        """Génère les tokens INDENT et DEDENT selon le niveau d'indentation."""
        actuel = self.pile_indentation[-1]
        if niveau > actuel:
            self.pile_indentation.append(niveau)
            self.tokens.append(Token('INDENT', niveau, self.ligne, 1))
        elif niveau < actuel:
            while self.pile_indentation and self.pile_indentation[-1] > niveau:
                self.pile_indentation.pop()
                self.tokens.append(Token('DEDENT', niveau, self.ligne, 1))
            if self.pile_indentation[-1] != niveau:
                raise ErreurLexicale("Indentation incohérente", self.ligne, 1)

    def tokeniser(self):
        while self.pos < len(self.source):
            char = self.char_actuel()

            if self.colonne == 1 and char not in ('\n', '#', None):
                niveau = 0
                pos_temp = self.pos
                while pos_temp < len(self.source) and self.source[pos_temp] in (' ', '\t'):
                    if self.source[pos_temp] == '\t':
                        niveau += 4
                    else:
                        niveau += 1
                    pos_temp += 1
                if pos_temp < len(self.source) and self.source[pos_temp] not in ('\n', '#'):
                    self.gerer_indentation(niveau)
                while self.char_actuel() in (' ', '\t'):
                    self.avancer()
                continue

            if char in (' ', '\t'):
                self.avancer()
                continue

            if char == '#':
                self.sauter_commentaire()
                continue

            if char == '\n':
                if self.tokens and self.tokens[-1].type not in ('NEWLINE', 'INDENT', 'DEDENT', 'DEUXPOINTS'):
                    self.tokens.append(Token('NEWLINE', '\n', self.ligne, self.colonne))
                self.avancer()
                continue

            if char == '\\' and self.regarder() == '\n':
                self.avancer(); self.avancer()
                continue

            debut_ligne = self.ligne
            debut_col = self.colonne

            if char.isdigit():
                self.tokens.append(self.lire_nombre())
                continue

            if char in ('"', "'"):
                self.tokens.append(self.lire_chaine(char))
                continue

            if char.isalpha() or char == '_' or char in 'éèêëàâùûîïôçÉÈÊÀÂÙÛÎÏÔÇ':
                self.tokens.append(self.lire_identifiant())
                continue

            if char == '+':
                if self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('PLUSEG', '+=', debut_ligne, debut_col))
                else:
                    self.avancer()
                    self.tokens.append(Token('PLUS', '+', debut_ligne, debut_col))
            elif char == '-':
                if self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('MOINSEG', '-=', debut_ligne, debut_col))
                elif self.regarder() == '>':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('FLECHE', '->', debut_ligne, debut_col))
                else:
                    self.avancer()
                    self.tokens.append(Token('MOINS', '-', debut_ligne, debut_col))
            elif char == '*':
                if self.regarder() == '*':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('DOUBLEETOILE', '**', debut_ligne, debut_col))
                elif self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('ETOILEEG', '*=', debut_ligne, debut_col))
                else:
                    self.avancer()
                    self.tokens.append(Token('ETOILE', '*', debut_ligne, debut_col))
            elif char == '/':
                if self.regarder() == '/':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('DOUBLESLASH', '//', debut_ligne, debut_col))
                elif self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('SLASHEG', '/=', debut_ligne, debut_col))
                else:
                    self.avancer()
                    self.tokens.append(Token('SLASH', '/', debut_ligne, debut_col))
            elif char == '%':
                if self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('MODEG', '%=', debut_ligne, debut_col))
                else:
                    self.avancer()
                    self.tokens.append(Token('MODULO', '%', debut_ligne, debut_col))
            elif char == '=':
                if self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('EG', '==', debut_ligne, debut_col))
                elif self.regarder() == '>':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('FLECHE', '=>', debut_ligne, debut_col))
                else:
                    self.avancer()
                    self.tokens.append(Token('ASSIGNER', '=', debut_ligne, debut_col))
            elif char == '!':
                if self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('NEG', '!=', debut_ligne, debut_col))
                else:
                    raise ErreurLexicale(f"Caractère inattendu '!'", debut_ligne, debut_col)
            elif char == '<':
                if self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('LTE', '<=', debut_ligne, debut_col))
                else:
                    self.avancer()
                    self.tokens.append(Token('LT', '<', debut_ligne, debut_col))
            elif char == '>':
                if self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('GTE', '>=', debut_ligne, debut_col))
                else:
                    self.avancer()
                    self.tokens.append(Token('GT', '>', debut_ligne, debut_col))
            elif char == ':':
                if self.regarder() == '=':
                    self.avancer(); self.avancer()
                    self.tokens.append(Token('WALRUS', ':=', debut_ligne, debut_col))
                else:
                    self.avancer()
                    self.tokens.append(Token('DEUXPOINTS', ':', debut_ligne, debut_col))
            elif char == '(':
                self.avancer()
                self.tokens.append(Token('LPAREN', '(', debut_ligne, debut_col))
            elif char == ')':
                self.avancer()
                self.tokens.append(Token('RPAREN', ')', debut_ligne, debut_col))
            elif char == '[':
                self.avancer()
                self.tokens.append(Token('LBRACKET', '[', debut_ligne, debut_col))
            elif char == ']':
                self.avancer()
                self.tokens.append(Token('RBRACKET', ']', debut_ligne, debut_col))
            elif char == '{':
                self.avancer()
                self.tokens.append(Token('LBRACE', '{', debut_ligne, debut_col))
            elif char == '}':
                self.avancer()
                self.tokens.append(Token('RBRACE', '}', debut_ligne, debut_col))
            elif char == ',':
                self.avancer()
                self.tokens.append(Token('VIRGULE', ',', debut_ligne, debut_col))
            elif char == '.':
                self.avancer()
                self.tokens.append(Token('POINT', '.', debut_ligne, debut_col))
            elif char == ';':
                self.avancer()
                self.tokens.append(Token('POINTVIRGULE', ';', debut_ligne, debut_col))
            elif char == '@':
                self.avancer()
                self.tokens.append(Token('AROBASE', '@', debut_ligne, debut_col))
            elif char == '~':
                self.avancer()
                self.tokens.append(Token('TILDE', '~', debut_ligne, debut_col))
            else:
                raise ErreurLexicale(f"Caractère inconnu '{char}'", debut_ligne, debut_col)

        while len(self.pile_indentation) > 1:
            self.pile_indentation.pop()
            self.tokens.append(Token('DEDENT', 0, self.ligne, 1))

        self.tokens.append(Token('EOF', None, self.ligne, self.colonne))
        return self.tokens
