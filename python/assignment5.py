#High Level functions

#Q1 Filter out the odd numbers and then square each of the remaining even numbers

numbers = [1,2,3,4,5,6,7,8,9,10]

# Filter out odd numbers and square even numbers
def is_even(n):
    return n % 2 == 0

def square(n):
    return n ** 2

filter_square = list(map(square, filter(is_even, numbers)))
print("Filtered and Squared Numbers:", filter_square)


#Q2 Find Factorial of a given number

from functools import reduce

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))

number = 5
print("Factorial of", number, "is:", factorial(number))


#Q3 Create a dictionary of student names and grades

names = ["Kaustubh", "Yash", "Raj"]
grades = [98, 90, 95]
student_grades = dict(zip(names, grades))
print("Result:", student_grades)


#Q4 Filter out the elements from the first list that are greater than the 
#   corresponding elements in the second list.

l1 = [5, 3, 7, 9, 2]
l2 = [4, 6, 3, 8, 5]

z1=list(zip(l1,l2))
def fn(n):
    if n[0]>n[1]:
        return 1
    
def fn1(n):
    if n[0] > n[1]:
        return n[0]
    
ans=list(filter(fn,z1))
result=list(map(fn1,ans))
print("Result: ",result)

#Q5 map each integer to its square, filter out the negative squares, 
#   and then find the sum of the remaining squares.

l1 = [5, 3, 7, 9, 2]

def square(n):
    return n ** 2

squared_no=list(map(square,l1))
print("Squared No: ",squared_no)
sum_squared=sum(squared_no)
print("Sum: ", sum_squared)


#Q6 Triangle

a = [3, 4, 5, 2]
b = [4, 3, 8, 2]
c = [5, 6, 2, 10]

def is_valid_triangle(sides):
    if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:  
        return (sides)
    
sides=list(zip(a,b,c))
result=(list(filter(is_valid_triangle, sides)))
print("Result: ",result)
    

#Q7 filter out the strings that contain only vowels and then concatenate 
# the remaining strings into a single string.

from functools import reduce
vowels=['a','e','i','o','u','A','E','I','O','U']
l=input("Enter The List of String: ").split()
def isVowl(str):
    for ch in str:
        if ch not in vowels:
            return 0
    return 1
def fun(str):
    if(isVowl(str)):
        return 0
    return 1
iterable_list=list(filter(fun,l))
ans=reduce(lambda x,y:x+y,iterable_list)
print(ans)


#Iterators and Generators

#Q1 Write a program that reads a large file line by line and yields each line 
# as it's read. This allows you to process large files without loading the entire contents into memory.

def read_large_file(sample):
    with open(sample, 'r') as file:
        for line in file:
            yield line.strip('\n')

gen=read_large_file("sample.txt")
print(next(gen))
print(next(gen))

#Q2 Write program to implement lazy evaluation for complex computations.
# E.g. Fibonacci,finding even numbers etc.. 
#Instead of eagerly computing all results upfront, generate values on-the-fly.

# Even Numbers
def even_number(num):
    for i in num:
        if i % 2==0:
            yield i
number=[1,2,3,4,5,6]
even_gen=even_number(number)
print(next(even_gen))
print(next(even_gen))

it=iter(number)
itr2=even_number(number)
print(next(itr2))
print(next(itr2))

#Fibonacci

def fibonacci(n):

    a, b = 1, 2
    for i in range(n):
        yield a
        a, b = b, a + b

n = 5
gen = fibonacci(n)
for i in range(n):
    print(next(gen))  


it=iter(fibonacci(n))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


#Q3 Filter and transform data streams on-the-fly

l=input("Enter Numbers: ").split()
input_list=[int(i) for i in l]

def odd_number(num):
    for i in num:
        if i%2 !=0:
            yield i

odd_gen=odd_number(input_list)
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))

iter1=odd_number(input_list)
it=iter(iter1)
print(next(it))
print(next(it))
print(next(it))


#Add-on Question
#Map Function

def map_func(func,iterable):
    ans=[]
    for item in iterable:
        ans.append(func(item))
    return ans

def square(num):
    return num**2

l=[1,2,3,4]
sq=map_func(square,l)
print(sq)