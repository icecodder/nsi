import PySimpleGUI as sg
import re

def ipValide(ip):
  block = re.findall(r"\d{1,3}", ip);

  for e in block:
    e = int(e)
    
    if e > 256:
      return False

  if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
    return True

  return False

def testerIP(ip):
  valide = ipValide(ip)

  if valide:
    window['Affichage1'].update(f"L'addresse {ip} est valide")
  else:
    window['Affichage1'].update(f"L'addresse {ip} n'est pas valide")

sg.theme('DarkAmber')

layout = [
  [sg.Text("Vérifier la validité d'une adresse IP")],
  [sg.Text('Saisir une adresse'), sg.InputText(key='Saisie1')],
  [sg.Text(size=(40,1), key='Affichage1')],
  [sg.Button('Valider'), sg.Button('Quitter')]
]

window = sg.Window("Vérifier la validité d'une adresse IP", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quitter':
        break
    
    print(values) # Pour déboguer
    testerIP(values['Saisie1'])

window.close()
