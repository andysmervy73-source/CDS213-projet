import csv

def charger_donnees(chemin):
    """"Lire le CSV et renvoie une liste de dictionnaires"""
    with open(chemin,newline="") as f:
        return list(csv.DictReader(f))
def prix_moyen(maisons):
    """Calcule le prix moyen des maisons."""
    prix = [float(m["prix"]) for m in maisons]
    return sum(prix) / len(prix)

def prix_par_m2(maisons):
    """Calculons le prix moyen au m2"""
    total = sum(float(m["prix"]) / float(m["surface_m2"]) for m in maisons)
    return total / len(maisons)

def prix_min(maisons):
    """Retourne le prix le plus bas."""
    return min(float(m["prix"]) for m in maisons)

def prix_max(maisons):
    """Retourne le prix le plus haut"""
    return max(float(m["prix"]) for m in maisons)
if __name__ == "__main__":
    try:
        maisons = charger_donnees("data/maisons.csv")
    except FileNotFoundError:
        print("Erreur : le fichier data/maisons.csv est introuvable.")
    else:
        print(f"Nombre de maisons : {len(maisons)}")
        print(f"Prix moyen : {prix_moyen(maisons):.0f}")
        print(f"Prix moyen au m2 : {prix_par_m2(maisons):.0f}")
        print(f"Prix minimum : {prix_min(maisons):.0f}")
        print(f"Prix maximum : {prix_max(maisons):.0f}")