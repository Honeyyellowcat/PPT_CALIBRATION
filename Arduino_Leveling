#include <AccelStepper.h>

const int stepPin = 2; // Step pin connected to Arduino digital pin 2
const int dirPin = 3;  // Direction pin connected to Arduino digital pin 3

AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin); // Stepper motor object

void setup() {
  stepper.setMaxSpeed(1000); // Set maximum speed
  stepper.setAcceleration(500); // Set acceleration
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  stepper.run(); // Continuously run the stepper motor

  if (Serial.available() > 0) { // Check if there's serial data available
    char command = Serial.read(); // Read the command sent from Python
    
    // Check the command received
    switch (command) {
      case 'A': // Forward 100 steps
        moveForward(100);
        break;
      case 'B': // Backward 100 steps
        moveBackward(100);
        break;
    }
  }
}

void moveForward(int steps) {
  stepper.moveTo(steps); // Move forward by the specified number of steps
}

void moveBackward(int steps) {
  stepper.moveTo(-steps); // Move backward by the specified number of steps
}
