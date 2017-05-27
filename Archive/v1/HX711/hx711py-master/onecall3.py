import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

def cleanAndExit():
    GPIO.cleanup()
    sys.exit()

object = HX711(23,24)
pre_val = 0
val =0
object.set_reading_format("LSB","MSB")
# set reference unit is 435 for 5kg scale and 770 for 3kg scale
object.set_reference_unit(435)
object.reset()
object.tare()

print ("ready!")

# time.sleep(5)

# val = object.get_weight(5)
while True:
    if val!=pre_val or val<=0:
        pre_val = val
        val = object.get_weight(5)
        print("current reading: "+str(val)+"g")
        time.sleep(0.5)
        if val<0:
            object.tare()

    elif val == pre_val and val>0:
        print ("final reading: "+str(val)+"g")
        object.power_down()
        object.power_up()
        break
cleanAndExit()
