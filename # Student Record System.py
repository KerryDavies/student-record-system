# Student Record System
name = input("Enter student name: ")
student_id = input("Enter student ID: ")

score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

average = (score1 + score2 + score3) / 3

if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print("Student Record")
print("Name:", name)
print("ID:", student_id)
print("Average:", average)
print("Grade:", grade)