import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        miles = float(entry_miles.get())
        gallons = float(entry_gallons.get())
        mpg = miles / gallons
        messagebox.showinfo("Result", f"MPG: {mpg:.2f} miles per gallon")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("MPG Calculator")

tk.Label(root, text="Miles driven:").grid(row=0, column=0)
entry_miles = tk.Entry(root)
entry_miles.grid(row=0, column=1)

tk.Label(root, text="Gallons of gas:").grid(row=1, column=0)
entry_gallons = tk.Entry(root)
entry_gallons.grid(row=1, column=1)

tk.Button(root, text="Calculate MPG", command=calculate_mpg).grid(row=2, column=0, columnspan=2)

root.mainloop()
