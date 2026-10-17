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
import tkinter as tk
from tkinter import messagebox
import time

# ==========================================
# HOLDING: mo-cybersec (v3.0)
# SECURITY COMPLIANCE: Admin Authentication
# ==========================================

class SecureCapitalApp:
    def _init_(self, root):
        self.root = root
        self.root.title("mo-cybersec // Capital Flow Engine v3.0")
        self.root.geometry("450x300")
        self.root.configure(bg="#0f172a") # Elegant dark old money theme
        self.root.resizable(False, False)
        
        # System Credentials
        self.SECRET_PASSWORD = "mo-cybersec-admin"
        
        # Initialize Security Gateway
        self.render_login_screen()

    def render_login_screen(self):
        """Renders the secure gateway login screen."""
        self.clear_screen()
        
        # Header
        lbl_title = tk.Label(self.root, text="SECURITY GATEWAY v3.0", font=("Arial", 14, "bold"), fg="#38bdf8", bg="#0f172a")
        lbl_title.pack(pady=20)
        
        lbl_prompt = tk.Label(self.root, text="Enter Admin Password to Access System:", font=("Arial", 10), fg="#94a3b8", bg="#0f172a")
        lbl_prompt.pack(pady=5)
        
        # Password Input Field
        self.ent_password = tk.Entry(self.root, show="*", font=("Arial", 12), width=25, bg="#1e293b", fg="#ffffff", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#334155")
        self.ent_password.pack(pady=10)
        self.ent_password.focus()
        
        # Auth Button
        btn_login = tk.Button(self.root, text="Authenticate Session", font=("Arial", 10, "bold"), bg="#0284c7", fg="#ffffff", activebackground="#0369a1", activeforeground="#ffffff", bd=0, padx=10, pady=5, command=self.verify_credentials)
        btn_login.pack(pady=15)

    def verify_credentials(self):
        """Cybersec module checking access token."""
        entered_pass = self.ent_password.get()
        
        if entered_pass == self.SECRET_PASSWORD:
            messagebox.showinfo("AUTH SUCCESS", "Access granted. Loading mo-cybersec environment...")
            self.render_main_dashboard()
        else:
            messagebox.showerror("AUTH FAILED", "Invalid password! Access denied by system firewall.")
            self.ent_password.delete(0, tk.END)

    def render_main_dashboard(self):
        """Loads the secure financial dashboard after successful authentication."""
        self.clear_screen()
        self.root.geometry("500x400")
        
        # Dashboard Header
        lbl_dash = tk.Label(self.root, text="SYSTEM AUTHORIZED // DASHBOARD", font=("Arial", 12, "bold"), fg="#22c55e", bg="#0f172a")
        lbl_dash.pack(pady=15)
        
        # Business Logic Input with Try/Except Protection
        lbl_input = tk.Label(self.root, text="Enter Target Annual Capital (PLN):", font=("Arial", 10), fg="#94a3b8", bg="#0f172a")
        lbl_input.pack(pady=5)
        
        self.ent_capital = tk.Entry(self.root, font=("Arial", 12), width=20, bg="#1e293b", fg="#ffffff", insertbackground="white", bd=0)
        self.ent_capital.pack(pady=5)
        
        btn_calc = tk.Button(self.root, text="Initialize Engine", font=("Arial", 10, "bold"), bg="#22c55e", fg="#ffffff", activebackground="#16a34a", bd=0, padx=10, pady=5, command=self.start_engine)
        btn_calc.pack(pady=10)
        
        # Real-time counter labels
        self.lbl_sec_status = tk.Label(self.root, text="Capital Flow / Second: --", font=("Arial", 11), fg="#e2e8f0", bg="#0f172a")
        self.lbl_sec_status.pack(pady=15)

    def start_engine(self):
        """Cybersec try/except block protecting business logic from crashes."""
        try:
            annual_target = float(self.ent_capital.get())
            per_second = annual_target / (365 * 24 * 60 * 60)
            self.lbl_sec_status.config(text=f"Capital Flow / Second: {per_second:.6f} PLN", fg="#22c55e")
        except ValueError:
            # System protection against alphabetical inputs
            messagebox.showwarning("DATA CORRUPTION WARNING", "CRITICAL ERROR: Please enter a valid numerical value. Alphabetical characters are blocked by system rules.")

    def clear_screen(self):
        """Utility function to clear widgets from screen frame."""
        for widget in self.root.winfo_children():
            widget.destroy()

if _name_ == "_main_":
    app_root = tk.Tk()
    app = SecureCapitalApp(app_root)
    app_root.mainloop()
