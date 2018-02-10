# rpi_gamepad_receive_test.py
# Created: 2018.02.09
# Uvindu Wijesinghe and Oliver Wilkins
#
# Description:
# Opens a serial connection with the Arduino.
# Creates a socket object for communication with the PC.
# Continuously receives gamepad data from the PC and sends it to the Pi.
#
# Usage:
# Simply start this program and the corresponding PC and Arduino programs.
#

import serial
import socket

# Set IP and port.
ip_address = "192.168.0.22"
local_address = "0.0.0.0"
port = 8000

# Open a serial connection with the Arduino.
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Create a socket object for control signal transmission.
socket_control = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the IP and port to the socket object.
socket_control.bind((local_address, port))

while True:
    # Receive control strings over the socket from the PC.
    data, addr = socket_control.recvfrom(1024)
    
    # Print the messages and send them to the Arduino.
    print "Message: ", data
    arduino.write(str(data).encode())
