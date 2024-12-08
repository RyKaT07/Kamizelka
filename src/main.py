import adafruit_dht
import digitalio
from board import D27, D17, D0, D5, D6, D13, D19, D26
import time
import adafruit_character_lcd.character_lcd as character_lcd

lcd_rs = digitalio.DigitalInOut(D0)
lcd_en = digitalio.DigitalInOut(D5)
lcd_d7 = digitalio.DigitalInOut(D26)
lcd_d6 = digitalio.DigitalInOut(D19)
lcd_d5 = digitalio.DigitalInOut(D13)
lcd_d4 = digitalio.DigitalInOut(D6)

lcd_columns = 16
lcd_rows = 2

lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
lcd.message = "  Menti Sense\nOdruch zostanie"

buzzer = digitalio.DigitalInOut(D17)
buzzer.direction = digitalio.Direction.OUTPUT

dht_device = adafruit_dht.DHT11(D27)
time.sleep(2)
lcd.clear()

while True:
    try:
        print("{}, {}".format(dht_device.temperature, dht_device.humidity))
        lcd.message="T={}\nH={}".format(dht_device.temperature, dht_device.humidity)
    except:
        print("Error in read")
    time.sleep(0.5)