# statistiques.fy — Calculs statistiques en Frython (sans bibliothèque externe)

déf moyenne(donnees):
    retourner somme(donnees) / longueur(donnees)

déf mediane(donnees):
    tries = trier(donnees)
    n = longueur(tries)
    milieu = n // 2
    si n % 2 == 0:
        retourner (tries[milieu - 1] + tries[milieu]) / 2
    retourner tries[milieu]

déf mode(donnees):
    frequences = {}
    pour val dans donnees:
        frequences[val] = frequences.obtenir(val, 0) + 1
    max_freq = maximum(frequences.valeurs())
    modes = [k pour k, v dans frequences.elements() si v == max_freq]
    retourner trier(modes)

déf variance(donnees):
    moy = moyenne(donnees)
    retourner somme((x - moy) ** 2 pour x dans donnees) / longueur(donnees)

déf ecart_type(donnees):
    retourner variance(donnees) ** 0.5

déf quartiles(donnees):
    tries = trier(donnees)
    n = longueur(tries)
    q1 = mediane(tries[:n // 2])
    q2 = mediane(tries)
    q3 = mediane(tries[(n + 1) // 2:])
    retourner q1, q2, q3

déf etendue(donnees):
    retourner maximum(donnees) - minimum(donnees)

déf normaliser(donnees):
    """Normalise les données entre 0 et 1."""
    mini = minimum(donnees)
    maxi = maximum(donnees)
    si maxi == mini:
        retourner [0.0 pour _ dans donnees]
    retourner [(x - mini) / (maxi - mini) pour x dans donnees]

déf histogramme(donnees, barres=10):
    """Affiche un histogramme ASCII."""
    mini = minimum(donnees)
    maxi = maximum(donnees)
    largeur = (maxi - mini) / barres
    
    compteurs = [0] * barres
    pour val dans donnees:
        idx = entier((val - mini) / largeur)
        si idx == barres:
            idx = barres - 1
        compteurs[idx] += 1
    
    max_count = maximum(compteurs)
    hauteur = 15
    
    afficher()
    pour ligne dans intervalle(hauteur, 0, -1):
        seuil = (ligne / hauteur) * max_count
        rangee = ""
        pour count dans compteurs:
            si count >= seuil:
                rangee += "█ "
            sinon:
                rangee += "  "
        afficher(f"  {rangee}")
    afficher("  " + "──" * barres)


# ── Jeu de données ──────────────────────────────────
notes = [12, 15, 8, 19, 11, 14, 16, 9, 13, 17, 
         10, 18, 12, 14, 15, 11, 16, 13, 7, 20,
         12, 15, 14, 13, 16, 11, 18, 9, 15, 12]

afficher("📊 Analyse statistique en Frython")
afficher("=" * 40)
afficher(f"Données ({longueur(notes)} valeurs): {notes[:10]}...")

afficher()
afficher("📈 Statistiques descriptives:")
afficher(f"  Minimum:      {minimum(notes)}")
afficher(f"  Maximum:      {maximum(notes)}")
afficher(f"  Étendue:      {etendue(notes)}")
afficher(f"  Moyenne:      {arrondir(moyenne(notes), 2)}")
afficher(f"  Médiane:      {mediane(notes)}")
afficher(f"  Mode(s):      {mode(notes)}")
afficher(f"  Variance:     {arrondir(variance(notes), 2)}")
afficher(f"  Écart-type:   {arrondir(ecart_type(notes), 2)}")

q1, q2, q3 = quartiles(notes)
afficher(f"  Q1:           {q1}")
afficher(f"  Q2 (médiane): {q2}")
afficher(f"  Q3:           {q3}")
afficher(f"  IQR:          {q3 - q1}")

afficher()
afficher("📉 Histogramme des notes:")
histogramme(notes, barres=13)

afficher()
afficher("🎓 Répartition par mention:")
mentions = {"Insuffisant (< 10)": 0, "Passable (10-11)": 0,
            "Assez bien (12-13)": 0, "Bien (14-15)": 0, "Très bien (16+)": 0}
pour n dans notes:
    si n < 10:
        mentions["Insuffisant (< 10)"] += 1
    sinonsi n < 12:
        mentions["Passable (10-11)"] += 1
    sinonsi n < 14:
        mentions["Assez bien (12-13)"] += 1
    sinonsi n < 16:
        mentions["Bien (14-15)"] += 1
    sinon:
        mentions["Très bien (16+)"] += 1

pour mention, count dans mentions.elements():
    barre = "█" * count
    afficher(f"  {mention:<25} {barre} ({count})")
