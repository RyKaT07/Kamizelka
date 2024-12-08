import spidev
import time

def test_spi(bus=0, device=0, max_speed_hz=500000):
    try:
        # Inicjalizacja SPI
        spi = spidev.SpiDev()
        spi.open(bus, device)  # Bus 0, Device 0 (CE0)

        # Ustawienia SPI
        spi.max_speed_hz = max_speed_hz
        spi.mode = 0b00  # Mode 0 (CPOL=0, CPHA=0)
        print(f"SPI otwarte na bus {bus}, device {device} z prędkością {max_speed_hz} Hz")

        # Wysyłanie danych i odbieranie odpowiedzi
        test_data = [0xDE, 0xAD, 0xBE, 0xEF]  # Przykładowe dane do wysłania
        print(f"Wysyłanie: {test_data}")

        response = spi.xfer2(test_data)  # Przesyłanie danych
        print(f"Odpowiedź: {response}")

        # Zamknięcie SPI
        spi.close()
        print("SPI test zakończony.")
    except Exception as e:
        print(f"Błąd SPI: {e}")

if __name__ == "__main__":
    print("Rozpoczynanie testu SPI...")
    test_spi()
