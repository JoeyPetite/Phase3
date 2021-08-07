import RPi.GPIO as GPIO
import time

servo = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
Servo1 = GPIO.PWM(servo,50)
Servo1.start(0)

def servo(angle):
    #Rotate Servo 90 Degrees to the Left.
    if angle == 0:
        Servo1.ChangeDutyCycle(2.5)
    #Rotate Servo 90 Degrees to the Middle.
    if angle == 90:
        Servo1.ChangeDutyCycle(7.5)
    #Rotate Servo 90 Degrees to the Right.
    if angle == 180:
        Servo1.ChangeDutyCycle(12.5)
        
while True:
    print("Rotating to Left")
    time.sleep(1)
    servo(0)
    time.sleep(1)
    print("Rotating to Middle")
    time.sleep(1)
    servo(90)
    time.sleep(1)
    print("Rotating to Right")
    time.sleep(1)
    servo(180)
    time.sleep(1)