import RPi.GPIO as GPIO
import time
from RPLCD import CharLCD, cleared, cursor
import socket
import fcntl
import struct


GPIO.setwarnings(False)
 ###initialization of Pins using GPIO.BOARD mode
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
##lcd.cursor_pos = (0, 1)  ## Positioning the coursor = (ROW,COLUMN)
##lcd.write_string(u'Hello world!') ## This to write to the lcd
##time.sleep(2)
##lcd.clear() ##clear the screen

#### Blinking Text
##while True:
##    lcd.write_string(u"Hello world!")
##    time.sleep(1)
##    lcd.clear()
##    time.sleep(1)


##Print Date & Time
##while True:
##    lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
##    
##    lcd.cursor_pos = (1, 0)
##    lcd.write_string("Date: %s" %time.strftime("%m/%d/%Y"))
##



#### PRINTING MULTIPLE CUSTOM CHARACTERS
##smiley = (
##    0b00000,
##    0b01010,
##    0b01010,
##    0b00000,
##    0b10001,
##    0b10001,
##    0b01110,
##    0b00000,
##)
##
##omega = (
##    0b00000,
##    0b01110,
##    0b10001,
##    0b10001,
##    0b10001,
##    0b01010,
##    0b11011,
##    0b00000,
##)
##
##pi = (
##    0b00000,
##    0b00000,
##    0b11111,
##    0b01010,
##    0b01010,
##    0b01010,
##    0b10011,
##    0b00000,
##)
##
##mu = (
##    0b00000,
##    0b10010,
##    0b10010,
##    0b10010,
##    0b10010,
##    0b11101,
##    0b10000,
##    0b10000,
##)
##
##drop = (
##    0b00100,
##    0b00100,
##    0b01010,
##    0b01010,
##    0b10001,
##    0b10001,
##    0b10001,
##    0b01110,
##)
##
##temp = (
##    0b00100,
##    0b01010,
##    0b01010,
##    0b01110,
##    0b01110,
##    0b11111,
##    0b11111,
##    0b01110,
##)
##
##lcd.create_char(0, omega)
##lcd.create_char(1, pi)
##lcd.create_char(2, mu)
##lcd.create_char(3, drop)
##lcd.create_char(4, temp)
##lcd.create_char(0, smiley)
##
##
##
##lcd.write_string(chr(0))
##lcd.write_string(chr(1))
##lcd.write_string(chr(2))
##lcd.write_string(chr(3))
##lcd.write_string(chr(4))
##lcd.write_string(chr(5))
## Want to generate urs?? go to https://omerk.github.io/lcdchargen/

### SCROLLING TEXT
framebuffer = [
    'Hello!',
    '',
]

def write_to_lcd(lcd, framebuffer, num_cols):
    """Write the framebuffer out to the specified LCD."""
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')

from RPLCD import CharLCD
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
write_to_lcd(lcd, framebuffer, 16)

import time
long_string = 'This string is too long to fit'

def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.5): #DELAY= CONTROLS THE SPEED OF SCROLL
##we need to manipulate the framebuffer, write it to the display, sleep for a short while and repeat
    padding = ' ' * num_cols
    s = padding + string + padding
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)

while True:
    loop_string(long_string, lcd, framebuffer, 1, 16)



### when doing several update in a row the display of the lcd get corrupted so we run this
##code to fully clear the screen
##lcd.clear()
##lcd.cursor_pos = (0, lineStartPos(lcdLine1))
##lcd.write_string(str(lcdLine1))
##lcd.cursor_pos = (1, lineStartPos(lcdLine2))
##lcd.write_string(str(lcdLine2))
##lcd.cursor_pos = (2, lineStartPos(lcdLine3))
##lcd.write_string(str(lcdLine3))
##lcd.cursor_pos = (3, 0)
##lcd.write_string("Target:")
##lcd.write_string(str(targetTemp))
##lcd.write_string(chr(223) + " ")
##lcd.write_string("Temp:")
##lcd.write_string(str(currentTemp))
##lcd.write_string(chr(223))



