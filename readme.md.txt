# 🐈 Projekt "Kot" (CatWorkGuard)

Inteligentna aplikacja wspierająca ergonomię pracy i wymuszająca przerwy od ekranu komputera (zgodnie z zasadami higieny pracy w IT). Program monitoruje aktywność użytkownika na poziomie systemu operacyjnego i bezwzględnie blokuje dostęp do stacji roboczej, dbając o zdrowie programisty.

## 🚀 Kluczowe Funkcjonalności

*   **Low-Level Input Hooking:** Śledzenie ruchów myszy oraz klawiatury w tle systemu Windows za pomocą biblioteki `pynput`.
*   **Algorytm Bezpiecznej Bezczynności:** Automatyczne odliczanie czasu pracy z uwzględnieniem 60-sekundowego limitu bezczynności. Jeśli odejdziesz od biurka, licznik pracy pauzuje.
*   **Królewskie Przejęcie Ekranu (GUI):** Po 2 godzinach pracy aplikacja tworzy pełnoekranowe okno w `Tkinter` w trybie `-fullscreen` oraz `-topmost`, blokując skróty systemowe (np. Alt+F4) i odcinając dostęp do pulpitu na 30 minut.
*   **Asynchroniczny System Audio:** Wykorzystanie modułu `threading` do równoległego odtwarzania powiadomień dźwiękowych bez blokowania głównego wątku interfejsu graficznego.
*   **Personalizacja Doświadczenia (Easter Egg):** Powiadomienie o przerwie sygnalizowane jest unikalnym, spersonalizowanym komunikatem głosowym ("meaw-xd" w wykonaniu zmysłowego, męskiego głosu) oraz losowym cytatem motywacyjnym.
*   **Windows Registry Integration:** Automatyczne dodawanie wpisu do rejestru Windows (`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`) przy pierwszym uruchomieniu, w celu zapewnienia autostartu aplikacji wraz z systemem.
*   **Brama Awaryjna:** Możliwość natychmiastowej dezaktywacji programu za pomocą dedykowanego hasła administratora (`12345`).

## 🛠️ Architektura Techniczna i Biblioteki

Projekt został w całości napisany w języku **Python 3** przy użyciu następujących technologii:
*   `pynput` – przechwytywanie zdarzeń systemowych z myszy i klawiatury.
*   `pywin32` (`win32api`, `win32gui`, `win32con`) – integracja z niskopoziomowym API systemu Windows 11 Pro i rejestrem.
*   `tkinter` – autorskie, pełnoekranowe środowisko blokady stacji roboczej.
*   `winsound` – obsługa natywnych formatów audio (.wav) systemu Windows.
*   `threading` – zarządzanie wątkami w celu zapewnienia płynności działania aplikacji.

## 📦 Jak uruchomić projekt?

1. Sklonuj repozytorium.
2. Zainstaluj wymagane pakiety systemowe:
   ```bash
   pip install pynput pywin32
   ```
3. Umieść w folderze projektu pliki audio `meaw-xd.wav` oraz `budzik_do_roboty.wav`.
4. Uruchom aplikację:
   ```bash
   python kot.py
   ```

---
*Projekt stworzony w celach edukacyjnych, zdrowotnych oraz dla poprawy humoru podczas długich sesji kodowania.*
