# art_ascii.fy — Art ASCII et fractales en Frython 🎨

afficher("🎨 Art ASCII — Frython")
afficher("=" * 50)

# ── Triangle de Pascal ───────────────────────────────
afficher("\n📐 Triangle de Pascal:")

déf triangle_pascal(n):
    triangle = [[1]]
    pour i dans intervalle(1, n):
        ligne = [1]
        pour j dans intervalle(1, i):
            ligne.ajouter(triangle[i-1][j-1] + triangle[i-1][j])
        ligne.ajouter(1)
        triangle.ajouter(ligne)
    retourner triangle

lignes = triangle_pascal(10)
largeur_max = longueur(" ".join(chaine(n) pour n dans lignes[-1]))
pour ligne in lignes:
    contenu = " ".join(f"{n:3d}" pour n dans ligne)
    afficher(contenu.center(largeur_max + 20))

# ── Ensemble de Mandelbrot (ASCII) ──────────────────
afficher("\n🌀 Ensemble de Mandelbrot:")

déf mandelbrot(c, max_iter=50):
    z = 0
    pour i dans intervalle(max_iter):
        si absolu(z) > 2:
            retourner i
        z = z * z + c
    retourner max_iter

largeur, hauteur = 60, 25
x_min, x_max = -2.5, 1.0
y_min, y_max = -1.2, 1.2
caracteres = " .:-=+*#%@█"

pour ligne dans intervalle(hauteur):
    rangee = ""
    pour col dans intervalle(largeur):
        x = x_min + (x_max - x_min) * col / largeur
        y = y_min + (y_max - y_min) * ligne / hauteur
        c = complex(x, y)
        m = mandelbrot(c)
        idx = entier(m / 50 * (longueur(caracteres) - 1))
        rangee += caracteres[idx]
    afficher(rangee)

# ── Flocon de Koch (ASCII simplifié) ────────────────
afficher("\n❄️  Flocon de neige (simplifié):")

déf dessiner_flocon(taille):
    pour ligne dans intervalle(taille, 0, -1):
        espaces = " " * (taille - ligne)
        etoiles = "*" * (2 * ligne - 1)
        afficher(espaces + etoiles)
    pour ligne dans intervalle(2, taille + 1):
        espaces = " " * (taille - ligne)
        etoiles = "*" * (2 * ligne - 1)
        afficher(espaces + etoiles)

dessiner_flocon(8)

# ── Spirale numérique ───────────────────────────────
afficher("\n🌀 Spirale numérique:")

déf spirale(n):
    grille = [[0] * n pour _ dans intervalle(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dr, dc = 0, 0
    r, c = 0, 0
    
    pour num dans intervalle(1, n * n + 1):
        grille[r][c] = num
        nr, nc = r + directions[dr][0], c + directions[dc][1]
        si nr < 0 ou nr >= n ou nc < 0 ou nc >= n ou grille[nr][nc] != 0:
            dr = (dr + 1) % 4
        r += directions[dr][0]
        c += directions[dr][1]
    
    retourner grille

grille_spirale = spirale(7)
pour ligne dans grille_spirale:
    afficher("  " + " ".join(f"{n:3d}" pour n dans ligne))

# ── Table de multiplication colorée ─────────────────
afficher("\n✖️  Table de multiplication (1-9):")
afficher("    " + "  ".join(f"{i:3d}" pour i dans intervalle(1, 10)))
afficher("    " + "─" * 30)
pour i dans intervalle(1, 10):
    ligne = f"{i:2d} │"
    pour j dans intervalle(1, 10):
        ligne += f"{i*j:4d}"
    afficher(ligne)
