n = int(input("Enter number of students: "))
quota = int(input("Enter scholarship quota: "))

students = []

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    if marks >= 75 and attendance >= 75 and income <= 250000:
        students.append([name, marks])

# Rank students by marks
students.sort(key=lambda x: x[1], reverse=True)

print("\nSelected Scholarship Students:")

if quota < 0:
    print("Invalid scholarship quota")
else:
    count = 0
    for student in students:
        if count < quota:
            count += 1
            print(count, student[0], "Marks:", student[1])

    if count == 0:
        print("No students selected")