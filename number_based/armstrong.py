# armstrong.py
# This program checks whether a number is an Armstrong number

num = int(input("Enter a number: "))
original = num
total = 0

while num > 0:
    digit = num % 10
    total += digit ** 3
    num //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
