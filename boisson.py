import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import subprocess
from gpiozero import Button
from gpiozero import LED
from signal import pause


friche = Button(25)
led = LED(17)

def bouton_friche():
    led.blink(0.2,0.2,29)
    subprocess.Popen(['lp', 'boisson.bmp'])
    print("Impression de tickets")

        
friche.when_pressed = bouton_friche

pause()
