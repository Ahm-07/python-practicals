print("UIN:251A025")
print("Date:17-02-26")
try:
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    c=a/b
except ZeroDivisionError,ValueError,TypeError:
    print("b should not be zero")
else:
    print(c)