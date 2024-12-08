from pirc522 import RFID
from RPi.GPIO as GPIO

GPIO.setwarnings(False)

rdr = RFID()

print("Nasłuchiwanie tagów RFID...")

while True:
    rdr.wait_for_tag()
    (error, tag_type) = rdr.request()
    if not error:
        print(f"Tag wykryty! Typ: {tag_type}")

        (error, uid) = rdr.anticoll()
        if not error:
            print(f"UID tagu: {uid}")