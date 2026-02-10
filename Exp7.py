Student={}
n=int(input("Enter the number of students:"))
for _ in range(n):
    name=input("Name: ")
    Student[name]={"UIN":input("Enter UIN: "), "Grade":input("Enter Grade: "),"Attendance":input("Enter Attendance: ")}
print(Student)
u=input("Update Attendance for: ")
if u in Student:
    Student[u]["Attendance"]=input("New Attendance: ")
print(Student)