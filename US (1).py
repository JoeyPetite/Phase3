import RPi.GPIO as GPIO
import time

trig = 18
echo = 24
servo = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
    GPIO.output(trig,True) 
    time.sleep(0.0001)
    GPIO.output(trig, False)
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(echo) ==0:
        StartTime = time.time()
        
    while GPIO.input(echo) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    distance = TimeElapsed*34300/65
    
    return distance

while True:
    straightdistance = distance()
    print("Distance Forward is",straightdistance,"Feet")
    time.sleep(5)
