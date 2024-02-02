# Driving Requirements ━━ ♡ ━━
- Recording Deflection Data The software captures raw deflection data from the rangefinder.
- Conversion of Measurements It converts deflection measurements into thrust measurements along with their respective uncertainties.
- Graphical Display: The software presents deflection measurements and their uncertainties graphically. It supports exporting both figures and raw data.
- Calibration System: The thrust stand requires an integrated calibration system capable of calibrating to 10 micronewtons.

# Design - Python Overview
## PySerial: ━━ ♡ ━━
- ୨୧ Python library enabling communication between the computer and external hardware, such as the Arduino.
- ୨୧ Instructs the Arduino to perform tasks like moving a stepper motor a certain number of steps.
- ୨୧ Defines variables for motor control flags and markers
- ୨୧ Sets a newline character for message termination.
- ୨୧ Attempts to open the specified serial port at a baud rate of 9600.
- ୨୧ `sendData()` function structures and sends motor control commands over the serial port.
- ୨୧ Commands include motor activation flag, speed, angle, direction, and newline termination.
- ୨୧ Employs an EMI low pass filter to control the smoothing effect of the filter.

## NI-DAQmx / nidaqmx: ━━ ♡ ━━
- ୨୧ Facilitates communication with the NI DAQ-6009 device provided by National Instruments.
- ୨୧ Controls and interacts with DAQ devices for data acquisition, control, and configuration.
- ୨୧ Facilitates communication with the NI DAQ-6009 device.
- ୨୧ Integration with PySerial allows interaction with DAQ for data acquisition, control, and configuration.

## Graphical User Interface (GUI) Tkinter: ━━ ♡ ━━
- ୨୧ Ideal for simple GUI applications, emphasizing basic user interaction and data display.
- ୨୧ Simplifies user interaction and data presentation in Python applications.
- ୨୧ Utilizes Tkinter to create a graphical user interface for motor control.
- ୨୧ Includes widgets such as sliders, entry boxes, labels, and buttons for user interaction.

# Design - Arduino Overview ━━ ♡ ━━
- Serial Communication: ୨୧ Arduino communicates with the computer via a serial port. ୨୧ Commands from the computer control the stepper motor.
- Parameter Conversion: ୨୧ Received parameters are converted for motor control: speed is converted to a delay between steps, and angle to the number of steps required for rotation.
- Stepper Motor Control: ୨୧ Four digital output pins interface with the stepper motor's driver.
- Motor Operation: ୨୧ Loop continuously checks for incoming data. ୨୧ Parsed parameters determine motor speed, angle, and direction.
- Motor Control Functions: ୨୧ `stepper_Anticlockwise()` and `stepper_Clockwise()` control motor rotation.
- Data Processing: ୨୧ The `Parse_the_Data()` function extracts and parses parameters from the received string.

# Test Objective - Calibration ━━ ♡ ━━
- Electrostatic Fin Connection: ୨୧ Facilitates communication with the electrostatic fin for precise control and manipulation.
- Laser Displacement Sensing: ୨୧ Utilizes laser displacement sensing technology integrated with the NI DAQ-6009 device.
- Displacement Measurement: ୨୧ Enables accurate measurement of displacements in real-time.

# Summary ━━ ♡ ━━
This project integrates Python, Arduino, and NI DAQ technologies to control a thrust stand, record deflection data, and perform calibration. 
It employs PySerial and NI-DAQmx/nidaqmx for communication and data acquisition, while Tkinter provides a user-friendly interface. 
The system ensures precise measurement and control of thrust parameters for various applications.
