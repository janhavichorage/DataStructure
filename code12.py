# Student Marks Calculator

name = input("Enter student name: ")
marks = []
for i in range(3):
    m = float(input(f"Enter marks {i+1}: "))
    marks.append(m)
total = sum(marks)
percentage = total / 3
print("Name:", name)
print("Total:", total, "Percentage:", percentage)