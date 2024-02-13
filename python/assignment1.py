# Question 1 - List Operations

list1 = [1,2,3,4,5,6,7]
print(list1)
list1.append(8)
print(list1)
list1.pop(2)
print(list1)


list2 = [1,2,3,4,5]
print(list2)
list2.append(6)
print(list2)
list2.pop(0)
print(list2)
print(len(list2))
print(list2[2:4])
present=3 in list2
print(present)

# Question 2 - String Operations

s1=input()
s2=input()
s=s1+s2
print(s)
print(len(s1))
string = input("Enter a string: ")
print("First three characters:", string[:3])
print("Last three characters:", string[-3:])
print("Every second character:", string[::2])
print("Reversed string:", string[::-1])

str=input()
ch=input()
count=str.count(ch)
print(count)
print(str.upper())
print(str.lower())


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string2 in string1:
    print("Substring found")
else:
    print("Substring not found")

string = input("Enter a string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")
new_string = string.replace(old_substring, new_substring)
print("Updated string:", new_string)


sentence = input("Enter a sentence: ")
words = sentence.split()
print(words)
for i in words:
    print(i)

str=input()
print(str.strip(' '))

# Question 3 - Joins

l4 = input("Enter a list of strings separated by spaces: ").split()
print(l4)
joined_string = ' '.join(l4)
print("Joined string:", joined_string)

l5 = input("Enter a list of strings separated by spaces: ").split()
separator = input("Enter the separator: ")
joined_string = separator.join(l5)
print("Joined string:", joined_string)


numbers_list = input("Enter a list of numbers separated by spaces: ").split()
joined_string = ','.join(numbers_list)
print("Joined string:", joined_string)

sentence = input("Enter a sentence: ")
words_list = sentence.split()
print(words_list)
joined_string = '_'.join(words_list)
print("Joined string:", joined_string)

fragments = input("Enter several string fragments separated by spaces: ").split()
joined_string = ' '.join(fragments)
print("Joined string:", joined_string)


# Question 4 - Dictionary operations

student_scores = {'Raj': 85, 'Yash': 99, 'Max': 90, 'David': 65}
del student_scores['Max']
student_scores['Rakesh'] = 78

student_to_check = 'Yash'
if student_to_check in student_scores:
    print(student_to_check, "is present in the dictionary.")
else:
    print(student_to_check, "is not present in the dictionary.")

print("Keys:", student_scores.keys())
print("Values:", student_scores.values())

fruit_dict = {'apple': 10, 'banana': 20, 'orange': 30}
fruit_dict['grape'] = 15

del fruit_dict['banana']

if 'orange' in fruit_dict:
    print("orange is present in the dictionary.")
else:
    print("orange is not present in the dictionary.")

print("Keys:", fruit_dict.keys())
print("Values:", fruit_dict.values())

person = {
    "name": "Yash",
    "age": 21,
    "city": "Bengaluru"
}

print("Age:", person["age"])
person["profession"]="SWE"
person["gender"]="male"
print(person)
del person["city"]
removed_gender = person.pop("gender")

if "city" in person:
    print("City found")
else:
    print("City not found")

for key, value in person.items():
    print("%s: %s" % (key, value))

person.clear()
print("Dictionary after clearing:", person)

info = {
    "p1": {"name": "yash", "age": 21, "city": "delhi"},
    "p2": {"name": "rakesh", "age": 25, "city": "patna"},
    "p3": {"name": "shyam", "age": 19, "city": "gujarat"}
}

# Question 5 - Tuple Operations

t1=('hello', 'cloudwick', 'swe', 'intern','swe')
t2=('ui', 'qa')
concat = t1 + t2
print(concat)
index = concat.index("cloudwick")
print("Index of 'cloudwick':", index)
print(concat.count('swe'))
print("Subset of elements:", concat[2:5])

t3=("apple", "banana", "cherry", "date")
print(t3[2])
print(t3.index('banana'))
print(t3.count('apple'))
t4=("elderberry", "fig")
t5=t3+t4
if "grape" in t5:
    print("'grape' is present in the tuple.")
else:
    print("'grape' is not present in the tuple.")

# Question 6 - Set Operations

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)

subset_check = set1.issubset(set2)
print("Is set1 a subset of set2?", subset_check)

set1.add(9)
set2.remove(2)

print("Length of set1:", len(set1))
print("Length of set2:", len(set2))

subset_check2 = {1, 2, 3}.issubset(set1)
print("Is {1, 2, 3} a subset of set1?", subset_check2)

#Question 7 - Operations on Frozen Sets

frozenset1 = frozenset({1, 2, 3, 4, 5})
frozenset2 = frozenset({4, 5, 6, 7, 8})

union = frozenset1.union(frozenset2)
intersection = frozenset1.intersection(frozenset2)
difference = frozenset1.difference(frozenset2)
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)

subset_check = frozenset1.issubset(frozenset2)
print("Is frozenset1 a subset of frozenset2?", subset_check)

