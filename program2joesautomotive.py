import tkinter as tk

def calculate_total():
    total = 0
    if var_oil.get(): total += 30.00
    if var_lube.get(): total += 20.00
    if var_radiator.get(): total += 40.00
    if var_transmission.get(): total += 100.00
    if var_inspection.get(): total += 35.00
    if var_muffler.get(): total += 200.00
    if var_tire.get(): total += 20.00
    total_label.config(text=f"Total Charges: ${total:.2f}")

# GUI setup
root = tk.Tk()
root.title("Joe's Automotive")

var_oil = tk.BooleanVar()
var_lube = tk.BooleanVar()
var_radiator = tk.BooleanVar()
var_transmission = tk.BooleanVar()
var_inspection = tk.BooleanVar()
var_muffler = tk.BooleanVar()
var_tire = tk.BooleanVar()

services = [
    ("Oil Change - $30.00", var_oil),
    ("Lube Job - $20.00", var_lube),
    ("Radiator Flush - $40.00", var_radiator),
    ("Transmission Fluid - $100.00", var_transmission),
    ("Inspection - $35.00", var_inspection),
    ("Muffler Replacement - $200.00", var_muffler),
    ("Tire Rotation - $20.00", var_tire),
]

for i, (service, var) in enumerate(services):
    tk.Checkbutton(root, text=service, variable=var).grid(row=i, column=0, sticky="w")

tk.Button(root, text="Calculate Total", command=calculate_total).grid(row=len(services), column=0)

total_label = tk.Label(root, text="Total Charges: $0.00")
total_label.grid(row=len(services) + 1, column=0)

root.mainloop()
