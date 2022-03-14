import csv

def ecriture():
    with open("sorties.csv", "w", newline="") as fichier:
        fieldnames = ["nom", "prenom"]
        writer = csv.DictWriter(fichier, fieldnames)

        writer.writeheader()
        writer.writerow({"prenom": "Lucie", "nom": "Lafitte"})
        writer.writerow({"prenom": "Lucien", "nom": "Lafargue"})
        writer.writerow({"prenom": "Max", "nom": "Charrier"})
        writer.writer
    
    return None

ecriture()
