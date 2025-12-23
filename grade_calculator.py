# Project: Student Grade Calculator
# Description: Calculates grades for multiple students, stores results,
# shows statistics, and allows searching & saving data.
# Author: ujjwal raj


def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'
    
def grade_comment(grade):
    if grade == 'A':
        return "Exellent work!"
    if grade == 'B':
        return "Good job!"
    if grade == 'C':
        return "Fair effort."
    if grade == 'D':
        return "Needs improvement."
    if grade == 'F':
        return "Failed. Better luck next time."
    return "No comment."

print("-" * 40)    
print("Welcome to the Student Grade Calculator")
print("-" * 40)

print( )
    
students = []
results = []

# Validate number of students
while True:
    
    try:
        total_students = int(input("Enter number of students: "))
        if total_students > 0:
            break
        else:
            print("Enter a positive number.")
    except ValueError:
        print("Invalid input. Enter a number.")

for i in range(total_students):
    
    print(f"{"="*3}Student{i+1}{"="*3}")
    

    name = input("Enter student name: ")

    marks = []
    for j in range(3):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {j+1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid marks. Enter a number.")

    average = sum(marks) / 3
    grade = calculate_grade(average)
    comment = grade_comment(grade)

    student_data = {
        "name": name,
        "marks": marks,
        "average": average,
        "grade": grade,
        "comment": comment
    }

    results.append(student_data)
averages = [student["average"] for student in results]

class_avg = sum(averages) / len(averages)
highest = max(averages)
lowest = min(averages)
print("\n--- Student Results ---")
print("-" * 70)
print(f"{'Name':15}{'Avg':10}{'Grade':10}{'Comment'}")
print("-" * 70)

for s in results:
    grade_color = ""
    if s["grade"] == "A":
        grade_color = "\033[92m"  # Green
    elif s["grade"] == "F":
        grade_color = "\033[91m"  # Red
    else:
        grade_color = "\033[93m"  # Yellow

    print(f"{s['name']:15}{s['average']:<10.2f}{grade_color}{s['grade']:<10}\033[0m{s['comment']}")

print("-" * 70)
print(f"Class Average: {class_avg:.2f}")
print(f"Highest Average: {highest:.2f}")
print(f"Lowest Average: {lowest:.2f}")
search_name = input("\nEnter student name to search (or press Enter to skip): ")

if search_name:
    found = False
    for s in results:
        if s["name"].lower() == search_name.lower():
            print("\nStudent Found:")
            print(s)
            found = True
            break
    if not found:
        print("Student not found.")

save = input("\nDo you want to save results to file? (yes/no): ")

if save.lower() == "yes":
    with open("student_results.txt", "w") as file:
        for s in results:
            file.write(f"{s}\n")
    print("Results saved successfully.")


print('-' * 50)
print("Thank you for using the Student Grade Calculator!")
print('-' * 50)