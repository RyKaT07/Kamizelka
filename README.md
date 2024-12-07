# My Raspberry Pi Project

Jest to projekt innowacyjnej kamizelki MentiSense, która wykorzystuje czujniki do określenia stanu zdrowia fizycznego oraz psychicznego użytkownika. 
Projekt jest skonfigurowany jako serwis systemowy (`systemd`), co pozwala na jego automatyczne uruchamianie po starcie systemu.

## Wymagania
- Raspberry Pi z systemem Raspberry Pi OS
- Python 3
- Zainstalowany `git`

## Instalacja

1. **Sklonuj repozytorium**:
   ```bash
   git clone https://github.com/RyKaT07/odruch_zostanie.git /home/pi/odruch
   cd /home/pi/odruch
   ```

2. **Zainstaluj wymagane biblioteki Python**:
   Jeśli Twój projekt wymaga dodatkowych bibliotek Python, zainstaluj je za pomocą `pip`. W katalogu projektu:
   ```bash
   pip3 install -r requirements.txt
   ```
   Jeśli nie masz pliku `requirements.txt`, możesz zainstalować biblioteki ręcznie, np.:
   ```bash
   pip3 install RPi.GPIO
   ```

3. **Skopiuj plik serwisu systemowego**:
   Plik serwisu `kamizelka.service` znajduje się w repozytorium w katalogu projektu. Skopiuj go do odpowiedniego miejsca:
   ```bash
   sudo cp /home/pi/odruch/kamizelka.service /etc/systemd/system/
   ```
   Plik serwisu został przygotowany tak, aby działał poprawnie, ale jeśli lokalizacja Twojego repozytorium różni się, zaktualizuj w pliku ścieżki:
   ```ini
   WorkingDirectory=/home/pi/odruch
   ExecStart=/usr/bin/python3 /home/pi/odruch/src/main.py
   ```

   Jeśli Twoje repozytorium znajduje się w innej lokalizacji, zamień `/home/pi/odruch` na pełną ścieżkę do Twojego projektu.

4. **Aktywuj serwis**:
   Przeładuj konfigurację systemd i aktywuj serwis:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable kamizelka.service
   sudo systemctl start kamizelka.service
   ```

5. **Sprawdź status serwisu**:
   Aby upewnić się, że serwis działa:
   ```bash
   systemctl status kamizelka.service
   ```

## Struktura projektu
```
/home/pi/odruch/
│
├─ src/
│   ├─ main.py           # Główny skrypt aplikacji
│   ├─ gpio_control.py   # Moduł do sterowania pinami GPIO
│   └─ __init__.py       # Plik inicjalizacyjny Pythona
│
├─ logs/
│   └─ service.log       # Logi działania serwisu
│
├─ requirements.txt      # Lista wymaganych bibliotek Python
├─ kamizelka.service    # Plik serwisowy systemd
└─ README.md             # Dokumentacja projektu
```

## Logowanie
Logi działania serwisu można znaleźć w pliku:
```
/home/pi/odruch/logs/service.log
```

Możesz też sprawdzić logi za pomocą `journalctl`:
```bash
journalctl -u my_project.service -f
```

## Debugowanie
Jeśli serwis nie działa poprawnie:
1. Sprawdź logi:
   ```bash
   journalctl -u kamizelka.service
   ```
2. Upewnij się, że Python nie zgłasza błędów w pliku `main.py`.

## Autorzy
- Patryk Skibniewski
- Jakub Słupczewski
- Dariusz Wróblewski
- Patryk Mazur
- Link do repozytorium: [GitHub](https://github.com/RyKaT07/odruch_zostanie.git)