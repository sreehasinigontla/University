
# University Scholarship Allocation System

# Scholarship Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

# Function to check student eligibility
def check_eligibility(student):

    reasons = []

    if student["aggregate"] < MIN_AGGREGATE:
        reasons.append("Aggregate marks below 75%")

    if min(student["subjects"]) < MIN_SUBJECT_MARKS:
        reasons.append("Subject-wise marks below 60")

    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if student["income"] > MAX_INCOME:
        reasons.append("Family income exceeds limit")

    return reasons


# Function to calculate scholarship ranking
def rank_students(students):

    eligible = []
    rejected = []

    for student in students:

        reasons = check_eligibility(student)

        if len(reasons) == 0:
            eligible.append(student)
        else:
            student["reasons"] = reasons
            rejected.append(student)

    # Ranking based on predefined tie-breaking rules
    eligible.sort(
        key=lambda s: (
            -s["aggregate"],
            -sum(s["subjects"]),
            -s["attendance"],
            s["income"],
            s["id"]
        )
    )

    return eligible, rejected


# Main program
students = []

n = int(input("Enter number of applicants: "))

for i in range(n):

    print("\nEnter details of Student", i + 1)

    student_id = int(input("Application ID: "))
    name = input("Student Name: ")

    aggregate = float(input("Aggregate Marks (%): "))

    print("Enter marks of 3 subjects:")
    subjects = []

    for j in range(3):
        marks = float(input("Subject " + str(j + 1) + ": "))
        subjects.append(marks)

    attendance = float(input("Attendance (%): "))
    income = float(input("Annual Family Income: "))

    student = {
        "id": student_id,
        "name": name,
        "aggregate": aggregate,
        "subjects": subjects,
        "attendance": attendance,
        "income": income
    }

    students.append(student)


# Process scholarship applications
eligible, rejected = rank_students(students)


# Display eligible students
print("\n========== SCHOLARSHIP ELIGIBLE STUDENTS ==========")

if len(eligible) == 0:
    print("No eligible students found.")

else:
    for rank, student in enumerate(eligible, start=1):

        print("\nRank:", rank)
        print("Application ID:", student["id"])
        print("Name:", student["name"])
        print("Aggregate:", student["aggregate"], "%")
        print("Subject Marks:", student["subjects"])
        print("Attendance:", student["attendance"], "%")
        print("Annual Income: Rs.", student["income"])


# Display rejected students
print("\n========== INELIGIBLE STUDENTS ==========")

if len(rejected) == 0:
    print("All applicants are eligible.")

else:
    for student in rejected:

        print("\nName:", student["name"])
        print("Application ID:", student["id"])
        print("Reasons for rejection:")

        for reason in student["reasons"]:
            print("-", reason)


print("\n========== PROCESS COMPLETED ==========")
