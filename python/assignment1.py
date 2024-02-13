#list operation
list=[11,22,33,44,55]
list.append(66)
print(list)
del list[2]
print(list)

list1=[1,2,3,4,5]
list1.append(6)
print(list1)
del list1[0]
print(list1)
list_len=len(list1)
print(list_len)
sub=list1[2:5]
print(sub)
print(' Is value Present?', 3 in list1)  

#string operation 

str1=input("Enter the string1: ")
str2=input("Enter the string2: ")
concat_str=str1+str2
print(concat_str)

str_len=len(str1)
print(str_len)

first_three=str1[:3]
last_three=str1[-3:]
every_second=str1[::2]
print(first_three)
print(last_three)
print(every_second)

rev_str=str1[::-1]
print(rev_str)

char_count=input("Enter char to count: ")
occur=str2.count(char_count)
print(occur)

str_upper=str2.upper()
str_lower=str2.lower()
print(str_upper)
print(str_lower)

str3=input("Enter string:")
if str3 in str1:
    print("Substring found")
else:
    print("Substring not found")

str4=input("Enter a string: ")
old_str=input("Enter substring to be replaced: ")
new_str=input("Enter new substring: ")
modified_str=str4.replace(old_str,new_str)
print(modified_str)

words=str4.split()
for word in words:
    print(word)

str5=input("Enter the string: ")
trim_str=str5.strip()
print(trim_str)

#joins

string_list=["hani" ,"is" ,"a","good","girl"]
joined_str=' '.join(string_list)
print(joined_str)

separator=input("Enter the separtor: ")
joined_str=separator.join(string_list)
print(joined_str)

str6=input("Enter a string:")
join_str6='-'.join(str6)
print(join_str6)

numbers=[1,2,3,4,5]
join_num=','.join(str(numbers) for  numbers in numbers)
print(join_num)

str7=input("Enter a string:")
join_str7='_'.join(str7.split())
print(join_str7)

fragments_str= input("Enter the string:").split()
joined=' '.join(fragments_str)
print(joined)


#dictionary operation

student_score={'Hani': 90,'Kittu':85,'Ramu':70,'Sita':60}
print(student_score)
del student_score['Ramu']
print(student_score)
student_score.update({'Ani':45})
print(student_score)
key_check='Kittu'
if key_check in student_score:
    print("Student exists")
else:
    print("Not exist")
print(student_score.keys())
print(student_score.values())


fruit_dict={'apple':10,'banana':20,'orange':30}
fruit_dict['grape']=15
print(fruit_dict)
del fruit_dict['banana']
print(fruit_dict)
if 'orange' in fruit_dict:
    print("orange exist")
else:
    print("not exist")
print(fruit_dict.keys())
print(fruit_dict.values())


person_dict={'name':'hani','age':20,'city':'banglore'}
print(person_dict)
print(person_dict['age'])
person_dict['gender']='female'
person_dict['age']='21'
print(person_dict)
del person_dict['city']
gender_remove=person_dict.pop('gender')
print(person_dict)
if 'city' in person_dict:
    print("city foun")
else:
    print("city not found")
for key,value in person_dict.items():
    print(f"{key}:{value}")
person_dict.clear()
print(person_dict)


#nested dictionary

person_info={
    'p1': {'name':'hani','age':20,'city':'banglore'},
    'p2': {'name':'kittu','age':25,'city':'hyderabad'},
    'p3': {'name':'mahi','age':45,'city':'chennai'}
}

print(person_info['p2']['name'])

#tuple operation

t1=("hani","kittu","ramu")
t2=("ani","juhi")
concat_tup=t1+t2
print(concat_tup)
print(concat_tup.index("ramu"))
print(concat_tup.count("kittu"))
print(concat_tup[2:4])


fruit_tuple=('apple','banana','cherry','date')
print(fruit_tuple[2])
print(fruit_tuple.index('banana'))
print(fruit_tuple.count('apple'))
update_tuple=fruit_tuple+('elderberry','fig')
print(update_tuple)
print('grape' in update_tuple)

#set operation 

set1={11,22,33,44,55}
set2={44,55,66,77,88}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.issubset(set2))
set1.add(66)
set2.remove(66)
print(set1)
print(set2)
print(len(set1))



set_1={1,2,3,4,5}
set_2={4,5,6,7,8}
print(set_1.union(set_2))
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
set_1.add(9)
set_2.discard(2)
print(set_1)
print(set_2)
print({1,2,3}.issubset(set_1))


#frozenset

set3=frozenset({15,25,35,45,65})
set4=frozenset({45,65,75,85,95})
print(set3.union(set4))
print(set3.intersection(set4))
print(set3.difference(set4))
print(set3.issubset(set4))


