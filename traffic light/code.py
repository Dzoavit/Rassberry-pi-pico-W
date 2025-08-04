from machine import Pin #import pin leb
import time #imports time

ledy = Pin(17, Pin.OUT) #creates a variable called ledy(set it as a output pin)
ledr = Pin(16, Pin.OUT) #creates a variable called ledr(set it as a output pin)
ledg = Pin(15, Pin.OUT) #creates a variable called ledg(set it as a output pin)

while True: 
    ledg.value(1)  #turn it on
    time.sleep(1) #The timer after which the next line will execute
    ledg.value(0)  #turn it off
    
    ledy.value(0.25)  #turn it on
    time.sleep(1) #The timer after which the next line will execute
    ledy.value(0)  #turn it off
    
    ledr.value(0.75)  #turn it on
    time.sleep(1) #The timer after which the next line will execute
    ledr.value(0)  #turn it off