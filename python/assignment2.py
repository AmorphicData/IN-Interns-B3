import copy
#Question 1

# print("Enter the number: ")
# num1 = int(input())
# if num1<0:
#     if num1%2==0:
#         print("Negative and Even")
#     else:
#         print("Negative and odd")
# else:
#     if num1%2==0:
#         print("Positive and even")
#     else:
#         print("Positive and odd")
'''
print("Enter the number: ")
num1 = int(input())
print("Enter the marks: ")
marks = int(input())
if marks>90:
    print("S")
elif marks>80:
    print("A")
elif marks>70:
    print("B")
elif marks>50:
    print("C")
else:
    print("F")

'''    

'''
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "leap year"
    else:
        return "Not a leap year"
def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        if is_leap_year(year)=='leap year':
            return 29
        else:
            return 28

'''

'''  
def main():
    #x = int(input())
    #y = is_leap_year(x)
    #print(y)
    m = int(input())
    y = int(input())
    print(days_in_month(m,y))
    
main()
 
cha= input()
if cha.isalpha():
    ch=cha.lower()
    if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Special Character")

month = input()
if(month=="Jan" or month=="Feb" or month=="Mar"):
    print("Spring")
elif(month=="Apr" or month=="May" or month=="June"):
    print("Summer")
elif(month=="July" or month=="August" or month=="Sept"):
    print("Autumn")
else:
    print("Winter")
'''
#Question 2
'''
x=int(input("Enter 1 Number: "))
y=int(input("Enter 2 Number: "))
try:
    ans=x/y
    print(ans)
except ZeroDivisionError:
    print("Not Allowed")
    
try:
    x=int(input("Enter 1 Number: "))
    print(x)
except ValueError:
    print("Not Allowed")

l1 = [1,2,3]
try:
    a = l1[5]
    print(a)
except:
    print("Not Allowed")

try:
    x=int(input("Enter 1 Number: "))
    print(x)
except ValueError:
    print("Not Allowed")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
try:
     result = a / b
     val= int(input("Enter an integer: "))
     print("Result:", result + val)
except (ZeroDivisionError, ValueError) as e:
     print("Error:", e)

'''

#Question 4
'''
def max_number(a,b,c):
    if b>a and b>c:
        max_num=b
    elif c>a and c>b:
        max_num=c
    else:
        max_num=a
    print(max_num)
max_number(5,2,3)

#Factorial
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*(num-1)
    
print(fact(5))

#Question 4
def string_concat(*args):
    return "".join(args)

print(string_concat("se", "es","we","qw"))

def count_args(*args):
    return len(args)

print(count_args(1,2,3,4,5))

def format_name(**kwargs):
    return f"{kwargs.get('first_name', '')} {kwargs.get('last_name', '')}"

print(format_name(first_name="John", last_name="Sharma"))

def create_dict(**kwargs):
    """Creates a dict using keyword args"""
    return kwargs
print(create_dict(Nayan=1, Ram=2, Shyaam=3))



def create_tuple(*kwargs):
    """Creates a tuple"""
    return tuple(kwargs)

print(create_tuple(1,2,3,4))



def varconcat(*ar):
    return "".join(ar)
print(varconcat("Hello","Bye"))


'''

def default_arg(name, age="21"):
    return f"{name} I am {age} years old "
print(default_arg("Nayan"))