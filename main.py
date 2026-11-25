import csv

def charger_donnees(chemin):
    """"Lire le CSV et renvoie une liste de dictionnaires"""
    with open(chemin,newline="") as f:
        return list(csv.DictReader(f))
def prix_moyen(maisons):
    """Calcule le prix moyen des maisons."""
    prix = [float(m["prix"]) for m in maisons]
    return sum(prix) / len(prix)

if __name__ == "__main__":
    maisons = charger_donnees("data/maisons.csv")
    print(f"Nombre de maisons : {len(maisons)}")
    print(f"Prix moyen : {prix_moyen(maisons):.0f}")