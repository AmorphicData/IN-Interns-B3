#!/usr/bin/env python3

# Check if a number is positive/negative even/odd or zero
def check_num(number):
    if number > 0:
        if number % 2 == 0:
            return "Positive & Even"
        else:
            return "Positive & Odd"
    elif number < 0:
        if number % 2 == 0:
            return "Negative & Even"
        else:
            return "Negative & Odd"
    else:
        return "Zero"
    
num_result = check_num(7)
print(num_result)


# Grade classification based on percentage
def grade(percentage):
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
    
grade_result = grade(85)
print(grade_result)


# Check if a year is a leap year and if the month has 28/29, 30 or 31 days and the given day is valid
def check_date(year, month, day):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_year = True
    else:
        leap_year = False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    else:
        days = 29 if leap_year else 28

    if 1 <= day <= days:
        return "Valid Date"
    else:
        return "Invalid Date"
    
date_result = check_date(2024, 2, 29)
print(date_result)


# Check if a character is a vowel, consonant, or special character
def check_character(char):
    vowels = "aeiouAEIOU"
    if char.isalpha():
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Special Character"
    
char_result = check_character('A')
print(char_result)


# Determine the season based on the month
def determine_season(month_no):
    if 1 <= month_no <= 3:
        return "Spring"
    elif 4 <= month_no <= 6:
        return "Summer"
    elif 7 <= month_no <= 9:
        return "Autumn"
    elif 10 <= month_no <= 12:
        return "Winter"
    else:
        return "Invalid Month"
    
season_result = determine_season(6)
print(season_result) 

# Errors and Exceptions

# Handling division by zero error
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero not possible"

divide_result = divide(10, 0)
print(divide_result)


# Handling invalid input error
def get_integer():
    try:
        user_input = int(input())
        return user_input
    except ValueError as e:
        return f"Enter an integer"
    
integer_result = get_integer()
print(integer_result) 


# Handling index out of range error
def list_element(my_list, i):
    try:
        result = my_list[i]
        return result
    except IndexError:
        return "Error: Index out of range"
    
list_result = list_element([1, 2, 3], 5)
print(list_result)


# Handling a ValueError when converting user inputs to an integer
def convert_to_int(input_str):
    try:
        result = int(input_str)
        return result
    except ValueError:
        return "Error: Invalid input, not an integer"
    
convert_result = convert_to_int("abc")
print(convert_result) 


# Handling multiple potential errors
def complex_oper(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid data types"
    
complex_result = complex_oper(10, "5")
print(complex_result)


# Functions

# Find the maximum of three numbers
def find_maximum(a, b, c):
    return max(a, b, c)

max_result = find_maximum(8, 12, 5)
print(max_result) 


# Calculate the factorial of a number
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

factorial_result = calculate_factorial(4)
print(factorial_result) 

# Functions with arguments

# Concatenate strings with dynamic arguments
def concatenate_strings(*args):
    return ''.join(args)

concat_result = concatenate_strings("Hello", " ", "World")
print(concat_result)


# Count the number of arguments passed
def count_arg(*args):
    return len(args)

count_result = count_arg(1, 2, 3, 4)
print(count_result) 


# Format a person's name using keyword arguments
def format_name(**kwargs):
    first_name = kwargs.get('first_name', '')
    last_name = kwargs.get('last_name', '')
    return f"{first_name} {last_name}"

result = format_name(first_name="John", last_name="Smith")
print(result)


# Create a dictionary using keyword arguments
def create_dict(**kwargs):
    return kwargs

dict_result = create_dict(name="Alice", age=25, city="New York")
print(dict_result)


# Create a tuple using variable arguments
def create_tuple(*args):
    return tuple(args)

tuple_result = create_tuple(1, 2, 3)
print(tuple_result) 

# Concatenate strings with variable length arguments
def concatenate_var(*args):
    return ''.join(args)

concat_var_result = concatenate_var("I", " ", "am", " ", "Ananya")
print(concat_var_result)

# Illustrate default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet_result = greet("Alice")
print(greet_result)  

