"""
Jeu de l'oie (simplifiée)
Auteur: Max

License: MIT
"""
from pprint import pprint
import random
import csv

# Question 1
def creer_plateau():
  regles = {
    "nombres_cases": 31,
    "defaut": (1, "oie"),
    "cases_speciales": {
      4: (0, "hotel"),
      5: (2, "pont"),
      10: (2, "pont"),
      15: (0, "puits"),
      20: (2, "prison"),
      25: (0, "labyrinthe"),
      26: (2, "pont"),
      29: (0, "mort")
    }
  }
  plateau = []
  for i in range(regles["nombres_cases"]):
    p = i + 1
    if p in regles["cases_speciales"].keys():
      #print(p, regles["cases_speciales"][p])
      plateau.append(regles["cases_speciales"][p])
    else:
      #print(p, regles["defaut"])
      plateau.append(regles["defaut"])

  return plateau

# Creer le plateau
plateau = creer_plateau()
pprint(plateau)

# Question 2
def deplacer_pion(plateau: list, pion: int):
  deplacement = random.randint(1, 4)

  case_type = plateau[pion][0]

  if case_type == 2:
    pion += deplacement * 2
  else:
    pion += deplacement

  return (pion, deplacement)

# Creer les pions
pion1 = -1
pion2 = -1

# Question 3
def lancer_partie(plateau: list, pion1: int, pion2: int):
  etapes = 0
  partie = []
  gagnants = 0

  while gagnants == 0:
    # Gestion pion 1
    pion1, deplacement1 = deplacer_pion(plateau, pion1)

    if pion1 >= 30:
      gagnants = 1

    # Gestion pion 2
    pion2, deplacement2 = deplacer_pion(plateau, pion2)

    if pion2 >= 30:
      gagnants = 2

    etapes += 1

    partie.append({
      "Etapes": etapes,
      "depPion1": deplacement1,
      "posPion1": pion1 + 1,
      "depPion2": deplacement2,
      "posPion2": pion2 + 1
    })

  return (partie, gagnants)

# Lancer une partie
partie, gagnants = lancer_partie(plateau, pion1, pion2)
pprint(partie)
print(f"Le ou les gagnants sont pion {gagnants}")

# Question 4
def simuler_parties(n: int):
  nb_etapes = []

  for i in range(n):
    partie, gagnants = lancer_partie(plateau, pion1, pion2)
    nb_etapes.append(partie[len(partie) - 1].get("Etapes"))

  etape_minimum = min(nb_etapes)
  etape_maximum = max(nb_etapes)
  etape_moyenne = sum(nb_etapes) / len(nb_etapes)

  return (etape_minimum, etape_maximum, etape_moyenne)

min, max, moy = simuler_parties(100000)
print(f"Minimum: {min}, Maximum: {max}, Moyenne: {moy}")

# Question 5:
def export_csv(table: list, nom_fichier, ordre: list):
  with open(nom_fichier, 'w', newline='') as fichier_CSV:
    dico_CSV = csv.DictWriter(fichier_CSV, fieldnames=ordre)
    dico_CSV.writeheader()
    #print(table)
    
    for dico in table:
      #print(dico)
      dico_CSV.writerow(dico)
    
  return None

fichier = "sortie.csv"
ordre = ["Etapes", "depPion1", "posPion1", "depPion2", "posPion2"]
export_csv(partie, fichier, ordre)
