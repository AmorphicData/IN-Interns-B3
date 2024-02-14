# Check if a number is positive/negative, even/odd, or zero

num = int(input("Enter a number:"))
if num > 0:
    print("Positive", end=" & ")
elif num < 0:
    print("Negative", end=" & ")
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
if num == 0:
        print("Zero")

print("============================================")
# Grade if-else
gr = int(input("Enter score:"))

if gr >= 90:
    print('S')
elif gr >= 80:
    print('A')
elif gr >= 70:
    print('B')
elif gr >= 50:
    print('C')
else:
    print('F')
    
print("============================================")

# Leap year check
year = int(input("Enter year :"))
month = int(input("Enter month :"))
day = int(input("Enter day :"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
if month in [1, 3, 5, 7, 8, 10, 12]:
    dom = 31
elif month == 2:
    dom = 29 if (year % 100 != 0 and year % 4 == 0 ) or (year % 400 == 0) else 28
else:
    dom = 30
if 1 <= day <= dom:
    print("Valid day")
else:
    print("Invalid!")

print("============================================")

# Check if a char is vowel, consonant, or special char

ch = input("Enter a character:")
if ch.isalpha():
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
        print("Special Character")

print("============================================")

# Seasons
mn = int(input("Enter month(integer):"))
if 1 <= mn <= 3:
    print("Spring")
elif 4 <= mn <= 6:
    print("Summer")
elif 7 <= mn <= 9:
    print("Autumn")
elif 10 <= mn <= 12:
    print("Winter")
else:
    print("Invalid month")

print("============================================")

#ERROR HANDLING
# Zero div
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
try:
    result = a / b
    print("Division result:", result)
except ZeroDivisionError:
    print("Error: Division by zero")

# Invalid input
try:
    number = int(input("Enter a positive integer: "))
    if number < 0:
        raise ValueError("Input should be a positive integer")
except ValueError as e:
    print("Error:", e)

# Index out of range
li = input("Enter list elements:").split(" ")
ind = int(input("Enter index:"))
try:
    value = li[ind]
    print("Value at index", ind, ":", value)
except IndexError:
    print("Error: Index out of range")

# Value error
try:
    number = int(input("Enter an integer: "))
    print("Integer:", number)
except ValueError:
    print("Error: Invalid input. Please enter an integer")

# Multiple errors
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
try:
    result = a / b
    value = int(input("Enter an integer: "))
    print("Result:", result + value)
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)

print("============================================")

def maxthree(a, b, c):
    """Maximum of three numbers"""
    return max(a, b, c)

def factorial(n):
    """Recursivly finding the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def strconcat(*args):
    """Takes multiple inputs and concatenates them"""
    return "".join(args)

def cntargs(*args):
    """Count the number of arguments passed"""
    return len(args)

def fnaming(**kwargs):
    """Formating a name via keyword arguments"""
    return f"{kwargs.get('first_name', '')} {kwargs.get('last_name', '')}"

def crea_dict(**kwargs):
    """Creates a dict using keyword args"""
    return kwargs

def create_tuple(*args):
    """Creates a tuple"""
    return tuple(args)

def var_concat(*ar):
    """Function to concatenate strings with multiple args"""
    return "".join(ar)

def greet_person(name, greeting="Hello"):
    """Illustrates the usage of  default arguments"""
    return f"{greeting}, {name}!"


print("Maximum:", maxthree(34, 7, 55))
print("Factorial of 7:", factorial(7))
print("Concatenated Strings:", strconcat("Hello", " ", "World"))
print("Number of Arguments:", cntargs(13, 42, 13, 32144, 12))
print("Formatted Name:", fnaming(first_name="John", last_name="McTavish"))
print("Created Dictionary:", crea_dict(name="Alan", age=25))
print("Created Tuple:", create_tuple(11, 43, 38))
print("Concatenated Strings (Variable Length):", var_concat("Python", " ", "Programming", " ", "shall", " ", "be"," ","done."))
print(greet_person("Ghost"))
print(greet_person("Bob", greeting="How are you"))
