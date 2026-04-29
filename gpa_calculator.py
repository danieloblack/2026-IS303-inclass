"""
Daniel Black
IS 303

Inputs:
-Student name
-Grade for three classes
-Credits for three classes

Processes:
-Calculate the GPA using the grades and the credit total.

Outputs:
-GPA
-Report card for students

"""

# INPUTS
name = input("Student name: ")
grade1 = int(input("Course 1 grade point: "))
grade2 = int(input("Course 2 grade point: "))
grade3 = int(input("Course 3 grade point: "))
credit1 = int(input("Course 1 credits: "))
credit2 = int(input("Course 2 credits: "))
credit3 = int(input("Course 3 credits: "))

# PROCESSES

total_credits = credit1 + credit2 + credit3
gpa = (grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / total_credits

# OUTPUTS

print(f"{name}'s Report Card:")
print(f"credits taken: {total_credits}")
print(f"course 1: grade {grade1} credits {credit1}")
print(f"course 2: grade {grade2} credits {credit2}")
print(f"course 3: grade {grade3} credits {credit3}")
print(f"GPA: {gpa}")
