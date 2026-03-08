print("UIN:251A025")
print("Date:23-02-26")
def factorial():
    fact=1
    n=int(input("Enter the number: "))
    for i in range(1,n):
        fact=fact*i
    print("Factorial=",fact)
factorial()