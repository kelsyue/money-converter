import tkinter as tk
from tkinter import messagebox
from converter import convert_currency

class CurrencyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GlobalScale Currency")
        self.root.geometry("300x200")

        tk.Label(root, text="Amount:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Label(root, text="To (e.g. EUR, JPY):").pack()
        self.to_cur = tk.Entry(root)
        self.to_cur.pack()

        tk.Button(root, text="Convert from USD", command=self.handle_convert).pack(pady=10)
        self.result_label = tk.Label(root, text="Result: --", font=("Arial", 10, "bold"))
        self.result_label.pack()

    def handle_convert(self):
        try:
            amt = float(self.amount_entry.get())
            res = convert_currency(amt, "USD", self.to_cur.get())
            self.result_label.config(text=f"Result: {res}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyApp(root)
    root.mainloop()