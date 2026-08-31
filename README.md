# 🐈 Projekt "Kot" (CatWorkGuard)

Inteligentna aplikacja wspierająca ergonomię pracy i wymuszająca przerwy od ekranu komputera (zgodnie z zasadami higieny pracy w IT). Program monitoruje aktywność użytkownika na poziomie systemu operacyjnego i bezwzględnie blokuje dostęp do stacji roboczej, dbając o zdrowie programisty.
An intelligent application supporting workplace ergonomics and enforcing computer screen breaks (in accordance with IT occupational health guidelines). The program monitors user activity at the operating system level and strictly blocks access to the workstation, actively caring for the developer's health.


## 🚀 Kluczowe Funkcjonalności

* **Low-Level Input Hooking:** Śledzenie ruchów myszy oraz klawiatury w tle systemu Windows za pomocą biblioteki `pynput`.
* **Algorytm Bezpiecznej Bezczynności:** Automatyczne odliczanie czasu pracy z uwzględnieniem 60-sekundowego limitu bezczynności. Jeśli odejdziesz od biurka, licznik pracy pauzuje.
* **Królewskie Przejęcie Ekranu (GUI):** Po 2 godzinach pracy aplikacja tworzy pełnoekranowe okno w `Tkinter` w trybie `-fullscreen` oraz `-topmost`, blokując skróty systemowe (np. Alt+F4) i odcinając dostęp do pulpitu na 30 minut.
* **Asynchroniczny System Audio:** Wykorzystanie modułu `threading` do równoległego odtwarzania powiadomień dźwiękowych bez blokowania głównego wątku interfejsu graficznego.
* **Personalizacja Doświadczenia (Easter Egg):** Powiadomienie o przerwie sygnalizowane jest unikalnym, spersonalizowanym komunikatem głosowym ("meaw-xd" w wykonaniu zmysłowego, męskiego głosu) oraz losowym cytatem motywacyjnym.
* **Windows Registry Integration:** Automatyczne dodawanie wpisu do rejestru Windows (`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`) przy pierwszym uruchomieniu, w celu zapewnienia autostartu aplikacji wraz z systemem.
* **Brama Awaryjna:** Możliwość natychmatowej dezaktywacji programu za pomocą dedykowanego hasła administratora (`12345`).

## 🛠️ Architektura Techniczna i Biblioteki

Projekt został w całości napisany w języku **Python 3** przy użyciu następujących technologii:
* `pynput` – przechwytywanie zdarzeń systemowych z myszy i klawiatury.
* `pywin32` (`win32api`, `win32gui`, `win32con`) – integracja z niskopoziomowym API systemu Windows 11 Pro i rejestrem.
* `tkinter` – autorskie, pełnoekranowe środowisko blokady stacji roboczej.
* `winsound` – obsługa natywnych formatów audio (.wav) systemu Windows.
* `threading` – zarządzanie wątkami w celu zapewnienia płynności działania aplikacji.

---

# 🐈 CatWorkGuard Project

An intelligent application designed to improve workplace ergonomics by enforcing screensaver and desk breaks (aligned with IT occupational health guidelines). The program monitors user activity at the OS level and strictly locks down the workstation, actively protecting the developer's health.

## 🚀 Key Features

* **Low-Level Input Hooking:** Tracks mouse movements and keyboard strokes in the background of Windows using the `pynput` library.
* **Smart Idle Algorithm:** Automatic work timer with a built-in 60-second inactivity buffer. Stepping away from the desk automatically pauses the counter.
* **Workstation Takeover (GUI):** After 2 hours of continuous work, the app triggers a full-screen window in `Tkinter` using `-fullscreen` and `-topmost` attributes, overriding system shortcuts (such as Alt+F4) and blocking desktop access for 30 minutes.
* **Asynchronous Audio System:** Implements the `threading` module for parallel playback of audio notifications without interrupting or freezing the main GUI thread.
* **Custom User Experience (Easter Egg):** Break notifications feature a unique, personalized voice alert ("meaw-xd" delivered by a rich, deep male voice) alongside randomized motivational quotes.
* **Windows Registry Integration:** Automatically injects a launch key into the Windows Registry (`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`) on the initial startup to ensure application persistence via system autostart.
* **Emergency Override:** Allows immediate program deactivation using a dedicated administrator password (`12345`).

## 🛠️ Technical Architecture & Libraries

Built entirely in **Python 3** using the following ecosystem components:
* `pynput` – OS-level event listening for mouse and keyboard inputs.
* `pywin32` (`win32api`, `win32gui`, `win32con`) – Integration with low-level Windows 11 Pro APIs and Registry.
* `tkinter` – Custom full-screen workstation lock interface.
* `winsound` – Native handling of Windows audio (.wav formats).
* `threading` – Thread management ensuring high software responsiveness.

## 📦 How to Run

1. Clone the repository.
2. Install required system packages:
   ```bash
   pip install pynput pywin32
   ```
3. Place the `meaw-xd.wav` and `budzik_do_roboty.wav` files in the root folder.
4. Run the application:
   ```bash
   python kot.py
   ```

---
*Projekt stworzony w celach edukacyjnych, zdrowotnych oraz dla poprawy humoru podczas długich sesji kodowania.*
*Project created for educational and health promotion purposes, adding a bit of humor to long coding sessions.*

