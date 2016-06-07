from Adafruit_CharLCD import Adafruit_CharLCD
import time


lcd = Adafruit_CharLCD(25,24,23,17,27,22,16,2,None)

lcd.clear()

lcd.message("Butt Butt Travels\nthru time")
