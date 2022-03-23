import csv
from pprint import pprint

def lecture(fichier, delimiteur):
    with open(fichier, newline="") as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=delimiteur)
        return [dict(ligne) for ligne in reader]

fichier = "velib-emplacement-des-stations.csv"
table = lecture(fichier, ";")

for ligne in table:
    #ligne["Identifiant_station"] = int(ligne["Identifiant_station"])
    ligne["Capacite_station"] = int(ligne["Capacite_station"])
    ligne["Latitude"] = float(ligne["Coordonnees"].split(",")[0])
    ligne["Longitude"] = float(ligne["Coordonnees"].split(",")[1])

pprint(table[:2])

# Q5
def select(table, critere):
    return [ligne for ligne in table if eval(critere)]

# Q6
print(len(select(table, "ligne['Capacite_station'] == 0")))

# Q7
# SELECT Capacite_station FROM table WHERE Capacite_station = 0

# Q8
print(len(select(table, "ligne['Capacite_station'] >= 60")))

# Q9
# SELECT Capacite_station FROM table WHERE Capacite_station >= 60

# Q10
print(len(select(table, "ligne['Capacite_station'] >= 70 and ligne['Capacite_station'] <= 75")))

# Q11
# SELECT Capacite_station FROM table WHERE Capacite_station >= 70 AND Capacite_station <= 75

# Q12
def projection(table, liste_attributs):
    return [{cle:ligne[cle] for cle in ligne if cle in liste_attributs} for ligne in table]

# Q13
table_projection = projection(table, ["Nom_station", "Capacite_station"])
pprint(table_projection[:3])

# Q14
def export(table, fichier, ordre):
    with open(fichier, "w", newline="") as fichier_csv:
        writer = csv.DictWriter(fichier_csv, fieldnames=ordre)
        writer.writeheader()
        for ligne in table:
            writer.writerow(ligne)
    return None

# Q15
fichier = "table_projection.csv"
ordre = ["Nom_station", "Capacite_station"]
export(table_projection, fichier, ordre)

# Q16 - Vérificaion avec libreoffice

# Q17
def tri_colonne(table, attribut, decroissant=True):
    def critere(ligne):
        return ligne[attribut]
    return sorted(table, key=critere, reverse=decroissant)

# Q18
table_triee = tri_colonne(table_projection, "Capacite_station", True)
#pprint(table_triee)

fichier = "table_triee.csv"
ordre = ["Nom_station", "Capacite_station"]
export(table_triee, fichier, ordre)

# Q19 - Vérification avec libreoffice
