# calculatrice.fy — Une calculatrice interactive en Frython

afficher("🧮 Calculatrice Frython")
afficher("=" * 30)
afficher("Opérations: +  -  *  /  **  %")
afficher("Tapez 'quitter' pour sortir.")
afficher()

tantque Vrai:
    essayer:
        entree = saisir(">>> ")
        
        si entree.minuscule() dans ("quitter", "q", "exit"):
            afficher("À bientôt! 👋")
            casser
        
        si entree.supprimer_espaces() == "":
            continuer
        
        resultat = eval(entree)
        afficher(f"  = {resultat}")
    
    sauf ZeroDivisionError:
        afficher("  ❌ Erreur: Division par zéro!")
    sauf SyntaxError:
        afficher("  ❌ Erreur: Expression invalide.")
    sauf Exception as e:
        afficher(f"  ❌ Erreur: {e}")
