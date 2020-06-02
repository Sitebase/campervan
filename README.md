# Campervan
Code and documentation for my complete campervan build.

## Requirements
* Navigation system in dashboard with large display
* Able to call handsfree over bluetooth
* Able to stream music from phone to speakers in van
* Battery pack with inverter:
  * Laptop charging
  * TV/Remove laptop screen
  * Indunction cooking
  * Small fridge
* Solar setup to charge batteries
* Batteries should also get charged while driving
* Way to monitor certain parameters of the setup
  * Power produced by solar panels
  * Power going in/out of the battery pack
  * AC usage vs DC usage
* Easy way to disconnect everything from the battery in case of emergency or at night
* Easy to install remove double bed
* Water supply (70L) for drinking/cooking or outside shower
* Rearcamera (RPI camera) automatically activated on reverse
* Listen to Radio1 and StuBru (probably using MP3 stream
* Finding a good solution to have internet on the road. 4G access point for example.

## Software
* Raspberry PI with Crankshaft and 7" official display
  * Enable dev mode to get SSH access
  * Install Kodi as media center on Raspberry pi (sudo install kodi && kodi)
  * Install [Netflix on Kodi](https://pimylifeup.com/raspberry-pi-netflix/)
    * https://github.com/asciidisco/plugin.video.netflix/issues/489 needed for widevine CDM
    * [inputstream.adaptive](https://forum.odroid.com/viewtopic.php?t=34076) was missing for me
    * Follow this https://discourse.osmc.tv/t/how-to-all-platforms-can-i-use-netflix-on-osmc-post-4/54741/299
  
## Hardware

## Power consumption
If this will be the brain of the van it's a good idea to do some power monitoring of it to get an idea of what it's consuming.
  
## Tips
* First try to make a test setup of all components instead of trying to install this directly in the van
* Use a powerful USB power supply to run the Raspberry Pi otherwise you we run into some weird behaviour (at least 2A)
