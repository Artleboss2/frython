# pendu.fy — Le jeu du pendu en Frython 🪢

importer random

MOTS = [
    "python", "frython", "programmation", "algorithme", "ordinateur",
    "variable", "fonction", "boucle", "classe", "heritage",
    "dictionnaire", "liste", "tuple", "ensemble", "lambda",
    "recursion", "iteration", "compilateur", "interpreteur", "syntaxe",
    "bibliotheque", "framework", "interface", "debugger", "terminal"
]

PENDU = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]

déf jouer_pendu():
    mot = random.choice(MOTS)
    lettres_trouvees = ensemble()
    lettres_ratees = ensemble()
    max_erreurs = longueur(PENDU) - 1
    
    tantque Vrai:
        erreurs = longueur(lettres_ratees)
        afficher(PENDU[erreurs])
        
        # Afficher le mot masqué
        mot_affiche = " ".join(
            l si l dans lettres_trouvees sinon "_"
            pour l dans mot
        )
        afficher(f"\n  Mot: {mot_affiche}")
        afficher(f"  Lettres ratées ({erreurs}/{max_erreurs}): {' '.join(trier(lettres_ratees)) si lettres_ratees sinon '—'}")
        
        # Vérifier victoire
        si tout(l dans lettres_trouvees pour l dans mot):
            afficher(f"\n  🎉 BRAVO ! Le mot était bien '{mot.majuscule()}' !")
            retourner Vrai
        
        # Vérifier défaite
        si erreurs >= max_erreurs:
            afficher(f"\n  💀 Perdu ! Le mot était '{mot.majuscule()}'.")
            retourner Faux
        
        # Saisir une lettre
        essayer:
            lettre = saisir("\n  Entre une lettre: ").minuscule().supprimer_espaces()
        sauf (EOFError, KeyboardInterrupt):
            casser
        
        si longueur(lettre) != 1 ou non lettre.est_alpha():
            afficher("  ⚠️  Entre une seule lettre!")
            continuer
        
        si lettre dans lettres_trouvees ou lettre dans lettres_ratees:
            afficher(f"  ⚠️  Tu as déjà essayé '{lettre}'!")
            continuer
        
        si lettre dans mot:
            lettres_trouvees.ajouter(lettre)
            occurrences = mot.compter(lettre)
            afficher(f"  ✅ Bien ! '{lettre}' est dans le mot ({occurrences}x).")
        sinon:
            lettres_ratees.ajouter(lettre)
            afficher(f"  ❌ Raté ! '{lettre}' n'est pas dans le mot.")


# utiliser tout() de Python directement
tout = all

afficher("🪢 Le Pendu — Frython Edition")
afficher("=" * 35)

victoires = 0
parties = 0

tantque Vrai:
    parties += 1
    si jouer_pendu():
        victoires += 1
    
    afficher(f"\n  📊 Score: {victoires}/{parties}")
    afficher()
    encore = saisir("Rejouer ? (o/n) → ").minuscule()
    si encore != "o":
        afficher("\nMerci d'avoir joué ! 🎮")
        casser
