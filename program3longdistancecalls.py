import tkinter as tk
from tkinter import messagebox

def calculate_charges():
    try:
        minutes = float(entry_minutes.get())
        rate = rate_var.get()
        total_charges = minutes * rate
        messagebox.showinfo("Result", f"Total Charges: ${total_charges:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value for minutes.")

# GUI setup
root = tk.Tk()
root.title("Long-Distance Call Charges")

tk.Label(root, text="Minutes:").grid(row=0, column=0)
entry_minutes = tk.Entry(root)
entry_minutes.grid(row=0, column=1)

rate_var = tk.DoubleVar(value=0.02)

rate_categories = [
    ("Daytime ($0.02 per minute)", 0.02),
    ("Evening ($0.12 per minute)", 0.12),
    ("Off-Peak ($0.05 per minute)", 0.05),
]

for i, (label, rate) in enumerate(rate_categories):
    tk.Radiobutton(root, text=label, variable=rate_var, value=rate).grid(row=i+1, column=0, columnspan=2, sticky="w")

tk.Button(root, text="Calculate Charges", command=calculate_charges).grid(row=len(rate_categories)+1, column=0, columnspan=2)

root.mainloop()
