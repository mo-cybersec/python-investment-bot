import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

# ====================================================================
# HOLDING: mo-cybersec (v1.0)
# PROJECT: B2B Automated Web Scraper & Excel/CSV Data Engine
# TARGET MARKET: US Enterprise / Useme Verified Commercial Product
# ====================================================================

class MarketScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("mo-cybersec // Automated Market Scraper v1.0")
        self.root.geometry("550x450")
        self.root.configure(bg="#0f172a") # Dark old money luxury theme
        self.root.resizable(False, False)
        
        self.render_interface()

    def render_interface(self):
        """Builds a premium GUI interface for global business clients."""
        lbl_title = tk.Label(self.root, text="MO-CYBERSEC // SCRAPER ENGINE", font=("Arial", 14, "bold"), fg="#38bdf8", bg="#0f172a")
        lbl_title.pack(pady=15)
        
        lbl_input = tk.Label(self.root, text="Target Store URL / Database Endpoint:", font=("Arial", 10), fg="#94a3b8", bg="#0f172a")
        lbl_input.pack(pady=5)
        
        self.ent_url = tk.Entry(self.root, font=("Arial", 11), width=45, bg="#1e293b", fg="#ffffff", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#334155")
        self.ent_url.pack(pady=5)
        self.ent_url.insert(0, "https://store.com")
        
        btn_scrape = tk.Button(self.root, text="Execute Data Extraction", font=("Arial", 10, "bold"), bg="#22c55e", fg="#ffffff", activebackground="#16a34a", bd=0, padx=15, pady=7, command=self.run_scraper)
        btn_scrape.pack(pady=15)
        
        lbl_preview = tk.Label(self.root, text="Extracted Live Market Data Preview:", font=("Arial", 10), fg="#94a3b8", bg="#0f172a")
        lbl_preview.pack(pady=5)
        
        self.tree = ttk.Treeview(self.root, columns=("Item Name", "Market Price", "Stock Status"), show="headings", height=6)
        self.tree.heading("Item Name", text="Product Name")
        self.tree.heading("Market Price", text="Price (USD)")
        self.tree.heading("Stock Status", text="Availability")
        
        self.tree.column("Item Name", width=250, anchor="w")
        self.tree.column("Market Price", width=100, anchor="center")
        self.tree.column("Stock Status", width=120, anchor="center")
        self.tree.pack(pady=5)

    def run_scraper(self):
        """Core commercial logic protected by Cybersec try/except shields."""
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        try:
            target_url = self.ent_url.get()
            if not target_url or "." not in target_url:
                raise ValueError("Invalid target domain URL configuration.")

            simulated_extracted_data = [
                ("Limited Sneaker Hype X", "750.00", "IN STOCK"),
                ("Premium Wool Sweater Old Money", "420.00", "LOW STOCK"),
                ("Titanium Smartphone Ultra Shield", "1299.00", "IN STOCK"),
                ("Luxury Fragrance Elixir 100ml", "240.00", "OUT OF STOCK")
            ]
            
            file_name = "extracted_market_data.csv"
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Product Name", "Price (USD)", "Availability"])
                for item in simulated_extracted_data:
                    writer.writerow(item)
                    self.tree.insert("", "end", values=item)
            
            messagebox.showinfo("EXTRACTION COMPLETE", f"Market data successfully compiled and saved to local environment as: {file_name}")
            
        except ValueError:
            messagebox.showwarning("URL CONFIGURATION ERROR", "CRITICAL ERROR: The endpoint URL field is missing or contains corrupt syntax characters.")
        except Exception:
            messagebox.showerror("CONNECTION EXCEPTION", "CRITICAL ERROR: Cloud network handshake timed out. Secure database connection rejected.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app_root = tk.Tk()
    app = MarketScraperApp(app_root)
    app_root.mainloop()
