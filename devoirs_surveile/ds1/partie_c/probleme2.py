"""
Sujet: NSI DS1 - Partie C : Problème 2
Nom: Charrier
Prénom: Max
Date: 7/10/2021
"""

def population(n):
  pop = 10000
  for _ in range(n):
    pop = pop + 5/100 * pop
  return pop

print(population(10))
