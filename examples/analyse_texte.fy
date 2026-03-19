# analyse_texte.fy — Analyseur de texte en Frython

afficher("📖 Analyseur de texte — Frython")
afficher("=" * 40)

texte = """
Le petit prince est un roman de l'écrivain français Antoine de Saint-Exupéry,
publié le 6 avril 1943 aux États-Unis. Il est la troisième œuvre de fiction
de l'auteur après le Petit Lac Ladoga et Courrier Sud. Le petit prince est
la troisième œuvre de fiction de l'auteur. C'est l'un des livres les plus
traduits et les plus vendus dans le monde avec plus de deux cents millions
d'exemplaires vendus dans deux cent trente et un pays et territoires.
Le roman relate la rencontre d'un aviateur avec le petit prince, personnage
enfantin qui voyage de planète en planète dans l'univers. Il aborde, avec
un regard d'enfant, des sujets philosophiques comme la solitude,
l'amitié, l'amour et le sens de la vie.
"""

déf nettoyer_mot(mot):
    """Supprime la ponctuation d'un mot."""
    ponctuations = ".,;:!?'\"-()[]{}«»"
    pour p dans ponctuations:
        mot = mot.remplacer(p, "")
    retourner mot.minuscule().supprimer_espaces()

déf analyser(texte):
    lignes = texte.diviser("\n")
    mots_bruts = texte.diviser()
    mots = [nettoyer_mot(m) pour m dans mots_bruts si nettoyer_mot(m)]
    
    # Fréquences
    frequences = {}
    pour mot dans mots:
        frequences[mot] = frequences.obtenir(mot, 0) + 1
    
    # Mots les plus fréquents
    top_mots = trier(frequences.elements(), key=lambda x: x[1], reverse=Vrai)
    
    # Mots uniques
    mots_uniques = ensemble(mots)
    
    # Longueur moyenne des mots
    longueur_moy = somme(longueur(m) pour m dans mots) / longueur(mots)
    
    # Phrases (séparées par . ! ?)
    phrases = [p.supprimer_espaces() pour p dans texte.remplacer("!", ".").remplacer("?", ".").diviser(".") si p.supprimer_espaces()]
    
    retourner {
        "nb_caracteres": longueur(texte),
        "nb_mots": longueur(mots),
        "nb_mots_uniques": longueur(mots_uniques),
        "nb_phrases": longueur(phrases),
        "nb_lignes": longueur([l pour l dans lignes si l.supprimer_espaces()]),
        "longueur_moy_mots": arrondir(longueur_moy, 2),
        "top_mots": top_mots[:15],
        "frequences": frequences,
        "mots_uniques": mots_uniques,
    }

stats = analyser(texte)

afficher("\n📊 Statistiques générales:")
afficher(f"  Caractères:        {stats['nb_caracteres']}")
afficher(f"  Mots (total):      {stats['nb_mots']}")
afficher(f"  Mots uniques:      {stats['nb_mots_uniques']}")
afficher(f"  Phrases:           {stats['nb_phrases']}")
afficher(f"  Lignes:            {stats['nb_lignes']}")
afficher(f"  Longueur moy/mot:  {stats['longueur_moy_mots']} lettres")

richesse = arrondir(stats['nb_mots_uniques'] / stats['nb_mots'] * 100, 1)
afficher(f"  Richesse lexicale: {richesse}%")

afficher("\n🏆 Top 10 des mots les plus fréquents:")
mots_vides = {"le", "la", "les", "de", "du", "des", "un", "une",
              "et", "en", "au", "aux", "il", "est", "l", "d",
              "qui", "que", "avec", "dans", "sur", "par", "se",
              "sa", "son", "ses", "ce", "ou", "a", "s"}

top_filtres = [(m, n) pour m, n dans stats['top_mots'] si m non dans mots_vides]

pour i, (mot, count) dans enumerer(top_filtres[:10]):
    barre = "█" * count
    afficher(f"  {i+1:2d}. {mot:<20} {barre} ({count})")

afficher("\n🔤 Mots longs (> 10 lettres):")
mots_longs = trier(
    [m pour m dans stats['mots_uniques'] si longueur(m) > 10],
    key=longueur,
    reverse=Vrai
)
pour mot dans mots_longs[:8]:
    afficher(f"  • {mot} ({longueur(mot)} lettres)")

afficher("\n📏 Distribution des longueurs de mots:")
distribution = {}
pour mot dans stats['mots_uniques']:
    n = longueur(mot)
    distribution[n] = distribution.obtenir(n, 0) + 1

pour n dans trier(distribution.cles()):
    si n <= 15:
        barre = "▪" * distribution[n]
        afficher(f"  {n:2d} lettres: {barre} ({distribution[n]})")
