#!/usr/bin/env python
#
# GrovePi Example for using the Grove Temperature Sensor (http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
# NOTE: 
# 	The sensor uses a thermistor to detect ambient temperature.
# 	The resistance of a thermistor will increase when the ambient temperature decreases.
#	
# 	There are 3 revisions 1.0, 1.1 and 1.2, each using a different model thermistor.
# 	Each thermistor datasheet specifies a unique Nominal B-Constant which is used in the calculation forumla.
#	
# 	The second argument in the grovepi.temp() method defines which board version you have connected.
# 	Defaults to '1.0'. eg.
# 		temp = grovepi.temp(sensor)        # B value = 3975
# 		temp = grovepi.temp(sensor,'1.1')  # B value = 4250
# 		temp = grovepi.temp(sensor,'1.2')  # B value = 4250

import time
from grovepi import *
from grovepi_rgb_lcd import *

import paho.mqtt.client as mqtt
import sys
sys.path.append('../..Software/Python/')

# Connect the Grove Temperature Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = 3


# Connect the Grove LED to digital port D4
led = 4

pinMode(led,"OUTPUT")

def on_connect(client, userdata, flagas, rc):
	print("Connected to server(i.e. broker) with result code" + str(rc))
	client.subscriber("anrg-pi8/led")
	client.message_callback_add("anrg-pi8/led", led_callback)

	client.subscriber("anrg-pi8/lcd")
	client.message_callback_add("anrg-pi8/lcd", lcd_callback)

def on_message(client, userdata, msg):
	print("on_message:" + msg.topic + " " + str(msg.payload, "utf-8"))

def lcd_callback(client, lcd_data, lcd_msg)
	lcd_data = str(lcd_msg.payload, "utf-8")

	setRGB(0, 255, 0)
	setText(lcd_data)

def led_callback(client, led_data, led_msg)
	led_data = str(msg, payload, "utf-8")

	if (led_data = "LED_toggle"):
			if (digitalRead(led)):
				digitalWrite(led,0)
			else:
				digitalWrite(led,1)



if__name__=='__main__'
	clinet = mqtt.Clinet()
	client.on.message = on_message
	clien.on.connect = on_connect
	client.connect(host="eclipse.usc.edu", port = 11000, keepalive = 60)
	client loop.start()

	while True:
	    
	    	time.sleep(1)

	    	[temp,hum] = dht(sensor,1)

	    	t = str(temp)
	    	h = str(hum)

	    	client.publish("anrg-pi8/temp", t)
	    	client.publish("anrg-pi8/humidity", h)



