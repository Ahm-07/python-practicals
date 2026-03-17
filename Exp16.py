print("UIN:251A025")
print("Date:17-03-2026")
import re
phone = input("Enter your number:")
email = input("Enter your Email:")

mobile_pattern= r"^[6-9]\d{9}$"
email_pattern= r"^[\w\.-]+@[\w\.-]+
\.[\w\.-]{2,}+$"

if re.fullmatch(mobile_pattern,phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

if re.match(email_pattern,email):
    print("Valid Email Id")
else:
    print("Invalid Email Id")
