"""
Sujet: Devoir Maison Turtle Ex2
Classe: 1G2
Nom: Charrier
Prénom: Max
Date: 19/09/21
Version: 1.0.0
License: MIT
Repository: https://github.com/icecodder/nsi
"""

import turtle as turtle

n = int(input("Choissisez un nombre : "))
radius = 10

turtle.reset()
turtle.speed(10)

def goto(x, y):
    turtle.up()
    turtle.goto(x , y)
    turtle.down()

def drawPipes(number, x, y):
    goto(radius * 2 * number + x, y) if number != 0 else None
    turtle.circle(radius)

# Rangée du bas
for i in range(n + 1):
    drawPipes(i, 0, 0)

goto(radius, radius * 2 - 2)

# Rangée supérieur
for i in range(n):
    drawPipes(i, 10, radius * 2 - 2)

# Rangée final
if n == 2:
    goto(radius * 2, radius * 4 - 4)

    for i in range(n - 1):
        drawPipes(i, radius * 2, radius * 4 - 4)
elif n == 3:
    goto(radius * 2, radius * 4 - 4)

    for i in range(n - 1):
        drawPipes(i, radius * 2, radius * 4 - 4)

    goto(radius * 3, radius * 6 - 6)

    for i in range(n - 2):
        drawPipes(i, radius * 3, radius * 6 - 6)
elif n == 4:
    goto(radius * 2, radius * 4 - 4)

    for i in range(n - 1):
        drawPipes(i, radius * 2, radius * 4 - 4)

    goto(radius * 3, radius * 6 - 6)

    for i in range(n - 2):
        drawPipes(i, radius * 3, radius * 6 - 6)

    goto(radius * 4, radius * 8 -8)

    for i in range(n - 3):
        drawPipes(i, radius * 4, radius * 8 - 8)

turtle.hideturtle()
turtle.done()

