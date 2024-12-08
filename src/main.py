import adafruit_dht
import digitalio
import RPi.GPIO as GPIO
from board import D27, D17, D0, D5, D6, D13, D19, D26
import time
from mfrc522 import SimpleMFRC522
import adafruit_character_lcd.character_lcd as character_lcd
import logging
from picamzero import Camera
from datetime import datetime
import threading

Darek = "192463859248"
nieznany_uzytkownik = "86474552968"

available_tags = [Darek, nieznany_uzytkownik]
lcd_rs = digitalio.DigitalInOut(D0)
lcd_en = digitalio.DigitalInOut(D5)
lcd_d7 = digitalio.DigitalInOut(D26)
lcd_d6 = digitalio.DigitalInOut(D19)
lcd_d5 = digitalio.DigitalInOut(D13)
lcd_d4 = digitalio.DigitalInOut(D6)

lcd_columns = 16
lcd_rows = 2

cam = Camera()

def pictureTakerDaemon():
    threading.Timer(10.0, pictureTakerDaemon).start()
    now = datetime.now()
    filename = "/home/admin/odruch_zostanie2/images/{}.jpg".format(now.strftime("%d-%m-%Y_%H:%M:%S.%f"))
    cam.take_photo(filename)
    print("Saved", filename, "photo.")

def WaitForTag():
    reader = SimpleMFRC522()
    try:
        uid = ""
        text = ""
        print("Przyłóż tag RFID...")
        while uid == "" and text == "":
            uid, text = reader.read()  # Odczyt UID i zapisanych danych
            print(f"UID: {uid}")
            print(f"Tekst: {text}")
    except KeyboardInterrupt:
        print("Zamykanie programu...")

    return uid

def ReadTag():
    reader = SimpleMFRC522()
    try:
        uid, text = reader.read()  # Odczyt UID i zapisanych danych
    except KeyboardInterrupt:
        print("Zamykanie programu...")

    return uid

if __name__=="__main__":
    # Inicjalizcja wyswietlacza
    lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
    lcd.message = "  Menti Sense \n Ladowanie" 

    logging.basicConfig(
    filename='../logs/service.log',   # Plik do logowania
    level=logging.INFO,       # Poziom logowania (INFO, DEBUG, ERROR itp.)
    format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Zaincjalizowano wyświetlacz.")

    # Inicjalizacja buzzera
    buzzer = digitalio.DigitalInOut(D17)
    buzzer.direction = digitalio.Direction.OUTPUT

    logging.info("Zaincjalizowano buzzer")
    # Inicjalizacja czujnika temperatury
    dht_device = adafruit_dht.DHT11(D27)

    logging.info("Zaincjalizowano czujnik temperatury")
    while True:
        lcd.message = "  Menti Sense  \n Przyloz karte" 
        tag = WaitForTag()
        logging.info("Próba autoryzacji.")
        time.sleep(1)
        if str(tag) in available_tags:
            logging.info("Znaleziono uytkownika")
            lcd.clear()
            lcd.message = "  Witaj Darku \nJak sie masz?"
            zalogowany = True
            time.sleep(4)
            lcd.clear()
            pictureTakerDaemon()
            while zalogowany:
                try:
                    print("{}, {}".format(dht_device.temperature, dht_device.humidity))
                    lcd.message="T={}\nH={}".format(dht_device.temperature, dht_device.humidity)
                    logging.info("Zmierzona temperatura {}, {}".format(dht_device.temperature, dht_device.humidity))
                    new_tag = ReadTag()
                    if str(new_tag) == str(tag):
                        zalogowany = False
                except:
                    print("Error in read")
                time.sleep(0.5)
            lcd.clear()
            lcd.message = "  Zegnaj Darku \nDo zobaczenia"
            time.sleep(2)
            lcd.clear()
        elif:
            lcd.clear()
            lcd.message = "  Menti Sense \n Niezautoryzowany uzytkownik" 
            lcd.clear()

"""
while True:
    try:
        print("{}, {}".format(dht_device.temperature, dht_device.humidity))
        lcd.message="T={}\nH={}".format(dht_device.temperature, dht_device.humidity)
    except:
        print("Error in read")
    time.sleep(0.5)
"""
