from machine import *
import time
import tm1637 # Pilotes de l'afficheur 7-segments






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




# ---- PP / Init ----

# ---- configurer la carte ----
# Servo on p27
d6 = PWM(Pin(27), freq=50, duty=0)

# Button on p25
pin_bouton = Pin(25, mode=Pin.IN)

# LED on 26
pin_led = Pin(26, mode=Pin.OUT)

# Potentiometer on p35
a2 = pinADC(35)

# Initialisation de l'afficheur 7-segments
#tm = tm1637.TM1637(clk=Pin('A0'), dio=Pin('A1'))
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(4))

# ---- Initialiser le système ----
# Initialiser le servomoteur à 0°
setServoAngle(d6, 0)


# Initialiser le compteur de distribution
compteur = 0
tm.number(compteur)

# ---- Répéter indéfiniment ----
while True:
    vPot = a2.read()
    
    # Si le bouton est appuyé alors
    if pin_bouton.value() == 0:
        pin_led.on()            # Allumer la LED
        angle = map(vPot, 0, 1023, 0, 150)
        setServoAngle(d6, angle)  # Placer le servomoteur à 150°
        print(f"Ouverture de {angle}")
        time.sleep(1)           # Attendre 1 seconde
        
        pin_led.off()           # Éteindre la LED
        setServoAngle(d6, 0)    # Placer le servomoteur à 0°
        print("Fermeture")
        
        # Compter le nombre de distributions
        compteur += 1
        tm.number(compteur)
        
        



