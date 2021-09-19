def f(x):
  if 0 <= x <= 5:
    return 50 * x
  elif 5 < x <= 8:
    return 50 / 3 * (x - 5) + 250
  else:
    return None

def remplirTableau():
  for i in range (9):
    return(print(i, f(i)))

# remplirTableau()

def creerListes():
    listeX = [i for i in range(9)]
    listeY = [f(i) for i in range(9)]
    
    return listeX, listeY

print(creerListes())
