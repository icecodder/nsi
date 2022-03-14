import csv

def lecture():
    with open("villes_virgule.csv", newline="") as fichier:
        lecteur = csv.DictReader(fichier)
        tab = [dict(ligne) for ligne in lecteur]

        for ligne in tab[:5]:
            print(ligne)

lecture()

def compteur(nom_fichier):
    with open(nom_fichier, newline="") as fichier:
        lecteur = csv.DictReader(fichier)
        tab = [dict(ligne) for ligne in lecteur]
    return len(tab)

print(compteur("villes_virgule.csv"))
