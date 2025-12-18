import random
import tkinter as tk
from tkinter import ttk

clear_job = None
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
errors = []

def copy_to_clipboard():
    selection = output.curselection()
    if selection:
        password_line = output.get(selection[0])
        password_only = password_line.split()[0]
        root.clipboard_clear()
        root.clipboard_append(password_only)

def clear_errors():
    output.delete(0, tk.END)

def on_select(event):
    if output.curselection():
        copy_button.config(state="normal")
    else:
        copy_button.config(state="disabled")

def password_strength(password):
        length = len(password)
        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        symbol = any(c in symbols for c in password)

        types_count = sum([lower, upper, digit, symbol])
        if length < 8 or types_count == 2:
            return "Weak"
        elif length < 12 or types_count == 3:
            return "Moderate"
        else:
            return "Strong"

def generate_passwords():

    global clear_job
    errors.clear()

    all_chars = ""

    if upper_var.get():
        all_chars += upper
    if lower_var.get():
        all_chars += lower
    if digits_var.get():
        all_chars += digits
    if symbols_var.get():
        all_chars += symbols

    output.delete(0, tk.END)

    if not all_chars:
        errors.append("Select at least one character set.\n")

    try:
        length = int(length_entry.get())
        amount = int(amount_entry.get())
    
    except ValueError:
        errors.append("Length and amount must numbers greater than 0.\n")
    else:
        if length <= 0:
            errors.append("Length must be greater than 0.\n")
        if amount <= 0:
            errors.append("Amount must be greater than 0.\n")

    if errors:
        output.delete(0, tk.END)
        for err in errors:
            output.insert(tk.END, err + "")
        
        if clear_job is not None:
            root.after_cancel(clear_job)
        
        clear_job = root.after(3000, clear_errors)
        return

    for x in range(amount):
        password_chars = []
        selected_sets = []
        if upper_var.get():
            selected_sets.append(upper)
        if lower_var.get():
            selected_sets.append(lower)
        if digits_var.get():
            selected_sets.append(digits)
        if symbols_var.get():
            selected_sets.append(symbols)

        for char_set in selected_sets:
            password_chars.append(random.choice(char_set))
        
        remaining_length = length - len(password_chars)
        if remaining_length > 0:
            password_chars += random.choices(all_chars, k=remaining_length)

        random.shuffle(password_chars)
        password = "".join(password_chars)

        strength = password_strength(password)
        output.insert(tk.END, f"{password} [{strength}]")

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
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.pack(pady=5)

output = tk.Listbox(root, height=10)
output.pack(fill="both", expand=True)
output.bind("<<ListboxSelect>>", on_select)

root.mainloop()