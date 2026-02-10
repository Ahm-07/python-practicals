print("UIN:251A025")
print("Date:09-02-2026")
# Printing a right-angled triangle pattern

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()