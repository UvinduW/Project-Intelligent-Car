# pc_gamepad_transmit_test.py
# Created: 2018.02.09
# Uvindu Wijesinghe and Oliver Wilkins
#
# Description:
# Connect to the gamepad.
# Open a socket for PC-RPi communication.
# Read values from three gamepad axes (steering, forward, reverse).
# Create a message string and transmit this over the socket.
#
# Usage:
# Simply start this program and the corresponding RPi program, ensuring
#  the Arduino has been flashed and is on.
#

import socket
import pygame
from time import sleep

# Name the gamepad axes.
axis_steer = 0
axis_forwards = 4
axis_reverse = 5

# Initialise flags and throttle value.
forwards_moved = 0
reverse_moved = 0
reverse_engaged = 0
throttle = "090"

# Set IP and port.
ip_address = "192.168.0.32"
port = 8000

# Create a socket object (UDP) for message transmission.
socket_control = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Setup the pygame library
pygame.init()
pygame.joystick.init()
j_count = pygame.joystick.get_count()

# Set the gamepad to be the first one found
gamepad = pygame.joystick.Joystick(1)
gamepad.init()

while True:
    # Refresh the values from gamepad
    pygame.event.pump()
    
    # Get the steering angle from axis0. Round, scale, and shift it, make it a three-char string.
    steer_angle = str(int(round(gamepad.get_axis(axis_steer)*90 + 90, 0))).zfill(3)
    
    # Latch the forwards_moved flag if the forward gamepad axis ever moves from zero.
    if gamepad.get_axis(axis_forwards) != 0:
        forwards_moved = 1

    # Latch the reverse_moved flag if the reverse gamepad axis ever moves from zero.
    if gamepad.get_axis(axis_reverse) != 0:
        reverse_moved = 1

    # Start calculating throttle values once the throttle has been moved once.
    if forwards_moved == 1:
        # Read the forward axis and calculate a throttle value, rounded, scaled, shifted, stringed, extended.
        throttle = str(90 - int(round(gamepad.get_axis(axis_forwards)*45 + 45, 0))).zfill(3)

    # If the reverse trigger is pressed at all, override throttle value with this value.
    if reverse_moved == 1 and gamepad.get_axis(axis_reverse) != -1:
        # Read the reverse axis and calculate a throttle value, rounded, scaled, shifted, stringed, extended.
        throttle = str(90 + int(round(gamepad.get_axis(axis_reverse)*45 + 45, 0))).zfill(3)

    # Create a string to transmit over the socket.
    transmission_string = throttle + steer_angle

    # Print and send the string.
    print transmission_string
    socket_control.sendto(transmission_string, (ip_address, port))
    sleep(0.1)
    