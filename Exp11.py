print("UIN:251A025")
print("Date:16-02-2026")

def add(a, b):
    return a + b
    
def sub(a, b):
    return a - b 

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Number should be Non zero!!!")
        return
    else:    
        return a / b

def modulus(a,b):
    return a % b
    
choice = ""
while choice != "exit":
    choice = input("---MENU---\n 1:ADDITION\n 2:SUBTRACTION\n 3:DIVISION\n 4:MULTIPLICATION\n 5:MODULUS\n EXIT:Exit the Program\n").lower()
    if choice == "exit":
        print("Exiting Program!!!")
        break
    else:
        a=int(input("Enter the first number(a): "))
        b=int(input("Enter the second number(b): "))
        if choice == "1":
            print("Sum=",add(a ,b))
        elif choice == "2":
            print("Difference=",sub(a ,b))
        elif choice == "3":
            print("Division=",divide(a ,b))
        elif choice == "4":
            print("Product=",multiply(a ,b))
        elif choice == "5":
            print("Remainder=",modulus(a,b))    
        else:
            print("Wrong input!!Please Try Again")