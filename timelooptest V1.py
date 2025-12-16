import time

lines = 5
seconds = 1

timetest = f"this is a time test file. Will print {lines} lines in {seconds} seconds"
print(timetest)
for i in range(lines):
    time.sleep(seconds)
    print(f"Line {i + 1}")