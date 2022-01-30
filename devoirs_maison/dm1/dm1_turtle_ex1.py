"""
Sujet: Devoir Maison Turtle Ex1
Classe: 1G2
Nom: Charrier
Prénom: Max
Date: 18/09/21
Version: 1.0.0
License: MIT
Repository: https://github.com/icecodder/nsi
"""

import turtle as turtle

turtle.reset()
turtle.speed(7)

def drawYang():
  turtle.fillcolor("black")
  turtle.begin_fill()
  turtle.left(180)
  turtle.circle(-50, 180)
  turtle.circle(50, 180)
  turtle.left(180)
  turtle.circle(-100, 180)
  turtle.end_fill()

def drawSmallCircles():
  turtle.fillcolor("black")
  turtle.up()
  turtle.goto(0, 32)
  turtle.down()
  turtle.begin_fill()
  turtle.circle(18)
  turtle.end_fill()
  turtle.fillcolor("white")
  turtle.up()
  turtle.goto(0, 132)
  turtle.down()
  turtle.begin_fill()
  turtle.circle(18)
  turtle.end_fill()

def drawFullYinYang():
  turtle.circle(100, 180)
  drawYang()
  drawSmallCircles()

drawFullYinYang()

turtle.hideturtle()
turtle.done()
