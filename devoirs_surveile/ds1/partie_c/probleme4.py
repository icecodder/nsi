"""
Sujet: NSI DS1 - Partie C : Problème 4
Nom: Charrier
Prénom: Max
Date: 7/10/2021
"""

suite = [1, 2, 3, 5, 8, 13]

while len(suite) < 10:
  suite.append(suite[len(suite) - 1] + suite[len(suite) - 2])

print(suite)
