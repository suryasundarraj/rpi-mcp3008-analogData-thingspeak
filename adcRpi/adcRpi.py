import spidev
import os
import urllib2
from time import sleep

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

#Setup our API and delay
myAPI = "EOCM5SPM8VM5YDVB"

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
# Define sensor channels
adc_channel = 0
 
# Define delay between readings
delay = 2

# main() function
def main():

	baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

	while True:
		# Read the light sensor data
		adc_level = ReadChannel(adc_channel)
		adc_volts = ConvertVolts(adc_level,2)
		# f = urllib2.urlopen(baseURL + "&field1=%s" % (adc_level))
		# f.close()	
		# Print out results
		print "--------------------------------------------"
		print("POT Value: {} ({}V)".format(adc_level,adc_volts))

		# Wait before repeating loop
		sleep(delay)

# call main
if __name__ == '__main__':
    main()
