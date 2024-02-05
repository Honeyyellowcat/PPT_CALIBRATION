import tkinter as tk # Importing the tkinter library for GUI DAQ_Python.py
from tkinter import ttk # Importing themed widgets from tkinter for a modern look and feel
import nidaqmx # Importing nidaqmx for interacting with National Instruments Data Acquisition hardware
import numpy as np # Importing numpy for numerical computing
import matplotlib.pyplot as plt # Importing matplotlib.pyplot for plotting and visualization
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Importing FigureCanvasTkAgg from matplotlib.backends.backend_tkagg for embedding matplotlib figures in Tkinter GUIs
import serial # Importing serial for serial communication
import pandas as pd # Importing pandas for data manipulation and analysis

# Global variables for raw deflection data and uncertainties
deflection_data = []
uncertainties = []

# Function to record raw deflection data from the rangefinder
def record_deflection():
    global deflection_data
    try:
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan("your_channel")
            task.timing.cfg_samp_clk_timing(rate=1000, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS)
            deflection_data = task.read(number_of_samples_per_channel=1000)  # Recording Deflection Data

    except nidaqmx.DaqError as e:
        print(f"DAQ Error: {e}")
        print(f"Error Code: {e.error_code}")
        print(f"Error Details: {e.__cause__}")

# Function to convert deflection measurements to thrust measurements
def convert_to_thrust():
    global deflection_data, uncertainties
    try:
        # Perform Calibration
        calibration_force = 0.01  # Calibrating to 10 micronewtons (0.01 Newtons)
        measured_deflection = 50  # Example measured deflection in units

        # Calculate sensitivity
        sensitivity = measured_deflection / calibration_force

        # Apply calibration to convert deflection measurements to thrust measurements
        thrust_data = deflection_data * sensitivity

        # Set uncertainties to a fixed value
        uncertainties = np.full_like(thrust_data, 0.05)  # Set uncertainties to 0.05 for all measurements

    except Exception as e:
        print(f"An error occurred during conversion: {e}")

# Function to display deflection measurements and corresponding uncertainties graphically
def display_graph():
    global deflection_data, uncertainties
    try:
        # Plot data with uncertainties
        fig = plt.figure(figsize=(8, 6))
        plt.errorbar(np.arange(len(deflection_data)), deflection_data, yerr=uncertainties, fmt='o', ecolor='red', capsize=5)
        plt.xlabel('Time')
        plt.ylabel('Deflection')
        plt.title('Deflection Measurements with Uncertainties')
        plt.grid(True)

        # Save the plot as an image
        fig.savefig('deflection_plot.png')

        # Display the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred during graph display: {e}")

# Function to export figures and raw data
def export_data():
    global deflection_data, uncertainties
    try:
        # Save raw data to a CSV file
        df = pd.DataFrame({'Deflection': deflection_data, 'Uncertainties': uncertainties})
        df.to_csv('C:/Users/every/OneDrive/Desktop/CODE/PPT/raw_data.csv', index=False)

        print("Raw data exported successfully.")

    except Exception as e:
        print(f"An error occurred during data export: {e}")

# Create main window
root = tk.Tk()
root.title("Deflection Data Analysis")

# Create frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=5)

# Create buttons for recording, converting, and displaying data
record_button = ttk.Button(button_frame, text="Record Deflection", command=record_deflection)
record_button.grid(row=0, column=0, padx=5)

convert_button = ttk.Button(button_frame, text="Convert to Thrust", command=convert_to_thrust)
convert_button.grid(row=0, column=1, padx=5)

plot_button = ttk.Button(button_frame, text="Display Graph", command=display_graph)
plot_button.grid(row=0, column=2, padx=5)

export_button = ttk.Button(button_frame, text="Export Data", command=export_data)
export_button.grid(row=0, column=3, padx=5)

# Create quit button
quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=5)

root.mainloop()
