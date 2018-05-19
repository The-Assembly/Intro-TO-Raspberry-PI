import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
Count=0
##print ("LED on")
##GPIO.output(8,GPIO.HIGH)
##time.sleep(3)
##print ("LED off")
##GPIO.output(8,GPIO.LOW)

while Count<5:
    S1=GPIO.input(8)
    GPIO.output(8,GPIO.LOW)
    time.sleep(.5)
    GPIO.output(8,GPIO.HIGH)
    time.sleep(1)
    S2=GPIO.input(10)
    GPIO.output(10,GPIO.LOW)
    time.sleep(.5)
    GPIO.output(10,GPIO.HIGH)
    time.sleep(1)
