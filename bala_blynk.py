from blynkapi import Blynk
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
ledPin = 22 # Broadcom pin 23 (P1 pin 16)

#led_light = Blynk(auth_token, pin = "V14")

dc = 95 # duty cycle (0-100) for PWM pin

auth_token = "d082a9e4063b48d39d687de69a4b6195"

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
    	led_light = Blynk(auth_token, pin = "V14")
	pinval = led_light.get_val()
        GPIO.output(ledPin, GPIO.LOW)
       	#print pinval.encode('UTF-8')
        if str(pinval) == "[u'1']" : # button is released
            GPIO.output(ledPin, GPIO.HIGH)
            print pinval
        else: # button is pressed:
            GPIO.output(ledPin, GPIO.LOW)
            print pinval
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO

