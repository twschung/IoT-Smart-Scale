#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

@author: Bastian Raschke <bastian.raschke@posteo.de>
"""

import os
import serial
import Image

import utilities


## Baotou start byte
FINGERPRINT_STARTCODE = 0xEF01

## Packet identification
##

FINGERPRINT_COMMANDPACKET = 0x01

FINGERPRINT_ACKPACKET = 0x07
FINGERPRINT_DATAPACKET = 0x02
FINGERPRINT_ENDDATAPACKET = 0x08

## Instruction codes
##

FINGERPRINT_VERIFYPASSWORD = 0x13
FINGERPRINT_SETPASSWORD = 0x12
FINGERPRINT_SETADDRESS = 0x15
FINGERPRINT_SETSYSTEMPARAMETER = 0x0E
FINGERPRINT_GETSYSTEMPARAMETERS = 0x0F
FINGERPRINT_TEMPLATEINDEX = 0x1F
FINGERPRINT_TEMPLATECOUNT = 0x1D

FINGERPRINT_READIMAGE = 0x01

## Note: The documentation mean upload to host computer.
FINGERPRINT_DOWNLOADIMAGE = 0x0A

FINGERPRINT_CONVERTIMAGE = 0x02

FINGERPRINT_CREATETEMPLATE = 0x05
FINGERPRINT_STORETEMPLATE = 0x06
FINGERPRINT_SEARCHTEMPLATE = 0x04
FINGERPRINT_LOADTEMPLATE = 0x07
FINGERPRINT_DELETETEMPLATE = 0x0C

FINGERPRINT_CLEARDATABASE = 0x0D
FINGERPRINT_GENERATERANDOMNUMBER = 0x14
FINGERPRINT_COMPARECHARACTERISTICS = 0x03

## Note: The documentation mean download from host computer.
FINGERPRINT_UPLOADCHARACTERISTICS = 0x09

## Note: The documentation mean upload to host computer.
FINGERPRINT_DOWNLOADCHARACTERISTICS = 0x08

## Packet reply confirmations
##

FINGERPRINT_OK = 0x00
FINGERPRINT_ERROR_COMMUNICATION = 0x01

FINGERPRINT_ERROR_WRONGPASSWORD = 0x13

FINGERPRINT_ERROR_INVALIDREGISTER = 0x1A

FINGERPRINT_ERROR_NOFINGER = 0x02
FINGERPRINT_ERROR_READIMAGE = 0x03

FINGERPRINT_ERROR_MESSYIMAGE = 0x06
FINGERPRINT_ERROR_FEWFEATUREPOINTS = 0x07
FINGERPRINT_ERROR_INVALIDIMAGE = 0x15

FINGERPRINT_ERROR_CHARACTERISTICSMISMATCH = 0x0A

FINGERPRINT_ERROR_INVALIDPOSITION = 0x0B
FINGERPRINT_ERROR_FLASH = 0x18

FINGERPRINT_ERROR_NOTEMPLATEFOUND = 0x09

FINGERPRINT_ERROR_LOADTEMPLATE = 0x0C

FINGERPRINT_ERROR_DELETETEMPLATE = 0x10

FINGERPRINT_ERROR_CLEARDATABASE = 0x11

FINGERPRINT_ERROR_NOTMATCHING = 0x08

FINGERPRINT_ERROR_DOWNLOADIMAGE = 0x0F
FINGERPRINT_ERROR_DOWNLOADCHARACTERISTICS = 0x0D

## Unknown error codes
##

FINGERPRINT_ADDRCODE = 0x20
FINGERPRINT_PASSVERIFY = 0x21

FINGERPRINT_PACKETRESPONSEFAIL = 0x0E

FINGERPRINT_ERROR_TIMEOUT = 0xFF
FINGERPRINT_ERROR_BADPACKET = 0xFE


class PyFingerprint(object):
    """
    A python written library for the ZhianTec ZFM-20 fingerprint sensor.

    @attribute integer(4 bytes) __address
    Address to connect to sensor.

    @attribute integer(4 bytes) __password
    Password to connect to sensor.

    @attribute Serial __serial
    UART serial connection via PySerial.
    """
    __address = None
    __password = None
    __serial = None

    def __init__(self, port = '/dev/ttyUSB0', baudRate = 57600, address = 0xFFFFFFFF, password = 0x00000000):
        """
        Constructor

        @param string port
        @param integer baudRate
        @param integer(4 bytes) address
        @param integer(4 bytes) password
        """

        if ( os.path.exists(port) == False ):
            raise ValueError('The fingerprint sensor port "' + port + '" was not found!')

        if ( baudRate < 9600 or baudRate > 115200 or baudRate % 9600 != 0 ):
            raise ValueError('The given baudrate is invalid!')

        if ( address < 0x00000000 or address > 0xFFFFFFFF ):
            raise ValueError('The given address is invalid!')

        if ( password < 0x00000000 or password > 0xFFFFFFFF ):
            raise ValueError('The given password is invalid!')

        self.__address = address
        self.__password = password

        ## Initialize PySerial connection
        self.__serial = serial.Serial(port = port, baudrate = baudRate, bytesize = serial.EIGHTBITS, timeout = 2)

        if ( self.__serial.isOpen() == True ):
            self.__serial.close()

        self.__serial.open()

    def __del__(self):
        """
        Destructor

        """

        ## Close connection if still established
        if ( self.__serial is not None and self.__serial.isOpen() == True ):
            self.__serial.close()

    def __writePacket(self, packetType, packetPayload):
        """
        Send a packet to fingerprint sensor.

        @param integer(1 byte) packetType
        @param tuple packetPayload

        @return void
        """

        ## Write header (one byte at once)
        self.__serial.write(utilities.byteToString(utilities.rightShift(FINGERPRINT_STARTCODE, 8)))
        self.__serial.write(utilities.byteToString(utilities.rightShift(FINGERPRINT_STARTCODE, 0)))

        self.__serial.write(utilities.byteToString(utilities.rightShift(self.__address, 24)))
        self.__serial.write(utilities.byteToString(utilities.rightShift(self.__address, 16)))
        self.__serial.write(utilities.byteToString(utilities.rightShift(self.__address, 8)))
        self.__serial.write(utilities.byteToString(utilities.rightShift(self.__address, 0)))

        self.__serial.write(utilities.byteToString(packetType))

        ## The packet length = package payload (n bytes) + checksum (2 bytes)
        packetLength = len(packetPayload) + 2

        self.__serial.write(utilities.byteToString(utilities.rightShift(packetLength, 8)))
        self.__serial.write(utilities.byteToString(utilities.rightShift(packetLength, 0)))

        ## The packet checksum = packet type (1 byte) + packet length (2 bytes) + payload (n bytes)
        packetChecksum = packetType + utilities.rightShift(packetLength, 8) + utilities.rightShift(packetLength, 0)

        ## Write payload
        for i in range(0, len(packetPayload)):
            self.__serial.write(utilities.byteToString(packetPayload[i]))
            packetChecksum += packetPayload[i]

        ## Write checksum (2 bytes)
        self.__serial.write(utilities.byteToString(utilities.rightShift(packetChecksum, 8)))
        self.__serial.write(utilities.byteToString(utilities.rightShift(packetChecksum, 0)))

    def __readPacket(self):
        """
        Receive a packet from fingerprint sensor.

        Return a tuple that contain the following information:
        0: integer(1 byte) The packet type.
        1: integer(n bytes) The packet payload.

        @return tuple
        """

        receivedPacketData = []
        i = 0

        while ( True ):

            ## Read one byte
            receivedFragment = self.__serial.read()

            if ( len(receivedFragment) != 0 ):
                receivedFragment = utilities.stringToByte(receivedFragment)
                ## print 'Received packet fragment = ' + hex(receivedFragment)

            ## Insert byte if packet seems valid
            receivedPacketData.insert(i, receivedFragment)
            i += 1

            ## Packet could be complete (the minimal packet size is 12 bytes)
            if ( i >= 12 ):

                ## Check the packet header
                if ( receivedPacketData[0] != utilities.rightShift(FINGERPRINT_STARTCODE, 8) or receivedPacketData[1] != utilities.rightShift(FINGERPRINT_STARTCODE, 0) ):
                    raise Exception('The received packet do not begin with a valid header!')

                ## Calculate packet payload length (combine the 2 length bytes)
                packetPayloadLength = utilities.leftShift(receivedPacketData[7], 8)
                packetPayloadLength = packetPayloadLength | utilities.leftShift(receivedPacketData[8], 0)

                ## Check if the packet is still fully received
                ## Condition: index counter < packet payload length + packet frame
                if ( i < packetPayloadLength + 9 ):
                    continue

                ## At this point the packet should be fully received

                packetType = receivedPacketData[6]

                ## Calculate checksum:
                ## checksum = packet type (1 byte) + packet length (2 bytes) + packet payload (n bytes)
                packetChecksum = packetType + receivedPacketData[7] + receivedPacketData[8]

                packetPayload = []

                ## Collect package payload (ignore the last 2 checksum bytes)
                for j in range(9, 9 + packetPayloadLength - 2):
                    packetPayload.append(receivedPacketData[j])
                    packetChecksum += receivedPacketData[j]

                ## Calculate full checksum of the 2 separate checksum bytes
                receivedChecksum = utilities.leftShift(receivedPacketData[i - 2], 8)
                receivedChecksum = receivedChecksum | utilities.leftShift(receivedPacketData[i - 1], 0)

                if ( receivedChecksum != packetChecksum ):
                    raise Exception('The received packet is corrupted (the checksum is wrong)!')

                return (packetType, packetPayload)

    def verifyPassword(self):
        """
        Verifie password of the fingerprint sensor.

        @return boolean
        """

        packetPayload = (
            FINGERPRINT_VERIFYPASSWORD,
            utilities.rightShift(self.__password, 24),
            utilities.rightShift(self.__password, 16),
            utilities.rightShift(self.__password, 8),
            utilities.rightShift(self.__password, 0),
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Sensor password is correct
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        ## DEBUG: Sensor password is wrong
        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_WRONGPASSWORD ):
            return False

        else:
            raise Exception('Unknown error')

    def setPassword(self, newPassword):
        """
        Set the password of the sensor.

        @param integer(4 bytes) newPassword
        @return boolean
        """

        ## Validate the password (maximum 4 bytes)
        if ( newPassword < 0x00000000 or newPassword > 0xFFFFFFFF ):
            raise ValueError('The given password is invalid!')

        packetPayload = (
            FINGERPRINT_SETPASSWORD,
            utilities.rightShift(newPassword, 24),
            utilities.rightShift(newPassword, 16),
            utilities.rightShift(newPassword, 8),
            utilities.rightShift(newPassword, 0),
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Password set was successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        else:
            raise Exception('Unknown error')

    def setAddress(self, newAddress):
        """
        Set the module address of the sensor.

        @param integer(4 bytes) newAddress
        @return boolean
        """

        ## Validate the address (maximum 4 bytes)
        if ( newAddress < 0x00000000 or newAddress > 0xFFFFFFFF ):
            raise ValueError('The given address is invalid!')

        packetPayload = (
            FINGERPRINT_SETADDRESS,
            utilities.rightShift(newAddress, 24),
            utilities.rightShift(newAddress, 16),
            utilities.rightShift(newAddress, 8),
            utilities.rightShift(newAddress, 0),
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Address set was successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        else:
            raise Exception('Unknown error')

    def setSystemParameter(self, parameterNumber, parameterValue):
        """
        Sets a system parameter of the sensor.

        @param integer(1 byte) parameterNumber
        @param integer(1 byte) parameterValue
        @return boolean
        """

        ## Validate the baudrate parameter
        if ( parameterNumber == 4 ):

            if ( parameterValue < 1 or parameterValue > 12 ):
                raise ValueError('The given baudrate parameter is invalid!')

        ## Validate the security level parameter
        elif ( parameterNumber == 5 ):

            if ( parameterValue < 1 or parameterValue > 5 ):
                raise ValueError('The given security level parameter is invalid!')

        ## Validate the package length parameter
        elif ( parameterNumber == 6 ):

            if ( parameterValue < 0 or parameterValue > 3 ):
                raise ValueError('The given package length parameter is invalid!')

        ## The parameter number is not valid
        else:
            raise ValueError('The given parameter number is invalid!')

        packetPayload = (
            FINGERPRINT_SETSYSTEMPARAMETER,
            parameterNumber,
            parameterValue,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Parameter set was successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_INVALIDREGISTER ):
            raise Exception('Invalid register number')

        else:
            raise Exception('Unknown error')

    def getSystemParameters(self):
        """
        Get all available system information of the sensor.

        Return a tuple that contain the following information:
        0: integer(2 bytes) The status register.
        1: integer(2 bytes) The system id.
        2: integer(2 bytes) The storage capacity.
        3: integer(2 bytes) The security level.
        4: integer(4 bytes) The sensor address.
        5: integer(2 bytes) The packet length.
        6: integer(2 bytes) The baudrate.

        @return tuple
        """

        packetPayload = (
            FINGERPRINT_GETSYSTEMPARAMETERS,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Read successfully
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):

            statusRegister     = utilities.leftShift(receivedPacketPayload[1], 8) | utilities.leftShift(receivedPacketPayload[2], 0)
            systemID           = utilities.leftShift(receivedPacketPayload[3], 8) | utilities.leftShift(receivedPacketPayload[4], 0)
            storageCapacity    = utilities.leftShift(receivedPacketPayload[5], 8) | utilities.leftShift(receivedPacketPayload[6], 0)
            securityLevel      = utilities.leftShift(receivedPacketPayload[7], 8) | utilities.leftShift(receivedPacketPayload[8], 0)
            deviceAddress      = ((receivedPacketPayload[9] << 8 | receivedPacketPayload[10]) << 8 | receivedPacketPayload[11]) << 8 | receivedPacketPayload[12] ## TODO
            packetLength       = utilities.leftShift(receivedPacketPayload[13], 8) | utilities.leftShift(receivedPacketPayload[14], 0)
            baudRate           = utilities.leftShift(receivedPacketPayload[15], 8) | utilities.leftShift(receivedPacketPayload[16], 0)

            return (statusRegister, systemID, storageCapacity, securityLevel, deviceAddress, packetLength, baudRate)

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        else:
            raise Exception('Unknown error')

    def getTemplateIndex(self, page):
        """
        Get a list of the template positions with usage indicator.

        @param integer(1 byte) page
        @return list
        """

        if ( page < 0 or page > 3 ):
            raise ValueError('The given index page is invalid!')

        packetPayload = (
            FINGERPRINT_TEMPLATEINDEX,
            page,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Read index table successfully
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):

            templateIndex = []

            ## Contain the table page bytes (skip the first status byte)
            pageElements = receivedPacketPayload[1:]

            for pageElement in pageElements:
                ## Test every bit (bit = template position is used indicator) of a table page element
                for p in range(0, 7 + 1):
                    positionIsUsed = (utilities.bitAtPosition(pageElement, p) == 1)
                    templateIndex.append(positionIsUsed)

            return templateIndex

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        else:
            raise Exception('Unknown error')

    def getTemplateCount(self):
        """
        Get the number of stored templates.

        @return integer(2 bytes)
        """

        packetPayload = (
            FINGERPRINT_TEMPLATECOUNT,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Read successfully
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            templateCount = utilities.leftShift(receivedPacketPayload[1], 8)
            templateCount = templateCount | utilities.leftShift(receivedPacketPayload[2], 0)
            return templateCount

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        else:
            raise Exception('Unknown error')

    def readImage(self):
        """
        Read the image of a finger and stores it in ImageBuffer.

        @return boolean
        """

        packetPayload = (
            FINGERPRINT_READIMAGE,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Image read successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        ## DEBUG: No finger found
        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_NOFINGER ):
            return False

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_READIMAGE ):
            raise Exception('Could not read image')

        else:
            raise Exception('Unknown error')

    ## TODO:
    ## Implementation of uploadImage()

    def downloadImage(self, imageDestination):
        """
        Download the image of a finger to host computer.

        @param string imageDestination
        @return void
        """

        destinationDirectory = os.path.dirname(imageDestination)

        if ( os.access(destinationDirectory, os.W_OK) == False ):
            raise ValueError('The given destination directory "' + destinationDirectory + '" is not writable!')

        packetPayload = (
            FINGERPRINT_DOWNLOADIMAGE,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)

        ## Get first reply packet
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: The sensor will sent follow-up packets
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            pass

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_DOWNLOADIMAGE ):
            raise Exception('Could not download image')

        else:
            raise Exception('Unknown error')

        ## Initialize image library
        resultImage = Image.new('L', (256, 288), 'white')
        pixels = resultImage.load()

        ## Y coordinate of current pixel
        line = 0

        ## Get follow-up data packets until the last data packet is received
        while ( receivedPacketType != FINGERPRINT_ENDDATAPACKET ):

            receivedPacket = self.__readPacket()

            receivedPacketType = receivedPacket[0]
            receivedPacketPayload = receivedPacket[1]

            if ( receivedPacketType != FINGERPRINT_DATAPACKET and receivedPacketType != FINGERPRINT_ENDDATAPACKET ):
                raise Exception('The received packet is no data packet!')

            ## X coordinate of current pixel
            x = 0

            for i in range(0, len(receivedPacketPayload)):

                ## Thanks to Danylo Esterman <soundcracker@gmail.com> for the "multiple with 17" improvement:

                ## Draw left 4 Bits one byte of package
                pixels[x, line] = (receivedPacketPayload[i] >> 4) * 17
                x = x + 1

                ## Draw right 4 Bits one byte of package
                pixels[x, line] = (receivedPacketPayload[i] & 0b00001111) * 17
                x = x + 1

            line = line + 1

        resultImage.save(imageDestination)

    def convertImage(self, charBufferNumber = 0x01):
        """
        Convert the image in ImageBuffer to finger characteristics and store in CharBuffer1 or CharBuffer2.

        @param integer(1 byte) charBufferNumber
        @return boolean
        """

        if ( charBufferNumber != 0x01 and charBufferNumber != 0x02 ):
            raise ValueError('The given charbuffer number is invalid!')

        packetPayload = (
            FINGERPRINT_CONVERTIMAGE,
            charBufferNumber,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Image converted
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_MESSYIMAGE ):
            raise Exception('The image is too messy')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_FEWFEATUREPOINTS ):
            raise Exception('The image contains too few feature points')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_INVALIDIMAGE ):
            raise Exception('The image is invalid')

        else:
            raise Exception('Unknown error')

    def createTemplate(self):
        """
        Combine the characteristics which are stored in CharBuffer1 and CharBuffer2 to a template.
        The created template will be stored again in CharBuffer1 and CharBuffer2 as the same.

        @return boolean
        """

        packetPayload = (
            FINGERPRINT_CREATETEMPLATE,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Template created successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        ## DEBUG: The characteristics not matching
        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_CHARACTERISTICSMISMATCH ):
            return False

        else:
            raise Exception('Unknown error')

    def storeTemplate(self, positionNumber = -1, charBufferNumber = 0x01):
        """
        Save a template from the specified CharBuffer to the given position number.

        @param integer(2 bytes) positionNumber
        @param integer(1 byte) charBufferNumber
        @return integer
        """

        ## Find a free index
        if ( positionNumber == -1 ):
            for page in range(0, 4):
                ## Free index found?
                if ( positionNumber >= 0 ):
                    break

                templateIndex = self.getTemplateIndex(page)

                for i in range(0, len(templateIndex)):
                    ## Index not used?
                    if ( templateIndex[i] == False ):
                        positionNumber = (len(templateIndex) * page) + i
                        break

        if ( positionNumber < 0x0000 or positionNumber >= self.getStorageCapacity() ):
            raise ValueError('The given position number is invalid!')

        if ( charBufferNumber != 0x01 and charBufferNumber != 0x02 ):
            raise ValueError('The given charbuffer number is invalid!')

        packetPayload = (
            FINGERPRINT_STORETEMPLATE,
            charBufferNumber,
            utilities.rightShift(positionNumber, 8),
            utilities.rightShift(positionNumber, 0),
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Template stored successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return positionNumber

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_INVALIDPOSITION ):
            raise Exception('Could not store template in that position')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_FLASH ):
            raise Exception('Error writing to flash')

        else:
            raise Exception('Unknown error')

    def searchTemplate(self):
        """
        Search the finger characteristiccs in CharBuffer in database.

        Return a tuple that contain the following information:
        0: integer(2 bytes) The position number of found template.
        1: integer(2 bytes) The accuracy score of found template.

        @return tuple
        """

        ## CharBuffer1 and CharBuffer2 are the same in this case
        charBufferNumber = 0x01

        ## Begin search at index 0
        positionStart = 0x0000
        templatesCount = self.getStorageCapacity()

        packetPayload = (
            FINGERPRINT_SEARCHTEMPLATE,
            charBufferNumber,
            utilities.rightShift(positionStart, 8),
            utilities.rightShift(positionStart, 0),
            utilities.rightShift(templatesCount, 8),
            utilities.rightShift(templatesCount, 0),
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Found template
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):

            positionNumber = utilities.leftShift(receivedPacketPayload[1], 8)
            positionNumber = positionNumber | utilities.leftShift(receivedPacketPayload[2], 0)

            accuracyScore = utilities.leftShift(receivedPacketPayload[3], 8)
            accuracyScore = accuracyScore | utilities.leftShift(receivedPacketPayload[4], 0)

            return (positionNumber, accuracyScore)

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        ## DEBUG: Did not found a matching template
        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_NOTEMPLATEFOUND ):
            return (-1, -1)

        else:
            raise Exception('Unknown error')

    def loadTemplate(self, positionNumber, charBufferNumber = 0x01):
        """
        Load an existing template specified by position number to specified CharBuffer.

        @param integer(2 bytes) positionNumber
        @param integer(1 byte) charBufferNumber
        @return boolean
        """

        if ( positionNumber < 0x0000 or positionNumber >= self.getStorageCapacity() ):
            raise ValueError('The given position number is invalid!')

        if ( charBufferNumber != 0x01 and charBufferNumber != 0x02 ):
            raise ValueError('The given charbuffer number is invalid!')

        packetPayload = (
            FINGERPRINT_LOADTEMPLATE,
            charBufferNumber,
            utilities.rightShift(positionNumber, 8),
            utilities.rightShift(positionNumber, 0),
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Template loaded successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_LOADTEMPLATE ):
            raise Exception('The template could not be read')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_INVALIDPOSITION ):
            raise Exception('Could not load template from that position')

        else:
            raise Exception('Unknown error')

    def deleteTemplate(self, positionNumber):
        """
        Delete one template from fingerprint database.

        @param integer(2 bytes) positionNumber
        @return boolean
        """

        if ( positionNumber < 0x0000 or positionNumber >= self.getStorageCapacity() ):
            raise ValueError('The given position number is invalid!')

        ## Delete only one template
        count = 0x0001

        packetPayload = (
            FINGERPRINT_DELETETEMPLATE,
            utilities.rightShift(positionNumber, 8),
            utilities.rightShift(positionNumber, 0),
            utilities.rightShift(count, 8),
            utilities.rightShift(count, 0),
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Template deleted successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        ## DEBUG: Could not delete template
        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_DELETETEMPLATE ):
            return False

        else:
            raise Exception('Unknown error')

    def clearDatabase(self):
        """
        Clear the complete template database.

        @return boolean
        """

        packetPayload = (
            FINGERPRINT_CLEARDATABASE,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Database cleared successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            return True

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        ## DEBUG: Could not clear database
        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_CLEARDATABASE ):
            return False

        else:
            raise Exception('Unknown error')

    def compareCharacteristics(self):
        """
        Compare the finger characteristics of CharBuffer1 with CharBuffer2 and return the accuracy score.

        @return integer(2 bytes)
        """

        packetPayload = (
            FINGERPRINT_COMPARECHARACTERISTICS,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: Comparation successful
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            accuracyScore = utilities.leftShift(receivedPacketPayload[1], 8)
            accuracyScore = accuracyScore | utilities.leftShift(receivedPacketPayload[2], 0)
            return accuracyScore

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        ## DEBUG: The characteristics do not matching
        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_NOTMATCHING ):
            return 0

        else:
            raise Exception('Unknown error')

    def uploadCharacteristics(self, charBufferNumber = 0x01, characteristicsData = [0]):
        """
        Upload finger characteristics to CharBuffer1 or CharBuffer2.

        @author: David Gilson <davgilson@live.fr>

        @param integer(1 byte) charBufferNumber
        @param integer(list) characteristicsData

        @return boolean
        Return true if everything is right.
        """

        if ( charBufferNumber != 0x01 and charBufferNumber != 0x02 ):
            raise ValueError('The given charbuffer number is invalid!')

        if ( characteristicsData == [0] ):
            raise ValueError('The characteristics data is required!')

        maxPacketSize = self.getMaxPacketSize()

        ## Upload command

        packetPayload = (
            FINGERPRINT_UPLOADCHARACTERISTICS,
            charBufferNumber
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)

        ## Get first reply packet
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: The sensor will sent follow-up packets
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            pass

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        elif ( receivedPacketPayload[0] == FINGERPRINT_PACKETRESPONSEFAIL ):
            raise Exception('Could not upload characteristics')

        else:
            raise Exception('Unknown error')

        ## Upload data packets
        packetNbr = len(characteristicsData) / maxPacketSize

        if ( packetNbr <= 1 ):
            self.__writePacket(FINGERPRINT_ENDDATAPACKET, characteristicsData)
        else:
            i = 1
            while ( i < packetNbr ):
                lfrom = (i-1) * maxPacketSize
                lto = lfrom + maxPacketSize
                self.__writePacket(FINGERPRINT_DATAPACKET, characteristicsData[lfrom:lto])
                i += 1

            lfrom = (i-1) * maxPacketSize
            lto = lfrom + maxPacketSize
            self.__writePacket(FINGERPRINT_ENDDATAPACKET, characteristicsData[lfrom:lto])

        ## Verify uploaded characteristics
        characterics = self.downloadCharacteristics(charBufferNumber)
        return (characterics == characteristicsData)

    def getMaxPacketSize(self):
        """
        Get the maximum allowed size of packet by sensor.

        @author: David Gilson <davgilson@live.fr>

        @return int
        Return the max size. Default 32 bytes.
        """

        packetMaxSizeType = self.getSystemParameters()[5]

        if (packetMaxSizeType == 1):
            return 64
        elif (packetMaxSizeType == 2):
            return 128
        elif (packetMaxSizeType == 3):
            return 256
        else:
            return 32

    def getStorageCapacity(self):
        """
        Gets the sensor storage capacity.

        @return int
        The storage capacity.
        """

        return self.getSystemParameters()[2]

    def generateRandomNumber(self):
        """
        Generates a random 32-bit decimal number.

        @author: Philipp Meisberger <team@pm-codeworks.de>

        @return int
        The generated random number
        """
        packetPayload = (
            FINGERPRINT_GENERATERANDOMNUMBER,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            pass

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        else:
            raise Exception('Unknown error')

        number = 0
        number = number | utilities.leftShift(receivedPacketPayload[1], 24)
        number = number | utilities.leftShift(receivedPacketPayload[2], 16)
        number = number | utilities.leftShift(receivedPacketPayload[3], 8)
        number = number | utilities.leftShift(receivedPacketPayload[4], 0)
        return number

    def downloadCharacteristics(self, charBufferNumber = 0x01):
        """
        Download the finger characteristics of CharBuffer1 or CharBuffer2.

        @param integer(1 byte) charBufferNumber

        @return list
        Return a list that contains 512 integer(1 byte) elements of the characteristic.
        """

        if ( charBufferNumber != 0x01 and charBufferNumber != 0x02 ):
            raise ValueError('The given charbuffer number is invalid!')

        packetPayload = (
            FINGERPRINT_DOWNLOADCHARACTERISTICS,
            charBufferNumber,
        )

        self.__writePacket(FINGERPRINT_COMMANDPACKET, packetPayload)

        ## Get first reply packet
        receivedPacket = self.__readPacket()

        receivedPacketType = receivedPacket[0]
        receivedPacketPayload = receivedPacket[1]

        if ( receivedPacketType != FINGERPRINT_ACKPACKET ):
            raise Exception('The received packet is no ack packet!')

        ## DEBUG: The sensor will sent follow-up packets
        if ( receivedPacketPayload[0] == FINGERPRINT_OK ):
            pass

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_COMMUNICATION ):
            raise Exception('Communication error')

        elif ( receivedPacketPayload[0] == FINGERPRINT_ERROR_DOWNLOADCHARACTERISTICS ):
            raise Exception('Could not download characteristics')

        else:
            raise Exception('Unknown error')

        completePayload = []

        ## Get follow-up data packets until the last data packet is received
        while ( receivedPacketType != FINGERPRINT_ENDDATAPACKET ):

            receivedPacket = self.__readPacket()

            receivedPacketType = receivedPacket[0]
            receivedPacketPayload = receivedPacket[1]

            if ( receivedPacketType != FINGERPRINT_DATAPACKET and receivedPacketType != FINGERPRINT_ENDDATAPACKET ):
                raise Exception('The received packet is no data packet!')

            for i in range(0, len(receivedPacketPayload)):
                completePayload.append(receivedPacketPayload[i])

        return completePayload
