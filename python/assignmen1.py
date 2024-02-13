#List 
my_list=[1,2,3,4]
print(my_list)
my_list.append(5)
print(my_list)
my_list.pop(2) #pop is used to remove elements by giving by index
print(my_list)


my_list2=[1,2,3,4,5]
print(my_list2)
my_list2.append(6)
print(my_list2)
my_list2.pop(0)
print(my_list2)
print(len(my_list2))
print(my_list2[2:5])
is_present=3 in my_list2
print(is_present)

#String
str1=input()
str2=input()
str3=str1+str2
print(str3)
print(len(str2))
#for first three Characters
print("First Three Characters",str1[:3])
print("Last Three Characters",str1[-3:])
print("Every Second Character",str1[::2])
print(str1[::-1])

str3=input()
ch=input()
count=str3.count(ch)
print(count)
print(str3.upper())
print(str3.lower())

str4=input()
str5=input()
if str5 in str4:
    print("Substring found")
else:
    print("No SubString Found")


str6=input("Enter a String")
old_substring=input("Enter old substring")
new_substring=input("Enter a new Substring")
new_string=str6.replace(old_substring,new_substring)
print(new_string)

sentence=input("Enter a Sentence")
words=sentence.split()
for word in words:
    print(word)

str=input()
print(str.strip(' '))


#Joins 
l1=input("Enter a List of Strings:").split()
print(l1)
joined_string=' '.join(l1)
print("merged String "+joined_string)

l2=input("Enter a List of Strings:").split()
print(l1)
separtor=input("Enter Separator")
joined_string=separtor.join(l2)
print("merged String "+joined_string)

list=input("Enter Sentence").split()
joined_string=','.join(list)
print("Joined String "+joined_string)

list=input("Enter Sentence").split()
joined_string='-'.join(list)
print("Joined String "+joined_string)

l1=input("Enter a List of Strings:").split()
print(l1)
joined_string=' '.join(l1)
print("merged String "+joined_string)

#Dictionary Operation
student_scores={"Rounak":100,"Kaustubh":99,"Agam":90}
print(student_scores)
del student_scores['Agam']
print(student_scores)
#now i have to add new Student in Dictionary
student_scores['Saksham']=80
print(student_scores)
student_to_check='Nayan'
if student_to_check in student_scores:
    print(student_to_check+" is Present in Dict")
else:
    print(student_to_check+" is not present in Dict")

print("Keys",student_scores.keys())
print("Values",student_scores.values())


fruits={"Apple":10,"Banana":20,"Orange":30}
print(fruits)
fruits['Grapes']=15
print(fruits)
del fruits['Banana']
print(fruits)
if 'Orange' in fruits:
    print("Yes Orange is Present")
else:
    print("No Orange is Not Present")

print("Keys",fruits.keys())
print("Values",fruits.values())

person={
    "name":"Rounak",
    "age":22,
    "city":"Bangalore"
}
#now i have to print the age
print("Age ",person["age"])
person['profession']='SDE'
person['gender']='Male'
print(person)
del person['city']
removed_gender=person.pop('gender')
#in Python for String single double and triple quotes will work 
#so i can put any quotes as per wish
if 'city' in person:
    print("City Found")
else:
    print("Not found")

for key, value in person.items():
    print("%s: %s" % (key, value))

person.clear()
print("Dictionary after clearing:", person)

info = {
    "p1": {"name": "Rounak", "age": 21, "city": "delhi"},
    "p2": {"name": "Saksham", "age": 25, "city": "patna"},
    "p3": {"name": "kaustubh", "age": 19, "city": "gujarat"}
}


#Tuple Operation

t1=('hello','my','name','is','rounak')
t2=('i','work','at','cloudwick')
concat_tuple=t1+t2
print(concat_tuple)
index=concat_tuple.index("cloudwick")
print("Index of that element",index)
print(concat_tuple.count('cloudwick'))
print("Subset of Elements",concat_tuple[2:5])

t3=("apple","banana","cherry","date")
print(t3[2])
print(t3.index('banana'))
print(t3.count('apple'))
t4=("elderberry","fig")
final_tuple=t3+t4
if 'grape' in final_tuple:
    print("Grape is Present")
else:
    print("Grape is not present")


#Set operation
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


#Frozen Sets

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



