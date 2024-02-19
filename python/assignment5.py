#High level function 

#Given a list of strings representing numbers, filter out the odd numbers and then square each of the remaining even numbers.

def finding(numbers):

    even =filter(lambda x:int(x)%2==0,numbers)
    sq_even=map(lambda x:int(x)**2,even)
    res=list(sq_even)
    return res

numbers=[1,2,3,4,5,6,7,8,9]
print(finding(numbers))

#To compute the factorial of a given number.

from functools import reduce
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))
print(factorial(5))

#Given two lists of equal length, one containing student names and the other containing their respective grades, create a dictionary where the keys are student names and the values are their corresponding grades.

names=["hani","kittu","sita","rama","thani"]
grades=[80,85,60,75]
print(dict(zip(names,grades)))


#Given two lists of numbers of equal length, filter out the elements from the first list that are greater than the corresponding elements in the second list.

l1=[10,25,15,30]
l2=[12,20,18,25]
filtered_list=[x for x ,y in zip(l1,l2) if x<=y]
print(filtered_list)



#Given a list of integers, map each integer to its square, filter out the negative squares, and then find the sum of the remaining squares.

list=[1,-2,3,-4,5]
square=map(lambda x:x*x,list)
p_square=filter(lambda x:x>0,square)
print(sum(p_square))

#Given three lists representing the lengths of the sides of triangles, to filter out the triangles that are not valid (i.e., the sum of any two sides is less than or equal to the third side).

s1 = [3, 4, 5, 2]
s2 = [4, 5, 7, 6]
s3 = [5, 6, 12, 10]

valid_triangles = [(a, b, c) for a, b, c in zip(s1, s2, s3) if a + b > c and b + c > a and c + a > b]
print(valid_triangles)

#Given a list of strings, filter out the strings that contain only vowels and then concatenate the remaining strings into a single string.


string_list = ["apple", "banana", "grape", "aeiou","orange", "kiwi"]
filtered_strings = filter(lambda x: not all(char.lower() in 'aeiou' for char in x), string_list)
result = "".join(filtered_strings)
print(result)

#Iterators and Generators

#Write a program that reads a large file line by line and yields each line as it's read. This allows you to process large files without loading the entire contents into memory.

#generator 
def read_lines_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip('\n')
for line in read_lines_generator('demo.txt'):
    print(line)


#iterator 
class FileReaderIterator:
    def __init__(self, filename):
        self.filename = filename
        

    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.rstrip('\n') 
file_reader_iterator = FileReaderIterator('demo.txt')
for line in file_reader_iterator:
    print(line)


#Write program to implement lazy evaluation for complex computations.E.g. Fibonacci, prime numbers, or sequences, finding even numbers/ squares, etc.. Instead of eagerly computing all results upfront, generate values on-the-fly.
    
#Even numbers
    
def generate_even_numbers(n):
    current_number = 0
    while current_number < n:
        if current_number % 2 == 0:
            yield current_number
        current_number += 1

even_numbers_generator = generate_even_numbers(10)
for number in even_numbers_generator:
    print(number)

class EvenNumbersIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_number < self.limit:
            if self.current_number % 2 == 0:
                result = self.current_number
                self.current_number += 2  
                return result
            self.current_number += 1

        raise StopIteration

even_numbers_iterator = EvenNumbersIterator(10)
for number in even_numbers_iterator:
    print(number)

#Prime numbers
    
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def generate_primes():
    current_number = 2
    while True:
        if is_prime(current_number):
            yield current_number
        current_number += 1

primes_generator = generate_primes()
for i in range(5):
    print(next(primes_generator))


#Write program to filter and transform data streams on-the-fly. For example, you can filter out invalid or irrelevant data points, or transform raw data into a more usable format as it's being read.
    
def generator(data_stream):
    for data_point in data_stream:
        if data_point >= 0:
            yield data_point ** 2

data_stream = [1, -2, 3, -4, 5]
x = generator(data_stream)

for result in x :
    print(result)


class FilterAndTransformDataIterator:
    def __init__(self, data_stream):
        self.data_stream = data_stream
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data_stream):
            data_point = self.data_stream[self.index]
            self.index += 1
            if data_point >= 0:
                return data_point ** 2
        raise StopIteration

data_stream = [1, -2, 3, -4, 5]
x = FilterAndTransformDataIterator(data_stream)
for result in x:
    print(result)


