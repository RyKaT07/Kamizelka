import adafruit_dht
import digitalio
from board import D27, D17
import time

buzzer = digitalio.DigitalInOut(D17)
buzzer.direction = digitalio.Direction.OUTPUT

dht_device = adafruit_dht.DHT11(D27)

while True:
    try:
        print("{}, {}".format(dht_device.temperature, dht_device.humidity))
    except:
        print("Error in read")
    time.sleep(2)