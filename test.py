import RPi.GPIO as gpio
import time 

in1 = 3
in2 = 4
enA = 2
enB = 14
in3 = 15
in4 = 18

def init():    
    gpio.setmode(gpio.BCM)
    gpio.setup(in1, gpio.OUT)
    gpio.setup(in2, gpio.OUT)
    gpio.setup(in3, gpio.OUT)
    gpio.setup(in4, gpio.OUT)
    
def forward(sec):
    init()
    gpio.output(in1, False)
    gpio.output(in2, True)
    gpio.output(in3, True)
    gpio.output(in4, False)
    time.sleep(sec)
    gpio.cleanup() 
    
def reverse(sec):
    init()
    gpio.output(in1, True)
    gpio.output(in2, False)
    gpio.output(in3, False)
    gpio.output(in4, True)
    time.sleep(sec)
    gpio.cleanup()
    
def left_turn(sec):
    init()
    gpio.output(in1, True)
    gpio.output(in2, False)
    gpio.output(in3, True)
    gpio.output(in4, False)
    time.sleep(sec)
    gpio.cleanup()

def right_turn(sec):
    init()
    gpio.output(in1, False)
    gpio.output(in2, True)
    gpio.output(in3, False)
    gpio.output(in4, True)
    time.sleep(sec)
    gpio.cleanup()
    
seconds = 5

time.sleep(seconds)
print("forward")
forward(seconds)
time.sleep(seconds-2)

print("right")
right_turn(seconds)
time.sleep(seconds-2)

time.sleep(seconds)
print("forward")
forward(seconds)
time.sleep(seconds-2)

print("right")
right_turn(seconds)
time.sleep(seconds-2)