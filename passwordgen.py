import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*()-_="

upper, lower, digit, symbol = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if digit:
    all += digits
if symbol:
    all += symbols

length = 12
amount = 2

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)