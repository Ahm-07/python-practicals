print("UIN:251A025")
print("Date:10-02-2026")
def is_prime(n):
    if n == 1:
        return print("Neither Prime Nor Composite")
    else:
        tf_value = True
        for i in range(2, n):
            if n%i == 0:
                tf_value=False
                break
            else:
                tf_value=True
            
        if tf_value == True:
            print("the given number is prime.")
        else:
            print("the given number is not prime.")
        
n=int(input("Enter the number: "))
is_prime(n)