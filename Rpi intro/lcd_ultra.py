import RPi.GPIO as GPIO
import time
from RPLCD import CharLCD, cleared, cursor
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO_TRIGGER= 22
GPIO_ECHO= 18


GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 

 ###initialization of Pins using GPIO.BOARD mode
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.clear()

lcd.cursor_pos=(0,0)
lcd.write_string ("Ultrasonic Meas.")
time.sleep(1)
lcd.clear()

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
     # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            lcd.cursor_pos=(0,0)
            lcd.write_string ("Measured \n\rDistance = %.1f cm" % dist)
            time.sleep(1)

    
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        lcd.cursor_pos=(0,0)
        lcd.write_string ("Measurement \n\rstopped by User")
        
        GPIO.cleanup()

