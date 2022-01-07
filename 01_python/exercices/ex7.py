from random import randint

liste = []

while len(liste) < 10:
  rd = randint(0, 10)

  if rd not in liste:
    liste.append(rd)

print(liste)

liste2 = [randint(0, 20) for _ in range(10)]

print(liste2)

def posMax(liste: list):
  return liste.index(max(liste))

print("Position du maxium : ", posMax(liste2))

def moyenne(liste):
  return sum(liste) / len(liste)

print("Moyenne : ", moyenne(liste2))
