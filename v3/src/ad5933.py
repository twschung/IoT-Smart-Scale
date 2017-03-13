import smbus
import math, time, numpy
import csv

### Register Map ###
# Control Register
CNTRL_1=0x80
CNTRL_2=0x81
# Start Frequency Register
START_FREQ_1=0x82
START_FREQ_2=0x83
START_FREQ_3=0x84
# Frequency Increment Register
FREQ_INC_1=0x85
FREQ_INC_2=0x86
FREQ_INC_3=0x87
# Number of Increments Register
NUM_FREQ_1=0x88
NUM_FREQ_2=0x89
# Number of Settling Time Cycles Register
SETTL_CYCL_1=0x8A
SETTL_CYCL_2=0x8B
# Status Register
STATUS_REG=0x8F
# Temp Data Register
TEMP_1=0x92
TEMP_2=0x93
# Real Data Register
REAL_1=0x94
REAL_2=0x95
# Imaginary Data Register
IMAG_1=0x96
IMAG_2=0x97

bus = smbus.SMBus(1)

DEV_ADD = 0x0D

class AD5933:
	resistance_list = []
	admittance_list = []
	real_dsp_list = []
	imag_dsp_list = []
	
	run_num = 0
	result_num = 0
	def __init__(self, gainFactor, sysPhase, numSamples):
		self.GAIN_FACTOR = gainFactor
		self.SYSTEM_PHASE = sysPhase
		self.samples_num  = numSamples
	
	def POWER_DOWN(self):
		##Power-Down (ie 1010 0000)	
		bus.write_byte_data(DEV_ADD, CNTRL_1, bus.read_byte_data(DEV_ADD,CNTRL_1)&0x07 | 0xA0)
		print('Power-Down Command Issued')
	def SET_START_FREQ(self):
		bus.write_byte_data(DEV_ADD, START_FREQ_1, 0x0E) #186A73 @ 50kHz
		bus.write_byte_data(DEV_ADD, START_FREQ_2, 0xA6) 
		bus.write_byte_data(DEV_ADD, START_FREQ_3, 0x45)
	def SET_NUM_OF_INCREMENTS(self):
		bus.write_byte_data(DEV_ADD, NUM_FREQ_1, 0x00)  #0096 @ 150 increments #00C8 @ 200 increments
		bus.write_byte_data(DEV_ADD, NUM_FREQ_2, 0x00) 
	def SET_FREQ_INCREMENT(self):
		bus.write_byte_data(DEV_ADD, FREQ_INC_1, 0x00)  #00014F @10hz #000140 @10hz(16,776mhz)
		bus.write_byte_data(DEV_ADD, FREQ_INC_2, 0x3E)  #004189 @500hz #003E81 @500hz (16,776mhz)
		bus.write_byte_data(DEV_ADD, FREQ_INC_3, 0x81)
	def STNBY_MODE(self):
		bus.write_byte_data(DEV_ADD, CNTRL_1, bus.read_byte_data(DEV_ADD,CNTRL_1)&0x07 |0xB0)
	def INIT_START_FREQ_CMD(self):
		bus.write_byte_data(DEV_ADD, CNTRL_1, bus.read_byte_data(DEV_ADD,CNTRL_1)&0x07 |0x10)
	def START_FREQ_SWEEP(self):
		bus.write_byte_data(DEV_ADD, CNTRL_1, bus.read_byte_data(DEV_ADD,CNTRL_1)&0x07 |0x20)
	def READ_TEMP(self):
		bus.write_byte_data(DEV_ADD, CNTRL_1, bus.read_byte_data(DEV_ADD,CNTRL_1)&0x07 |0x90)
	def SETTLE_TIME_CYCLE(self):
		bus.write_byte_data(DEV_ADD, SETTL_CYCL_1, 0x01) #0x07
		bus.write_byte_data(DEV_ADD, SETTL_CYCL_2, 0xFF) #0x4F
	def SET_OPERATING_RANGE(self, op_range):
		if op_range == 1:
			bus.write_byte_data(DEV_ADD, CNTRL_1, 0x01)  # Setting this to Range 1 (i.e. 00 (D10 and D9)
			print("Operating in Range 1")
		elif op_range == 2:
			bus.write_byte_data(DEV_ADD, CNTRL_1, 0x07)  # Setting this to Range 2 (i.e. 11 (D10 and D9)
			print("Operating in Range 2")
		elif op_range == 3:
			bus.write_byte_data(DEV_ADD, CNTRL_1, 0x05)  # Setting this to Range 3 (i.e. 10 (D10 and D9)
			print("Operating in Range 3")
		elif op_range == 4:
			bus.write_byte_data(DEV_ADD, CNTRL_1, 0x03)  # Setting this to Range 4 (i.e. 01 (D10 and D9)
			print("Operating in Range 4")
		else:
			print("Error: SET_OPERATION_RANGE Failed")
	
	def MEASURE_IMPEDANCE(self):
		self.SET_START_FREQ()
		self.SET_NUM_OF_INCREMENTS()
		self.SET_FREQ_INCREMENT()
		self.STNBY_MODE()
		self.INIT_START_FREQ_CMD()
		self.START_FREQ_SWEEP()
		
		while True:
			self.run_num += 1
			self.STATUS = bus.read_byte_data(DEV_ADD,STATUS_REG)
			# Status 0000 0010 - Valid Real/Imag Data
			if (self.STATUS & 0x02) == 2:
				self.result_num += 1
				
				UNINT_REAL = (bus.read_byte_data(DEV_ADD, REAL_1) << 8)|bus.read_byte_data(DEV_ADD, REAL_2)
				UNINT_IMAG = (bus.read_byte_data(DEV_ADD, IMAG_1) << 8)|bus.read_byte_data(DEV_ADD, IMAG_2)
				SIGNED_REAL = -((UNINT_REAL)&0x8000)|(UNINT_REAL&0x7fff)
				SIGNED_IMAG = -((UNINT_IMAG)&0x8000)|(UNINT_IMAG&0x7fff)
				MAGNITUDE = math.sqrt((SIGNED_IMAG**2)+(SIGNED_REAL**2))
				Z_PHASE = math.atan2(SIGNED_IMAG, SIGNED_REAL) - self.SYSTEM_PHASE
				
				impedance = (1/(MAGNITUDE*self.GAIN_FACTOR))
				resistance = impedance * math.cos(Z_PHASE)
				admittance = impedance * math.sin(Z_PHASE)
				
				self.real_dsp_list.append(int(SIGNED_REAL))
				self.imag_dsp_list.append(int(SIGNED_IMAG))
				self.resistance_list.append(int(resistance))
				self.admittance_list.append(int(admittance))
				
				
				if (self.STATUS & 0x04) != 4: #Status Register of 0000 0100 - Freq Sweep Complete
					### increment frequency ###
					#cont_reg = bus.read_byte_data(DEV_ADD,CNTRL_1)
					#cont_reg_inc_buffer = cont_reg | (0x03 << 4)
					#bus.write_byte_data (DEV_ADD, CNTRL_1, cont_reg_inc_buffer)
					#print('CNTRL_1\AFT INC FREQ: %s'%bin(bus.read_byte_data(DEV_ADD,CNTRL_1)))
					#print('Status: %s'%(bin(status)))
					
					### repeat frequency ###
					cont_reg = bus.read_byte_data(DEV_ADD,CNTRL_1)
					cont_reg_buffer = cont_reg&0x07 |(0b0100 << 4)
					bus.write_byte_data (DEV_ADD, CNTRL_1, cont_reg_buffer)
					#print('CNTRL_1\AFTER REPEAT FREQ: %s'%bin(bus.read_byte_data(DEV_ADD,CNTRL_1)))
					#print('Status: %s'%(bin(status)))
					
					if (self.result_num == self.samples_num):
						self.average_imag = numpy.mean(self.admittance_list)
						self.average_real = numpy.mean(self.resistance_list)
						self.average_dsp_real = numpy.mean(self.real_dsp_list)
						self.average_dsp_imag = numpy.mean(self.imag_dsp_list)
						print('|Re{Z} (average)|:%.2f Ohm' %(self.average_real))
						print('|Im{Z} (average)|:%.2f Ohm' %(self.average_imag))
						self.cumulative_impedance = math.sqrt((self.average_real**2) + (self.average_imag**2))
						print('|Z (average)|:%.2f Ohm' %(self.cumulative_impedance))#/(self.samples_num)))
						self.POWER_DOWN()
						break
					
					elif (self.STATUS & 0x04) == 4:
						self.POWER_DOWN()
						break
			elif (self.STATUS & 0x02) != 2:
				pass
			
		return [self.average_dsp_real, self.average_dsp_imag, self.average_real, self.average_imag]
	
def READ_REG_VALUES():
	print('CNTRL_1: %s'%bin(bus.read_byte_data(DEV_ADD,CNTRL_1)))
	print('CNTRL_2: %s'%bin(bus.read_byte_data(DEV_ADD,CNTRL_2)))
	print('')
	print('START_FREQ_1: %s'%bin(bus.read_byte_data(DEV_ADD,START_FREQ_1)))
	print('START_FREQ_2: %s'%bin(bus.read_byte_data(DEV_ADD,START_FREQ_2)))
	print('START_FREQ_3: %s'%bin(bus.read_byte_data(DEV_ADD,START_FREQ_3)))
	print('')
	print('FREQ_INC_1: %s'%bin(bus.read_byte_data(DEV_ADD,FREQ_INC_1)))
	print('FREQ_INC_2: %s'%bin(bus.read_byte_data(DEV_ADD,FREQ_INC_2)))
	print('FREQ_INC_3: %s'%bin(bus.read_byte_data(DEV_ADD,FREQ_INC_3)))
	print('')
	print('NUM_FREQ_1: %s'%bin(bus.read_byte_data(DEV_ADD,NUM_FREQ_1)))
	print('NUM_FREQ_2: %s'%bin(bus.read_byte_data(DEV_ADD,NUM_FREQ_2)))
	print('')
	print('SETTL_CYCL_1: %s'%bin(bus.read_byte_data(DEV_ADD,SETTL_CYCL_1)))
	print('SETTL_CYCL_2: %s'%bin(bus.read_byte_data(DEV_ADD,SETTL_CYCL_2)))
	print('')
	print('STATUS_REG: %s'%bin(bus.read_byte_data(DEV_ADD,STATUS_REG)))
	print('')
	print('TEMP_1: %s'%bin(bus.read_byte_data(DEV_ADD,TEMP_1)))
	print('TEMP_2: %s'%bin(bus.read_byte_data(DEV_ADD,TEMP_2)))
	print('')
	print('REAL_1: %s'%bin(bus.read_byte_data(DEV_ADD,REAL_1)))
	print('REAL_2: %s'%bin(bus.read_byte_data(DEV_ADD,REAL_2)))
	print('')
	print('IMAG_1: %s'%bin(bus.read_byte_data(DEV_ADD,IMAG_1)))
	print('IMAG_2: %s'%bin(bus.read_byte_data(DEV_ADD,IMAG_2)))
