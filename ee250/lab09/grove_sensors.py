# Lab09: P2UX

from grovepi import *
from grove_rgb_lcd import *
import paho.mqtt.client as mqtt
import sys
import time

sys.path.append('../../Software/Python/')

# Components' ports
led = 2	#Connect the LED to digital port D4
dht_sensor = 4 #Connect the DHT sensor to analog port A0

# Set LED as output
pinMode(led, "OUTPUT") 

def lcd_callback(client, lcd_data, lcd_msg):

	lcd_data = str(lcd_msg.payload, "utf-8")

	setRGB(0, 255, 0)
	setText(lcd_data)

def led_callback(client, data, msg):

	data = str(msg.payload, "utf-8")
	
	print("LED_toggle")

	if (data == "LED_toggle"):
		print("Toggling now")

		# if LED is on, turn it off
		if (digitalRead(led)):
			digitalWrite(led,0)
		# if LED is off, turn it on
		else:
			digitalWrite(led,1)

def on_connect(client, userdata, flags, rc):
	print("Connected to server (i.e., broker) with result code "+str(rc))

	client.subscribe("anrg-pi8/led")
	client.subscribe("anrg-pi8/lcd")

	client.message_callback_add("anrg-pi8/led", led_callback)
	client.message_callback_add("anrg-pi8/lcd", lcd_callback)

def on_message(client, userdata, msg):
	print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()

	while True:

		time.sleep(1)

		[temp,humidity] = dht(dht_sensor,1)

		t = str(temp)
		h = str(humidity)

		#Publish Temperature and Humidity Data
		client.publish("anrg-pi8/temperature", t)
		client.publish("anrg-pi8/humidity", h)

		#Print Temperature and Humidity Data
		print("\nTemperature: " + t + "\nHumidity: " + h)

