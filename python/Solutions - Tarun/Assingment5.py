#Given a list of strings representing numbers, filter out the odd numbers and then square each of the remaining even numbers.

nums = [1,2,3,4,5,6,7,8,9,10]
fil_res = filter(lambda x: int(x)%2 == 0, nums)
ans1 = list(map(lambda x: x** 2, fil_res))

print(ans1)

#To compute the factorial of a given number.

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * list(map(fact, range(1, n)))[-1]

num = 5
ans2 = fact(num)

print(ans2)

# Given two lists of equal length, one containing student names and the other containing their respective grades, create 
# a dictionary where the keys are student names and the values are their corresponding grades.

nam = ["Ram", "Shyam", "Rahul","Vipin"]
grad = [91, 85, 34,56]
ans3 = dict(zip(nam, grad))

print(ans3)

# Given two lists of numbers of equal length, filter out the elements from the first list that are greater than the 
# corresponding elements in the second list.

l1 = [42, 56, 24, 48]
l2 = [20, 34, 94, 68]
cl_l = list(map(lambda x: x[0] if x[0] <= x[1] else None, zip(l1,l2)))
ans4 = list(filter(lambda x : x is not None, cl_l))
print(ans4)

# Given a list of integers, map each integer to its square, filter out the negative squares, and then find the sum of the remaining squares.

l3 = [6,3,-6,9,7,78,-23,53,27]

fil_val = list(filter(lambda x:x > 0, map(lambda x : x**2 , l3)))
ans5 = sum(fil_val)
print(ans5)

# Given three lists representing the lengths of the sides of triangles, to filter out the triangles 
# that are not valid (i.e., the sum of any two sides is less than or equal to the third side).

s1 = [4,7,18]
s2 = [3,12,17]
s3 = [5,13,91]

ans6 = list(filter(lambda x: x[0] + x[1] > x[2] and x[1] + x[2] > x[0] and x[0] + x[2] > x[1], zip(s1, s2, s3)))
print(ans6)

# Given a list of strings, filter out the strings that contain only vowels and then concatenate the remaining strings into a single string.

str_lt= ["apple", "iou", "elephant", "orange", "ae"]

# Filter out strings that contain only vowels and concatenate the remaining strings
from functools import reduce
fil_str = list(filter(lambda x: not set(x).issubset({'a', 'e', 'i', 'o', 'u'}), str_lt))
ans7 = reduce(lambda x,y: x+y, fil_str, "")
print(ans7)

print("=================================================")

# Write a program that reads a large file line by line and yields each line as it's read. This allows 
# you to process large files without loading the entire contents into memory.

#Iterator
def file_iterator(path):
    with open(path, 'r') as f:
        for line in f:
            yield line.strip()

f_iter = iter(file_iterator('sample.txt'))

for line in f_iter:
    print(line)

#Generator
def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

f = read_file('sample.txt')
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f)) # Stop Iteration post this point

print("=============================")

# Write program to implement lazy evaluation for complex computations.E.g. Fibonacci, 
# prime numbers, or sequences, finding even numbers/ squares, etc.. Instead of eagerly computing 
# all results upfront, generate values on-the-fly.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def primes():
    prime = []
    cnt = 2
    while True:
        is_prime = all(cnt % p != 0 for p in prime)
        if is_prime:
            yield cnt
            prime.append(cnt)
        cnt += 1

fib_gen = fibonacci()
print("Fibonacci:")
for _ in range(10):
    print(next(fib_gen))

prime_gen = primes()
print("Primes:")
for _ in range(10):
    print(next(prime_gen))

print("=============================")
# Write program to filter and transform data streams on-the-fly. For example, you can filter out 
# invalid or irrelevant data points, or transform raw data into a more usable format as it's being read.
    
#Generator
def filt_transform():
    ft_list = [_ for _ in range(1,10)]
    i=0
    while True:
        ele =  (ft_list[i] if ft_list[i]%2 == 0 else None)
        yield ele
        i+=1

ft = filt_transform()
print("Filtering data by even values(Generator):")
print(next(ft))
print(next(ft))
print(next(ft))
print(next(ft))

print("=============================")
#Iterator
print("Filtering data by even values(Iterator):")
tr_list = [ i for i in range(1,10)]
ft = filter(lambda x:x %2 ==0,tr_list)
iter_ft = iter(ft)
print(next(iter_ft))
print(next(iter_ft))
print(next(iter_ft))
print(next(iter_ft))

print("=================================================")

#Custom random function using LCG{ x(n+1) = (a*x(n) +c) mod m}

class CustomRandomGenerator:
    def __init__(self, seed=0):
        self.state = seed

    def _generate_next(self):
        # Linear congruential generator parameters
        a = 1664525
        c = 1013904223
        m = 2**32
        self.state = (a * self.state + c) % m   # Update the state using the linear congruential formula

    def custom_random(self, start, end):
        self._generate_next()
        random_number = start + (self.state % (end - start + 1))
        return random_number

random_gen = CustomRandomGenerator(seed=45)
random_number = random_gen.custom_random(1, 100)
print(f"The custom random number is: {random_number}")