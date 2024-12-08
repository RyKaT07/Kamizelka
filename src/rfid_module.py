import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def WaitForTag():
    reader = SimpleMFRC522()
    try:
        print("Przyłóż tag RFID...")
        while uid == "" and text == "":
            uid, text = reader.read()  # Odczyt UID i zapisanych danych
            print(f"UID: {uid}")
            print(f"Tekst: {text}")
    except KeyboardInterrupt:
        print("Zamykanie programu...")
    finally:
        GPIO.cleanup()

    return uid
