from machine import Pin  # Import Pin class from machine module to control GPIO
import time              # Import time module for delays

# Initialize the onboard LED (usually labeled "LED") as an output pin
led = Pin("LED", Pin.OUT)

# Initialize GPIO pin 15 as an input pin for the button
button = Pin(15, Pin.IN)

# Start an infinite loop
while True:
    if button.value() == 1:     # If button is pressed (value is HIGH)
        led.on()                # Turn the LED on
        time.sleep(0.1)             # Small delay to debounce and reduce CPU usage
    else:
        led.off()               # Otherwise, turn the LED off
        time.sleep(0.1)             # Small delay to debounce and reduce CPU usage
