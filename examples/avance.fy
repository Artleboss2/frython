# avance.fy — Fonctionnalités avancées: décorateurs, générateurs, contextes

importer time
importer functools

afficher("🚀 Frython — Fonctionnalités avancées")
afficher("=" * 45)

# ── Décorateurs ─────────────────────────────────────
afficher("\n🎨 Décorateurs:")

déf minuteur(fonction):
    """Décorateur qui mesure le temps d'exécution."""
    @functools.wraps(fonction)
    déf enveloppe(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        duree = (time.time() - debut) * 1000
        afficher(f"  ⏱️  {fonction.__name__}() → {duree:.3f} ms")
        retourner resultat
    retourner enveloppe

déf memoriser(fonction):
    """Décorateur de mémoïsation (cache des résultats)."""
    cache = {}
    @functools.wraps(fonction)
    déf enveloppe(*args):
        si args non dans cache:
            cache[args] = fonction(*args)
        retourner cache[args]
    retourner enveloppe

déf repeter(n):
    """Décorateur-fabrique qui répète une fonction n fois."""
    déf decorateur(fonction):
        @functools.wraps(fonction)
        déf enveloppe(*args, **kwargs):
            pour _ dans intervalle(n):
                resultat = fonction(*args, **kwargs)
            retourner resultat
        retourner enveloppe
    retourner decorateur

@minuteur
déf somme_lente(n):
    retourner somme(intervalle(n))

@memoriser
@minuteur
déf fibonacci_memo(n):
    si n <= 1:
        retourner n
    retourner fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

@repeter(3)
déf saluer(nom):
    afficher(f"  Bonjour, {nom}!")

resultat = somme_lente(1000000)
afficher(f"  Somme(1M) = {resultat}")

afficher()
afficher("  Fibonacci avec mémoïsation:")
pour i dans [10, 20, 30, 35]:
    afficher(f"  F({i}) = {fibonacci_memo(i)}")

afficher()
afficher("  Décorateur @repeter(3):")
saluer("Frython")

# ── Générateurs ─────────────────────────────────────
afficher("\n⚡ Générateurs:")

déf compter_infini(debut=0, pas=1):
    """Générateur infini."""
    n = debut
    tantque Vrai:
        rendement n
        n += pas

déf nombres_premiers():
    """Générateur de nombres premiers à l'infini."""
    rendement 2
    candidats = compter_infini(3, 2)
    premiers = []
    pour n dans candidats:
        si tout(n % p != 0 pour p dans premiers si p * p <= n):
            premiers.ajouter(n)
            rendement n

déf prendre(generateur, n):
    """Prend les n premiers éléments d'un générateur."""
    retourner [suivant(generateur) pour _ dans intervalle(n)]

tout = all
suivant = next

gen = compter_infini(0, 5)
afficher(f"  Multiples de 5: {prendre(gen, 8)}")

premiers = nombres_premiers()
afficher(f"  20 premiers nombres premiers: {prendre(premiers, 20)}")

# Pipeline de générateurs
déf au_carre(gen):
    pour x dans gen:
        rendement x ** 2

déf filtrer_pairs(gen):
    pour x dans gen:
        si x % 2 == 0:
            rendement x

source = compter_infini(1)
carres = au_carre(source)
pairs = filtrer_pairs(carres)
afficher(f"  Carrés pairs: {prendre(pairs, 6)}")

# ── Compréhensions avancées ──────────────────────────
afficher("\n🧩 Compréhensions avancées:")

matrice = [[i * j pour j dans intervalle(1, 6)] pour i dans intervalle(1, 6)]
afficher("  Table de multiplication (5x5):")
pour ligne dans matrice:
    afficher("  " + "  ".join(f"{n:2d}" pour n dans ligne))

# Dict comprehension
carres_dict = {n: n**2 pour n dans intervalle(1, 11)}
afficher(f"\n  Carrés (dict): {carres_dict}")

# Set comprehension
lettres_uniques = {lettre pour lettre dans "frython est magnifique" si lettre != " "}
afficher(f"  Lettres uniques: {trier(lettres_uniques)}")
