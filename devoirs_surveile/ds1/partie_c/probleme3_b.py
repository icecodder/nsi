"""
Sujet: NSI DS1 - Partie C : Problème 3)b
Nom: Charrier
Prénom: Max
Date: 7/10/2021
"""
import turtle

turtle.reset()
turtle.speed(1)

def tracerSpirale(x, n):
  u = x
  s = u
  tailleSegment = []

  turtle.backward(u)

  for _ in range(n):
    u = 1.5 * u
    s = s + u
    tailleSegment.append(u)

  turtle.right(90)
  for i in range(len(tailleSegment) - 1):
    turtle.forward(tailleSegment[i])
    turtle.left(90)
  
  return s

x = 10
tracerSpirale(x, 3)

turtle.done()
