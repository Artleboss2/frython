
importer random
importer time

déf tri_bulles(lst):
    """Tri à bulles — O(n²)"""
    arr = liste(lst)
    n = longueur(arr)
    pour i dans intervalle(n):
        pour j dans intervalle(0, n - i - 1):
            si arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    retourner arr

déf tri_insertion(lst):
    """Tri par insertion — O(n²)"""
    arr = liste(lst)
    pour i dans intervalle(1, longueur(arr)):
        cle = arr[i]
        j = i - 1
        tantque j >= 0 et arr[j] > cle:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cle
    retourner arr

déf tri_selection(lst):
    """Tri par sélection — O(n²)"""
    arr = liste(lst)
    n = longueur(arr)
    pour i dans intervalle(n):
        idx_min = i
        pour j dans intervalle(i + 1, n):
            si arr[j] < arr[idx_min]:
                idx_min = j
        arr[i], arr[idx_min] = arr[idx_min], arr[i]
    retourner arr

déf tri_fusion(lst):
    """Tri fusion — O(n log n)"""
    si longueur(lst) <= 1:
        retourner lst
    milieu = longueur(lst) // 2
    gauche = tri_fusion(lst[:milieu])
    droite = tri_fusion(lst[milieu:])
    retourner fusionner(gauche, droite)

déf fusionner(gauche, droite):
    resultat = []
    i = j = 0
    tantque i < longueur(gauche) et j < longueur(droite):
        si gauche[i] <= droite[j]:
            resultat.ajouter(gauche[i])
            i += 1
        sinon:
            resultat.ajouter(droite[j])
            j += 1
    resultat.etendre(gauche[i:])
    resultat.etendre(droite[j:])
    retourner resultat

déf tri_rapide(lst):
    """Tri rapide — O(n log n) en moyenne"""
    si longueur(lst) <= 1:
        retourner lst
    pivot = lst[longueur(lst) // 2]
    gauche = [x pour x dans lst si x < pivot]
    milieu = [x pour x dans lst si x == pivot]
    droite = [x pour x dans lst si x > pivot]
    retourner tri_rapide(gauche) + milieu + tri_rapide(droite)

déf mesurer(nom, fonction, donnees):
    debut = time.time()
    resultat = fonction(donnees)
    duree = (time.time() - debut) * 1000
    afficher(f"  {nom:<20} → {duree:.3f} ms")
    retourner resultat

# Générer des données aléatoires
taille = 500
donnees = [random.randint(1, 1000) pour _ dans intervalle(taille)]

afficher("🔢 Algorithmes de tri en Frython")
afficher("=" * 40)
afficher(f"Données: {taille} nombres aléatoires")
afficher(f"Aperçu: {donnees[:8]}...")
afficher()
afficher("⏱️  Performances:")

mesurer("Tri à bulles", tri_bulles, donnees)
mesurer("Tri par insertion", tri_insertion, donnees)
mesurer("Tri par sélection", tri_selection, donnees)
mesurer("Tri fusion", tri_fusion, donnees)
mesurer("Tri rapide", tri_rapide, donnees)
mesurer("Tri Python (natif)", trier, donnees)

afficher()
resultat = tri_rapide(donnees)
afficher(f"Résultat (10 premiers): {resultat[:10]}")
afficher(f"Résultat (10 derniers): {resultat[-10:]}")
afficher(f"Correctement trié: {resultat == trier(donnees)}")
