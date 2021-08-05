import RPi.GPIO as GPIO
import time

trig = 18
echo = 24
servo = 12

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
    distance = TimeElapsed*34300/60
    
    return distance


def servo(angle):
    if angle == 0:
        Servo1.ChangeDutyCycle(2.5)
    if angle == 90:
        Servo1.ChangeDutyCycle(7.5)
    if angle == 180:
        Servo1.ChangeDutyCycle(12.5)

servo(180)
time.sleep(1)

leftdistance = distance()
print(leftdistance)
time.sleep(1.5)

servo(0)
time.sleep(1)

rightdistance = distance()
print(rightdistance)
time.sleep(1.5)

servo(90)
time.sleep(1)

straightdistance = distance()
print(straightdistance)
time.sleep(1.5)

