#!/usr/bin/python

import signal
import sys
import subprocess, os
import RPi.GPIO as GPIO

DISPLAY_SELECTION_GPIO = 6 
REARCAMERA_GPIO = 5 

print("Press Ctrl & C to Quit")

def signal_handler(sig, frame):
    print("Quit")
    GPIO.cleanup()
    sys.exit(0)
    
def button_pressed_callback(channel):
    print("Button pressed!", channel)

    if channel == REARCAMERA_GPIO:
        #print(GPIO.input(BUTTON_GPIO))
        #subprocess.call("logger pressed",shell=True)
        subprocess.call("crankshaft brightness set 25",shell=True)

    if channel == DISPLAY_SELECTION_GPIO:
        os.system("sudo reboot")

def handle_buttons():
    GPIO.setmode(GPIO.BCM)

    # GPIO.setup(REARCAMERA_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.add_event_detect(REARCAMERA_GPIO, GPIO.FALLING, callback=button_pressed_callback, bouncetime=300)
    
    GPIO.setup(DISPLAY_SELECTION_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(DISPLAY_SELECTION_GPIO, GPIO.BOTH, callback=button_pressed_callback, bouncetime=1000)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
