import RPi.GPIO as GPIO        # calling for header file for GPIO’s of PI
import time                           # calling for time to provide delays in program
GPIO.setwarnings(False)          # do not show any warnings
GPIO.setmode (GPIO.BOARD)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
GPIO.setup(10,GPIO.OUT)             # initialize GPIO19 as an output
p = GPIO.PWM(10,50)              # GPIO19 as PWM output, with 50Hz frequency
p.start(7.5)                             # generate PWM signal with 7.5% duty cycle
while 1:                                                       # execute loop forever                                    
        p.ChangeDutyCycle(7.5)                   # change duty cycle for getting the servo position to 90º
        time.sleep(1)                                      # sleep for 1 second
        p.ChangeDutyCycle(12.5)                  # change duty cycle for getting the servo position to 180º
        time.sleep(1)                                     # sleep for 1 second
        p.ChangeDutyCycle(2.5)                  # change duty cycle for getting the servo position to 0º
        time.sleep(1)                                     # sleep for 1 second
 
