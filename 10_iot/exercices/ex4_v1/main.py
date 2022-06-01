# Source :  complete project details at https://RandomNerdTutorials.com


# ---- Les modules pour la carte ----
from machine import *
import time
import tm1637 # Pilotes de l'afficheur 7-segments


# ---- Les modules le wifi----
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()




# ---- Les fonctions pour la partie web ----
def web_page(angle):  
  html = """<html>
<head>
    <meta charset="utf-8">
    <title>Distributeur de croquettes</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
        h1{color: #0F3376; padding: 2vh;}
        p{font-size: 1.5rem;}
        .button{display: inline-block; background-color: #e7bd3b; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
        .button2{background-color: #4286f4;}
    </style>
</head>
<body>
    <h1>Distributeur de croquettes pour chat</h1>
    <p>Quantité:</p>
    <p>Nombre: <strong>""" + str(compteur) + """</strong></p>
    <p>Angle: <strong>""" + str(round(angle)) + """</strong></p>
    <p><a href="/?dist=on"><button class="button">Distribuer</button></a></p>
    <p><a href="/?dist=off"><button class="button button2">RAZ</button></a></p>
</body>
</html>"""
  return html
 

# ---- Les fonction pour commander la partie opérative ----
def setServoAngle(pin, angle):
  if (angle >= 0 and angle <= 180):
    pin.duty(int(0.025*1023 + (angle*0.1*1023)/180))
  else:
    raise ValueError("Servomotor angle have to be set between 0 and 180")


def pinADC(pinNumber, db=ADC.ATTN_11DB, bit=ADC.WIDTH_10BIT):
  pin = ADC(Pin(pinNumber))
  pin.atten(db)
  pin.width(bit)
  return pin


def map(x, x1, x2, y1, y2):
  return x * (y2 - y1) / (x2 - x1) + y1





#--------------------------------------------------------------
# ---- PP et Init ---
#--------------------------------------------------------------

# ---- codes wifi ---
#ssid = 'REPLACE_WITH_YOUR_SSID'
#password = 'REPLACE_WITH_YOUR_PASSWORD'
ssid = 'a_modifier'
password = 'a_modifier'


# Initialisation de la connection
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())



# --------------------- Initialisation de la carte --------------------------------
# Servo on p27
d6 = PWM(Pin(27), freq=50, duty=0)

# Button on p25
pin_bouton = Pin(25, mode=Pin.IN)

# LED on 26
pin_led = Pin(26, mode=Pin.OUT)

# Potentiometer on p35
a2 = pinADC(35)


# ---- Initialisation de l'afficheur 7-segments ----
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(4))


# ---- Initialiser le système ----
# Initialiser le servomoteur à 0°
setServoAngle(d6, 0)


# Initialiser le compteur de distribution
compteur = 0
tm.number(compteur)



# ---- Initialisation du serveur Web ----
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


# ---- Répéter indéfiniment ----
while True:
    
    
    # ---- Gestion du bouton poussoir ----
    vPot = a2.read()
    angle = map(vPot, 0, 1023, 0, 150)
    
    print(pin_bouton.value(), angle)
    time.sleep(1)
    
    # Si le bouton est appuyé alors
    if pin_bouton.value() == 0:
        pin_led.on()            # Allumer la LED
        setServoAngle(d6, angle)  # Placer le servomoteur à 150°
        print(f"Ouverture de {angle}")
        time.sleep(1)           # Attendre 1 seconde
        
        pin_led.off()           # Éteindre la LED
        setServoAngle(d6, 0)    # Placer le servomoteur à 0°
        print("Fermeture")
        
        # Compter le nombre de distributions
        compteur += 1
        tm.number(compteur)
    
    
    
    # ---- Gestion des reqêtes Web ----
    # Récupérer la requête
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    #led_on = request.find('/?led=on')
    #led_off = request.find('/?led=off')
    dist_on = request.find('/?dist=on')
    dist_off = request.find('/?dist=off')
    
    # Analyser la requête
    if dist_on == 6:
        print('Distribution')
        pin_led.value(1)          # Allumer la LED           
        setServoAngle(d6, angle)  # Placer le servomoteur à 150°
        print(f"Ouverture de {angle}")
        time.sleep(1)           # Attendre 1 seconde
        
        pin_led.value(0)           # Éteindre la LED
        setServoAngle(d6, 0)    # Placer le servomoteur à 0°
        print("Fermeture")
        
        # Compter le nombre de distributions
        compteur += 1
        tm.number(compteur)
        
        
    if  dist_off== 6:
        print('Reset')
        pin_led.value(0)
        # réinitialiser le compteur
        compteur = 0
        tm.number(compteur)
        
    
    # Envoyer la nouvelle page
    response = web_page(angle)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
