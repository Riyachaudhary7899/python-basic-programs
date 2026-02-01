# right_triangle.py
# This program prints a right angle triangle star pattern

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
