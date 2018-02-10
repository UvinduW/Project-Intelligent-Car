# pc_gamepad_test.py
# Created: 2017.11.29
# Uvindu Wijesinghe and Oliver Wilkins
#
# Description:
# Connect to the gamepad.
# Print the value of axis 0 (left analog stick).
#
# Usage:
#

import pygame
from time import sleep

# Setup the pygame library
pygame.init()
pygame.joystick.init()
j_count = pygame.joystick.get_count()

# Set the gamepad to be the first one found
gamepad = pygame.joystick.Joystick(0)
gamepad.init()

while True:
    # Refresh the values from gamepad
    pygame.event.pump()
    
    # Get and print the value from axis 0 (left analog stick)
    zero_axis_pos = gamepad.get_axis(0)
    print zero_axis_pos
    sleep(0.1)
    