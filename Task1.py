n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks: "))

    subjects = list(map(float, input("Enter 5 subject marks: ").split()))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    if (marks >= 75 and min(subjects) >= 40
            and attendance >= 75 and income <= 250000):
        students.append([name, marks, attendance, income])

# Sort by marks, attendance, and income
students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\nScholarship Eligible Students:")

if len(students) == 0:
    print("No eligible students")
else:
    for rank, s in enumerate(students, 1):
        print(rank, s[0], "- Marks:", s[1])