# rpi-mcp3008-analogData-thingspeak

Basic Setup to integrate analog sensor with Raspberry Pi, where the data from the analog sensor are visualized in the Thingspeak API

## OVERVIEW

This Project Demonstrates how to integrate the analog input with the raspberry pi and track the data. The data is also visiualized with the Thingspeak API. There is no inbuilt analog input for the raspberry pi, MCP3008 is Analaog to Digital Converter which is used to interface the analog sensor with the Raspberry Pi. 

The interface between the MCP3008 and Raspberry Pi is acheived using SPI Communication Protocol.

## PREREQUISITES 

1.  Raspberry Pi with Raspbian OS 

2.  Account on Thingspeak and generate a channel, you will be provided with the unique API Key 

# Build and Install 

## Setting up the SPI enviroinment on Raspberry Pi

This process assumes you are using the latest Raspbian build from the official downloads page. You can update your current image using :

    sudo apt-get update
    sudo apt-get upgrade

To enable hardware SPI on the Pi we need to make a modification to a system file :

    sudo nano /boot/config.txt

Add the following line at the bottom :

    dtparam=spi=on
  
Use CTRL-X, then Y, then RETURN to save the file and exit. Reboot using the following :

    sudo reboot

## Checking If SPI Is Enabled (Optional)

To check if the SPI module is loaded by the system run the following command :

    lsmod

You should see “spi_bcm2708″ or “spi_bcm2835” listed in the output. You can use the following command to filter the list and make it easier to spot the spi entry :

    lsmod | grep spi_

SPI is now enabled.

## Python SPI Wrapper

In order to read data from the SPI bus in Python we need a library. This library is included in the latest Raspbian image so if you’ve got an uptodate SD card you don’t need to do anything else. You can confirm you’ve got “python-spidev” and “python3-spidev” installed by using :

    apt-mark showauto | grep spi

You should see the two python spidev packages listed in the output.

## Obsolete Installation Step

Previously you needed to install a library called ‘py-spidev’. I’ve left the instructions here for anyone who is using an older image.

To install it we first need to install ‘python-dev’ :

    sudo apt-get install python2.7-dev

Then to finish we can download ‘py-spidev’ and compile it ready for use :

    wget https://github.com/Gadgetoid/py-spidev/archive/master.zip
  
    unzip master.zip
  
    rm master.zip
  
    cd py-spidev-master
  
    sudo python setup.py install
  
    cd ..

## WORKING

1.  Clone the repo in the Raspberry pi 

        git clone https://github.com/suryasundarraj/rpi-mcp3008-analogData-thingspeak

2.  Modify the Uinque API Key from the thingspeak channel 

3.  Run the Program and visiualize the data graphically on the thingspeak         
  


