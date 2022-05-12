def remplir_sac(poids_max, liste_objets):
    liste_choisis = []
    poids_sac = 0
    i = 0
    i_max = len(liste_objets) - 1

    while poids_sac < poids_max and i <= i_max and liste_objets != []:
        if poids_sac + liste_objets[i][1] <= poids_max:
            liste_choisis.append(liste_objets[i])
            poids_sac += liste_objets[i][1]
            i += 1
        else:
            i += 1
    
    return liste_choisis

poids_max = 5
liste_objets = [
    ["Chat", 4, 8],
    ["Goûter", 2, 7],
    ["Bouteille", 1, 5],
    ["Jumelle", 0.4, 4],
    ["Livre", 0.2, 3]
]
print(remplir_sac(poids_max, liste_objets))
