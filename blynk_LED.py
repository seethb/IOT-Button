from blynkapi import Blynk
import RPi.GPIO as GPIO
import time

gpio_start = 22
gpio_end = 23
GPIO.setmode(GPIO.BCM)


auth_token = "d082a9e4063b48d39d687de69a4b6195"

#for x in range (gpio_start, gpio_end):
GPIO.setup(22, GPIO.OUT)
#   GPIO.output(22, False)

def stat_conv(res):
	"""Conver value from 1-0 to on-off"""
	if res[0] == "0":
		return "off"
	elif res[0] == "1":
		return "on"
	else:
		return "unknown"

while True:
   
   led_light = Blynk(auth_token, pin = "V14") 
   pinval = led_light.get_val()
   print pinval
#pinval = [str(pinval[0])]
   if pinval == "[u'1']" :
	#for y in range (gpio_start, gpio_end):
      GPIO.output(22, True)
      print pinval
     	#	print 'on ', y
        #	time.sleep(.5)
   else:
      GPIO.output(22, False)
      print pinval
         #GPIO.output(23, False)

#Blynk.run()
