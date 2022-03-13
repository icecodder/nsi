import matplotlib.pyplot as plt

def f(x):
  if 0 <= x <= 5:
    return 50 * x
  elif 5 < x <= 8:
    return 50 / 3 * (x - 5) + 250
  else:
    return None

listeX = [i for i in range(9)]
listeY = [f(i) for i in range(9)]
    
print(listeX, listeY)

plt.figure
plt.plot(listeX, listeY)
plt.grid(True)
plt.show()
