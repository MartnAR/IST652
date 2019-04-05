# Prompt user to enter a grade 
grade = input("Enter Score: ")

try:
    if float(grade) <= 1.0 and float(grade) >= 0.9:
        print("Grade: A")
    elif float(grade) < 0.9 and float(grade) >= 0.8:
        print("Grade: B")
    elif float(grade) < 0.8 and float(grade) >= 0.7:
        print("Grade: C")
    elif float(grade) < 0.7 and float(grade) >= 0.6: 
        print("Grade: D")
    elif float(grade) < 0.6:
        print("Grade: F")
    else:
        print("Bad Score")
except:
    print("Bad Score")