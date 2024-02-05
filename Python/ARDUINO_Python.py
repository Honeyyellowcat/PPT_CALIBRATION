import serial  # Package for serial communication
import serial.tools.list_ports  # Package for listing available serial ports
from tkinter import *  # Importing all modules from tkinter
import tkinter as tk  # Importing tkinter and aliasing it as 'tk'

# Defining the variables
motRun = "1" # Motor activation flag
indexA =  "A" # Data start marker
indexB =  "B" # Speed identifier
indexC =  "C" # Angle identifier
indexD =  "D" # Direction marker 
newLine = "\n" # New line marker

# Define variables for low-pass filter
alpha = 0.1
filtered_speed = 0

# Here we are defining the serial port and opening up before sending any data
serialInst = None
portVal = "/dev/cu.usbmodem11101"

try:
    import serial
    serialInst = serial.Serial(portVal, 9600)
    print(f"Serial port {portVal} opened successfully.")
except serial.SerialException as e:
    print(f"Failed to open serial port {portVal}: {e}")

# Low-pass filter 
def low_pass_filter(current_speed):
    global filtered_speed
    filtered_speed = alpha * current_speed + (1 - alpha) * filtered_speed
    return filtered_speed

# Sending the data to Serial Port
def sendData(motDir):
    global filtered_speed
    if serialInst:
        serialInst.write(motRun.encode('utf-8'))
        serialInst.write(indexA.encode('utf-8'))

        motSpeedInt = slider.get()
        motSpeedFiltered = int(low_pass_filter(motSpeedInt))
        motSpeed = str(motSpeedFiltered)
        serialInst.write(motSpeed.encode('utf-8'))
        serialInst.write(indexB.encode('utf-8'))

        motAngle = angleSet.get()
        if motAngle != "":
            serialInst.write(motAngle.encode('utf-8'))
            serialInst.write(indexC.encode('utf-8'))
        else:
            textAngle.config(text = "Please input angle")
            root.after(1000, textAngleReset)
            print("Please input angle")
        
        serialInst.write(motDir.encode('utf-8'))
        serialInst.write(indexD.encode('utf-8'))
        
        serialInst.write(newLine.encode('utf-8'))

        confirmTransfer()

        print("Data Sent")
    else:
        print("Serial port not available.")

# Showing confirmation message that the data has been sent in GUI
def confirmTransfer():
    canvas.itemconfig(confirm_text, text = "Data Sent")
    root.after(1000, confirmTransferReset)

# Resetting the confirmation message 
def confirmTransferReset():
    canvas.itemconfig(confirm_text, text = "")
# Resetting the message that request the user to input angle
def textAngleReset():
    textAngle.config(text = "")

# Functions to enable clockwise and anticlockwise rotation and to initiate the transmission of data to serial
def RotateClockwise():
    motDir = "Clockwise"
    sendData(motDir)
def RotateAnticlockwise():
    motDir = "Anticlockwise"
    sendData(motDir)

# GUI configuration
root = Tk()
root.title("Arduino Controller")

# GUI layout
# Set the width and height of the canvas
canvas_width = 600
canvas_height = 450
# creating the image for the GUI
motor_img = PhotoImage(file=r"C:\Users\every\OneDrive\Desktop\CODE\StepperMotor_ROHS.png")
canvas = Canvas(width=canvas_width, height=canvas_height)  # Adjust width and height as needed
canvas.create_image(canvas_width/2, canvas_height/2, image=motor_img)  # Center the image
canvas.grid(row=0, column=0, columnspan=2)
confirm_text = canvas.create_text(canvas_width/2, canvas_height/2, text="", fill="red", font=("Courier", 20, "bold"))  # Center the text
# Creating a label and slider to control the speed of the motor
speedLabel = Label(root, text="Speed (in RPM)")
speedLabel.grid(row=1, column=0)
slider = Scale(root, from_=1, to=9, length=300, tickinterval=1, orient=HORIZONTAL)
slider.set(4)
slider.grid(row=2, column=0, columnspan=2)
# Creating a label and entry box to set the angle of rotation for the motor
angleLabel = Label(root, text="Angle (in deg)")
angleLabel.grid(row=3, column=0)
angleSet = Entry(root, width=10)
angleSet.grid(row=3, column=1)
# Creating the text box, which activates when no angle input available
textAngle = Label(root, text="", fg="red")
textAngle.grid(row=4, column=1)
# Creating the buttons to set the direction of the rotation and to transmit data to the serial
btn_forward = tk.Button(root, text="Clockwise", command=RotateClockwise)
btn_forward.grid(row=5, column=0)

btn_backward = tk.Button(root, text="Anticlockwise", command=RotateAnticlockwise)
btn_backward.grid(row=5, column=1)
# Defining the size of the window and looping through to maintain the interface
root.geometry(f"{canvas_width}x{canvas_height + 200}")  # Adjust height to accommodate buttons and labels
root.mainloop()
