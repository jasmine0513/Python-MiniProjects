import random
import tkinter as tk
from tkinter import ttk

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

def generate_passwords():

    def password_strength(password):
        score = 0

        if any(c.islower() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in symbols for c in password):
            score += 1
        if len(password) >= 12:
            score += 1

        if score <= 2:
            return "Weak"
        elif score == 3:
            return "Moderate"
        else:
            return "Strong"

    all_chars = ""

    if upper_var.get():
        all_chars += upper
    if lower_var.get():
        all_chars += lower
    if digits_var.get():
        all_chars += digits
    if symbols_var.get():
        all_chars += symbols
    length = int(length_entry.get())
    amount = int(amount_entry.get())

    output.delete("1.0", tk.END)

    if not all_chars:
        output.insert(tk.END, "Please check at least one character set.\n")
        return

    for x in range(amount):
        password = "".join(random.choices(all_chars, k= length))
        strength = password_strength(password)
        output.insert(tk.END, f"{password} [{strength}]\n")

#GUI Setup

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

ttk.Checkbutton(root, text="Uppercase Letters", variable=upper_var).pack(anchor="w")
ttk.Checkbutton(root, text="Lowercase Letters", variable=lower_var).pack(anchor="w")
ttk.Checkbutton(root, text="Digits", variable=digits_var).pack(anchor="w")
ttk.Checkbutton(root, text="Symbols", variable=symbols_var).pack(anchor="w")

ttk.Label(root, text="Password Length:").pack()
length_entry = ttk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

ttk.Label(root, text="Amount").pack()
amount_entry = ttk.Entry(root)
amount_entry.insert(0, "5")
amount_entry.pack()

ttk.Button(root, text="Generate Passwords", command=generate_passwords).pack(pady=10)

output = tk.Text(root, height=10)
output.pack(fill="both", expand=True)

root.mainloop()