import matplotlib.pyplot as plt

def c(n):
  return 1 + 3 * (n - 1)

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

