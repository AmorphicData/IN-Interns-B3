marks=input("input your marks:")
marks=int(marks)
if marks>90:
      print("S")
elif marks>80:
      print("A")
elif marks>70:
        print("B")
elif marks>50:
        print("B")
elif marks<50:
        print("B")

char=input("enter a character:")
vowels = "aeiouAEIOU"
if char.isalpha():
    if char in vowels:
            print(f"{char} is a vowel.")
    else:
            print(f"{char} is a consonant.")
else:
    print(f"{char} is a special character.")


a=int(input("input numbers from 1-9 which will represent months in a year:"))
if(a<=3 & a>=1):
    print('Spring')
elif(a>3 & a<=6):
    print('Summer')
elif(a>7 & a<=9):
    print('Autumn')
else:
    print('Winter')


#Leap Year Check
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



#zero division error
a=int(input("Enter Number 1"))
b=int(input("Enter Number 2"))
try:
    ans=a/b
    print(ans)
except ZeroDivisionError:
    print("Divison by Zero erro")

#invalid input error
num=int(input("Enter a Number"))
try:
    if num>0:
        print("Valid Number")
except ValueError:
    raise("Negative Number")

#Index out of Range
list=input("Enter Number in List").split(' ')
try:
    num=list[4]
    print("Index is Prsent with value:",num)
except IndexError:
    print("Out Of range")

#int input error
try:
   num=int(input("Enter a Integer input"))
   print("Yes Input is Integer: ",num)
except ValueError:
    print("Wrong Type Input")

#Multiple Error
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
try:
     result = a / b
     value = int(input("Enter an integer: "))
     print("Result:", result + value)
except (ZeroDivisionError, ValueError) as e:
     print("Error:", e)




# a=[1,2,3]
# print(id(a))
# b=a
# b.append(4)
# print(a)
# print(type(a))
# print(id(b))
# print(b)
# print("shallow copy")
# import copy
# c=copy.copy(a)
# print(c)
# print(id(c))
# print("deep copy")
# d=copy.deepcopy(a)
# print(d)
# print(id(d))
     



     #Functions
def max_number(a,b,c):
    """this is an function used max of three numbers"""
    max_num=a
    if b>max_num:
        max_num=b
    if c>max_num:
        max_num=c
    
    return max_num


def factorial(n):
    """this is Recursive function used to find a factorial Number"""
    if n==0 or n==1:
        return n
    return n*factorial(n-1)


def string_concat(*args):
    """used to concat the String"""
    return "".join(args)

def count_args(*args):
    """Count the number of arguments passed"""
    return len(args)

def format_name(**kwargs):
    """Formating a name via keyword arguments"""
    return f"{kwargs.get('first_name', '')} {kwargs.get('last_name', '')}"

def create_dict(**kwargs):
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


print("Number of Arguments:", count_args(13, 42, 13, 32144, 12))
print("Formatted Name:", format_name(first_name="John", last_name="Tavish"))
print("Created Dictionary:", create_dict(name="Agam", age=22))
print("Created Tuple:", create_tuple(12, 43, 58))
print("Concatenated Strings (Variable Length):", var_concat("Python", " ", "Programming", " ", "will", " ", "be"," ","done."))
print(greet_person("Ghost"))
print(greet_person("Bob", greeting="How are you"))
print("Concatition of Number :",string_concat("hello"," ","aggy"))
print("Factorial of Number :",factorial(5))
print("Max Number :",max_number(3,4,5))

