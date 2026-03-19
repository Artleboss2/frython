# bonjour_monde.fy — Le classique Frython
# Votre premier programme en Frython!

afficher("Bonjour le monde! 🐓")
afficher("Bienvenue dans Frython!")

# Variables
prenom = "Marie"
age = 25
taille = 1.68

afficher(f"Je m'appelle {prenom}, j'ai {age} ans et je mesure {taille}m.")

# Condition simple
si age >= 18:
    afficher("Vous êtes majeur(e).")
sinon:
    afficher("Vous êtes mineur(e).")
