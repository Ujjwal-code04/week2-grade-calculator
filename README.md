# 🎓 Student Grade Calculator

A comprehensive Python-based Student Grade Calculator that processes multiple students’ marks, calculates grades with personalized comments, and provides class statistics.

---

## 📁 GitHub Structure

```
week2-grade-calculator/
│── grade_calculator.py
│── test_students.txt
│── results_sample.txt
│── README.md
└── .gitignore
```

---

## 📌 Project Description

The Student Grade Calculator is a command-line application that:
- Processes multiple students’ marks
- Calculates average scores and grades
- Provides personalized comments
- Displays results in a formatted table
- Generates class statistics (average, highest, lowest)
- Supports searching and saving results to a file

---

## 📘 What I Learned

- Conditional Logic: Using if / elif / else for decision making  
- Lists: Storing and manipulating collections of data  
- Loops: Using for and while loops  
- Error Handling: Using try-except for invalid inputs  
- Functions: Organizing code into reusable blocks  

---

## ✨ Features

✓ Processes multiple students  
✓ Calculates grades using a custom grading system  
✓ Personalized comments for each student  
✓ Class statistics (average, highest, lowest)  
✓ Formatted table output with color coding  
✓ Input validation for all user inputs  
✓ Error handling for edge cases  
✓ Search functionality for students  
✓ Save results to file option  

---

## ▶️ How to Run

```bash
# Navigate to project folder
cd week2-grade-calculator

# Run the program
python grade_calculator.py

# Test with provided input file
python grade_calculator.py < test_students.txt
```

---

## 🧮 Grading System

| Average Marks | Grade | Description |
|--------------|-------|-------------|
| 90 – 100 | A | Excellent! |
| 80 – 89 | B | Very Good! |
| 70 – 79 | C | Good |
| 60 – 69 | D | Needs Improvement |
| 0 – 59  | F | Failed – Please seek help |

---

## 📊 Sample Output

```
----------------------------------------
Welcome to the Student Grade Calculator
----------------------------------------

Enter number of students: 2
===Student1===
Enter student name: Ujjwal raj
Enter marks for subject 1: shreya
Invalid marks. Enter a number.
Enter marks for subject 1: 75
Enter marks for subject 2: 78
Enter marks for subject 3: 78
===Student2===
Enter student name: shreya
Enter marks for subject 1: 89
Enter marks for subject 2: 78
Enter marks for subject 3: 87

--- Student Results ---
----------------------------------------------------------------------
Name           Avg       Grade     Comment
----------------------------------------------------------------------
Ujjwal raj     77.00     C         Fair effort.
shreya         84.67     B         Good job!
----------------------------------------------------------------------
Class Average: 80.83
Highest Average: 84.67
Lowest Average: 77.00

Enter student name to search (or press Enter to skip):

Do you want to save results to file? (yes/no):
--------------------------------------------------
Thank you for using the Student Grade Calculator!
--------------------------------------------------

```

---

## 🧠 Challenges & Solutions

**Challenge:** Handling invalid marks input  
**Solution:** Used while loop with try-except validation  

**Challenge:** Formatting the results table  
**Solution:** Used fixed-width string formatting  

**Challenge:** Calculating multiple statistics  
**Solution:** Used list comprehensions and built-in functions  

---

## 👨‍💻 Author

ujjwal Raj  
Engineering Student  

---

## 📜 License

This project is for educational purposes and is free to use and modify.
