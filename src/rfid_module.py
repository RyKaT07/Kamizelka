import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Przyłóż tag RFID...")
    while True:
        uid, text = reader.read()  # Odczyt UID i zapisanych danych
        print(f"UID: {uid}")
        print(f"Tekst: {text}")
except KeyboardInterrupt:
    print("Zamykanie programu...")
finally:
    GPIO.cleanup()
