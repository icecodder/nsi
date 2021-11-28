"""
Sujet: NSI DS1 - Partie C : Problème 1
Nom: Charrier
Prénom: Max
Date: 7/10/2021
"""

def tiragePhotos(n):
  if n < 50:
    return 0.2 * n
  elif n >= 100 and n < 100:
    return 0.15 * n
  elif n >= 100:
    return 0.1 * n

print(tiragePhotos(10))
