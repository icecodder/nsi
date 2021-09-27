from random import randint

puce = 0
bande = 100
sauts = 0
listeSauts = []

while puce < bande:
  s = randint(1, 5)
  puce += s
  listeSauts.append(s)
  sauts += 1

print(f"Nombre de saut : {sauts} Listes sauts : {listeSauts} Minimum : {min(listeSauts)} Maximum : {max(listeSauts)} Moyenne : {sum(listeSauts) / len(listeSauts)}")
