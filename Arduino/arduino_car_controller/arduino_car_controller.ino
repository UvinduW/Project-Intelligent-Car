/* arduino_control_test.ino
 * Created: 2017.11.08
 * Uvindu Wijesinghe and Oliver Wilkins
 * 
 * Description:
 * This program allows the user to send steering and throttle PWM values to the ESC
 *  over Serial in order to control the vehicle's motion.
 * The intended use is for a connected Raspberry Pi to send control instructions
 *  to the car, allowing it to behave appropriately.
 * This program can be used to find the PWM value range required for steering.
 * This program can also be used to calbrate the ESC by sending maximum and 
 *  minimum throttle PWM values.
 *  
 * Usage:
 * After flashing the script, the motor speed and steering angle can be provided 
 *  over serial by entering them into the Arduino Command Window.
 * The input format is <motor_speed><turn_angle> where each parameter
 *  is between 0 and 180 and the two parameters are three characters long each
 *  with zero padding.
 * Example: Set the speed to 80 and steering angle to 120
 *          Command window input: 080120
 * 
 * Note: Serial prints should be commented out when not debugging
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

// Variables to hold received data
int received_data;
int instruction[6];
int array_index = 0;

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
    // Read data from serial, one character at a time
    received_data = Serial.read();

    // Convert string value to corresponding integer value
    received_data = received_data - 48;

    // Add value to instruction array & increment index
    instruction[array_index] = received_data;
    array_index++;
  }
  
  // If a full set of instructions has been received then process it
  if (array_index >= 6){
    // Obtain the drive speed and the turn angle using the elements of the matrix
    drive_speed = 100 * instruction[0] + 10 * instruction[1] + instruction[2];
    turn_angle = 100 * instruction[3] + 10 * instruction[4] + instruction[5];

    // If values are out of bounds, assume error and return to neutral position
    if ( (drive_speed>180) || (drive_speed<0) || (turn_angle>180) || (turn_angle<0) ){
      drive_speed = 90;
      turn_angle = 90;
    }

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

    // Initialise array index to obtain next set of instructions
    array_index = 0;

  }
}

