# Project Intelligent Car
*This project is in the early stages of development*

__Description:__

This project aims to implement autonomous capabilities with a convolutional neural network (CNN) and machine vision on a modified RC car, using a Raspberry Pi and an Arduino, written in Python and C, and utilising the TensorFlow and OpenCV libraries.

__Current state:__

The RC car can be controlled from the PC using a connected gamepad. The gamepad commands are read by the script running on the PC and sent over the local wireless network to a Raspberry Pi that is mounted on the car. The Raspberry Pi receives this information and sends it to the Arduino connected to it. The Arduino is connected directly to the ESC and steering servo of the car, and uses the instructions it receives to control the motion of the car.
