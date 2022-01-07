import PySimpleGUI as sg
import random

sg.theme('DarkAmber')

layout = [
  [sg.Text('Bonjour, je vous propose de deviner un nombre')],
  [sg.Text('Entrez un nombre'), sg.InputText(key='Saisie1')],
  [sg.Text(size=(40,1), key='Affichage1')],
  [sg.Button('Valider'), sg.Button('Quitter')]
]

window = sg.Window('Ma première fenêtre graphique', layout)

n = random.randint(0, 10)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quitter':
        break
    
    nombre = int(values['Saisie1'])
    
    if nombre > n:
      window['Affichage1'].update("Plus petit")
    elif nombre < n:
      window['Affichage1'].update("Plus grand")
    else:
      window['Affichage1'].update("Gagné!")


window.close()
