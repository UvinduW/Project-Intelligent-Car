/* arduino_control_test.ino
 * Created: 2017.11.08
 * Uvindu Wijesinghe and Oliver Wilkins
 * 
 * Description:
 * This program allows the user to send steering and throttle PWM values to the ESC
 *  in order to test the communication between the Arduino and the ESC.
 * This program can be used to find the PWM value range required for steering.
 * This program can also be used to calbrate the ESC by sending maximum and 
 *  minimum throttle PWM values.
 *  
 * Usage:
 * After flashing the script, the motor speed and steering angle can be provided 
 *  over serial by entering them into the Arduino Command Window.
 * The input format is <motor_speed> <turn_angle> where each parameter
 *  is between 0 and 180 and the two parameters are seperated by a space.
 * Example: Set the speed to 80 and steering angle to 120
 *          Command window input: 80 120
 */

/*
 * Steering values used for our car:
 * Full lock left: 70
 * Central: [further testing required]
 * Full lock right: 135
 * 
 * Throttle values used for our car:
 * Full speed forward: 0 [further testing required]
 * Neutral: 90 [further testing required]
 * Full speed reverse: 180 [further testing required]
 */

#include <Servo.h>

// Create two servo objects
Servo steering_servo;
Servo driving_servo;

// Specify arduino pins used
int steering_pin = 9;
int driving_pin = 8;

// Variables for throttle and steering position
int drive_speed;
int turn_angle;

void setup() {
  // Start serial monitor
  Serial.begin(9600);

  // Attach steering and driving motors as servos
  steering_servo.attach(steering_pin);
  driving_servo.attach(driving_pin);
}

// Continuously send steering and throttle values to the ESC
void loop() {
  if (Serial.available() > 0) {
    // Read values from serial
    drive_speed = Serial.parseInt();
    turn_angle = Serial.parseInt();

    // Print values to serial
    Serial.print("Speed: ");
    Serial.print(drive_speed);
    Serial.println();
    Serial.print("Turn: ");
    Serial.print(turn_angle);
    Serial.println();

    // Write values to servo
    steering_servo.write(turn_angle);
    driving_servo.write(drive_speed);
  }
}

