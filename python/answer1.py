'''List Operations'''
l1=[1,2,3,4,5]
l1.pop(2)
print(l1)
l1=[1,2,3,4,5]
l1.append(6)
print(l1)
l1.pop(0)
print(l1)
print(len(l1))
print(l1[2:5])
print(3 in l1)

#String Operations
str1=input()
str2=input()
str3=str1+str2
print(str3)
print(len(str3))
print("First three characters:", str3[:3])
print("last three characters:", str3[:-3])
print("every 2nd character:", str3[::2])
reversed_string = str3[::-1]
print(reversed_string)
str4=input()
char=input()
count = str4.count(char)
print(count)
print(str4.upper())
print(str4.lower())
str5 = input("Enter the first string: ")
str6 = input("Enter the second string: ")
if str6 in str5:
    print("Substring found")
else:
    print("Substring not found")
str7=input("enter a string:")
str8=input("enter the substring to replace: ")
str9=input("enter the replacement string: ")
modified_string = str7.replace(str8,str9)
print(modified_string)
print(str7.split(" "))
print(str7.strip())


# Joins
str1 = input("Enter string1: ").split()
newstring = " ".join(str1)
print(newstring)

str2 = input("Enter string1: ").split()
newstring = "-".join(str2)
print(newstring)


str3 =input("list numbers as input:").split()
newstring = ",".join(str3)
print(newstring)

str4 =input("type sentence:").split()
hello = "_".join(str4)
print(hello)

str4 =input("type sentence:").split()
hello = " ".join(str4)
print(hello)


dict= {"Alice": 85, "Bob": 90, "Charlie": 75, "David": 80}
print(dict)
updated_dict=dict.pop("Alice", None)
print(dict)
dict["agam"]=100
print(dict)
if "agam" in dict:
    print("yes")
keys_list = list(dict.keys())
values_list = list(dict.values())

print("Keys in the dictionary:", keys_list)
print("Values in the dictionary:", values_list)


fruits= {"Apple": 10, "Banana": 20, "Orange": 30}
print(fruits)
fruits["grape"]= 15
print(fruits)
fruitss=fruits.pop("Banana", 20)

if "Orange" in fruits:
    print("yes")
keys_list = list(fruits.keys())
values_list = list(fruits.values())

print("Keys in the dictionary:", keys_list)
print("Values in the dictionary:", values_list)

person = {
    "name": "Agam",
    "age": 22,
    "city": "faridabad"
}
print("age:", person["age"], "\n")

person["college"] = "MIT Manipal"
person["gender"] = "male"
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
    "p1": {"name": "Agam", "age": 22, "city": "faridabad"},
    "p2": {"name": "Amit", "age": 20, "city": "Delhi"},
    "p3": {"name": "Ram", "age": 22, "city": "Manipal"}
}
print(nested["p1"])

# TUPLE OPERATIONS

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

fruits = ("apple", "banana", "cherry", "date")
print(fruits)

access = fruits[2]
print(access)

index = fruits.index('banana')
print(index)

count_apple = fruits.count('apple')
print(count_apple)

fruits2 = ("elderberry", "fig")
fruits3 = fruits + fruits2
print(fruits3)

if "grape" in fruits3:
    print("grape is present in the tuple")
else:
    print("grape is not present in the tuple")


set1={1,2,3,4,5}
set2={6,7,8,9,10}
union_set=set1.union(set2)
print(union_set)
intersection_set=set1.intersection(set2)
print(intersection_set)
difference_set=set1.difference(set2)
print(difference_set)
is_subset=set1.issubset(set2)
set1.add(11)
set1.remove(3)
set1_length=len(set1)

set3={1,2,3,4,5}
set4={4,5,6,7,8}
union_set=set3.union(set4)
print(union_set)
intersection_set=set3.intersection(set4)
print(intersection_set)
difference_set=set3.difference(set4)
print(difference_set)
set3.add(9)
set4.remove(4)
is_subset={1,2,3}.issubset(set3)


frozenset1 = frozenset({1, 2, 3, 4, 5})
frozenset2 = frozenset({4, 5, 6, 7, 8})
union = frozenset1.union(frozenset2)
intersection = frozenset1.intersection(frozenset2)
difference = frozenset1.difference(frozenset2)
print("Union:", union)
print("Intersection:",intersection)
print("Difference:", difference)
subset_check = frozenset1.issubset(frozenset2)
print("Is frozenset1 a subset of frozenset2?", subset_check)








