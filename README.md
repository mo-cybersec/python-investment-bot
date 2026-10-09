import tkinter as tk
from tkinter import messagebox

# Zmienne globalne do obsługi uniwersalnego licznika gotówki
stan_kapitalu = 0.0
zysk_na_sekunde = 0.0
licznik_aktywny = False

# Funkcja obliczająca stawkę sekundową na podstawie budżetu rocznego
def uruchom_kalkulator():
    global zysk_na_sekunde, stan_kapitalu, licznik_aktywny
    try:
        # Pobranie rocznego celu finansowego od użytkownika
        cel_roczny = float(entry_cel.get())
        
        if cel_roczny <= 0:
            messagebox.showerror("BŁĄD VETTINGU", "Budżet musi być większy niż 0!")
            return
            
        # Obliczanie zysku na sekundę (Rok ma 31 536 000 sekund)
        zysk_na_sekunde = cel_roczny / 31536000.0
        stan_kapitalu = 0.0
        
        profil_tekst = f"📈 TRYB: Aktywna Symulacja Strumienia Kapitału\n📊 CEL ROCZNY: {cel_roczny:,.2f} ZŁ".replace(",", " ")
        label_profil.config(text=profil_tekst)
        
        if not licznik_aktywny:
            licznik_aktywny = True
            aktualizuj_licznik()
            
    except ValueError:
        messagebox.showerror("BŁĄD SYSTEMU", "Wprowadź poprawną wartość numeryczną!")

# Funkcja automatycznie generująca przyrost kapitału co 1 sekundę
def aktualizuj_licznik():
    global stan_kapitalu, zysk_na_sekunde, licznik_aktywny
    if licznik_aktywny:
        stan_kapitalu += zysk_na_sekunde
        label_kasa.config(text=f"💎 SKUMULOWANY KAPITAŁ: {stan_kapitalu:,.4f} ZŁ".replace(",", " "))
        root.after(1000, aktualizuj_licznik)

# Tworzenie nowoczesnego okna aplikacji biznesowej (GUI)
root = tk.Tk()
root.title("Algorytm Finansowy - mo-cybersec v2.5")
root.geometry("500x320")
root.configure(bg="#111111")

print("Zaczynamy budowac imperium!")

# Interfejs graficzny - Czysty styl biznesowy
tk.Label(root, text="GLOBALNY KALKULATOR PRZEPŁYWÓW FINANSOWYCH", font=("Arial", 11, "bold"), fg="#ffffff", bg="#111111").pack(pady=15)
tk.Label(root, text="Wpisz planowany przychód roczny (w PLN):", font=("Arial", 9), fg="#888888", bg="#111111").pack()

entry_cel = tk.Entry(root, font=("Arial", 12), justify="center", width=15, bg="#222222", fg="#ffffff", insertbackground="white")
entry_cel.pack(pady=10)

btn = tk.Button(root, text="URUCHOM ANALIZĘ PRZEPŁYWU", command=uruchom_kalkulator, bg="#006600", fg="white", font=("Arial", 9, "bold"), padx=10, pady=5)
btn.pack(pady=10)

label_profil = tk.Label(root, text="⚙️ Status systemu: Oczekiwanie na wprowadzenie danych...", font=("Arial", 9), fg="#aaaaaa", bg="#111111", justify="left")
label_profil.pack(pady=10)

label_kasa = tk.Label(root, text="💎 SKUMULOWANY KAPITAŁ: 0.0000 ZŁ", font=("Arial", 12, "bold"), fg="#00ff00", bg="#111111")
label_kasa.pack(pady=15)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Zmienne globalne do obsługi licznika czasu rzeczywistego
stan_kapitalu = 0.0
zysk_na_sekunde = 0.0
licznik_aktywny = False

# Funkcja obliczająca stawkę sekundową na podstawie budżetu rocznego
def uruchom_kalkulator():
    global zysk_na_sekunde, stan_kapitalu, licznik_aktywny
    try:
        # Pobranie rocznego celu finansowego od użytkownika
        cel_roczny = float(entry_cel.get())
        
        if cel_roczny <= 0:
            messagebox.showerror("BŁĄD SYSTEMU", "Wprowadzona wartość musi być większa niż 0!")
            return
            
        # Obliczanie zysku na sekundę (Rok ma dokładnie 31 536 000 sekund)
        zysk_na_sekunde = cel_roczny / 31536000.0
        stan_kapitalu = 0.0
        
        profil_tekst = f"📈 TRYB: Aktywna Symulacja Strumienia Kapitału\n📊 CEL ROCZNY: {cel_roczny:,.2f} ZŁ".replace(",", " ")
        label_profil.config(text=profil_tekst)
        
        if not licznik_aktywny:
            licznik_aktywny = True
            aktualizuj_licznik()
            
    except ValueError:
        messagebox.showerror("BŁĄD ZABEZPIECZENIA", "System wykrył niepoprawne dane. Wprowadź poprawną wartość numeryczną!")

# Funkcja automatycznie generująca przyrost kapitału co 1 sekundę
def aktualizuj_licznik():
    global stan_kapitalu, zysk_na_sekunde, licznik_aktywny
    if licznik_aktywny:
        stan_kapitalu += zysk_na_sekunde
        label_kasa.config(text=f"💎 SKUMULOWANY KAPITAŁ: {stan_kapitalu:,.4f} ZŁ".replace(",", " "))
        root.after(1000, aktualizuj_licznik)

# Tworzenie nowoczesnego okna aplikacji biznesowej (GUI)
root = tk.Tk()
root.title("Kalkulator Przepływów Finansowych - mo-cybersec v2.5")
root.geometry("500x320")
root.configure(bg="#111111")

print("Zaczynamy budowac imperium!")

# Interfejs graficzny - Czysty, profesjonalny styl biznesowy
tk.Label(root, text="GLOBALNY KALKULATOR PRZEPŁYWÓW FINANSOWYCH", font=("Arial", 11, "bold"), fg="#ffffff", bg="#111111").pack(pady=15)
tk.Label(root, text="Wpisz planowany przychód roczny (w PLN):", font=("Arial", 9), fg="#888888", bg="#111111").pack()

entry_cel = tk.Entry(root, font=("Arial", 12), justify="center", width=15, bg="#222222", fg="#ffffff", insertbackground="white")
entry_cel.pack(pady=10)

btn = tk.Button(root, text="URUCHOM ANALIZĘ PRZEPŁYWU", command=uruchom_kalkulator, bg="#006600", fg="white", font=("Arial", 9, "bold"), padx=10, pady=5)
btn.pack(pady=10)

label_profil = tk.Label(root, text="⚙️ Status systemu: Oczekiwanie na wprowadzenie danych...", font=("Arial", 9), fg="#aaaaaa", bg="#111111", justify="left")
label_profil.pack(pady=10)

label_kasa = tk.Label(root, text="💎 SKUMULOWANY KAPITAŁ: 0.0000 ZŁ", font=("Arial", 12, "bold"), fg="#00ff00", bg="#111111")
label_kasa.pack(pady=15)

root.mainloop()
