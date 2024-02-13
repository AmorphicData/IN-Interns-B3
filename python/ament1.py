#L1=[1,2,3,4]
#L1.append(5)
#print(#L1)
#L1.pop(2)
#print(L1)
#L2=[1,2,3,4,5]
#L2.append(6)
#L2.pop(0)
#print(len(L2))
#L3=L2[2:5]
#print(3 in L2)
#str1=input()
#str2=input()
#str3=str1+str2
#print(str3)
#print(len(str1))
#str = input()


#print("First 3 characters", str[:3])


#print("#Last 3 characters", str[-3:])

#print("Every second character", str[::2])
#str=input()
#print("Reverse of str " ,str[::-1])
#char=input()
#count=0
'''for i in str:
    if i==char:
        count=count+1'''
#print("number of occurrences ",count)

#print(str.upper())
#print(str.lower())
#str2=input()
#if str2 in str :
#   print("Found")
#else:
 #   print("Not Found")
#str1=input()
#old=input()
#new=input()
#replaced=str1.replace(old,new)
#str1=input()
#l=str1.split()
#for word in l:
#    print(word,"\n")
#print(replaced)
#str=input()
#list=str.strip()
#print(list)
#i=0
#l=[]
#for i in range(0,3):
#    l.append(input())
#fs=','.join(l)
#print(fs)
#s=input()
#fs='-'.join(s)
#print(fs)
'''l=[]
i=0
for i in range(0,3):
    l.append(int(input()))

s = [str(num) for num in l]
print(s)
l=input().split()
sp=input()
fs=sp.join(l)
print(fs)

fragments = input("Enter several string fragments separated by spaces: ").split()
joined_string = ' '.join(fragments)
print("Joined string:", joined_string)
#Dictionary operations
student_scores={'ram':99,'Yash':80,'Bunty':88}
del student_scores['Yash']
student_scores['Raj']=90
print(student_scores)
stu=input()
if stu in student_scores:
    print("Found")
else:
    print("Not Found")
print("Keys:", student_scores.keys())
print("Values:", student_score.values())
fruits={'apple':99,'banana':80,'orange':88}
del fruits['banana']
fruits['orange']=90
print("Keys:", fruits.keys())
print("Values:", fruits.values())
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
print(info["p1"]["name"])
#Tuple 
tu1=('hello', 'cloudwick', 'swe', 'intern','swe')
tu2=('ui', 'qa')
tu3 = tu1+ tu2
print(tu3)
index = tu3.index("cloudwick")
print("Index of 'cloudwick':", index)
print(tu3.count('swe'))
print("Subset of elements:", tu3[2:5])

tu4=("apple", "banana", "cherry", "date")
print(tu4[2])
print(tu4.index('banana'))
print(tu4.count('apple'))
tu5=("elderberry", "fig")
tu6=tu4+tu5
if "grape" in tu6:
    print("'grape' is present in the tuple.")
else:
    print("'grape' is not present in the tuple.")
#Set
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
#frozen set
fr1=frozenset({1,2,4,5,5})
fr2=frozenset({2,3,1,4,4,55,6})
uf=fr1.union(fr2)
inf=fr1.intersection(fr2)
diff=fr1.difference(fr2)
print("Union ",uf)
print("intersection ",inf)
print("difference ",diff)
s_check=fr1.issubset(fr2)
print(s_check)'''







    







