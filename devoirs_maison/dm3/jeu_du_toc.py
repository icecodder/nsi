"""
Jeu du TOCK (version simplifiée)
Auteur: Max CHARRIER
License: MIT (https://github.com/icecodder/nsi)
"""

# Importation des modules
from pprint import pprint # Pretty-Print pour afficher des listes plus jolies
from random import randint # Random pour choisir un nombre au hasard
import matplotlib.pyplot as plt # MatPlotLib pour les graphiques
import csv # CSV pour créer le tableau

regles = {
    "nb_joueurs": 4,
    "nb_cases": 18,
    "defaut": (0, "normal"),
    "cases_speciales": {
        17: (2, "maison"),
        18: (3, "départ")
    }
}

#print(regles)

# Création du plateau de jeu
def creer_plateau():
    plateau = []

    for i in range(regles["nb_cases"]):
        case = i + 1

        # Ajout des cases spéciales
        if case in regles["cases_speciales"].keys():
            #print(case, regles["cases_speciales"][case])
            plateau.append(regles["cases_speciales"][case])
        # Ajout des cases normales
        else:
            #print(case, regles["defaut"])
            plateau.append(regles["defaut"])

    return plateau * regles["nb_joueurs"]

plateau = creer_plateau()
#pprint(plateau)

# Créations des pions
# Joueur X = Position du pion
joueur_1 = -1
joueur_2 = -1
joueur_3 = -1
joueur_4 = -1

# Déplacement du pion
def deplacer_pion(joueur):
    carte = randint(1, 13)

    # Récupération du nombre de cases totales
    nb_cases_tot = regles["nb_cases"] * regles["nb_joueurs"]

    # Si le joueurr n'a pas un AS (1) ou un ROI (13), il ne peut pas rentrer dans le plateau de jeu
    if joueur == -1:
        if carte == 1 or carte == 13:
            joueur = 18
        else:
            joueur = -1
    else:
        # Si le joueur à un 4, il recule de 4 cases
        if carte == 4:
            joueur -= carte
        # Sinon le joueur avance du nombres de cases correspondant à la carte
        else:
            joueur += carte

    # Si le joueur est arrivé à la case départ, il revient au début
    if joueur > nb_cases_tot:
        joueur -= nb_cases_tot

    return joueur, carte

joueur_1, carte_1 = deplacer_pion(joueur_1)
joueur_2, carte_2 = deplacer_pion(joueur_2)
joueur_3, carte_3 = deplacer_pion(joueur_3)
joueur_4, carte_4 = deplacer_pion(joueur_4)
#print(f"Le joueur 1 est sur la case {joueur_1} et a jouée {carte_1}")

# Fonction pour lancer une partie
def lancer_partie(joueur_1, joueur_2, joueur_3, joueur_4):
    etape = 1
    partie = []
    gagnant = 0
    
    # Tant qu'un des joueurs n'est pas arrivé à la maison, on continue
    while joueur_1 != 17 and joueur_2 != 17 and joueur_3 != 17 and joueur_4 != 17:
        # Déplacement du joueur 1
        joueur_1, carte_1 = deplacer_pion(joueur_1)
        # Vérification si le joueur 1 a gagné
        if joueur_1 == 17:
            gagnant = 1

        # Déplacement du joueur 2
        joueur_2, carte_2 = deplacer_pion(joueur_2)
        # Vérification si le joueur 2 a gagné
        if joueur_2 == 17:
            gagnant = 2

        # Déplacement du joueur 3
        joueur_3, carte_3 = deplacer_pion(joueur_3)
        # Vérification si le joueur 3 a gagné
        if joueur_3 == 17:
            gagnant = 3

        # Déplacement du joueur 4
        joueur_4, carte_4 = deplacer_pion(joueur_4)
        # Vérification si le joueur 4 a gagné
        if joueur_4 == 17:
            gagnant = 4

        # Ajout des informations à la partie
        partie.append({
            "Etape": etape,
            "Carte J1": carte_1,
            "Carte J2": carte_2,
            "Carte J3": carte_3,
            "Carte J4": carte_4,
        })

        etape += 1

    return partie, gagnant

partie, gagnant = lancer_partie(joueur_1, joueur_2, joueur_3, joueur_4)
#pprint(partie)
#print(f"Le gagant est Joueur {gagnant} en {len(partie)} étapes")

# Listes pour matplotlib
liste_x = [i for i in range(len(partie))] # Chaque étape de la partie
liste_y_j1 = [partie[i]["Carte J1"] for i in liste_x] # Carte du joueur 1
liste_y_j2 = [partie[i]["Carte J2"] for i in liste_x] # Carte du joueur 2
liste_y_j3 = [partie[i]["Carte J3"] for i in liste_x] # Carte du joueur 3
liste_y_j4 = [partie[i]["Carte J4"] for i in liste_x] # Carte du joueur 4

# Largeur des barres
largeur = 0.5

fig = plt.figure()

plt.bar(liste_x, liste_y_j1, width=largeur, label="Joueur 1", color=(0.1, 0.6, 0.8, 1.0))
#plt.bar(liste_x, liste_y_j2, width=largeur, label="Joueur 2", color=(0.8, 0.1, 0.6, 1.0))
#plt.bar(liste_x, liste_y_j3, width=largeur, label="Joueur 3", color=(0.1, 0.6, 0.1, 1.0))
#plt.bar(liste_x, liste_y_j4, width=largeur, label="Joueur 4", color=(0.6, 0.1, 0.6, 1.0))

# Ajout des légendes
plt.title("Cartes jouées à chaque étape")
plt.xlabel("Etapes")
plt.ylabel("Cartes jouées")
plt.legend()

#plt.grid()
plt.show()

# Fonction pour crée le tableau avec les informations des simulations de chaque partie
def export_csv(tableau, nom_fichier, ordre):
    with open(nom_fichier, "w", newline="") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=ordre)
        writer.writeheader()

        for ligne in tableau:
            writer.writerow(ligne)
    
    return None

# Fonction pour simuler n parties
def simuler_parties(n: int):
    nb_etapes = []
    nb_partie = 1
    tableau = []

    ordre = ["Partie", "Joueur Gagnant", "Nombres de coups", "Durée"]

    for _ in range(n):
        partie, gagnant = lancer_partie(joueur_1, joueur_2, joueur_3, joueur_4)
        nb_etapes.append(len(partie))

        tableau.append({
            "Partie": nb_partie,
            "Joueur Gagnant": gagnant,
            "Nombres de coups": len(partie),
            "Durée": len(partie) / regles["nb_joueurs"]
        })

        nb_partie += 1


    #print(nb_etapes)
    #print(tableau)

    # Export du tableau
    export_csv(tableau, "parties.csv", ordre)

    # Affichage du minimum, du maximum et de la moyenne
    nb_etapes_minimum = min(nb_etapes)
    nb_etapes_maximum = max(nb_etapes)
    nb_etapes_moyenne = sum(nb_etapes) / len(nb_etapes)

    #print(f"Le nombre minimum d'étapes est {nb_etapes_minimum}.")
    #print(f"Le nombre maximum d'étapes est {nb_etapes_maximum}.")
    #print(f"La moyenne d'étapes est {nb_etapes_moyenne}.")

nb_parties = 1000
simuler_parties(nb_parties)
