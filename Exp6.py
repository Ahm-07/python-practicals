print("UIN:251A025")
print("Date:04-02-2026")
# Create sets for students appearing in different exams
CET = {"251A025", "251A026", "251A028", "251A029"}
JEE = {"251A025", "251A023", "251A029", "251A035"}
NEET = {"251A025", "251A023","251A028"}
# Union operation
all_students = CET | JEE | NEET
print("Students appearing in at least one exam:")
print(all_students)
# Intersection operation
common_students = CET & JEE & NEET
print("\nStudents appearing in all three exams:")
print(common_students)
# Difference operation
cet_only = CET - JEE - NEET
print("\nStudents appearing only for CET:")
print(cet_only)
# Appeared for CET and JEE but not NEET
cet_jee_not_neet = (CET & JEE) - NEET
print("\nStudents appeared for CET and JEE but not NEET:")
print(cet_jee_not_neet)
# Appeared for CET and NEET but not both
cet_neet_not_both = (CET | NEET) - (CET & NEET)
print("\nStudents appeared for CET or NEET but not both:")
print(cet_neet_not_both)
