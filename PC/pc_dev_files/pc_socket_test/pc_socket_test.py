# pc_socket_test.py
# Created: 2018.02.09
# Uvindu Wijesinghe and Oliver Wilkins
#
# Description:
# Sets up a UDP socket to facilitate communication between
#  the PC and an RPi.
# Waits to receive a message from the Pi and then sends one back.
#
# Usage:
# Start this program, and then run the corresponding program on 
#  the Pi: rpi_socket_test.py
#

import socket


ip_address = "0.0.0.0"
port = 8000
message = "received"

# Create a socket object (UDP) for message transmission.
socket_control = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the IP and port to the socket object.
socket_control.bind((ip_address, port))

# Wait to receive data over the created socket.
data, addr = socket_control.recvfrom(1024)

# Print the data and the address it was sent from.
print "Message: ", data, ", Address: ", addr

# Send a message back to confirm receipt.
socket_control.sendto(message, addr)
