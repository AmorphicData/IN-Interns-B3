#Q1
List=input("Enter the numbers with space").split()
input_list=[int(i) for i in List]# list comprehension
#map,filter me pehli arguement hota hai hamara function dosri argument hoti hai iterable
def even(num):
   return num%2==0
ans=list(map(lambda x:x**2,filter(even,input_list)))
print(ans)

#Q2
List=input("Enter The List of Numbers with Space").split()
input_list=[int(i) for i in List]
def fact(num):
   if num==0 or num==1:
      return num
   return num*fact(num-1)
ans=list(map(fact,input_list))
print(ans)
      
#Q3
#Zip function is used to combine two or more iterables into a single iterable convert to tuple
student_name=["Rounak","Saksham","Kaustubh","Nayan"]
grades=["A+","O","A","B"]
student_dict=dict(zip(student_name,grades))
print(student_dict)

#Q4
List=input("Enter The List of Numbers with Space").split()
input_list1=[int(i) for i in List]
List2=input("Enter The List Elements for List2 with space").split()
input_list2=[int(i) for i in List2]
final_list=list(zip(input_list1,input_list2))
#ab me is final list par iterate karoonga
def fun(final_list):
    if final_list[0]>final_list[1]:
        return final_list[0]
    
filter_list=list(filter(fun,final_list))
#filter will return true or false and it will return a tuple of tuple yeh hame iterator deta hai
print(filter_list)
filter_list=list(map(fun,filter_list))
#map vohi return karega jo ham usko bolunge
print(filter_list)

#Q5
def square_filter(num):
    return num >= 0
numbers = [-3, -2, -1, 0, 1, 2, 3]
squared_numbers = map(lambda x: x ** 2, numbers)
positive_squares = filter(square_filter, squared_numbers)
sum_of_squares = sum(positive_squares)
print(sum_of_squares)

#Q6
List=input("Enter The List of Numbers with Space").split()
side1=[int(i) for i in List]
List2=input("Enter The List of Numbers with Space").split()
side2=[int(i) for i in List2]
List3=input("Enter The List of Numbers with Space").split()
side3=[int(i) for i in List3]
list_sides=list(zip(side1,side2,side3))
print(list_sides)
def is_valid(side):
    if side[0]<side[1]+side[2] and side[1]<side[0]+side[2] and side[2]<side[1]+side[0]:
        return side
    # else:
    #     return 0

print(list(filter(is_valid,list_sides)))

#Q7
from functools import reduce
vowels=['a','e','i','o','u']
str_list=input("Enter The List of String").split()
def isVowl(str):
    for ch in str:
        if ch not in vowels:
            return 0
    return 1
def fun(str):
    if(isVowl(str)):
        return 0
    return 1
ir=list(filter(fun,str_list))
ans=reduce(lambda x,y:x+y,ir)
print(ans)

#Iterators and Generators
#Q1
def read_large_file(sample):
    try:
        with open(sample, 'r') as file:
            for line in file:
                yield line.strip('\n')
    except FileNotFoundError:
        pass

gen=read_large_file("sample.txt")
print(next(gen))
print(next(gen))
# print(next(gen)) it will print Stop Iteration


#Q2
def fibonaci():
    a=0
    b=1
    while True:
        yield a
        a,b=b,a+b

fib_gen=fibonaci()
for _ in range(10):
    print(next(fib_gen))

#idhar _ iska matlab hai ki jab ham java vagera me variable ko define nahi karte the us time ka
    
def even_number(num):
    for i in num:
        if i % 2==0:
            yield i

number=[1,2,3,4,5,6]
even_gen=even_number(number)
print(next(even_gen))
print(next(even_gen))
####
it=iter(number)
it2=even_number(number)
print(next(it2))
print(next(it2))

class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item*item
        else:
            raise StopIteration
    
number=[1,2,3,4]
for i in SequenceIterator(number):
    print(i)

#Q3
List=input("Enter The Numbers of List").split()
input_list=[int(i) for i in List]
#using Generator
def odd_number(num):
    for i in num:
        if i%2 !=0:
            yield i

odd_gen=odd_number(input_list)
print(next(odd_gen))
print(next(odd_gen))
#for Iterator
iter1=odd_number(input_list)
it=iter(iter1)
print(next(it))
print(next(it))
print(next(it))


#ADD ON Questions
#-> Map Function
def my_map(func,iterable):
    ans=[]
    for item in iterable:
        ans.append(func(item))
    return ans

def double(num):
    return num*2

numbers=[1,2,3,4]
double_number=my_map(double,numbers)
print(double_number)

#Zip Function
def my_zipp(*iterables):
    #agar length of list equal nahi hai toh minimum length nikalni padegi
    min_length=min(len(iterable) for iterable in iterables)#list comprehension bolte hai isse
    zipped=[[] for _ in range(min_length)]#har ke liye ek empty list banani padegi
    #create an empty list one for each iterable
    #now i will iterate over each iterable
    for iterable in iterables:
        #iterate over each element in iterable
        for i,ele in enumerate(iterable):
            zipped[i].append(ele)
    return zipped

number=[1,2,3]
letter=['a','b','c']
zipped_data=my_zipp(number,letter)
#list comprehension
list_of_tuple=[tuple(sublist) for sublist in zipped_data]
print(list_of_tuple)

#Filter function
def my_filter(func,iterable):
    ans=[]
    for item in iterable:
        if func(item):
            ans.append(item)
    return ans
def iseven(num):
    if num%2==0:
        return True
number=[1,2,3,4]
filtered_item=my_filter(iseven,number)
print(filtered_item)

