# rpg.fy — Mini jeu de rôle en Frython ⚔️

importer random

afficher("⚔️  Frython Quest — Mini RPG")
afficher("=" * 40)

classe Personnage:
    déf __init__(soi, nom, classe_perso):
        soi.nom = nom
        soi.classe_perso = classe_perso
        configs = {
            "guerrier":  {"pv": 120, "attaque": 15, "defense": 10, "vitesse": 8},
            "mage":      {"pv": 70,  "attaque": 25, "defense": 4,  "vitesse": 12},
            "voleur":    {"pv": 90,  "attaque": 18, "defense": 6,  "vitesse": 18},
        }
        cfg = configs.obtenir(classe_perso, configs["guerrier"])
        soi.pv_max = cfg["pv"]
        soi.pv = cfg["pv"]
        soi.attaque = cfg["attaque"]
        soi.defense = cfg["defense"]
        soi.vitesse = cfg["vitesse"]
        soi.niveau = 1
        soi.experience = 0
        soi.or_pieces = 50
        soi.inventaire = []

    déf est_vivant(soi):
        retourner soi.pv > 0

    déf attaquer(soi, cible):
        degats_base = random.randint(soi.attaque - 3, soi.attaque + 5)
        degats = maximum(1, degats_base - cible.defense // 2)
        critique = random.random() < 0.15
        si critique:
            degats = entier(degats * 1.8)
        cible.pv = maximum(0, cible.pv - degats)
        retourner degats, critique

    déf soigner(soi, quantite):
        soin = minimum(quantite, soi.pv_max - soi.pv)
        soi.pv += soin
        retourner soin

    déf gagner_xp(soi, xp):
        soi.experience += xp
        seuil = soi.niveau * 100
        si soi.experience >= seuil:
            soi.experience -= seuil
            soi.niveau += 1
            soi.pv_max += 15
            soi.pv = soi.pv_max
            soi.attaque += 3
            soi.defense += 1
            retourner Vrai
        retourner Faux

    déf statut(soi):
        barre_pv = "█" * (soi.pv * 20 // soi.pv_max) + "░" * (20 - soi.pv * 20 // soi.pv_max)
        afficher(f"  {soi.nom} (Niv.{soi.niveau} {soi.classe_perso.capitaliser()})")
        afficher(f"  PV: [{barre_pv}] {soi.pv}/{soi.pv_max}")
        afficher(f"  ATK:{soi.attaque} DEF:{soi.defense} VIT:{soi.vitesse} OR:{soi.or_pieces}🪙")


classe Monstre:
    déf __init__(soi, nom, pv, attaque, defense, xp, or_val):
        soi.nom = nom
        soi.pv = pv
        soi.pv_max = pv
        soi.attaque = attaque
        soi.defense = defense
        soi.xp = xp
        soi.or_val = or_val

    déf est_vivant(soi):
        retourner soi.pv > 0

    déf attaquer(soi, cible):
        degats = maximum(1, random.randint(soi.attaque - 2, soi.attaque + 3) - cible.defense // 3)
        cible.pv = maximum(0, cible.pv - degats)
        retourner degats


MONSTRES = [
    lambda: Monstre("Gobelin",    30,  8,  2, 25,  10),
    lambda: Monstre("Squelette",  45, 12,  4, 40,  20),
    lambda: Monstre("Orc",        70, 16,  7, 65,  35),
    lambda: Monstre("Troll",     100, 20, 10, 90,  50),
    lambda: Monstre("Dragon",    200, 30, 15, 200, 150),
]


déf combat(joueur, monstre):
    afficher(f"\n  ⚔️  Un {monstre.nom} apparaît ! (PV: {monstre.pv})")
    
    tantque joueur.est_vivant() et monstre.est_vivant():
        afficher(f"\n  Vos PV: {joueur.pv}/{joueur.pv_max}")
        afficher(f"  {monstre.nom}: {monstre.pv}/{monstre.pv_max} PV")
        afficher("  [1] Attaquer  [2] Potion  [3] Fuir")
        
        choix = saisir("  Choix → ")
        
        si choix == "1":
            degats, critique = joueur.attaquer(monstre)
            msg = "💥 CRITIQUE!" si critique sinon "⚔️"
            afficher(f"  {msg} Vous infligez {degats} dégâts!")
            
            si monstre.est_vivant():
                degats_recus = monstre.attaquer(joueur)
                afficher(f"  💢 {monstre.nom} vous inflige {degats_recus} dégâts!")
        
        sinonsi choix == "2":
            potions = [o pour o dans joueur.inventaire si o == "potion"]
            si non potions:
                afficher("  ❌ Aucune potion!")
                continuer
            joueur.inventaire.retirer("potion")
            soin = joueur.soigner(40)
            afficher(f"  💚 Vous récupérez {soin} PV!")
            degats_recus = monstre.attaquer(joueur)
            afficher(f"  💢 {monstre.nom} vous inflige {degats_recus} dégâts!")
        
        sinonsi choix == "3":
            si random.random() < 0.5:
                afficher("  🏃 Vous fuyez!")
                retourner "fuite"
            sinon:
                afficher("  ❌ Impossible de fuir!")
                degats_recus = monstre.attaquer(joueur)
                afficher(f"  💢 {monstre.nom} vous inflige {degats_recus} dégâts!")
    
    si joueur.est_vivant():
        xp = monstre.xp
        or_g = monstre.or_val + random.randint(-5, 10)
        joueur.or_pieces += or_g
        monte = joueur.gagner_xp(xp)
        afficher(f"\n  ✅ Victoire! +{xp} XP, +{or_g} 🪙")
        si monte:
            afficher(f"  🎉 NIVEAU {joueur.niveau} ! Vos stats augmentent!")
        retourner "victoire"
    sinon:
        afficher("\n  💀 Vous êtes mort... Game Over.")
        retourner "mort"


déf boutique(joueur):
    afficher(f"\n  🏪 Boutique — Vos pièces d'or: {joueur.or_pieces} 🪙")
    afficher("  [1] Potion de soin (20 🪙)  [2] Retour")
    choix = saisir("  Choix → ")
    si choix == "1":
        si joueur.or_pieces >= 20:
            joueur.or_pieces -= 20
            joueur.inventaire.ajouter("potion")
            afficher("  ✅ Potion achetée!")
        sinon:
            afficher("  ❌ Pas assez d'or!")


# ── Démarrage ──────────────────────────────────────
nom = saisir("  Ton nom de héros: ")
afficher("  Choisis ta classe:")
afficher("  [1] Guerrier (robuste)  [2] Mage (puissant)  [3] Voleur (rapide)")
choix_classe = saisir("  Choix → ")
classes = {"1": "guerrier", "2": "mage", "3": "voleur"}
classe = classes.obtenir(choix_classe, "guerrier")

joueur = Personnage(nom, classe)
afficher(f"\n  Bienvenue, {nom} le {classe.capitaliser()} !")
joueur.statut()

monstre_idx = 0
combats_gagnes = 0

tantque joueur.est_vivant() et monstre_idx < longueur(MONSTRES):
    afficher(f"\n  Zone {monstre_idx + 1}/5")
    afficher("  [1] Combattre  [2] Boutique  [3] Statut  [4] Quitter")
    action = saisir("  Action → ")
    
    si action == "1":
        monstre = MONSTRES[monstre_idx]()
        resultat = combat(joueur, monstre)
        si resultat == "victoire":
            combats_gagnes += 1
            monstre_idx += 1
        sinonsi resultat == "mort":
            casser
    sinonsi action == "2":
        boutique(joueur)
    sinonsi action == "3":
        joueur.statut()
    sinonsi action == "4":
        afficher("  À bientôt, aventurier!")
        casser

si monstre_idx >= longueur(MONSTRES) et joueur.est_vivant():
    afficher("\n  🏆 FÉLICITATIONS ! Vous avez vaincu tous les monstres !")
    afficher(f"  {nom} est le héros de Frython Quest !")

afficher(f"\n  📊 Résultats: {combats_gagnes} combats gagnés | Niveau {joueur.niveau}")
