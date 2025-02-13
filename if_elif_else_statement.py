# John Rey Bulfa
# ITELEC2
# Laboratory #09 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

def main():
    user_input = input("Enter your numeric grade: ")
    grade = int(user_input)
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    print("Your grade is:", letter_grade)
    
if __name__ == "__main__":
    main()