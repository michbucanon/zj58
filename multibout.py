import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import subprocess
from gpiozero import Button
from gpiozero import LED
from signal import pause
from time import sleep, localtime, strftime

led = LED(17)
boisson = Button(14)
repas = Button(15)
photo = Button(23)
rab = Button(24)

def bouton_boisson():
    subprocess.Popen(['lp', 'boisson.bmp'])
    print("boisson !")

def bouton_repas():
    subprocess.Popen(['lp', 'boisson.bmp'])
    print("repas !")
	
def bouton_photo():
	temps = strftime("%Y-%b-%d-%H-%M-%S", localtime())
	led.blink(0.2,0.2,8)
        sleep(1)
	subprocess.Popen(['raspistill', '-n', '-t', '400',  '-w', '384', '-h', '384',  '-co', '20', '-br', '95', '-o', temps+'.bmp'])
	sleep(1)
	subprocess.Popen(['lp', temps+'.bmp'])
	print("photo !")
	
def bouton_rab():
    subprocess.Popen(['lp', 'boisson.bmp'])
    print("rab !")

        
boisson.when_pressed = bouton_boisson
repas.when_pressed = bouton_repas
photo.when_pressed = bouton_photo
rab.when_pressed = bouton_rab

pause()
