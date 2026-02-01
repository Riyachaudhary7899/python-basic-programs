# table.py
# This program prints the multiplication table of a given number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
