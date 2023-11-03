#author: Ben Fisher
#file name: M02_Lab_GPA

#Description: Program will ask for a student name and gpa. It will then determine if that 
#   student has achieved academic honors. Loop will end when user enters 'ZZZ' for last name.

print("\nProgram will ask for a student's name and GPA.")
print("It will then determine their academic status.\n")
last_name = input("Enter a student's last name to begin or 'ZZZ' to exit: ")

while last_name != "ZZZ" and last_name != "zzz":   
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} made the Dean's list!")
    elif gpa >= 3.25:
        print(f"f{first_name} {last_name} made the Honor Roll!")
    else:
        print(f"{first_name} {last_name} needs to study more.")


    last_name = input("\nEnter another student's last name, or 'ZZZ' to exit: ")

print("\n\nYou chose to exit. Goodbye!")