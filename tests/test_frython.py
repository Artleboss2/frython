"""
Tests pour Frython — Le Python en français.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from frython.transpileur import transpiler
from frython.interpreteur import InterpreteurFrython


def executer(source: str) -> dict:
    """Exécute du code Frython et retourne l'environnement."""
    code_python = transpiler(source)
    env = {}
    exec(code_python, env)
    return env


class TestsTranspileur(unittest.TestCase):
    """Tests de base pour le transpileur."""

    def test_afficher(self):
        code = transpiler("afficher('Bonjour')")
        self.assertIn("print('Bonjour')", code)

    def test_si_sinon(self):
        code = transpiler("si x > 0:\n    afficher('positif')\nsinon:\n    afficher('négatif')")
        self.assertIn("if x > 0:", code)
        self.assertIn("print('positif')", code)
        self.assertIn("else:", code)

    def test_tantque(self):
        code = transpiler("tantque i < 10:\n    i += 1")
        self.assertIn("while i < 10:", code)

    def test_pour_dans(self):
        code = transpiler("pour x dans ma_liste:\n    afficher(x)")
        self.assertIn("for x in ma_liste:", code)

    def test_def(self):
        code = transpiler("déf ma_fonction(x, y):\n    retourner x + y")
        self.assertIn("def ma_fonction(x, y):", code)
        self.assertIn("return x + y", code)

    def test_classe(self):
        code = transpiler("classe MaClasse:\n    passer")
        self.assertIn("class MaClasse:", code)
        self.assertIn("pass", code)

    def test_valeurs_booleennes(self):
        code = transpiler("x = Vrai\ny = Faux\nz = Rien")
        self.assertIn("x = True", code)
        self.assertIn("y = False", code)
        self.assertIn("z = None", code)

    def test_operateurs_logiques(self):
        code = transpiler("si x et y ou non z:\n    passer")
        self.assertIn("if x and y or not z:", code)

    def test_importer(self):
        code = transpiler("importer mathématiques")
        self.assertIn("import math", code)

    def test_fonctions_integrees(self):
        correspondances = [
            ("longueur(x)", "len(x)"),
            ("intervalle(10)", "range(10)"),
            ("liste(x)", "list(x)"),
            ("dictionnaire()", "dict()"),
            ("ensemble(x)", "set(x)"),
            ("entier(x)", "int(x)"),
            ("decimal(x)", "float(x)"),
            ("chaine(x)", "str(x)"),
            ("booleen(x)", "bool(x)"),
            ("enumerer(x)", "enumerate(x)"),
            ("zipper(a, b)", "zip(a, b)"),
            ("somme(x)", "sum(x)"),
            ("maximum(x)", "max(x)"),
            ("minimum(x)", "min(x)"),
            ("absolu(x)", "abs(x)"),
            ("arrondir(x)", "round(x)"),
            ("trier(x)", "sorted(x)"),
        ]
        for frython, python in correspondances:
            with self.subTest(frython=frython):
                code = transpiler(frython)
                self.assertIn(python, code, f"'{frython}' devrait produire '{python}'")

    def test_methodes_liste(self):
        code = transpiler("ma_liste.ajouter(42)")
        self.assertIn(".append(42)", code)

    def test_methodes_chaine(self):
        code = transpiler("texte.majuscule()")
        self.assertIn(".upper()", code)
        code = transpiler("texte.minuscule()")
        self.assertIn(".lower()", code)
        code = transpiler("texte.diviser()")
        self.assertIn(".split()", code)

    def test_methodes_dict(self):
        code = transpiler("mon_dict.cles()")
        self.assertIn(".keys()", code)
        code = transpiler("mon_dict.valeurs()")
        self.assertIn(".values()", code)
        code = transpiler("mon_dict.elements()")
        self.assertIn(".items()", code)

    def test_chaines_non_modifiees(self):
        code = transpiler('afficher("si vous si")')
        self.assertIn('"si vous si"', code)

    def test_lambda(self):
        code = transpiler("f = lambda x: x * 2")
        self.assertIn("lambda x: x * 2", code)

    def test_essayer_sauf(self):
        code = transpiler("essayer:\n    x = 1\nsauf ValueError:\n    passer")
        self.assertIn("try:", code)
        self.assertIn("except ValueError:", code)

    def test_lever(self):
        code = transpiler("lever ValueError('erreur')")
        self.assertIn("raise ValueError('erreur')", code)

    def test_retourner(self):
        code = transpiler("déf f():\n    retourner 42")
        self.assertIn("return 42", code)

    def test_casser_continuer(self):
        code = transpiler("tantque Vrai:\n    casser")
        self.assertIn("break", code)
        code = transpiler("pour x dans liste:\n    continuer")
        self.assertIn("continue", code)


class TestsExecution(unittest.TestCase):
    """Tests d'exécution complète."""

    def test_variable_simple(self):
        env = executer("x = 42")
        self.assertEqual(env['x'], 42)

    def test_calcul(self):
        env = executer("resultat = 10 + 5 * 2")
        self.assertEqual(env['resultat'], 20)

    def test_chaine(self):
        env = executer('texte = "Bonjour Frython"')
        self.assertEqual(env['texte'], "Bonjour Frython")

    def test_booleen(self):
        env = executer("v = Vrai\nf = Faux")
        self.assertTrue(env['v'])
        self.assertFalse(env['f'])

    def test_rien(self):
        env = executer("x = Rien")
        self.assertIsNone(env['x'])

    def test_liste(self):
        env = executer("ma_liste = [1, 2, 3, 4, 5]")
        self.assertEqual(env['ma_liste'], [1, 2, 3, 4, 5])

    def test_dict(self):
        env = executer('mon_dict = {"cle": "valeur"}')
        self.assertEqual(env['mon_dict'], {"cle": "valeur"})

    def test_condition_vraie(self):
        env = executer("x = 10\nsi x > 5:\n    resultat = 'grand'\nsinon:\n    resultat = 'petit'")
        self.assertEqual(env['resultat'], 'grand')

    def test_condition_fausse(self):
        env = executer("x = 3\nsi x > 5:\n    resultat = 'grand'\nsinon:\n    resultat = 'petit'")
        self.assertEqual(env['resultat'], 'petit')

    def test_boucle_pour(self):
        env = executer("total = 0\npour i dans intervalle(1, 6):\n    total += i")
        self.assertEqual(env['total'], 15)

    def test_boucle_tantque(self):
        env = executer("n = 0\ntantque n < 5:\n    n += 1")
        self.assertEqual(env['n'], 5)

    def test_fonction(self):
        env = executer("déf additionner(a, b):\n    retourner a + b\nresultat = additionner(3, 4)")
        self.assertEqual(env['resultat'], 7)

    def test_fonction_recursive(self):
        env = executer("déf factorielle(n):\n    si n <= 1:\n        retourner 1\n    retourner n * factorielle(n - 1)\nresultat = factorielle(5)")
        self.assertEqual(env['resultat'], 120)

    def test_comprehension_liste(self):
        env = executer("carres = [x**2 pour x dans intervalle(1, 6)]")
        self.assertEqual(env['carres'], [1, 4, 9, 16, 25])

    def test_longueur(self):
        env = executer("n = longueur([1, 2, 3, 4])")
        self.assertEqual(env['n'], 4)

    def test_somme(self):
        env = executer("total = somme([1, 2, 3, 4, 5])")
        self.assertEqual(env['total'], 15)

    def test_maximum_minimum(self):
        env = executer("grand = maximum([3, 1, 4, 1, 5, 9])\npetit = minimum([3, 1, 4, 1, 5, 9])")
        self.assertEqual(env['grand'], 9)
        self.assertEqual(env['petit'], 1)

    def test_ajouter_liste(self):
        env = executer("lst = [1, 2, 3]\nlst.ajouter(4)")
        self.assertEqual(env['lst'], [1, 2, 3, 4])

    def test_majuscule(self):
        env = executer("texte = 'bonjour'\nresultat = texte.majuscule()")
        self.assertEqual(env['resultat'], 'BONJOUR')

    def test_diviser(self):
        env = executer("mots = 'un deux trois'.diviser()")
        self.assertEqual(env['mots'], ['un', 'deux', 'trois'])

    def test_exception(self):
        env = executer("succes = Faux\nessayer:\n    x = 1 / 0\nsauf ZeroDivisionError:\n    succes = Vrai")
        self.assertTrue(env['succes'])

    def test_classe(self):
        code = """
classe Personne:
    def __init__(soi, nom, age):
        soi.nom = nom
        soi.age = age
    
    déf saluer(soi):
        retourner f"Bonjour, je suis {soi.nom}!"

p = Personne("Alice", 30)
message = p.saluer()
"""
        env = executer(code)
        self.assertEqual(env['message'], "Bonjour, je suis Alice!")

    def test_lambda(self):
        env = executer("doubler = lambda x: x * 2\nresultat = doubler(21)")
        self.assertEqual(env['resultat'], 42)

    def test_filtrer(self):
        env = executer("pairs = liste(filtrer(lambda x: x % 2 == 0, [1,2,3,4,5,6]))")
        self.assertEqual(env['pairs'], [2, 4, 6])

    def test_mapper(self):
        env = executer("carres = liste(mapper(lambda x: x**2, [1,2,3]))")
        self.assertEqual(env['carres'], [1, 4, 9])

    def test_enumerer(self):
        env = executer("paires = liste(enumerer(['a', 'b', 'c']))")
        self.assertEqual(env['paires'], [(0, 'a'), (1, 'b'), (2, 'c')])

    def test_zipper(self):
        env = executer("paires = liste(zipper([1,2,3], ['a','b','c']))")
        self.assertEqual(env['paires'], [(1, 'a'), (2, 'b'), (3, 'c')])


class TestsInterpreteur(unittest.TestCase):
    """Tests de l'interpréteur complet."""

    def setUp(self):
        self.interp = InterpreteurFrython()

    def test_execution_simple(self):
        code = self.interp.executer_source("x = 42", nom_fichier='<test>')
        self.assertEqual(code, 0)

    def test_syntaxe_invalide(self):
        import io
        from contextlib import redirect_stderr
        f = io.StringIO()
        with redirect_stderr(f):
            code = self.interp.executer_source("si si si si:", nom_fichier='<test>')
        self.assertNotEqual(code, 0)


if __name__ == '__main__':
    print("🐓 Tests Frython\n")
    unittest.main(verbosity=2)
