#If-else statements

# to check +ve/-ve even/odd or zero

number=int(input("Enter the number : "))
if number > 0:
    if number % 2 == 0:
        print(f"{number} is Positive & Even")
    else:
        print(f"{number} is Positive & Odd")
elif number < 0:
    if number % 2 == 0:
        print(f"{number} is Negative & Even")
    else:
        print(f"{number} is Negative & Odd")
else:
        print("The number is Zero")


# grade claasification based on percent

percentage = float(input("Enter the percentage: "))
if percentage > 90:
    grade = "S"
elif percentage > 80:
    grade = "A"
elif percentage > 70:
    grade = "B"
elif percentage > 50:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

#check leapyear and also month has 28|29 ,30 or 31 days 

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
date= int(input("Enter the date: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

if month in [1, 3, 5, 7, 8, 10, 12]:
    days_in_month = 31
elif month in [4, 6, 9, 11]:
    days_in_month = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month = 29
    else:
        days_in_month = 28
else:
    print("Invalid month input.")

if 1 <= date <= days_in_month:
    print(f"{year}-{month}-{date} is a valid date.")
else:
    print(f"{year}-{month}-{date} is an invalid date.")


#check char is vowel or consonant or special char
    
ch = input("Enter a character: ")
if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print(f"{ch} is a vowel.")
elif ch.isalpha():
    print(f"{ch} is a consonant.")
else:
    print(f"{ch} is a special character.")


#determine season based on month
    
month = input("Enter the month (1-12): ")
month = int(month)
if 1 <= month <= 3:
    season = "Spring"
elif 4 <= month <= 6:
    season = "Summer"
elif 7 <= month <= 9:
    season = "Autumn"
elif 10 <= month <= 12:
    season = "Winter"
else:
    season = "Invalid month"
print(f"The season is {season}.")


#Errors and Exceptions

#divison by zero

n= float(input("Enter the numerator: "))
d = float(input("Enter the denominator: "))
try:
    result = n/ d
    print(f"The result of the division is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


#invalid input error

input_text = input("Enter value: ")
try:
    user_input = int(input_text)
    print("You entered a valid integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

#index out of range

a_list = [1, 2, 3, 4, 5]
index = 5
try:
    element = a_list[index]
    print(f"The element at index {index} is {element}.")
except IndexError:
    print(f"Invalid index.")

#valueerror 

input_text = input("Enter value: ")
try:
    user_input = int(input_text)
    print("You entered a valid integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

#multiple potential errors
    
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(result)
except ValueError:
    print("Error: Please enter valid integers for numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Exception solved")


#Functions 
    
#to find max of 3 numbers
    
def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
maximum = find_maximum(num1, num2, num3)
print(f"The maximum  number is: {maximum}")

#cal factorial of num

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")

#Function with arguments

#concat string 

def concatenate_strings(*args):
    result = ""
    for string in args:
        result += string
    return result

string1 = "Hello, "
string2 = "world!"
concatenated_result = concatenate_strings(string1, string2)
print(concatenated_result)

#count no of arg passed

def count_arguments(*args):
    return len(args)
num_args = count_arguments(1, 'two', 3.0, [4, 5], {'hani': '2'})
print(f"Number of arguments passed: {num_args}")


#format using keyword arg

def format_name(**kwargs):
    first_name = kwargs.get('first_name', '')
    last_name = kwargs.get('last_name', '')
    return f"{first_name} {last_name}"

formatted_name = format_name(first_name='John', last_name='Smith')
print(f"Formatted Name: {formatted_name}")


#dict using keyword arg

def create_dictionary(**kwargs):
     return kwargs
person_info = create_dictionary(first_name='Hani', last_name='Kittu', age=30, city='Banglore')

print("Person Information:")
for key, value in person_info.items():
    print(f"{key}: {value}")

#tuple using variable arg
    
def create_tuple(*args):
    return tuple(args)
created_tuple = create_tuple('apple', 'banana', 'orange', 1, 2, 3)
print("Created Tuple:", created_tuple)

#concat strings using variable len arg

def concatenate_strings(*args):
    result = ""
    for string in args:
        result += string
    return result

concatenated_result = concatenate_strings('Hello, ', 'world!', ' This is', ' a', ' variable', ' argument', ' example.')
print("Concatenated Result:", concatenated_result)


#illustarte default arg

def add_numbers(a, b=10):
    result = a + b
    return result
print(add_numbers(5,15))
print(add_numbers(6))

