Student Grade Calculator
Project Description
A comprehensive grade calculator that processes multiple students' marks, calculates grades with personalized comments, and provides class statistics.

What I Learned
Conditional Logic: Using if/elif/else for decision making
Lists: Storing and manipulating collections of data
Loops: Using for and while loops for repetition
Error Handling: Using try-except to handle invalid inputs
Functions: Organizing code into reusable blocks
Features
✓- Processes multiple students
✓- Calculates grades based on custom grading system
✓- Provides personalized comments for each student
✓- Calculates class statistics (average, highest, lowest)
✓- Formatted table output with color coding
✓- Input validation for all user inputs
✓- Error handling for edge cases
✓- Search functionality for specific students
✓- Save results to file option
How to Run
bash Copy
# Navigate to project folder
cd week2-grade-calculator

# Run the program
python grade_calculator.py

# Sample test with provided data
python grade_calculator.py < test_students.txt
Grading System
A: 90-100 (Excellent!)
B: 80-89 (Very Good!)
C: 70-79 (Good)
D: 60-69 (Needs Improvement)
F: 0-59 (Failed - Please seek help)
Sample Output
Code Copy
----------------------------------------
Welcome to the Student Grade Calculator
----------------------------------------

Enter number of students: 2
===Student1===
Enter student name: ujjwal raj
Enter marks for subject 1: 78
Enter marks for subject 2: 68
Enter marks for subject 3: 78
===Student2===
Enter student name: shreya
Enter marks for subject 1: 48
Enter marks for subject 2: 75
Enter marks for subject 3: 85

--- Student Results ---
----------------------------------------------------------------------
Name           Avg       Grade     Comment
----------------------------------------------------------------------
ujjwal raj     74.67     C         Fair effort.
shreya         69.33     D         Needs improvement.
----------------------------------------------------------------------
Class Average: 72.00
Highest Average: 74.67
Lowest Average: 69.33

Enter student name to search (or press Enter to skip): 

Do you want to save results to file? (yes/no): yes
Results saved successfully.
--------------------------------------------------
Thank you for using the Student Grade Calculator!
--------------------------------------------------
Challenges & Solutions
Challenge: Handling invalid marks input

Solution: Used while loop with try-except to validate

Challenge: Formatting the results table

Solution: Used string formatting with fixed widths

Challenge: Calculating multiple statistics

Solution: Used list comprehensions and built-in functions
