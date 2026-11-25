# University
# University Scholarship Allocation System

## Project Overview

The **University Scholarship Allocation System** is a Python-based project designed to evaluate scholarship applications and identify eligible students based on academic performance, attendance, and family income.

The system automatically checks eligibility, ranks qualified students, and resolves ranking ties using predefined rules.

## Objectives

- Evaluate students based on aggregate marks.
- Check minimum subject-wise marks.
- Verify attendance percentage.
- Check annual family income.
- Identify eligible and ineligible students.
- Rank eligible students based on merit.
- Resolve ties using predefined rules.

## Eligibility Criteria

| Criteria | Requirement |
|---|---|
| Aggregate Marks | Minimum 75% |
| Subject-wise Marks | Minimum 60 in each subject |
| Attendance | Minimum 75% |
| Annual Family Income | Maximum ₹2,50,000 |

## Tie-Breaking Rules

When students have equal aggregate marks, the system follows these rules:

1. Higher total subject marks.
2. Higher attendance percentage.
3. Lower annual family income.
4. Lower application ID.

## Technologies Used

- Python 3
- Visual Studio Code
- Git and GitHub

## Python Concepts Used

- Variables and Data Types
- Lists
- Dictionaries
- Conditional Statements
- For Loops
- Functions
- Sorting
- User Input and Output

## Algorithm

1. Start the program.
2. Get the number of scholarship applicants.
3. Collect student details.
4. Check aggregate marks.
5. Verify subject-wise minimum marks.
6. Check attendance and family income.
7. Separate eligible and rejected students.
8. Sort eligible students according to merit.
9. Apply tie-breaking rules.
10. Display the final scholarship ranking.
11. Display rejection reasons.
12. Stop the program.

## Project Structure

```text
University-Scholarship-Allocation/
│
├── scholarship.py
├── README.md
├── algorithm.txt
├── pseudocode.txt
├── flowchart.png
├── test_cases.txt
└── output_screenshots/
    ├── output1.png
    └── output2.png
```

## How to Run the Program

**Step 1:** Install Python 3.

**Step 2:** Download or clone this repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal.

**Step 5:** Execute the following command:

```bash
python scholarship.py
```

**Step 6:** Enter the applicant details when prompted.

The program will display eligible students, their merit rankings, and rejected students with reasons.

## Sample Test Cases

| Test Case | Condition | Expected Result |
|---|---|---|
| TC01 | All criteria satisfied | Eligible |
| TC02 | Aggregate below 75% | Rejected |
| TC03 | One subject below 60 | Rejected |
| TC04 | Attendance below 75% | Rejected |
| TC05 | Income above ₹2,50,000 | Rejected |
| TC06 | Equal aggregate marks | Apply tie-breaking rules |

## Expected Output

The program displays:

- Scholarship-eligible students.
- Merit ranking of eligible applicants.
- Application ID and student name.
- Aggregate and subject-wise marks.
- Attendance and annual income.
- Reasons for rejection.

## Conclusion

The University Scholarship Allocation System provides a simple and systematic method for evaluating scholarship applications using Python.

It reduces manual work, applies consistent eligibility criteria, ranks students based on merit, and resolves ties through predefined rules.

This project demonstrates the practical application of fundamental Python programming concepts.

---

**Project:** Python Activity-Based Learning  
**Case Study:** University Scholarship Allocation System  
**Language:** Python 3
