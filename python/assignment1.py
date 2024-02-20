#!/usr/bin/env python3

# FOR LIST
my_list = [10, 20, 30]
my_list.append(40)
del my_list[2]

int_list = [1, 2, 3, 4, 5]
int_list.append(6)
del int_list[0]
length = len(int_list)
print(int_list[2:5])
print(3 in int_list)


# FOR STRING
a = input()
b = input()
print(a + b)
print(len(a))
print(a[:3])
print(a[-3:])
print(a[::-1])

c = input()
print(b.count(c))

d = input()
e = input()
if d in e:
    print('substring found')
else:
    print('substring not found')

print(d.capitalize())

s1 = input()
s2 = input()
s3 = input()
print(s1.replace(s2, s3))

sentence = input()
words = sentence.split()

for word in words:
    print(word)

print(sentence.strip())


# FOR JOINS

strings = input().split()
print(' '.join(strings))

separator = input()
print(separator.join(strings))

print('-'.join(strings))
print(','.join(strings))
print('_'.join(strings))
print(' '.join(strings))


# FOR DICTIONARY

d1 = {'Ram': 90, 'Arjun': 85, 'Gopal': 92}

del d1['Arjun']

d1['David'] = 88

check_student = 'Ram' in d1

print(list(d1.items()))

d2 = {'apple': 10, 'banana': 20, 'orange': 30}

d2['grape'] = 15

del d2['banana']

print('orange' in d2)

print(list(d2.keys()))

print(list(d2.values()))

# Creating and Accessing Dictionary

d = {'name': 'John', 'age': 25, 'city': 'New York'}

age = d['age']

d['gender'] = 'Male'

d['age'] = 26

del d['city']

gender = d.pop('gender')

print('city' in d)

# Iterating Over Dictionary

for key, value in d.items():
    print(f"{key}: {value}")

# Clearing Dictionary
d.clear()

print(d)

# Nested Dictionaries

persons = {
    'p1': {'name': 'Alice', 'age': 18, 'city': 'London'},
    'p2': {'name': 'Bob', 'age': 21, 'city': 'Paris'},
    'p3': {'name': 'Charlie', 'age': 23, 'city': 'New York'}
}

person_name = persons['p2']['name']
print(person_name)


# FOR TUPLE
t1 = ("apple", "banana", "cherry", "date")

print(t1[2])
print(t1.index("banana"))
print(t1.count("apple"))
t2 = ("elderberry", "fig")
print(t1 + t2)
print(t1[1:4])
print("grape" in t1)


# FOR SET
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

un = s1.union(s2)
inter = s1.intersection(s2)
diff = s1.difference(s2)

print({1, 2, 3}.issubset(s1))

s1.add(9)
s2.remove(2)

print(len(s1))


#FOR FROZENSET
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({3, 4, 5})

un_fs = fs1.union(fs2)
inter_fs = fs1.intersection(fs2)
diff_fs = fs1.difference(fs2)

sub_fs = fs1.issubset(fs2)