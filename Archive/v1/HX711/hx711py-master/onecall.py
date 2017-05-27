import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

def cleanAndExit():
    GPIO.cleanup()
    sys.exit()

object = HX711(23,24)

object.set_reading_format("LSB","MSB")

object.set_reference_unit(435)
object.reset()
object.tare()

try:
    print ('Place food item on scale')
    time.sleep(10)
    val = object.get_weight(5)
    print (val)

    object.power_down()
    object.power_up()

except (KeyboardInterrupt, SystemExit):
    cleanAndExit()
