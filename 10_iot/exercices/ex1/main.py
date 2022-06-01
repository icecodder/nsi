from machine import *
import time

def setServoAngle(pin, angle):
  if (angle >= 0 and angle <= 180):
    pin.duty(int(0.025*1023 + (angle*0.1*1023)/180))
  else:
    raise ValueError("Servomotor angle have to be set between 0 and 180")



# ---- PP / Init ----

# ---- configurer la carte ----
# Servo on p27
d6 = PWM(Pin(27), freq=50, duty=0)

# Button on p25
pin_bouton = Pin(25, mode=Pin.IN)

# LED on 26
pin_led = Pin(26, mode=Pin.OUT)


# ---- Initialiser le système ----
# Initialiser le servomoteur à 0°
setServoAngle(d6, 0)



# Répéter indéfiniment
while True:
    # Si le bouton est appuyé alors
    
    if pin_bouton.value() == 0:
        pin_led.on()            # Allumer la LED 
        print("Ouverture de 150°")
        setServoAngle(d6, 150)  # Placer le servomoteur à 150°
        time.sleep(1)           # Attendre 1 seconde
        pin_led.off()           # Éteindre la LED
        print("Ouverture de 0°")
        setServoAngle(d6, 0)    # Placer le servomoteur à 0°
    # FinSi
# FinRépéter



