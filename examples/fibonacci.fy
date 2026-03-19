# fibonacci.fy — Suite de Fibonacci en Frython

déf fibonacci(n):
    """Calcule la suite de Fibonacci jusqu'à n."""
    si n <= 0:
        retourner []
    sinonsi n == 1:
        retourner [0]
    
    suite = [0, 1]
    tantque longueur(suite) < n:
        suivant = suite[-1] + suite[-2]
        suite.ajouter(suivant)
    
    retourner suite


# Calculer les 10 premiers nombres
nombres = fibonacci(10)
afficher("Suite de Fibonacci (10 premiers):")
afficher(nombres)

# Afficher avec enumerer
pour i, nombre dans enumerer(nombres):
    afficher(f"  F({i}) = {nombre}")

# Filtrer les pairs
pairs = liste(filtrer(lambda x: x % 2 == 0, nombres))
afficher(f"\nNombres pairs: {pairs}")

# Somme
afficher(f"Somme de la suite: {somme(nombres)}")
