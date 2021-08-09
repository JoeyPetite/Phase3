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
def motorturn():
    #Activate all Motors in a Forwards Direction.
    GPIO.output(motorR1, 0)
    GPIO.output(motorR2, 1)
    GPIO.output(motorL1, 1)
    GPIO.output(motorL2, 0)
    time.sleep(.75)
    #Stop all Motors
    motorstop()
    
print("Going Straight")
time.sleep(5)
motorturn()
