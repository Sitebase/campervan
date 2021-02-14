# Campervan Head Unit (WIP)
Code and documentation for my complete campervan central computer that uses [OpenAuto Pro](https://bluewavestudio.io/index.php/bluewave-shop/openauto-pro-detail).

**Note that this repo is work in progress**

## External screen
Hold button GPIO 17 while booting to use HDMI display as main screen.

## Requirements
* [x] Navigation system in dashboard with large display
* [x] Able to call handsfree over bluetooth
* [x] Able to stream music from phone to speakers in van
* [ ] Rearcamera (RPI camera) automatically activated on reverse
* [ ] Listen to Radio1 and StuBru (probably using MP3 stream
* [ ] Finding a good solution to have internet on the road. 4G access point for example.

## Hardware
* Raspberry Pi 4 Model B
* 7inch touch display
* BerryGPS (not really needed if you don't use offline navigation)

## Buttons
* Enable rearview camera
* Button to shutdown the system (i don't have a clear shutdown flow implemented yet based on ignition I/O input)
    * Hold this same button while booting to use the HDMI output as main screen

## Case
I've made a basic structure for holding the screen and making a test setup for this head unit.
I use the screen mirror mounting point with a custom printed adapter to attach the head unit to the window.

How you attach the unit to your window will depend on what's available in your car.

In the case folder you can take a look at the step files for the current case.

## Service
Handling of GPIOs (button click detection) is done using a python script which is run as a service on the system.

### Monitor logs of the service
tail -f /var/log/syslog

## Installation
* SSH into OpenAuto Pro clean install
* Go to home folder
* Do a git clone
* Run install.sh

## Power consumption
If this will be the brain of the van it's a good idea to do some power monitoring of it to get an idea of what it's consuming.
  
## Tips
* First try to make a test setup of all components instead of trying to install this directly in the van
* Use a powerful USB power supply to run the Raspberry Pi otherwise you we run into some weird behaviour (at least 2A)
* When trying to use android auto make sure you have a sound card plugged in otherwise it doesn't seem to start up.
