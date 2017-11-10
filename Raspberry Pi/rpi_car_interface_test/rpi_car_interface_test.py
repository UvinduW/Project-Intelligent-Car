# rpi_car_interface_test.py
# Created: 2017.11.10
# Uvindu Wijesinghe and Oliver Wilkins
#
# Description:
# This program sets up a serial port and allows the Raspberry Pi to
#  send data to the Arduino that is connected to the USB port.
# This can be used to control the driving speed and steering input
#  of the car
#
# Usage:
# Set the speed and angle parameters as desired. Ensure they are
#  between 0 and 180.
# Once set, run the script to send the instruction to the Arduino
#
# Note: ttyUSB0 is the bottom right USB port on our Raspberry Pi
#
# TODO: Limit input values
# TODO: Get user input from command line and loop

import serial

# Start a serial connection with the Arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Enter variables
speed = 90
angle = 90

# Combines instructions as <drive_speed><turn_angle> and pads both
# variables with zeros so that they are 3 characters long each
instruction = str(speed).zfill(3) + str(angle).zfill(3)

# Print resulting instruction to user
print (instruction)

# Send instruction to Arduino
arduino.write(instruction.encode())