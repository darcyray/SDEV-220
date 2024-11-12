# Darcy Ralstin - Module 2 Lab
# The program will accept students' first and last names & gpa as input. 
# It will then process the input. 
# If the gpa is 3.5 or higher, it will print a 'Dean's List' message. 
# If the gpa is 3.25 or higher, it will print an ' Honor Role' message.

first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
gpa = float(input("Enter your grade point average:"))

while first_name or last_name != "zzz" or "ZZZ":
    if gpa >= 3.5:
        print("You qualify for the Dean's List!")
    elif gpa >= 3.25:
        print("You qualify for the Honor Roll!")

