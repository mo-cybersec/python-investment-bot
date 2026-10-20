import tkinter as tk
from tkinter import messagebox
import time
import threading

# ====================================================================
# HOLDING: mo-cybersec (v3.0)
# CORE INTEGRATION: Secure Authentication Gateway + Financial Engine
# TARGET MARKET: US Enterprise B2B / Useme Verified Infrastructure
# ====================================================================

class SecureCapitalApp:
    def _init_(self, root):
        self.root = root
        self.root.title("mo-cybersec // Enterprise Capital Flow Engine v3.0")
        self.root.geometry("500x350")
        self.root.configure(bg="#0f172a") # Dark old money luxury theme
        self.root.resizable(False, False)
        
        # System Master Security Credentials
        self.SECRET_PASSWORD = "mo-cybersec-admin"
        
        # Initialize Boot and Security Protocol
        self.render_boot_screen()

    def render_boot_screen(self):
        """Simulates a professional cybersec integrity check to impress clients."""
        self.clear_screen()
        
        lbl_boot = tk.Label(self.root, text="INITIALIZING MO-CYBERSEC COMPLIANCE...", font=("Courier New", 12, "bold"), fg="#38bdf8", bg="#0f172a")
        lbl_boot.pack(pady=40)
        
        self.lbl_status = tk.Label(self.root, text="[ SYSTEM ] Loading firewall rules...", font=("Courier New", 10), fg="#94a3b8", bg="#0f172a")
        self.lbl_status.pack(pady=10)
        
        # Run system check simulation in a background thread
        threading.Thread(target=self.simulate_security_check).start()

    def simulate_security_check(self):
        steps = [
            "[ SHIELD ] Encrypted database handshake... OK",
            "[ FIREWALL ] Token verification gateway active... OK",
            "[ CYBERSEC ] Memory overflow protection armed... OK",
            "SECURE ENVIRONMENT VERIFIED. ACCESS READY."
        ]
        for step in steps:
            time.sleep(0.4)
            self.lbl_status.config(text=step)
            if "READY" in step:
                self.lbl_status.config(fg="#22c55e")
        
        time.sleep(0.4)
        self.root.after(0, self.render_login_screen)

    def render_login_screen(self):
        """Renders the secure gateway login screen."""
        self.clear_screen()
        self.root.geometry("450x320")
        
        lbl_title = tk.Label(self.root, text="SECURITY GATEWAY v3.0", font=("Arial", 14, "bold"), fg="#38bdf8", bg="#0f172a")
        lbl_title.pack(pady=20)
        
        lbl_prompt = tk.Label(self.root, text="Enter Admin Password to Authorize Session:", font=("Arial", 10), fg="#94a3b8", bg="#0f172a")
        lbl_prompt.pack(pady=5)
        
        # Password Input Field
        self.ent_password = tk.Entry(self.root, show="*", font=("Arial", 12), width=25, bg="#1e293b", fg="#ffffff", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#334155")
        self.ent_password.pack(pady=10)
        self.ent_password.focus()
        
        # Auth Button
        btn_login = tk.Button(self.root, text="Authenticate Session", font=("Arial", 10, "bold"), bg="#0284c7", fg="#ffffff", activebackground="#0369a1", activeforeground="#ffffff", bd=0, padx=15, pady=7, command=self.verify_credentials)
        btn_login.pack(pady=15)

    def verify_credentials(self):
        """Cybersec module checking access token against firewall."""
        entered_pass = self.ent_password.get()
        
        if entered_pass == self.SECRET_PASSWORD:
            messagebox.showinfo("ACCESS GRANTED", "Verification successful. Initializing secure dashboard...")
            self.render_main_dashboard()
        else:
            messagebox.showerror("ACCESS DENIED", "CRITICAL ERROR: Invalid password. Request blocked by system firewall.")
            self.ent_password.delete(0, tk.END)

    def render_main_dashboard(self):
        """Loads the secure financial dashboard and calculator after successful authentication."""
        self.clear_screen()
        self.root.geometry("500x420")
        
        lbl_dash = tk.Label(self.root, text="SYSTEM AUTHORIZED // FINANCIAL ENGINE", font=("Arial", 12, "bold"), fg="#22c55e", bg="#0f172a")
        lbl_dash.pack(pady=15)
        
        lbl_input = tk.Label(self.root, text="Enter Target Annual Capital (PLN):", font=("Arial", 10), fg="#94a3b8", bg="#0f172a")
        lbl_input.pack(pady=5)
        
        # Capital Input Field
        self.ent_capital = tk.Entry(self.root, font=("Arial", 12), width=20, bg="#1e293b", fg="#ffffff", insertbackground="white", bd=0)
        self.ent_capital.pack(pady=5)
        
        # Calculation Trigger
        btn_calc = tk.Button(self.root, text="Initialize Engine", font=("Arial", 10, "bold"), bg="#22c55e", fg="#ffffff", activebackground="#16a34a", bd=0, padx=15, pady=7, command=self.start_engine)
        btn_calc.pack(pady=10)
        
        # Real-time counter status outputs (Original Business Logic)
        self.lbl_sec_status = tk.Label(self.root, text="Capital Flow / Second: --", font=("Arial", 11), fg="#e2e8f0", bg="#0f172a")
        self.lbl_sec_status.pack(pady=10)
        
        self.lbl_min_status = tk.Label(self.root, text="Capital Flow / Minute: --", font=("Arial", 11), fg="#e2e8f0", bg="#0f172a")
        self.lbl_min_status.pack(pady=5)
        
        self.lbl_hour_status = tk.Label(self.root, text="Capital Flow / Hour: --", font=("Arial", 11), fg="#e2e8f0", bg="#0f172a")
        self.lbl_hour_status.pack(pady=5)

    def start_engine(self):
        """Cybersec try/except block protecting enterprise logic from data corruption crashes."""
        try:
            annual_target = float(self.ent_capital.get())
            
            # Mathematical formulas for business tracking
            per_second = annual_target / (365 * 24 * 60 * 60)
            per_minute = per_second * 60
            per_hour = per_minute * 60
            
            # Updating UI components with custom precision
            self.lbl_sec_status.config(text=f"Capital Flow / Second: {per_second:.6f} PLN", fg="#22c55e")
            self.lbl_min_status.config(text=f"Capital Flow / Minute: {per_minute:.4f} PLN", fg="#38bdf8")
            self.lbl_hour_status.config(text=f"Capital Flow / Hour: {per_hour:.2f} PLN", fg="#e2e8f0")
            
        except ValueError:
            # System protection module against alphabetical strings
            messagebox.showwarning("DATA CORRUPTION SHIELD", "CRITICAL EXCEPTION: Alphabetical inputs blocked by secure firewall rules. Please enter numerical values only.")

    def clear_screen(self):
        """Utility function to clear widgets from screen frame."""
        for widget in self.root.winfo_children():
            widget.destroy()

if _name_ == "_main_":
    app_root = tk.Tk()
    app = SecureCapitalApp(app_root)
    app_root.mainloop()
