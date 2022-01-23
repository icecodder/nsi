"""
Jeu de l'oie (simplifiée):
  - on avance un dé à 4 faces
  - les cases numérotées de 1 à 30
  - une case avec 0: retour à la case départ
  - une case avec 1: sans effet
  - une case avec 2: double le déplacement

Auteur: Max

License: MIT
"""
from pprint import pprint
import random
import csv
from turtle import color
import matplotlib.pyplot as plt

def creer_plateau():
  regles = {
    "nombres_cases": 30,
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
    p = i + 1 # position de l'oie : i de 0 à 29, p de 1 à 30
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

def deplacer_pion(plateau: list, pion: int):
  deplacement = random.randint(1, 4)

  pion += deplacement

  if pion <= 29:
    if plateau[pion][0] == 0:
      pion = 0
    elif plateau[pion][0] == 2:
      pion += deplacement
  
  if pion > 29:
    pion = 29 - (pion - 29)

  return (pion, deplacement)

# Creer les pions
pion1 = -1
pion2 = -1

# Déplacer les pions
pion1, deplacement1 = deplacer_pion(plateau, pion1)
pion2, deplacement2 = deplacer_pion(plateau, pion2)
print(pion1, pion2)

def lancer_partie(plateau: list, pion1: int, pion2: int):
  etape = 1
  partie = []
  gagnants = []

  while pion1 != 29 and pion2 != 29:
    # Déplacer pion 1
    pion1, deplacement1 = deplacer_pion(plateau, pion1)

    if pion1 == 29:
      gagnants.append("pion 1")

    # Déplacer pion 2
    pion2, deplacement2 = deplacer_pion(plateau, pion2)

    if pion2 == 29:
      gagnants.append("pion 2")

    # Enregister les déplacements
    partie.append({
      "Etapes": etape,
      "depPion1": deplacement1,
      "posPion1": pion1 + 1, # 0<= pion <= 29 mais affichage de 1 à 30
      "depPion2": deplacement2,
      "posPion2": pion2 + 1 # 0<= pion <= 29 mais affichage de 1 à 30
    })

    # Passer à l'étape suivante
    etape += 1

  return (partie, gagnants)

# Lancer une partie
partie, gagnants = lancer_partie(plateau, pion1, pion2)
pprint(partie)
print(f"Le ou les gagnants sont pion {gagnants} en {len(partie)} étapes.")

def simuler_parties(n: int):
  nb_etapes = []

  for i in range(n):
    partie, gagnants = lancer_partie(plateau, pion1, pion2)
    nb_etapes.append(len(partie))

  print(nb_etapes)

  nb_etapes_minimum = min(nb_etapes)
  nb_etapes_maximum = max(nb_etapes)
  nb_etapes_moyenne = sum(nb_etapes) / len(nb_etapes)

  print(f"Le nombre minimum d'étapes est {nb_etapes_minimum}.")
  print(f"Le nombre maximum d'étapes est {nb_etapes_maximum}.")
  print(f"La moyenne d'étapes est {nb_etapes_moyenne}.")

nb_parties = 100
simuler_parties(nb_parties)

def export_csv(table: list, nom_fichier, ordre: list):
  with open(nom_fichier, 'w', newline='') as fichier_CSV:
    dico_CSV = csv.DictWriter(fichier_CSV, fieldnames=ordre)
    dico_CSV.writeheader()
    #print(table)
    
    for dico in table:
      #print(dico)
      dico_CSV.writerow(dico)
    
  return None

# Création du fichier CSV
fichier = "sortie.csv"
ordre = ["Etapes", "depPion1", "posPion1", "depPion2", "posPion2"]
export_csv(partie, fichier, ordre)

# Diagramme avec matplotlib
liste_X = [i for i in range(1, len(partie) + 1)]
liste_dep_pion1 = [partie[i]["depPion1"] for i in range(len(partie))]
liste_dep_pion2 = [partie[i]["depPion2"] for i in range(len(partie))]

print(liste_X)
print(liste_dep_pion1)
print(liste_dep_pion2)

width = 0.5

fig = plt.figure()
plt.bar(liste_X, liste_dep_pion1, width, color=(0.1, 0.6, 0.8, 1.0))
plt.grid()
plt.show()

fig = plt.figure()
plt.bar(liste_X, liste_dep_pion2, width, color=(0.1, 0.8, 0.6, 1.0))
plt.grid()
plt.show()
