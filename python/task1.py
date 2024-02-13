#Question 1
'''list = [1,2,3,4]
print(list)
list.append(5)
print(list)
list.pop(2)
print(list)

list2 = [1,2,3,4,5]
list2.append(6)
print(list2)
list2.pop(0)
print(list2)
len_list2= len(list2)
print(len_list2)
print(list2[2:5])
is_present = 3 in list2
print(is_present)
'''

#Question 2
'''
str1 = input()
str2 = input()
str = str1+str2
print(str)
str3 = input()
length = len(str3)
print(length)

str4 = input()
rev_str = str4[::-1]
print(rev_str)
str = input()
char = input()
total = str.count(char)
print(total)

str = input()
print(str.upper())
print(str.lower())

str = input()
substr = input()
if substr in str:
    print("Substring Found")
else:
    print("Substring Not Found")

str = input()
final = str.replace('a','y')
print(final)

str = input()
result = str.split()
for i in result:
    print(i)
str = input()
result = str.strip()
print(result)
'''

#Question 3
'''
str = input("Enter a list of strings separated by spaces: ").split()
print(str)
joined_string = ' '.join(str)
print("Joined string:", joined_string)

str = input("Enter a list of strings separated by spaces: ").split()
separator = input("Enter the separator: ")
joined_string = separator.join(str)
print("Joined string:", joined_string)

str = input("Enter a list of numbers separated by spaces: ").split()
joined_string = ','.join(str)
print("Joined string:", joined_string)
sentence = input("Enter a sentence: ")

str = sentence.split()
print(str)
joined_string = '_'.join(str)
print("Joined string:", joined_string)

fragments = input("Enter several string fragments separated by spaces: ").split()
joined_string = ' '.join(fragments)
print("Joined string:", joined_string)
'''

#Question 4
'''
dict1 = {'Nayan': 90, 'Agam': 100, 'Saksham': 90, 'Tarun': 75}
del dict1['Saksham']
print (dict1)

dict1['Kaustubh'] = 78
student = 'Nayan'
if student in dict1:
    print(student, "is present in the dictionary.")
else:
    print(student, "is not present in the dictionary.")

print("Keys:", dict1.keys())

print("Values:", dict1.values())

fruit = {'apple': 10, 'banana': 20, 'orange': 30}
fruit['grape'] = 15
del fruit['banana']
if 'orange' in fruit:
    print("orange is present in the dictionary.")
else:
    print("orange is not present in the dictionary.")
print("Keys:", fruit.keys())
print("Values:", fruit.values())
'''
'''
person = {
    "name": "Nayan",
    "age": 21,
    "city": "Gurgaon"
}

print("Age:", person["age"],"\n")
person["college"]="MIT Manipal"
person["gender"]="male"
person["age"] = 22
print(person)

del person["city"]
removed = person.pop("gender")
if "city" in person:
    print("City found")
else:
    print("City not found")
for key, value in person.items():
    print("%s: %s" % (key, value))
person.clear()
print("Dictionary after clearing:", person)

nested = {
    "p1": {"name": "Nayan", "age": 22, "city": "Gurgaon"},
    "p2": {"name": "Amit", "age": 20, "city": "Delhi"},
    "p3": {"name": "Ram", "age": 22, "city": "Manipal"}
}

print(nested["p1"])
'''

#Question 5
'''
tuple1 = ('hello', 'how', 'are', 'you')
tuple2 = ('good', 'better')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)
index = concatenated_tuple.index('good')
print(index)
count_how = concatenated_tuple.count('how')
print(count_how)
subset = concatenated_tuple[2:5]
print(subset)

my_tuple = ("apple", "banana", "cherry", "date")
third_element = my_tuple[2]
print(third_element)
banana_index = my_tuple.index("banana")
print(banana_index)
apple_count = my_tuple.count("apple")
print(apple_count)
concatenated_tuple = my_tuple + ("elderberry", "fig")
print(concatenated_tuple)
'''
#Question 6
'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
is_subset = set1.issubset(set2)
set1.add(6)
set2.remove(7)
set1_length = len(set1)
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set 1 - Set 2):", difference_set)
print("Is Set 1 a subset of Set 2?", is_subset)
print("Length of Set 1:", set1_length)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
is_subset = set1.issubset(set2)
set2.add(9)
set1.remove(2)
is_subset = set1.issubset(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set 1 - Set 2):", difference_set)
print("Is Set 1 a subset of Set 2?", is_subset)
'''
#Question 7    
'''
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
'''
