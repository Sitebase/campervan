#!/usr/bin/python

import signal
import sys
import subprocess, os
import RPi.GPIO as GPIO

DISPLAY_SELECTION_GPIO = 17 
REARCAMERA_GPIO = 27 

print("Press Ctrl & C to Quit")

def signal_handler(sig, frame):
    print("Quit")
    GPIO.cleanup()
    sys.exit(0)
    
def button_pressed_callback(channel):
    print("Button pressed!", channel)

    if channel == REARCAMERA_GPIO:
        os.system("/sbin/runuser -l pi -c 'export DISPLAY=:0.0 && /usr/bin/xdotool key N'")

    if channel == DISPLAY_SELECTION_GPIO:
        os.system("sudo shutdown -h now")

def handle_buttons():
    print("Handle buttons")
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(REARCAMERA_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(REARCAMERA_GPIO, GPIO.RISING, callback=button_pressed_callback, bouncetime=300)
    
    GPIO.setup(DISPLAY_SELECTION_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(DISPLAY_SELECTION_GPIO, GPIO.RISING, callback=button_pressed_callback, bouncetime=1000)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
