import RPi.GPIO as GPIO
import blynklib
import time
#==================================
BLYNK_AUTH = 'USnZLvwVt83o94NGvgyY3Al7UoXSogRW'
# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
#================================== 
#Define Variables
motorR1 = 19
motorR2 = 26
motorL1 = 20
motorL2 = 21
trig = 18
echo = 24
servo = 12
#General Setup
mindistance = 0.75
motorState = 0
GPIO.setmode(GPIO.BCM)
#DC Motors Setup
GPIO.setup(motorR1,GPIO.OUT)
GPIO.setup(motorR2,GPIO.OUT)
GPIO.setup(motorL1,GPIO.OUT)
GPIO.setup(motorL2,GPIO.OUT)
#Ultrasonic Sensor Setup
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
#Servo Motor Setup
GPIO.setup(servo, GPIO.OUT)
Servo1 = GPIO.PWM(servo,50)
Servo1.start(0)
#================================== 
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
    time.sleep(0.725)
    #Stop all Motors
    motorstop()
#Function to Turn Robot to the Left    
def motorleft90():
    #Activate all Motors to Turn Left.
    GPIO.output(motorR1, 1)
    GPIO.output(motorR2, 0)
    GPIO.output(motorL1, 0)
    GPIO.output(motorL2, 1)
    time.sleep(0.725)
    #Stop all Motors
    motorstop()    
#Function to Make Robot Go Straight   
def motorstraight():
    #Activate all Motors in a Forwards Direction.
    GPIO.output(motorR1, 1)
    GPIO.output(motorR2, 0)
    GPIO.output(motorL1, 1)
    GPIO.output(motorL2, 0)
#Function to Make Robot Turn Around
def motorturnaround():
    #Activate all Motors to Turn Right.
    GPIO.output(motorR1, 1)
    GPIO.output(motorR2, 0)
    GPIO.output(motorL1, 0)
    GPIO.output(motorL2, 1)
    time.sleep(1.5)
    #Stop all Motors
    motorstop()
    #Turn Servo Back to Center.
    servo(90)
    time.sleep(1)
    #Determine Distance at Center and Replace Variable 3.
    straightdistance = distance()
    print("Distance Forward is",straightdistance,"Feet")
    time.sleep(1)
    while straightdistance > mindistance:
        straightdistance = distance()
        print(straightdistance)
        print("Going Straight")
        motorstraight()
        time.sleep(0.25)
    #Stop all Motors.
    motorstop()
    #Drive Forwards for "Straight Distance" - Padding

#==================================     
#Function to Define Servo Motor Angle Commands
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
#================================== 
#Function to Determine Distance
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
#==================================
READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"
@blynk.handle_event('read V1')
def write_virtual_pin_handler(pin, value):
    #Turn Servo to the Left 90 Degrees
    servo(180)
    time.sleep(1)
    #Determine Distance at Left and Replace Variable 1
    leftdistance = distance()
    print("Distance Left is",leftdistance,"Feet")
    time.sleep(1)
    #Turn Servo to the Right 90 Degrees
    servo(0)
    time.sleep(1)
    #Determine Distance at Right and Replace Variable 2
    rightdistance = distance()
    print("Distance Right is",rightdistance,"Feet")
    #==================================#    
    #If Left and Right are Less than the Minimum Distance, Turn Around.
    if leftdistance < mindistance > rightdistance:
        print("Turning Around")
        time.sleep(1)
        motorturnaround()
        time.sleep(1)
    #If Left is Greater than Right, Turn Left.  
    elif leftdistance > rightdistance:
        print("Turning Left")
        time.sleep(1)
        motorleft90()
        time.sleep(1)
    #If Right Greater than Left, Turn Right.
    else:
        print("Turning Right")
        time.sleep(1)
        motorright90()
        time.sleep(1)
    #==================================#    
    #Turn Servo Back to Center.
    servo(90)
    time.sleep(1)
    #Determine Distance at Center and Replace Variable 3.
    straightdistance=distance()
    print("Distance Forward is",straightdistance,"Feet")
    time.sleep(1.5)
    print("Moving Forwards")
    time.sleep(1)
    #Drive Forwards Untill Minimum Distance is Reached.
    while straightdistance > mindistance:
    straightdistance = distance()
    print(straightdistance)
    print("Going Straight")
    motorstraight()
    time.sleep(0.25)
    #Stop all Motors.
    motorstop()

#Repeat
while True:
    blynk.run()
#==================================# 
