# todo.fy — Gestionnaire de tâches en Frython

afficher("📝 Gestionnaire de tâches Frython")
afficher("=" * 40)

taches = []

déf afficher_taches():
    si non taches:
        afficher("  (aucune tâche pour l'instant)")
        retourner
    afficher()
    pour i, tache dans enumerer(taches):
        statut = "✅" si tache["faite"] sinon "⬜"
        afficher(f"  {i + 1}. {statut} {tache['titre']}")
    afficher()

déf ajouter_tache(titre):
    taches.ajouter({"titre": titre, "faite": Faux})
    afficher(f"  ✅ Tâche ajoutée: '{titre}'")

déf terminer_tache(numero):
    si numero < 1 ou numero > longueur(taches):
        afficher("  ❌ Numéro invalide.")
        retourner
    tache = taches[numero - 1]
    si tache["faite"]:
        afficher(f"  ⚠️  '{tache['titre']}' est déjà terminée.")
    sinon:
        tache["faite"] = Vrai
        afficher(f"  🎉 '{tache['titre']}' marquée comme terminée!")

déf supprimer_tache(numero):
    si numero < 1 ou numero > longueur(taches):
        afficher("  ❌ Numéro invalide.")
        retourner
    titre = taches[numero - 1]["titre"]
    taches.extraire(numero - 1)
    afficher(f"  🗑️  '{titre}' supprimée.")

déf stats():
    total = longueur(taches)
    faites = somme(1 pour t dans taches si t["faite"])
    restantes = total - faites
    afficher(f"  📊 Total: {total} | ✅ Faites: {faites} | ⬜ Restantes: {restantes}")

afficher("\nCommandes: ajouter, terminer, supprimer, liste, stats, quitter")

tantque Vrai:
    afficher()
    commande = saisir("🐓 > ").minuscule().supprimer_espaces()
    
    si commande == "quitter":
        afficher("À bientôt! 👋")
        casser
    sinonsi commande == "liste":
        afficher_taches()
    sinonsi commande == "stats":
        stats()
    sinonsi commande.commencer_par("ajouter "):
        titre = commande[8:].supprimer_espaces()
        si titre:
            ajouter_tache(titre)
        sinon:
            afficher("  ⚠️  Donne un titre à la tâche!")
    sinonsi commande.commencer_par("terminer "):
        essayer:
            num = entier(commande[9:])
            terminer_tache(num)
        sauf ValueError:
            afficher("  ❌ Entre un numéro valide.")
    sinonsi commande.commencer_par("supprimer "):
        essayer:
            num = entier(commande[10:])
            supprimer_tache(num)
        sauf ValueError:
            afficher("  ❌ Entre un numéro valide.")
    sinon:
        afficher("  ❓ Commande inconnue. Essaie: ajouter, terminer, supprimer, liste, stats, quitter")
