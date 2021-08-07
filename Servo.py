import RPi.GPIO as GPIO
import time

trig = 18
echo = 24
servo = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(servo, GPIO.OUT)
Servo1 = GPIO.PWM(servo,50)
Servo1.start(0)            

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


def servo(angle):
    if angle == 0:
        Servo1.ChangeDutyCycle(2.5)
    if angle == 90:
        Servo1.ChangeDutyCycle(7.5)
    if angle == 180:
        Servo1.ChangeDutyCycle(12.5)
  
while True:
    
    print("Rotating to Left")
    servo(0)
    time.sleep(1)

    leftdistance = distance()
    print("Distance Forward is",leftdistance,"Feet")
    time.sleep(1.5)

    print("Rotating to the Middle")
    servo(90)
    time.sleep(1)

    middledistance = distance()
    print("Distance Forward is",middledistance,"Feet")
    time.sleep(1.5)

    print("Rotating to the Right")
    servo(180)
    time.sleep(1)

    rightdistance = distance()
    print("Distance Forward is",rightdistance,"Feet")
    time.sleep(1.5)

