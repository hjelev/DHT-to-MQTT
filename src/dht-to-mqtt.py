# Install Adafruit_DHT module
# sudo pip3 install Adafruit_DHT

import time
import Adafruit_DHT as dht
import paho.mqtt.client as paho

# Configuration variables
mqtt_user =  "username"
mqtt_password = 'password'
mqtt_host = "host or ip address"
mqtt_port = 1883
rpi_gpio = 4

def read_DHT():
	h, t = dht.read_retry(dht.DHT22, rpi_gpio)
	t = format(t, '.2f')
	h = format(h, '.2f')
	return(t,h)

def publish(temperature, humidity):
	client = paho.Client()
	client.username_pw_set(mqtt_user, mqtt_password)
	client.connect(mqtt_host, mqtt_port)
	client.publish("livingroom/temperature", str(temperature), qos=1)
	time.sleep(1)
	client.publish("livingroom/humidity", str(humidity), qos=1)
	client.disconnect()
	
if __name__ == '__main__':
	temperature, humidity  = read_DHT()
	publish(temperature, humidity)
