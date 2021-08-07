import RPi.GPIO as GPIO
import time

#================================== 
#Define Variables
motorR1 = 19
motorR2 = 26
motorL1 = 20
motorL2 = 21

#General Setup
GPIO.setwarnings(False)
motorState = 0
GPIO.setmode(GPIO.BCM)
#DC Motors Setup
GPIO.setup(motorR1,GPIO.OUT)
GPIO.setup(motorR2,GPIO.OUT)
GPIO.setup(motorL1,GPIO.OUT)
GPIO.setup(motorL2,GPIO.OUT)

#Function to stop all motors
def motorstop():
    #Deactivates all Motors
    GPIO.output(motorR1, 0)
    GPIO.output(motorR2, 0)
    GPIO.output(motorL1, 0)
    GPIO.output(motorL2, 0)
    time.sleep(1)
#Function to Turn Robot to the Right   
def motorright90():
    #Activate all Motors to Turn Right.
    GPIO.output(motorR1, 0)
    GPIO.output(motorR2, 1)
    GPIO.output(motorL1, 1)
    GPIO.output(motorL2, 0)
    time.sleep(0.75)
    #Stop all Motors
    motorstop()
#Function to Turn Robot to the Left    
def motorleft90():
    #Activate all Motors to Turn Left.
    GPIO.output(motorR1, 1)
    GPIO.output(motorR2, 0)
    GPIO.output(motorL1, 0)
    GPIO.output(motorL2, 1)
    time.sleep(0.75)
    #Stop all Motors
    motorstop()    
#Function to Make Robot Go Straight   
def motorstraight():
    #Activate all Motors in a Forwards Direction.
    GPIO.output(motorR1, 1)
    GPIO.output(motorR2, 0)
    GPIO.output(motorL1, 1)
    GPIO.output(motorL2, 0)
    time.sleep(1)
    #Stop all Motors
    motorstop()
#Function to Make Robot Turn Around
def motorturnaround():
    #Activate all Motors to Turn Right.
    GPIO.output(motorR1, 0)
    GPIO.output(motorR2, 1)
    GPIO.output(motorL1, 1)
    GPIO.output(motorL2, 0)
    time.sleep(1.5)
    #Stop all Motors
    motorstop()
    
while True:
    print("Turning Right")
    time.sleep(1)
    motorright90()
    print("Turning Left")
    time.sleep(1)
    motorleft90()
    print("Going Straight")
    time.sleep(1)
    motorstraight()
    print("Turning Around")
    time.sleep(1)
    motorturnaround()