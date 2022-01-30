"""
Sujet: NSI DS1 - Partie C : Problème 3)a
Nom: Charrier
Prénom: Max
Date: 7/10/2021
"""

def longueurSpirale(x, n):
  u = x
  s = u

  for _ in range(n):
    u = 1.5 * u
    s = s + u
  
  return s

x = 10
print(longueurSpirale(x, 3))
