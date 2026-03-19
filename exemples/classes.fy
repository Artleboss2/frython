# classes.fy — Programmation orientée objet en Frython

classe Animal:
    """Classe de base pour les animaux."""
    
    def __init__(soi, nom, age):
        soi.nom = nom
        soi.age = age
    
    déf parler(soi):
        retourner "..."
    
    déf __str__(soi):
        retourner f"{soi.nom} ({soi.age} ans)"
    
    déf anniversaire(soi):
        soi.age += 1
        afficher(f"🎂 Joyeux anniversaire {soi.nom}! Vous avez maintenant {soi.age} ans.")


classe Chien(Animal):
    """Un chien, bien sûr."""
    
    def __init__(soi, nom, age, race):
        super().__init__(nom, age)
        soi.race = race
        soi.tours = []
    
    déf parler(soi):
        retourner "Ouaf! 🐕"
    
    déf apprendre_tour(soi, tour):
        soi.tours.ajouter(tour)
        afficher(f"{soi.nom} a appris: {tour}!")
    
    déf montrer_tours(soi):
        si non soi.tours:
            afficher(f"{soi.nom} ne connaît aucun tour.")
            retourner
        afficher(f"Tours de {soi.nom}:")
        pour tour dans soi.tours:
            afficher(f"  ✓ {tour}")


classe Chat(Animal):
    """Un chat, évidemment supérieur."""
    
    def __init__(soi, nom, age, vies=9):
        super().__init__(nom, age)
        soi.vies = vies
    
    déf parler(soi):
        retourner "Miaou 🐈"
    
    déf perdre_vie(soi):
        si soi.vies > 0:
            soi.vies -= 1
            afficher(f"{soi.nom} a perdu une vie! Il en reste {soi.vies}.")
        sinon:
            afficher(f"{soi.nom} n'a plus de vies... 😿")


# Utilisation
rex = Chien("Rex", 3, "Berger Allemand")
afficher(rex)
afficher(rex.parler())

rex.apprendre_tour("s'asseoir")
rex.apprendre_tour("donner la patte")
rex.apprendre_tour("rouler")
rex.montrer_tours()

afficher()

whiskers = Chat("Whiskers", 5)
afficher(whiskers)
afficher(whiskers.parler())
whiskers.perdre_vie()
whiskers.perdre_vie()

afficher()

# Polymorphisme
animaux = [rex, whiskers, Chien("Buddy", 2, "Golden"), Chat("Félix", 8)]
afficher("Tous les animaux parlent:")
pour animal dans animaux:
    afficher(f"  {animal.nom}: {animal.parler()}")
