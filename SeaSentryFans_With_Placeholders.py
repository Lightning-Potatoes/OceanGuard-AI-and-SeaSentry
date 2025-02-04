
# Online IDE - Code Editor, Compiler, Interpreteimport RPi.GPIO as GPIO
import time

# Define GPIO pins (Replace these with actual GPIO numbers)
IR_SENSOR_PIN = XX  # GPIO pin for the infrared sensor

# Define fan control GPIO pins (Replace with actual pins)
FAN_PINS = [YY1, YY2, YY3, YY4, YY5, YY6]  

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)  # Set sensor pin as input

# Set all fan pins as output
for pin in FAN_PINS:
    GPIO.setup(pin, GPIO.OUT)

def control_fans(state):
    """Turn all fans ON or OFF based on the state."""
    for pin in FAN_PINS:
        GPIO.output(pin, state)

def check_sensor():
    """Check the IR sensor and control all fans accordingly."""
    try:
        while True:
            if GPIO.input(IR_SENSOR_PIN) == 0:  # Object detected within range
                control_fans(GPIO.HIGH)  # Turn all fans on
                print("Object detected! Fans ON.")
            else:
                control_fans(GPIO.LOW)  # Turn all fans off
                print("No object. Fans OFF.")
            time.sleep(0.1)  # Small delay to avoid rapid switching
    except KeyboardInterrupt:
        print("Exiting program.")
        GPIO.cleanup()  # Reset GPIO on exit

# Run the function
check_sensor()

