"""
Jeu de TOCK (version simplifiée)
Simulation de nombreuses parties du jeu de TOCK afin d'estimer la durée moyenne d'une partie.
Auteur: Max CHARRIER
License: MIT (https://github.com/icecodder/nsi)
"""
# Importation des modules
from pprint import pprint # Pretty-Print pour afficher des listes plus jolies
from random import randint # Random pour choisir un nombre au hasard
import matplotlib.pyplot as plt # matploitlib pour créer le graphique
import numpy as np # Numpy pour gérer l'espacement entre les barres du graphique
import csv # CSV pour créer le tableau

# =====================================================================================================================

# Définition des règles du jeu
regles = {
    "nb_cases": 18,
    "defaut": (0, "normal"),
    "cases_speciales": {
        17: (2, "maison"),
        18: (3, "départ")
    }
}
#print(regles)

# Création du plateau de jeu
def creer_plateau() -> list:
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

    # Agrandissement du tableau pour les 4 joueurs
    return plateau * 4

plateau = creer_plateau()
#pprint(plateau)

# Créations des pions
# Joueur X = Position du pion
joueur_1 = -1
joueur_2 = -1
joueur_3 = -1
joueur_4 = -1


# Déplacement du pion
def deplacer_pion(joueur: int, autres_joueurs: list) -> tuple:
    carte = randint(1, 13)

    # Récupération du nombre de cases totales
    nb_cases_tot = regles["nb_cases"] * 4

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
        # Si le joueur à un 5, il fait avancer un autre joueurs de 5 cases (ce même joueur peut rentrer dans le plateau si ce n'est pas déjà le cas)
        if carte == 5:
            joueur_random = randint(0, 2)
            autres_joueurs[joueur_random] = 5
        # Si le joueur à un VALET (11), il échange de position avec un autre joueur
        if carte == 11:
            joueur_random = randint(0, 2)
            # Hormis si l'autre joueur est sur la case départ (18)
            if autres_joueurs[joueur_random] != 18:
                # On stocke la position du joueur
                ancien_joueur = joueur
                # Allocation des nouvelles positions
                joueur = autres_joueurs[joueur_random]
                autres_joueurs[joueur_random] = ancien_joueur
            else:
                return joueur, carte
        # Sinon le joueur avance du nombres de cases correspondant à la carte
        else:
            joueur += carte

    # Si le joueur est arrivé à la case départ, il revient au début
    if joueur > nb_cases_tot:
        joueur -= nb_cases_tot

    return joueur, carte

# Test des déplacements
joueur_1, carte_1 = deplacer_pion(joueur_1, [joueur_2, joueur_3, joueur_4])
joueur_2, carte_2 = deplacer_pion(joueur_2, [joueur_1, joueur_3, joueur_4])
joueur_3, carte_3 = deplacer_pion(joueur_3, [joueur_1, joueur_2, joueur_4])
joueur_4, carte_4 = deplacer_pion(joueur_4, [joueur_1, joueur_2, joueur_3])
#print(f"Le joueur 1 est sur la case {joueur_1} et a jouée {carte_1}")
#print(f"Le joueur 2 est sur la case {joueur_2} et a jouée {carte_2}")
#print(f"Le joueur 3 est sur la case {joueur_3} et a jouée {carte_3}")
#print(f"Le joueur 4 est sur la case {joueur_4} et a jouée {carte_4}")


# Lancement d'une partie
def lancer_partie(joueur_1: int, joueur_2: int, joueur_3: int, joueur_4: int) -> tuple:
    etape = 1
    partie = []
    gagnant = 0
    
    # Tant qu'un des joueurs n'est pas arrivé à la maison, on continue
    while joueur_1 != 17 and joueur_2 != 17 and joueur_3 != 17 and joueur_4 != 17:
        # Déplacement du joueur 1
        joueur_1, carte_1 = deplacer_pion(joueur_1, [joueur_2, joueur_3, joueur_4])
        # Vérification si le joueur 1 a gagné
        if joueur_1 == 17:
            gagnant = 1

        # Déplacement du joueur 2
        joueur_2, carte_2 = deplacer_pion(joueur_2, [joueur_1, joueur_3, joueur_4])
        # Vérification si le joueur 2 a gagné
        if joueur_2 == 17:
            gagnant = 2

        # Déplacement du joueur 3
        joueur_3, carte_3 = deplacer_pion(joueur_3, [joueur_1, joueur_2, joueur_4])
        # Vérification si le joueur 3 a gagné
        if joueur_3 == 17:
            gagnant = 3

        # Déplacement du joueur 4
        joueur_4, carte_4 = deplacer_pion(joueur_4, [joueur_1, joueur_2, joueur_3])
        # Vérification si le joueur 4 a gagné
        if joueur_4 == 17:
            gagnant = 4

        # Ajout des informations à la partie
        partie.append({
            "Etape": etape,
            "Position J1": joueur_1,
            "Carte J1": carte_1,
            "Position J2": joueur_2,
            "Carte J2": carte_2,
            "Position J3": joueur_3,
            "Carte J3": carte_3,
            "Position J4": joueur_4,
            "Carte J4": carte_4,
        })

        etape += 1

    return partie, gagnant

partie, gagnant = lancer_partie(joueur_1, joueur_2, joueur_3, joueur_4)
#pprint(partie)
#print(f"Le gagant est Joueur {gagnant} en {len(partie)} étapes")


# Simulation de N parties
def simuler_parties(n: int) -> tuple:
    nb_etapes = []

    for _ in range(n):
        partie, gagnant = lancer_partie(joueur_1, joueur_2, joueur_3, joueur_4)
        # Ajout du nombre d'étape de la partie
        nb_etapes.append(len(partie))

    #print(nb_etapes)

    # Affichage du minimum, du maximum et de la moyenne
    nb_etapes_min = min(nb_etapes)
    nb_etapes_max = max(nb_etapes)
    nb_etapes_moy = sum(nb_etapes) / len(nb_etapes)

    return nb_etapes_min, nb_etapes_max, nb_etapes_moy

nb_parties = 100
nb_min, nb_max, nb_moy = simuler_parties(nb_parties)
#print(f"Le nombre minimum d'étapes est {nb_min}.")
#print(f"Le nombre maximum d'étapes est {nb_max}.")
#print(f"La moyenne d'étapes est {nb_moy}.")

# =============================================================================
# MATPLOTLIB
# =============================================================================

# Listes pour les abscisses et les ordonnées
etapes = [i for i in range(len(partie))] # Liste des étapes

pos_j1 = [partie[i]["Position J1"] for i in range(len(partie))] # Liste des positions du joueur 1
pos_j2 = [partie[i]["Position J2"] for i in range(len(partie))] # Liste des positions du joueur 2
pos_j3 = [partie[i]["Position J3"] for i in range(len(partie))] # Liste des positions du joueur 3
pos_j4 = [partie[i]["Position J4"] for i in range(len(partie))] # Liste des positions du joueur 4

#print(etapes)
#print(pos_j1)
#print(pos_j2)
#print(pos_j3)
#print(pos_j4)

# Espacement des barres
x = np.arange(len(etapes))
largeur = 0.2

fig, ax = plt.subplots()

# Ajout des barres avec les positions des joueurs
j1 = ax.bar(x - 0.2, pos_j1, width=largeur, label="Joueur 1")
j2 = ax.bar(x, pos_j2, width=largeur, label="Joueur 2")
j3 = ax.bar(x + 0.2, pos_j3, width=largeur, label="Joueur 3")
j4 = ax.bar(x + 0.4, pos_j4, width=largeur, label="Joueur 4")

# Ajout d'une indication sur les positions des joueurs
ax.bar_label(j1, padding=3)
ax.bar_label(j2, padding=3)
ax.bar_label(j3, padding=3)
ax.bar_label(j4, padding=3)

# Paramètrage de l'échelle
plt.xticks(x)

# Ajout des informations
plt.title("Position des joueurs en fonction de l'étape")
plt.xlabel("Etape")
plt.ylabel("Position du joueur")
plt.legend()

# Ajustement et affichage
fig.tight_layout()
plt.show()

# =============================================================================
# CSV
# =============================================================================

# Création du fichier CSV
def export_csv(tableau, nom_fichier, ordre):
    with open(nom_fichier, "w", newline="") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=ordre)
        writer.writeheader()

        for ligne in tableau:
            writer.writerow(ligne)
    
    return None

# Simulation de N parties
def simuler_parties(n: int) -> tuple:
    nb_etapes = []
    tableau = []

    ordre = ["Partie", "Joueur Gagnant", "Nombres de coups", "Durée de la partie"]

    for i in range(1, n + 1):
        partie, gagnant = lancer_partie(joueur_1, joueur_2, joueur_3, joueur_4)
        # Ajout du nombre d'étape de la partie
        nb_etapes.append(len(partie))

        tableau.append({
            "Partie": i,
            "Joueur Gagnant": f"Joueur {gagnant}",
            "Nombres de coups": len(partie),
            "Durée de la partie": len(partie) * 0.5, # 2 Coups par seconde
        })

    #print(nb_etapes)
    #print(tableau)

    # Export du fichier CSV
    export_csv(tableau, "parties.csv", ordre)

    # Affichage du minimum, du maximum et de la moyenne
    nb_etapes_min = min(nb_etapes)
    nb_etapes_max = max(nb_etapes)
    nb_etapes_moy = sum(nb_etapes) / len(nb_etapes)

    return nb_etapes_min, nb_etapes_max, nb_etapes_moy

nb_parties = 100
nb_min, nb_max, nb_moy = simuler_parties(nb_parties)
#print(f"Le nombre minimum d'étapes est {nb_min}.")
#print(f"Le nombre maximum d'étapes est {nb_max}.")
#print(f"La moyenne d'étapes est {nb_moy}.")
