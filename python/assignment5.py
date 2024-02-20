#High Level functionss
#1
nums = ['1', '2', '3', '4', '5', '6', '7', '8']

filtered = list(
    map(lambda x: int(x) ** 2, filter(lambda x: int(x) % 2 == 0, nums))
)

print(filtered)

#2
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

result = factorial(5)
print(result)

#3
names = ['Ram', 'Arun', 'Amit', 'Rohan']
grades = [90, 85, 78, 92]

d = dict(zip(names, grades))

print(d)

#4
list1 = [10, 25, 15, 30, 5]
list2 = [12, 20, 18, 25, 10]

list3 = [x for x, y in zip(list1, list2) if x <= y]

print(list3)

#5
nums = [1, -2, 3, -4, 5]

sum_sq = sum(filter(lambda x: x >= 0, map(lambda x: x**2, nums)))

print(sum_sq)

#6
t = [
    (3, 2, 7),
    (3, 5, 1),
    (5, 6, 2)
]

valid = list(filter(lambda x: sum(x) - max(x) > max(x), t))
print(valid)

#7
strings = ['abcd', 'ei', 'hello', 'uai', 'yes']

new = ''.join(filter(lambda x: not set(x).issubset({'a', 'e', 'i', 'o', 'u'}), strings))
print(new)

#Iterators and Generators

#1
def read_file(path):
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()

file_path = '/Users/ananyapaliwal/documents/sample.txt'
for line in read_file(file_path):
    print(line)

#2
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
for _ in range(10): 
    print(next(f))


#3
def ft(data):
    for item in data:
        if item % 2 != 0:
            yield item ** 2

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ft(data)

for value in result:
    print(value)
