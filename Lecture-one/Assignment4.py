# If Else Assignment
# - Create a variable grade holding an integer between 0 - 100
#
# - Code if, elif, else statements to print the letter grade of the number grade variable
#
# Grades:
#
# A = 90 - 100
#
# B = 80 - 89
#
# C = 70-79
#
# D = 60 - 69
#
# F = 0 - 59
#
#
#
# Example:
#
# if grade = 87 then print('B')

grade = int(input("enter your Grade"))

if grade <= 59:
    print("f is your grade")
elif grade <= 69:
    print("d is your grade")
elif grade <= 79:
    print("c is your grade")
elif grade <= 89:
    print("b is your grade")
else:
    print ("a is your grade")

print(grade)


# (OR)

grade = 27
if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
else:
    print("F")