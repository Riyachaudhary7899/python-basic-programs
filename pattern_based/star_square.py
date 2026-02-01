# star_square.py
# This program prints a square star pattern

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()
