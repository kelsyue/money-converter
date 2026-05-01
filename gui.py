import tkinter as tk
from tkinter import messagebox
from converter import convert_currency

class CurrencyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GlobalScale Currency Utility")
        self.root.geometry("420x550")
        
        # Refined Color Palette
        self.bg_light = "#F8F9FA"
        self.primary_pink = "#FFC1CC"
        self.hover_pink = "#FFB2C1" # Slightly darker for the click
        self.border_gray = "#2C3E50"
        self.dark_text = "#2C3E50"

        self.root.configure(bg=self.bg_light, padx=40, pady=40)

        # Title
        tk.Label(
            root, text="Currency Converter", 
            bg=self.bg_light, fg=self.dark_text, 
            font=("Helvetica", 20, "bold")
        ).pack(pady=(0, 30))

        # Amount Entry
        tk.Label(root, text="Amount (USD):", bg=self.bg_light, fg=self.dark_text, font=("Helvetica", 11, "bold")).pack(anchor="w")
        self.amount_entry = tk.Entry(
            root, font=("Helvetica", 16), bg="white",
            fg=self.dark_text, relief="solid", highlightthickness=1, 
            highlightbackground=self.border_gray, bd=0, justify="center"
        )
        self.amount_entry.pack(fill="x", pady=(8, 20), ipady=8)
        self.amount_entry.insert(0, "23")

        # Currency Selection
        tk.Label(root, text="Target Currency:", bg=self.bg_light, fg=self.dark_text, font=("Helvetica", 11, "bold")).pack(anchor="w")
        self.currency_list = ["EUR", "GBP", "JPY", "USD"]
        self.selected_cur = tk.StringVar(root)
        self.selected_cur.set("GBP")
        
        self.opt = tk.OptionMenu(root, self.selected_cur, *self.currency_list)
        self.opt.config(
            bg="white", fg=self.dark_text, font=("Helvetica", 12), 
            relief="solid", highlightthickness=1, highlightbackground=self.border_gray, bd=0
        )
        self.opt["menu"].config(bg="white", fg=self.dark_text)
        self.opt.pack(fill="x", pady=(8, 30))

        # CONVERT Button - FIXED CLICK STATE
        self.calc_btn = tk.Button(
            root, text="CONVERT", command=self.handle_convert,
            bg=self.primary_pink, fg=self.dark_text, font=("Helvetica", 12, "bold"),
            relief="solid", bd=2, pady=15, cursor="hand2",
            activebackground=self.hover_pink, # Stays pink when clicked
            activeforeground=self.dark_text   # Text stays dark when clicked
        )
        self.calc_btn.pack(fill="x")

        # Result Display
        self.res_var = tk.StringVar(value="-- result --")
        self.result_label = tk.Label(
            root, textvariable=self.res_var, bg=self.primary_pink, 
            fg=self.dark_text, font=("Helvetica", 18, "bold"), 
            pady=25, relief="solid", bd=2
        )
        self.result_label.pack(fill="x", pady=30)

    def handle_convert(self):
        try:
            amt = float(self.amount_entry.get())
            target = self.selected_cur.get()
            res = convert_currency(amt, "USD", target)
            self.res_var.set(f"{res} {target}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyApp(root)
    root.mainloop()