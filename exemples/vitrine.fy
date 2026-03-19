# vitrine.fy — Démonstration complète de Frython

afficher("=" * 50)
afficher("🐓 VITRINE FRYTHON — Toutes les fonctionnalités")
afficher("=" * 50)

# ── Variables et types ──────────────────────────────
afficher("\n📦 Types de données:")
entier_val = 42
decimal_val = 3.14159
chaine_val = "Bonjour, Frython!"
booleen_val = Vrai
rien_val = Rien

afficher(f"  Entier:    {entier_val} (type: {type(entier_val).__name__})")
afficher(f"  Décimal:   {decimal_val} (type: {type(decimal_val).__name__})")
afficher(f"  Chaîne:    {chaine_val!r}")
afficher(f"  Booléen:   {booleen_val}")
afficher(f"  Rien:      {rien_val}")

# ── Structures de données ───────────────────────────
afficher("\n🗂️ Structures de données:")

ma_liste = [1, 2, 3, 4, 5]
ma_liste.ajouter(6)
afficher(f"  Liste:         {ma_liste}")

mon_dict = {"nom": "Alice", "age": 30, "ville": "Paris"}
afficher(f"  Dictionnaire:  {mon_dict}")
afficher(f"  Clés:          {liste(mon_dict.cles())}")

mon_ensemble = {1, 2, 3, 2, 1}
afficher(f"  Ensemble:      {mon_ensemble}")

mon_tuple = (10, 20, 30)
afficher(f"  Tuple:         {mon_tuple}")

# ── Structures de contrôle ──────────────────────────
afficher("\n🔀 Structures de contrôle:")

# Si / Sinon
score = 75
si score >= 90:
    mention = "Excellent"
sinonsi score >= 75:
    mention = "Bien"
sinonsi score >= 60:
    mention = "Passable"
sinon:
    mention = "Insuffisant"
afficher(f"  Score {score} → Mention: {mention}")

# Boucle pour
afficher("  Comptage: ", end="")
pour i dans intervalle(1, 6):
    afficher(i, end=" ")
afficher()

# Boucle tantque avec casser/continuer
afficher("  Nombres pairs < 10: ", end="")
n = 0
tantque n < 10:
    n += 1
    si n % 2 != 0:
        continuer
    afficher(n, end=" ")
afficher()

# ── Compréhensions ──────────────────────────────────
afficher("\n🧩 Compréhensions de liste:")
carres = [x**2 pour x dans intervalle(1, 8)]
afficher(f"  Carrés: {carres}")

pairs_cubes = [x**3 pour x dans intervalle(1, 10) si x % 2 == 0]
afficher(f"  Cubes des pairs: {pairs_cubes}")

# ── Fonctions ───────────────────────────────────────
afficher("\n⚙️ Fonctions:")

déf factorielle(n):
    """Calcule n! récursivement."""
    si n <= 1:
        retourner 1
    retourner n * factorielle(n - 1)

pour i dans [0, 1, 5, 10]:
    afficher(f"  {i}! = {factorielle(i)}")

# Fonction avec valeurs par défaut
déf saluer(nom, salutation="Bonjour", ponctuation="!"):
    retourner f"{salutation}, {nom}{ponctuation}"

afficher(f"  {saluer('Pierre')}")
afficher(f"  {saluer('Marie', 'Bonsoir', '...')}")

# Fonction avec *args et **kwargs
déf calculer(*nombres, op="somme"):
    si op == "somme":
        retourner somme(nombres)
    sinonsi op == "max":
        retourner maximum(nombres)
    sinonsi op == "min":
        retourner minimum(nombres)

afficher(f"  Somme: {calculer(1, 2, 3, 4, 5)}")
afficher(f"  Maximum: {calculer(3, 1, 4, 1, 5, 9, op='max')}")

# Lambda
doubler = lambda x: x * 2
afficher(f"  Doubler 7: {doubler(7)}")

# ── Exceptions ──────────────────────────────────────
afficher("\n⚠️ Gestion des exceptions:")

essayer:
    resultat = 10 / 0
sauf ZeroDivisionError:
    afficher("  Erreur capturée: Division par zéro!")

essayer:
    nombre = entier("pas un nombre")
sauf ValueError as e:
    afficher(f"  Erreur capturée: {e}")
enfin:
    afficher("  Bloc 'enfin' toujours exécuté.")

# ── Opérations sur les chaînes ──────────────────────
afficher("\n📝 Manipulation de chaînes:")
texte = "frython est fantastique"
afficher(f"  Original:   {texte}")
afficher(f"  Majuscule:  {texte.majuscule()}")
afficher(f"  Titre:      {texte.titrer()}")
afficher(f"  Mots:       {texte.diviser()}")
afficher(f"  Longueur:   {longueur(texte)}")
afficher(f"  Remplacer:  {texte.remplacer('fantastique', 'magnifique')}")

# ── Fonctions d'ordre supérieur ─────────────────────
afficher("\n🔧 Fonctions d'ordre supérieur:")
nombres = liste(intervalle(1, 11))
afficher(f"  Nombres: {nombres}")
afficher(f"  Pairs:   {liste(filtrer(lambda x: x % 2 == 0, nombres))}")
afficher(f"  Carrés:  {liste(mapper(lambda x: x**2, nombres))}")
afficher(f"  Triés ↓: {trier(nombres, reverse=Vrai)}")

afficher("\n" + "=" * 50)
afficher("✅ Frython fonctionne parfaitement!")
afficher("   Vive le Python en français! 🇫🇷🐓")
afficher("=" * 50)
