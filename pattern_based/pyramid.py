# pyramid.py
# This program prints a pyramid star pattern

rows = int(input("Enter number of rows: "))

for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("* " * (i + 1))
