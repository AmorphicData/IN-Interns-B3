
#Question 1.1
'''
from functools import reduce

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Filter out the odd numbers
even_numbers = list(filter(lambda x: int(x) % 2 == 0, numbers))

# Square each of the remaining even numbers
squared_even_numbers = list(map(lambda x: int(x) ** 2, even_numbers))

print("Filtered even numbers:", even_numbers)
print("Squared even numbers:", squared_even_numbers)

'''
'''
#Question 1.2
from functools import reduce

def factorial(n):
    # Compute factorial using reduce
    return reduce(lambda x, y: x * y, range(1, n + 1))

num = int(input("Enter a non-negative integer to compute its factorial: "))
if(num<0):
    print("Entered a negative number")
else:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")


#Question 1.3
def create_grade_dict(names, grades):
    if len(names) != len(grades):
        print ("Lists must have equal lengths.")

    grade_dict = dict(zip(names, grades))
    return grade_dict

names = ["Nayan", "Ram", "Suresh", "Ramesh"]
grades = [90, 85, 95, 88]
grade_dict = create_grade_dict(names, grades)

print(grade_dict)

'''
'''
#Question 1.4 Given two lists of numbers of equal length, filter out the elements from the first list that are greater than the corresponding elements in the second list.

def filter_numbers(list1, list2):
    if len(list1) != len(list2):
        print("Lists must have equal lengths.")

    else:
        # Use filter with a lambda function to filter elements
        filtered_result = filter(lambda x: x[0] <= x[1], zip(list1, list2))
        # Convert the filter object to a list and extract elements from the tuples
        return list(filtered_result)

list1 = [5, 10, 15, 20]
list2 = [7, 9, 10, 25]

filtered_numbers = filter_numbers(list1, list2)

print("Filtered numbers:", filtered_numbers)

'''

'''
#Question 1.5
def sum_of_squares(numbers):
    # Map each integer to its square
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(squared_numbers)
    
    # Filter out the negative squares
    positive_squares = tuple(filter(lambda x: x >= 0, squared_numbers))
    print(positive_squares)
    
    # Find the sum of the remaining squares
    sum_positive_squares = sum(positive_squares)
    
    return sum_positive_squares

numbers = [-2, -1, 0, 1, 2, 3]
result = sum_of_squares(numbers)

print("Sum of positive squares:", result)


'''
'''
def check(sides):
    if sides[0] + sides[2] > sides[1] and sides[1]+sides[2]>sides[0] and sides[0] + sides[1]>sides[2]:
        return sides
side1 = [3,5,7]
side2 = [4,3,2]
side3=[6,8,7]
sides = list(zip(side1,side2,side3))
print(sides)
res = list(filter(check,sides))
print("Valid triangles:", res)

'''

#Question 1.6
'''
from functools import reduce
vowels=['a','e','i','o','u']
str_list=input("Enter The List of String").split()
def isVowl(str):
    for ch in str:
        if ch not in vowels:
            return 0
    return 1
def fun(str):
    if(isVowl(str)):
        return 0
    return 1
res=list(filter(fun,str_list))
ans=reduce(lambda x,y:x+y,res)
print(ans)
'''


#Question 2.1

'''
def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.rstrip('\n')

filename = 'sample.txt'  
abc = read_large_file(filename)
# print(next(abc))
# print(next(abc))
for line in abc:
    print(line)
    
'''


#Question 2.2


def fibonacci():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr

fibonacci_generator = fibonacci
# for i in range(5):
#     print(next(fibonacci_generator))



'''
def even_numbers():
    num = 0
    while True:
        if num % 2 == 0:
            yield num
        num += 1

even_generator = even_numbers()
for i in range(5):
    print(next(even_generator))

#Question 2.3
'''
'''
def even(x):
    x = x% 2==0
    yield x
    
numbers = [1,2,3,4,5,6,7,8,9,10]
ans = filter(even, numbers)
print(next(ans))
print(next(ans))
'''


