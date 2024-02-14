# #Question 1 - If-else statements

def check_number(num):
    if num > 0:
        if num % 2 == 0:
            return "Positive & Even"
        else:
            return "Positive & Odd"
    elif num < 0:
        if num % 2 == 0:
            return "Negative & Even"
        else:
            return "Negative & Odd"
    else:
        return "Zero"
    
def grade_classification(percentage):
    if percentage > 90:
        return "S"
    elif percentage > 80:
        return "A"
    elif percentage > 70:
        return "B"
    elif percentage > 50:
        return "C"
    else:
        return "F"
    
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "leap year"
    else:
        return "Not a leap Year"
def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        if is_leap_year(year)=="leap year":
            return 29
        else:
            return 28

def check_character(char):
    if char.isalpha():
        if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Special Character"
    

def determine_season(month):
    if month in range(1, 4):
        return "Jan-Mar -> Spring"
    elif month in range(4, 7):
        return "Apr-June -> Summer"
    elif month in range(7, 10):
        return "July-Sept -> Autumn"
    else:
        return "Oct-Dec -> Winter"
    
def main():

    num = int(input("Enter a number: "))
    print("Number %d is %s" % (num, check_number(num)))

    percentage = float(input("Enter percentage: "))
    print("Grade: %s" % grade_classification(percentage))

    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))
    print("Year is: %s" % is_leap_year(year))
    print("Days in month: %d" % days_in_month(month, year))

    char = input("Enter a character: ")
    print("Character %s is a %s" % (char, check_character(char)))

    month = int(input("Enter a month (1-12): "))
    print("Season: %s" % determine_season(month))

main()

#Question 2 - Errors and Exceptions

x=int(input("Enter Number 1"))
y=int(input("Enter Number 2"))
try:
    ans=x/y
    print(ans)
except ZeroDivisionError:
    print("Divison by Zero erro")


try:
    num=int(input("Enter a Number: "))
    print("Valid Number")
except ValueError:
    raise("Invalid input")

list=input("Enter Number in List").split(' ')
try:
    num=list[4]
    print("Index is Prsent",num)
except IndexError:
    print("Out Of range")

value = input("Enter an integer: ")
try:
    integer_value = int(value)
    print("Valid input")
except ValueError:
    print("Error: Invalid input! Please enter an integer.")
    
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
try:
     result = a / b
     value = int(input("Enter an integer: "))
     print("Result:", result + value)
except (ZeroDivisionError, ValueError) as e:
     print("Error:", e)

# Question 3 - Functions

def find_max(num1, num2, num3):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return max_num

def calculate_factorial(num):
    factorial = 1
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial *= i
        return factorial

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Maximum of the three numbers is:", find_max(num1, num2, num3))

num = int(input("Enter a number to calculate its factorial: "))
print("Factorial of", num, "is:", calculate_factorial(num))

# Question 4 - Functions with arugments

# Function to concatenate strings with dynamic arguments
def concatenate_strings(*args):
    return ''.join(args)

# Function to count the number of arguments passed
def count_arguments(*args):
    return len(args)

# Function to format a person's name using keyword arguments
def format_name(**kwargs):
    return kwargs.get('first_name', '') + ' ' + kwargs.get('last_name', '')

# Function to create a dictionary using keyword arguments
def create_dictionary(**kwargs):
    return kwargs

# Function to create a tuple using variable arguments
def create_tuple(*args):
    return args

# Function to concatenate strings with variable length arguments
def concatenate_strings_variable_length(*args):
    return ' '.join(args)

# Function to illustrate default arguments
def greet(name='Guest'):
    return f"Hello, {name}!"

print("Concatenating strings with dynamic arguments:", concatenate_strings('Hello', ', ', 'world', '!'))
print("Number of arguments passed:", count_arguments(1, 2, 3, 'a', 'b', 'c'))
print("Formatted name:", format_name(first_name='Kaustubh', last_name='Pandey'))
print("Created dictionary:", create_dictionary(key1='value1', key2='value2', key3='value3'))
print("Created tuple:", create_tuple(1, 2, 'a', 'b', 'c'))
print("Concatenating strings with variable length arguments:", concatenate_strings_variable_length('Welcome', 'to', 'Cloudwick', 'Technologies.'))
print("Default argument example:", greet())
print("Default argument example with custom name:", greet('Yash'))








