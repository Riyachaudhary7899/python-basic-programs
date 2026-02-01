# sum_of_digits.py
# This program finds the sum of digits of a number

num = int(input("Enter a number: "))
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum of digits:", total)
