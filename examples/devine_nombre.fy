# devine_nombre.fy — Jeu de devinettes en Frython

importer random

afficher("🎲 Jeu: Devine le nombre !")
afficher("=" * 35)

déf jouer():
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    max_tentatives = 7
    
    afficher(f"J'ai choisi un nombre entre 1 et 100.")
    afficher(f"Tu as {max_tentatives} tentatives. Bonne chance !")
    afficher()
    
    tantque tentatives < max_tentatives:
        restantes = max_tentatives - tentatives
        essayer:
            entree = saisir(f"Tentative {tentatives + 1}/{max_tentatives} → ")
            devine = entier(entree)
        sauf ValueError:
            afficher("  ⚠️  Entre un nombre entier valide!")
            continuer
        
        tentatives += 1
        
        si devine == nombre_secret:
            afficher()
            afficher(f"  🎉 BRAVO ! C'était bien {nombre_secret} !")
            afficher(f"  Trouvé en {tentatives} tentative(s).")
            si tentatives == 1:
                afficher("  🏆 Incroyable, du premier coup !")
            sinonsi tentatives <= 3:
                afficher("  🥇 Excellent score !")
            sinonsi tentatives <= 5:
                afficher("  🥈 Bon score !")
            sinon:
                afficher("  🥉 Ouf, juste à temps !")
            retourner
        sinonsi devine < nombre_secret:
            diff = nombre_secret - devine
            si diff > 25:
                afficher("  📈 Beaucoup trop petit !")
            sinonsi diff > 10:
                afficher("  📈 Trop petit!")
            sinon:
                afficher("  📈 Tout petit peu plus grand...")
        sinon:
            diff = devine - nombre_secret
            si diff > 25:
                afficher("  📉 Beaucoup trop grand !")
            sinonsi diff > 10:
                afficher("  📉 Trop grand!")
            sinon:
                afficher("  📉 Tout petit peu plus petit...")
    
    afficher()
    afficher(f"  💀 Perdu ! C'était {nombre_secret}.")


déf menu():
    tantque Vrai:
        jouer()
        afficher()
        rejouer = saisir("Rejouer ? (o/n) → ").minuscule()
        si rejouer != "o":
            afficher("Merci d'avoir joué ! 🎮")
            casser
        afficher()

menu()
