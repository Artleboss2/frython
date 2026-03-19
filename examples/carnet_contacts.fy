# carnet_contacts.fy — Carnet de contacts en Frython

afficher("📒 Carnet de contacts Frython")
afficher("=" * 40)

contacts = {}

déf ajouter_contact(nom, telephone, email=""):
    contacts[nom.minuscule()] = {
        "nom": nom,
        "telephone": telephone,
        "email": email
    }
    afficher(f"  ✅ Contact '{nom}' ajouté!")

déf chercher_contact(recherche):
    resultats = [
        c pour c dans contacts.valeurs()
        si recherche.minuscule() dans c["nom"].minuscule()
    ]
    si non resultats:
        afficher(f"  ❌ Aucun contact trouvé pour '{recherche}'.")
        retourner
    afficher(f"  🔍 {longueur(resultats)} résultat(s):")
    pour c dans resultats:
        afficher_contact(c)

déf afficher_contact(c):
    afficher(f"  ┌─ {c['nom']}")
    afficher(f"  │  📱 {c['telephone']}")
    si c["email"]:
        afficher(f"  │  📧 {c['email']}")
    afficher(f"  └─────────────")

déf lister_contacts():
    si non contacts:
        afficher("  (carnet vide)")
        retourner
    afficher(f"  📋 {longueur(contacts)} contact(s):")
    pour c dans trier(contacts.valeurs(), key=lambda x: x["nom"]):
        afficher(f"  • {c['nom']} — {c['telephone']}")

déf supprimer_contact(nom):
    cle = nom.minuscule()
    si cle dans contacts:
        del contacts[cle]
        afficher(f"  🗑️  '{nom}' supprimé.")
    sinon:
        afficher(f"  ❌ '{nom}' introuvable.")

# Pré-remplir avec quelques contacts
ajouter_contact("Alice Martin", "06 12 34 56 78", "alice@exemple.fr")
ajouter_contact("Bob Dupont", "07 98 76 54 32")
ajouter_contact("Claire Petit", "06 11 22 33 44", "claire@exemple.fr")
ajouter_contact("David Bernard", "07 55 66 77 88", "david@exemple.fr")
ajouter_contact("Emma Leroy", "06 99 88 77 66")

afficher()
afficher("Commandes: liste, chercher, ajouter, supprimer, quitter")

tantque Vrai:
    afficher()
    commande = saisir("📒 > ").supprimer_espaces()

    si commande.minuscule() == "quitter":
        afficher("Au revoir! 👋")
        casser
    sinonsi commande.minuscule() == "liste":
        lister_contacts()
    sinonsi commande.minuscule().commencer_par("chercher "):
        chercher_contact(commande[9:])
    sinonsi commande.minuscule().commencer_par("supprimer "):
        supprimer_contact(commande[10:])
    sinonsi commande.minuscule() == "ajouter":
        nom = saisir("  Nom: ")
        tel = saisir("  Téléphone: ")
        email = saisir("  Email (optionnel): ")
        ajouter_contact(nom, tel, email)
    sinon:
        afficher("  ❓ Commande inconnue.")
