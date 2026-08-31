# -*- coding: utf-8 -*-
import sys
import os
import time
import random
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog
import winsound
from pynput import mouse, keyboard
import win32api
import win32gui
import win32con
from PIL import Image, ImageTk

# Konfiguracja czasów (w sekundach)
# Do szybkiego testu zmień na: CZAS_PRACY = 10, CZAS_PRZERWY = 15
CZAS_PRACY = 60 * 60 * 2       # 2 godziny = 7200 sekund
CZAS_PRZERWY = 30 * 60        # 30 minut = 1800 sekund
MAX_BEZCZYNNOSC = 60          # 60 sekund tolerancji na bezczynność

HASLO_DEZAKTYWACJI = "12345"

CYTATY = [
    "Praca bez przerwy sprawia, że jesteś spięty jak struna w gitarze. Odpocznij!",
    "Nawet najlepszy kot musi czasem uciąć sobie drzemkę. Twoja kolej!",
    "Komputer nie ucieknie, a Twoje oczy potrzebują chwili wytchnienia.",
    "Zrób przerwę! Twój kręgosłup podziękuje Ci za te 30 minut.",
    "Kot rządzi, praca leży. Regeneruj siły do dalszego działania!"
]

class AplikacjaKot:
    def __init__(self):
        self.ostatnia_aktywnosc = time.time()
        self.skumulowany_czas_pracy = 0.0
        self.w_trakcie_przerwy = False
        self.dziala = True
        
        # Główne niewidoczne okno-baza dla wszystkich pod-okien (zapobiega błędom pyimage)
        self.root = tk.Tk()
        self.root.withdraw() # Ukrywamy główne okno
        
        self.lock_window = None
        self.widget_window = None
        
        # Inicjalizacja nasłuchiwania myszy i klawiatury
        self.mouse_listener = mouse.Listener(on_move=self.rejestruj_aktywnosc, 
                                             on_click=self.rejestruj_aktywnosc, 
                                             on_scroll=self.rejestruj_aktywnosc)
        self.keyboard_listener = keyboard.Listener(on_press=self.rejestruj_aktywnosc)
        
        self.mouse_listener.start()
        self.keyboard_listener.start()
        
        # Uruchomienie widżetu i głównej pętli tk w bezpieczny sposób
        self.stworz_widzet_odliczania()

    def rejestruj_aktywnosc(self, *args, **kwargs):
        if self.w_trakcie_przerwy:
            return
        
        teraz = time.time()
        roznica = teraz - self.ostatnia_aktywnosc
        
        if roznica <= MAX_BEZCZYNNOSC:
            self.skumulowany_czas_pracy += roznica
        
        self.ostatnia_aktywnosc = teraz
        
        if self.skumulowany_czas_pracy >= CZAS_PRACY:
            self.skumulowany_czas_pracy = 0.0
            # Wywołujemy odpalenie przerwy bezpiecznie wewnątrz pętli tk (poprzez root.after)
            self.root.after(0, self.odpal_przerwe)

    def stworz_widzet_odliczania(self):
        # Tworzymy widżet jako Toplevel przypięty do root
        root_widget = tk.Toplevel(self.root)
        self.widget_window = root_widget
        root_widget.title("Licznik Kot")
        
        root_widget.overrideredirect(True)
        root_widget.attributes("-topmost", True)
        root_widget.attributes("-alpha", 0.8)
        root_widget.config(bg="#1e1e1e")
        
        szerokosc_ekranu = root_widget.winfo_screenwidth()
        wysokosc_ekranu = root_widget.winfo_screenheight()
        pozycja_x = szerokosc_ekranu - 160
        pozycja_y = wysokosc_ekranu - 80
        root_widget.geometry(f"150x40+{pozycja_x}+{pozycja_y}")
        
        label_widzet = tk.Label(
            root_widget, 
            text="Kot przyjdzie za: --:--", 
            font=("Arial", 11, "bold"), 
            fg="#ffcc00", 
            bg="#1e1e1e"
        )
        label_widzet.pack(expand=True, fill="both")
        
        def odswiezaj_widzet():
            if not self.dziala:
                return
                
            if self.w_trakcie_przerwy:
                label_widzet.config(text="KOT PRZEJĄŁ!", fg="red")
            else:
                pozostalo = int(CZAS_PRACY - self.skumulowany_czas_pracy)
                if pozostalo < 0:
                    pozostalo = 0
                minuty = pozostalo // 60
                sekundy = pozostalo % 60
                label_widzet.config(text=f"🐾 Kot za: {minuty:02d}:{sekundy:02d}", fg="#ffcc00")
                
            root_widget.after(1000, odswiezaj_widzet)
            
        root_widget.after(100, odswiezaj_widzet)

    def dzwiek_glodny_kot(self):
        katalog_aplikacji = os.path.dirname(os.path.abspath(__file__))
        sciezka_audio = os.path.join(katalog_aplikacji, "meaw-xd.wav")
        try:
            winsound.PlaySound(sciezka_audio, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
        except Exception as e:
            print(f"Błąd odtwarzania meaw-xd.wav: {e}")
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

    def dzwiek_zadowolony_kot(self):
        katalog_aplikacji = os.path.dirname(os.path.abspath(__file__))
        sciezka_audio = os.path.join(katalog_aplikacji, "budzik_do_roboty.wav")
        try:
            winsound.PlaySound(sciezka_audio, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
        except Exception as e:
            print(f"Błąd odtwarzania budzik_do_roboty.wav: {e}")
            winsound.MessageBeep(winsound.MB_OK)

    def odpal_przerwe(self):
        self.w_trakcie_przerwy = True
        
        threading.Thread(target=self.dzwiek_glodny_kot, daemon=True).start()
        
        # Tworzymy okno blokady jako Toplevel podpięty pod root
        root_lock = tk.Toplevel(self.root)
        self.lock_window = root_lock
        root_lock.title("KOT PRZEJMUJE LAPTOPA")
        
        root_lock.attributes("-fullscreen", True)
        root_lock.attributes("-topmost", True)
        root_lock.config(bg="black")
        
        root_lock.protocol("WM_DELETE_WINDOW", lambda: None)
        
        label_alert = tk.Label(
            root_lock, 
            text="PRZERWA 30 MINUT!!! KOT PRZEJMUJE LAPTOPA!!!", 
            font=("Arial", 30, "bold"), 
            fg="red", 
            bg="black",
            wraplength=1000
        )
        label_alert.pack(pady=20)
        
        # BEZPIECZNE ładowanie grafiki (teraz zadziała idealnie w tym samym wątku tk)
        try:
            katalog_aplikacji = os.path.dirname(os.path.abspath(__file__))
            sciezka_grafiki = os.path.join(katalog_aplikacji, "obrazek_kota.png")
            img = Image.open(sciezka_grafiki)
            img.thumbnail((500, 450))
            self.foto_kota = ImageTk.PhotoImage(img)
            label_grafika = tk.Label(root_lock, image=self.foto_kota, bg="black")
            label_grafika.pack(pady=10)
        except Exception as e:
            print(f"Błąd ładowania grafiki przez Pillow: {e}")

        cytat = random.choice(CYTATY)
        label_cytat = tk.Label(
            root_lock, 
            text=f'"{cytat}"', 
            font=("Arial", 18, "italic"), 
            fg="white", 
            bg="black",
            wraplength=800
        )
        label_cytat.pack(pady=15)
        
        label_czas = tk.Label(root_lock, text="", font=("Arial", 20), fg="yellow", bg="black")
        label_czas.pack(pady=10)
        
        btn_deaktywacja = tk.Button(
            root_lock, 
            text="Dezaktywuj (Podaj hasło)", 
            font=("Arial", 12), 
            command=self.poproś_o_haslo
        )
        btn_deaktywacja.pack(side="bottom", pady=40)

        sekundy_zostalo = CZAS_PRZERWY
        def aktualizuj_odliczanie():
            nonlocal sekundy_zostalo
            if not self.w_trakcie_przerwy:
                root_lock.destroy()
                return
            if sekundy_zostalo <= 0:
                self.koniec_przerwy(root_lock)
                return
            
            minuty = sekundy_zostalo // 60
            sekundy = sekundy_zostalo % 60
            label_czas.config(text=f"Pozostały czas przerwy: {minuty:02d}:{sekundy:02d}")
            sekundy_zostalo -= 1
            root_lock.after(1000, aktualizuj_odliczanie)
            
        root_lock.after(100, aktualizuj_odliczanie)

    def poproś_o_haslo(self):
        haslo = simpledialog.askstring(
            "Dezaktywacja", 
            "Wpisz hasło dezaktywujące:", 
            show='*', 
            parent=self.lock_window
        )
        if haslo == HASLO_DEZAKTYWACJI:
            self.dziala = False
            self.w_trakcie_przerwy = False
            self.mouse_listener.stop()
            self.keyboard_listener.stop()
            self.root.destroy()  # Zamknięcie nadrzędnego okna niszczy automatycznie wszystkie pod-okna
            messagebox.showinfo("Dezaktywacja", "Aplikacja Kot została wyłączona.")
            sys.exit(0)
        elif haslo is not None:
            messagebox.showerror("Błąd", "Nieprawidłowe hasło! Kot dalej pilnuje laptopa.", parent=self.lock_window)

    def koniec_przerwy(self, root_lock):
        self.w_trakcie_przerwy = False
        threading.Thread(target=self.dzwiek_zadowolony_kot, daemon=True).start()
        root_lock.destroy()
        self.ostatnia_aktywnosc = time.time()

def dodaj_do_autostartu():
    sciezka_skryptu = os.path.abspath(sys.argv[0])
    klucz_rejestru = r"Software\Microsoft\Windows\CurrentVersion\Run"
    nazwa_wpisu = "AplikacjaKot"
    try:
        klucz = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, klucz_rejestru, 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(klucz, nazwa_wpisu, 0, win32con.REG_SZ, sciezka_skryptu)
        win32api.RegCloseKey(klucz)
    except Exception as e:
        print(f"Nie udało się dodać do autostartu: {e}")

if __name__ == "__main__":
    dodaj_do_autostartu()
    app = AplikacjaKot()
    print("Aplikacja KOT uruchomiona i pilnuje Twojej pracy...")
    
    # Przekazujemy sterowanie głównej pętli tkinter, która utrzymuje program przy życiu
    app.root.mainloop()


