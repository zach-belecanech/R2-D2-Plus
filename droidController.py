import RPi.GPIO as GPIO          
from time import sleep
from gpiozero import Servo
from time import sleep
import math


from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

#Pin variables to store the pin number it's associated with on the PI
topArm = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
bottomArm = Servo(11, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
in1 = 3
in2 = 4
enA = 2
enB = 14
in3 = 15
in4 = 18
h_in1 = 7
h_in2 = 8
h_enA = 1



temp1=1
temp2=1
#Setup all of the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.setup(h_in1,GPIO.OUT)
GPIO.setup(h_in2,GPIO.OUT)
GPIO.setup(h_enA,GPIO.OUT)

#Set initial state of the motors
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(h_in1,GPIO.LOW)
GPIO.output(h_in2,GPIO.LOW)

p=GPIO.PWM(enA,1000)
p2=GPIO.PWM(enB,1000)
p3=GPIO.PWM(h_enA,1000)

#initial motor speed
p.start(100)
p2.start(100)
p3.start(100)

#instructions
print("\n")
print("The default speed & direction of motor is HIGH & Forward.....")
print("r-run s-stop f-forward b-backward a-arms h-head e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1 & temp2 == 1):
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=1
        temp2=1
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=0
        temp2=0
        x='z'

    elif x == 'tl':
        print("turning left")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        x='z'

    elif x=='tr':
        print("turning right")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='a':
        print("max")
        topArm.max()
        bottomArm.max()
        sleep(2)
        print("mid")
        topArm.mid()
        bottomArm.mid()
        x='z'

    elif x=='hr':
        print("head schmoove right")
        GPIO.output(h_in1,GPIO.HIGH)
        GPIO.output(h_in2,GPIO.LOW)
        x='z'
    elif x=='hl':
        print("head schmoove left")
        GPIO.output(h_in1,GPIO.LOW)
        GPIO.output(h_in2,GPIO.HIGH)
        x='z' 
    elif x == 'hs':
        print("head no schmoove")
        GPIO.output(h_in1,GPIO.LOW)
        GPIO.output(h_in2,GPIO.LOW)
        x='z'

    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")