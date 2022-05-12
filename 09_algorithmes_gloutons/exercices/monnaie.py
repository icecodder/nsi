def monnaie(somme, liste):
    monnaie = []
    somme_restante = somme
    i = len(liste) - 1

    while somme_restante > 0:
        if liste[i] <= somme_restante:
            monnaie.append(liste[i])
            somme_restante -= liste[i]
        else:
            i -= 1
    
    return monnaie

somme = 47
liste = [1, 2, 5, 10, 20, 50, 100, 200]
print(monnaie(somme, liste))
