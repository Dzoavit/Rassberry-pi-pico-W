from machine import Pin
import time

led = Pin("LED", Pin.OUT) #set it as a output and setting the action pin to onbroad led

while True: 
    led.value(1)  #turn it on
    time.sleep(1) #The timer after which the next line will execute
        
    led.value(0)  #turn it off
    time.sleep(1) #The timer after which the next line will execute