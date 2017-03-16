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
	cumulative_impedance = 0
	cumulative_real = 0
	cumulative_imag = 0
	cumulative_resistance = 0
	cumulative_admittance = 0
	
	run_num = 0
	result_num = 0
	def __init__(self, gainFactor, sysPhase, numSamples):
		self.GAIN_FACTOR = gainFactor
		self.SYSTEM_PHASE = sysPhase
		self.samples_num  = numSamples
	
	def POWER_DOWN(self):
		##Power-Down (ie 1010 0000)	
		bus.write_byte_data(DEV_ADD, CNTRL_1, bus.read_byte_data(DEV_ADD,CNTRL_1)&0x07 | 0xA0)
		# print('Power-Down Command Issued')
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
		bus.write_byte_data(DEV_ADD, CNTRL_1,bus.read_byte_data(DEV_ADD,CNTRL_1)&0x07 |0x20)

	####
	##	Other funtions such as set PGA Gain, Settling Time Cycle, Range of Operation, Read Temperature
	####
	
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
				
				self.cumulative_impedance += impedance
				self.cumulative_real += resistance
				self.cumulative_imag += admittance
				# Status 0000 0100 - Freq Sweep Complete
				if (self.STATUS & 0x04) != 4:
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
						print('|Re{Z} (average)|:%.2f Ohm' %(self.cumulative_real/(self.samples_num)))
						print('|Im{Z} (average)|:%.2f Ohm' %(self.cumulative_imag/(self.samples_num)))
						print('|Z (average)|:%.2f Ohm' %(self.cumulative_impedance/(self.samples_num)))
						self.POWER_DOWN()
						break
					
					elif (self.STATUS & 0x04) == 4:
						self.POWER_DOWN()
						break
			elif (self.STATUS & 0x02) != 2:
				pass
			
		#return [self.cumulative_real, cumulative_imag]
