# rpi_sockets_test.py
# Created: 2018.02.09
# Uvindu Wijesinghe and Oliver Wilkins
#
# Description:
# Sets up a UDP socket to facilitate communication between
#  the RPi and a PC.
# Sends a message to the PC, and then receives one back.
#
# Usage:
# Start the corresponding program on the PC (pc_socket_test.py),
#  then start this program on the Pi.
#

import socket


ip_address = "192.168.0.22"
local_address = "0.0.0.0"
port = 8000
message = "Hello, Server"

# Create a socket object (UDP) for message transmission.
socket_control = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the IP and port to the socket object.
socket_control.bind((local_address, port))

# Send an initial message to the specified IP.
socket_control.sendto(message, (ip_address, port))

# Wait to receive a reply.
data, addr = socket_control.recvfrom(1024)

# Print the reply.
print "Message: ", data
