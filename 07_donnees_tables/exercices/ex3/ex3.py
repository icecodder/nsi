import csv
from pprint import pprint
from copy import deepcopy

# Q1
def lecture(fichier, delimiteur):
    with open(fichier, newline="") as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=delimiteur)
        return [dict(ligne) for ligne in reader]

# Q2
fichier_etudiants = "etudiants.csv"
table_etudiants = lecture(fichier_etudiants, ";")
pprint(table_etudiants, indent=4, width=200)

fichier_matieres = "matieres.csv"
table_matieres = lecture(fichier_matieres, ";")
pprint(table_matieres, indent=4, width=40)

fichier_notes = "notes.csv"
table_notes = lecture(fichier_notes, ";")
pprint(table_notes, indent=4, width=200)

# Q3
def jointure(table1, table2, cle1, cle2=None):
    if cle2 is None:
        cle2 = cle1

    table3 = []
    for ligne1 in table1:
        for ligne2 in table2:
            if ligne1[cle1] == ligne2[cle2]:
                ligne3 = deepcopy(ligne1)
                for cle in ligne2:
                    if cle != cle2:
                        ligne3[cle] = ligne2[cle]
                table3.append(ligne3)
    
    return table3

# Q4
table_fusion1 = jointure(table_etudiants, table_notes, "IdEtu")
#pprint(table_fusion1, indent=4, width=200)

# Q5
table_fusion2 = jointure(table_fusion1, table_matieres, "IdMat")
#pprint(table_fusion2, indent=4, width=200)

# Q6
def export(table, fichier, ordre):
    with open(fichier, "w", newline="") as fichier_csv:
        writer = csv.DictWriter(fichier_csv, fieldnames=ordre)
        writer.writeheader()
        for ligne in table:
            writer.writerow(ligne)
    return None

# Q7
fichier = "table_fusion.csv"
ordre = ["IdEtu", "IdMat", "Nom", "Prenom", "Age", "Sexe", "Libelle", "Note", "Coeff"]
export(table_fusion2, fichier, ordre)
