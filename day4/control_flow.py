#Basic If-Else (Age Check)
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


#Comparison Operators
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is larger")
elif num2 > num1:
    print("Second number is larger")
else:
    print("Both numbers are equal")


#Elif Ladder (Grading System)
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


#Nested If (Login System)
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")


#Logical Operators
number = int(input("Enter a number: "))

if number > 0 and number % 2 == 0:
    print("Number is positive and even")
else:
    print("Condition not satisfied")


#Input Validation
user_input = input("Enter a number: ")

if user_input.isdigit():
    num = int(user_input)
    if num >= 0:
        print("Positive number")
    else:
        print("Negative number")
else:
    print("Invalid input, not a number")