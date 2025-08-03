from machine import Pin #import pin leb
import time #imports time

led = Pin("LED", Pin.OUT) #creates a variable called led(set it as a output pin and setting the action pin to onbroad led)

while True: 
    led.value(1)  #turn it on
    time.sleep(1) #The timer after which the next line will execute
        
    led.value(0)  #turn it off
    time.sleep(1) #The timer after which the next line will execute