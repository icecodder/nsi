def calculer_distance(liste_villes, distances, ville_a, ville_b):
    """ Déterminer la distance entre les villes A et B"""
    
    # Vérifier que les villes appartiennent à la liste des villes
    if ville_a not in liste_villes or ville_b not in liste_villes:
        return None
    # Déterminer la distance
    else:
        index_ville_a = liste_villes.index(ville_a)
        index_ville_b = liste_villes.index(ville_b)

        return distances[index_ville_a][index_ville_b]


def plus_proche(liste_villes, distances, villes_visitees, ville_courante):
    """Renvoyer la ville la plus proche non encore visitée : indice, nom et distance"""
    
    distance_min = None
    id_min = None
    nom_min = None
    
    # Déterminer la ville non visitée la plus proche
    id_courant = liste_villes.index(ville_courante)

    #print(id_courant, ville_courante)

    for ville in liste_villes:
        if ville not in villes_visitees:
            id_ville = liste_villes.index(ville)
            distance = distances[id_courant][id_ville]

            #print(id_ville, ville, distance)

            if distance != 0:
                if distance_min == None or distance_min > distance:
                    distance_min = distance
                    id_min = id_ville
                    nom_min = liste_villes[id_min]

    return id_min, nom_min, distance_min


def prob_voyageur(liste_villes, distances, ville_depart):
    """Parcourir toutes les villes avec le trajet le plus court"""
    
    nb_villes = len(liste_villes)
    ville_courante = ville_depart
    villes_visitees = []
    parcours = []
    
    # Tant que toutes les villes non pas été visitées
    villes_visitees.append(ville_courante)

    while len(villes_visitees) != nb_villes:
        # Déterminer la ville la plus proche
        _, ville, distance = plus_proche(liste_villes, distances, villes_visitees, ville_courante)
        
        # Mettre à jour le parcours et passer à la ville suivante
        ville_courante = ville
        villes_visitees.append(ville)
        parcours.append((distance, ville))

    return parcours


liste_villes = ["Nancy", "Metz", "Paris", "Reims", "Troyes"]
distances = [
    [0, 55, 303, 188, 183],
    [55, 0, 306, 176, 203],
    [303, 306, 0, 142, 153],
    [188, 176, 142, 0, 123],
    [183, 203, 153, 123, 0]
]


# Test 1 : distance entre deux villes
ville_1 = "Nancy"
for ville in liste_villes:
    retour = calculer_distance(liste_villes, distances, ville_1, ville)
    #print(ville, retour)

ville_1 = "Dax"
for ville in liste_villes:
    retour = calculer_distance(liste_villes, distances, ville_1, ville)
    #print(ville, retour)



# Test 2 : ville la plus proche
villes_visitees = []
for ville in liste_villes:
    retour = plus_proche(liste_villes, distances, villes_visitees, ville)
    #print(ville, retour)


# Test 3 : problème du voyageur
for ville in liste_villes:
    parcours = prob_voyageur(liste_villes, distances, ville)
    print(ville, parcours)
