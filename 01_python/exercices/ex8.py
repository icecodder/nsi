from random import randint
import matplotlib.pyplot as plt

positionPuce = 0
bande = 100
sauts = 0
listeSauts = []

while positionPuce < bande:
  saut = randint(1, 5)
  positionPuce += saut
  listeSauts.append(saut)
  sauts += 1

print(f"Nombre de saut : {sauts} Listes sauts : {[]} Minimum : {min(listeSauts)} Maximum : {max(listeSauts)} Moyenne : {sum(listeSauts) / len(listeSauts)}")

positions = 0
listePositions = []

for saut in listeSauts:
  positions += saut
  listePositions.append(positions)

listeX = list(range(1, len(listePositions) + 1))
listeY = listePositions

plt.figure()
plt.plot(listeX, listeY, label="Evolution de la puce")
plt.legend()
plt.grid(True)
plt.show()
