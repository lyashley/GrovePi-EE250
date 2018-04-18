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

def lcd_callback(client, lcd_data, lcd_msg):
	lcd_data = str(lcd_msg.payload, "utf-8")

	setRGB(0, 255, 0)
	setText(lcd_data)

def led_callback(client, led_data, led_msg):
	led_data = str(msg, payload, "utf-8")

	if (led_data == "LED_toggle"):
			if (digitalRead(led)):
				digitalWrite(led,0)
			else:
				digitalWrite(led,1)



if (__name__=="__main__")
	client = mqtt.Client()
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



