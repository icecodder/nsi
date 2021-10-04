import PySimpleGUI as sg
from random import randint
import sys

size = 10
point = 0

layout = [
  [sg.Text(f"Points : {point}")],
  [[sg.Button(" ", disabled=True, size=(4, 2), pad=(0, 0), button_color="green") for _ in range(size)] for _ in range(size)],
  [sg.Button("Quitter")]
]

applePosX, applePosY = randint(0, 9), randint(0, 9)
snakePosX, snakePosY = randint(0, 9), randint(0, 9)

while applePosX == snakePosX or applePosY == snakePosY:
  snakePosX, snakePosY = randint(0, 9), randint(0, 9)

print(f"Position pomme : {applePosX}, {applePosY}")
print(f"Position snake : {snakePosX}, {snakePosY}")

layout[1][applePosX][applePosY] = sg.Button(" ", disabled=True, size=(4, 2), pad=(0, 0), button_color="red")

layout[1][snakePosX][snakePosY] = sg.Button(" ", disabled=True, size=(4, 2), pad=(0, 0), button_color="blue")

window = sg.Window("Snake Python", layout, return_keyboard_events=True)

while True:
  event, values = window.read()

  print(f"Key pressed: {event}")

  #keyPos = ["Left:113", "Right:114", "Up:111", "Down:116"] # nsi
  keyPos = ["Left:100", "Right:102", "Up:98", "Down:104"] # moi

  if event in (keyPos[0], keyPos[1], keyPos[2], keyPos[3]):
    print(f"Key pressed: {event}")

  if event in (keyPos[0]):
    layout[1][snakePosX][snakePosY] = sg.Button(" ", disabled=True, size=(4, 2), pad=(0, 0), button_color="green")
    snakePosX = snakePosX - 1
    print(layout[1][snakePosX][snakePosY])
  elif event in (keyPos[1]):
    layout[1][snakePosX][snakePosY] = layout[1][snakePosX + 1][snakePosY]
    snakePosX =+ 1
  elif event in (keyPos[2]):
    layout[1][snakePosX][snakePosY] = layout[1][snakePosX][snakePosY - 1]
    snakePosY =- 1
  elif event in (keyPos[3]):
    layout[1][snakePosX][snakePosY] = layout[1][snakePosX][snakePosY + 1]
    snakePosY =+ 1

  if event == sg.WIN_CLOSED or event == "Quitter":
    break

window.close()
