import RPi.GPIO as GPIO
import time
import sys
import numpy  # sudo apt-get python-numpy

class HX711:
    def __init__(self, dout, pd_sck, gain=128):
        self.PD_SCK = pd_sck
        self.DOUT = dout

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PD_SCK, GPIO.OUT)
        GPIO.setup(self.DOUT, GPIO.IN)

        self.GAIN = 0
        self.REFERENCE_UNIT = 1  # The value returned by the hx711 that corresponds to your reference unit AFTER dividing by the SCALE.
        
        self.OFFSET = 1
        self.lastVal = long(0)

        # [start, stop, step]
        self.LSByte = [2, -1, -1]
        self.MSByte = [0, 3, 1]
        
        self.MSBit = [0, 8, 1]
        self.LSBit = [7, -1, -1]

        self.byte_range_values = self.LSByte
        self.bit_range_values = self.MSBit

        self.set_gain(gain)

        time.sleep(1)

    # From the data sheet, if DOUT is high, no data transmitted.
    # For data to be transmitted, DOUT needs to be low
    def is_ready(self):
        return GPIO.input(self.DOUT) == 0

    def set_gain(self, gain):
        if gain is 128:
            self.GAIN = 1
        elif gain is 64:
            self.GAIN = 3
        elif gain is 32:
            self.GAIN = 2

        GPIO.output(self.PD_SCK, False)
        self.read()
    
    def createBoolList(self, size=8):
        ret = []
        for i in range(8):
            ret.append(False)
        return ret

    def read(self):
        while not self.is_ready():
            #print("WAITING")
            pass

        dataBits = [self.createBoolList(), self.createBoolList(), self.createBoolList()]
        dataBytes = [0x0] * 4

        for j in range(self.byte_range_values[0], self.byte_range_values[1], self.byte_range_values[2]):
            for i in range(self.bit_range_values[0], self.bit_range_values[1], self.bit_range_values[2]):
                GPIO.output(self.PD_SCK, True)
                dataBits[j][i] = GPIO.input(self.DOUT)
                GPIO.output(self.PD_SCK, False)
            dataBytes[j] = numpy.packbits(numpy.uint8(dataBits[j]))

        #set channel and gain factor for next reading
        for i in range(self.GAIN):
            GPIO.output(self.PD_SCK, True)
            GPIO.output(self.PD_SCK, False)

        #check for all 1
        #if all(item is True for item in dataBits[0]):
        #    return long(self.lastVal)

        dataBytes[2] ^= 0x80

        return dataBytes
    """
    # I think we should be alright deleting this function
    # From here:
    def get_binary_string(self):
        binary_format = "{0:b}"
        np_arr8 = self.read_np_arr8()
        binary_string = ""
        for i in range(4):
            # binary_segment = binary_format.format(np_arr8[i])
            binary_segment = format(np_arr8[i], '#010b')
            binary_string += binary_segment + " "
        return binary_string

    def get_np_arr8_string(self):
        np_arr8 = self.read_np_arr8()
        np_arr8_string = "[";
        comma = ", "
        for i in range(4):
            if i is 3:
                comma = ""
            np_arr8_string += str(np_arr8[i]) + comma
        np_arr8_string += "]";
        
        return np_arr8_string
    # To Here
    """
    def read_np_arr8(self):
        dataBytes = self.read()
        np_arr8 = numpy.uint8(dataBytes)

        return np_arr8

    def read_long(self):
        np_arr8 = self.read_np_arr8()
        np_arr32 = np_arr8.view('uint32')
        self.lastVal = np_arr32

        return long(self.lastVal)

    def read_average(self, times=3):
        values = 0
        for i in range(times):
            values += self.read_long()

        return values / times

    def get_value(self, times=3):
        return self.read_average(times) - self.OFFSET

    def get_weight(self, times=3):
        value = self.get_value(times)
        value = value / self.REFERENCE_UNIT
        return value

    def tare(self, times=15):
       
        # Backup REFERENCE_UNIT value
        reference_unit = self.REFERENCE_UNIT
        self.set_reference_unit(1)

        value = self.read_average(times)
        self.set_offset(value)

        self.set_reference_unit(reference_unit)

    def set_reading_format(self, byte_format="LSB", bit_format="MSB"):
        if byte_format == "LSB":
            self.byte_range_values = self.LSByte
        elif byte_format == "MSB":
            self.byte_range_values = self.MSByte

        if bit_format == "LSB":
            self.bit_range_values = self.LSBit
        elif bit_format == "MSB":
            self.bit_range_values = self.MSBit

    def set_offset(self, offset):
        self.OFFSET = offset

    def set_reference_unit(self, reference_unit):
        self.REFERENCE_UNIT = reference_unit

    # HX711 datasheet states that setting the PDA_CLOCK pin on high for a more than 60 microseconds would power off the chip.
    # I used 100 microseconds, just min case.
    # I've found it is good practice to reset the hx711 if it wasn't used for more than a few seconds.
    def power_down(self):
        GPIO.output(self.PD_SCK, False)
        GPIO.output(self.PD_SCK, True)
        time.sleep(0.0001)

    def power_up(self):
        GPIO.output(self.PD_SCK, False)
        time.sleep(0.0001)

    def reset(self):
        self.power_down()
        self.power_up()

    # Try this: main prog calls this, stores current value, gets new value
    # returns new value if the current value is the same as previous value
    def call_this(self):
        current_val = 0
        pre_val = 0
        if current_val != pre_val or current_val<=0:
            # saves the previous value from scale
            pre_val = current_val
            # gets the new value from scale
            current_val = self.get_weight(5) 
            print("current reading: "+str(current_val)+"g")
            time.sleep(0.5)
            if current_val<0:
                self.tare()
                
        elif current_val == pre_val and current_val > 0:
            current_value = current_val
            return current_value
            self.power_down()
            self.power_up()


        
