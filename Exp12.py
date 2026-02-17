print("UIN:251A025")
print("Date:17-02-26")
file=open("File.txt","r")
content=file.read().split()
print(content)
n=int(input("Enter the word length: "))
for i in content:
    if len(i)==n:
        print(i)
file.close()