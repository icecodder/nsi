"""
Sujet: Représentation de l'information avec python Ex6 (sous forme de DM)
Classe: 1G2
Nom: Charrier
Prénom: Max
Date: 02/12/2021
Version: 1.0.0
License: MIT
Repository: https://github.com/icecodder/nsi
"""

import prettytable

"""
Crée une table UTF-8 à deux entrées
:param first_char: premier caractère de la table en décimale
:return: table de caractères
"""
def create_utf8_table(first_char):
    # Création de la table
    table = prettytable.PrettyTable([" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"])
    # Définition de la taille des lignes
    line_size = 16

    # Ajout des lignes 2 à 7
    for i in range(2, 8):
        line = [chr(j) for j in range(first_char, first_char + line_size)]
        line.insert(0, hex(i).split("x")[1].upper())

        table.add_row(line)
        first_char += line_size

    # Saut des lignes 8 et 9
    first_char += 2 * line_size

    # Ajout des lignes 10 à 15
    for i in range(10, 16):
        line = [chr(j) for j in range(first_char, first_char + line_size)]
        line.insert(0, hex(i).split("x")[1].upper())
        table.add_row(line)
        first_char += line_size

    return table

# Affichage et création de la table à partir du caractère 32|0x20 (espace)
print(create_utf8_table(32))

# Test à partir d'autre caractère, exemple: 8364|0x20AC (euro)
print(create_utf8_table(8364))
