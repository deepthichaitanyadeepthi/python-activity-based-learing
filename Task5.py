# Student Performance Trend Analysis

name = input("Enter student name: ")

n = int(input("Enter number of subjects: "))

for i in range(n):
    print("\nSubject", i + 1)

    subject = input("Enter subject name: ")
    s1 = float(input("Enter first exam marks: "))
    s2 = float(input("Enter second exam marks: "))
    s3 = float(input("Enter third exam marks: "))

    change = s3 - s1

    print("Subject:", subject)

    if change > 0:
        print("Performance improved by", change, "marks")
    elif change < 0:
        print("Performance declined by", abs(change), "marks")
    else:
        print("No change in performance")

    if s1 < 40 and s2 < 40 and s3 < 40:
        print("Weak subject")

    average = (s1 + s2 + s3) / 3

    print("Average Marks:", average)

    if average >= 75:
        print("Performance: Excellent")
    elif average >= 60:
        print("Performance: Good")
    elif average >= 40:
        print("Performance: Average")
    else:
        print("Performance: Poor")