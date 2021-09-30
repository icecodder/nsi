"""
Sujet: Devoir Maison Exposés Sujet 11
Classe: 1G2 & 1G10
Nom: Charrier & Mercier
Prénom: Max & Paul
Date: 29/09/21
Version: 1.0.0
License: MIT
Repository: https://github.com/icecodder/nsi
"""

import matplotlib.pyplot as plt

def c(n):
  return 1 + 3 * (n - 1)

# Question 1
print(f"Motif n°1 : {c(1)} carrés")
print(f"Motif n°2 : {c(2)} carrés")
print(f"Motif n°3 : {c(3)} carrés")
print(f"Motif n°1000 : {c(1000)} carrés")

# Question 2
print(f"{c(50)} carrés")

# Question 3
listeX = list(range(1, 1001, ))
listeY = [c(n) for n in listeX]

plt.figure()
plt.plot(listeX, listeY, label="Fonction c(n)")
plt.title("Evolution du nombre de carré en fonction du numéro de motif")
plt.xlabel("Numéro de motif n")
plt.ylabel("Nombre de carré c(n)")
plt.legend()
plt.grid(True)
plt.show()
