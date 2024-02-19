#Q1

'''L = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, L))
# even_numbers_list = list(filter(lambda x: x % 2 == 0, L)) #is done cause iterator gets full consumed
squared_numbers = map(lambda y: y ** 2, even_numbers)
print(list(squared_numbers))'''


#Q2

'''from functools import reduce 
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1),1)
number=7
print(f"The factorial of {number} is {factorial(number)}")'''


#Q3

'''from functools import reduce
names=["Agam", "Madhavan", "Himani", "Siddh"]
grades=[90,80,90,95]
names_grades=zip(names,grades)
student_grade_dict=dict(names_grades)
print(student_grade_dict)'''


#Q4

'''from functools import reduce
grade1=[90,95,97,85]
grade2=[91,75,100,80]
combined_grades=zip(grade1,grade2)
filtered_grades=filter(lambda x: x[0] >= x[1],combined_grades)
result = list(map(lambda x: x[0], filtered_grades))
print(result)'''

#Q5

'''def square_filter(num):
    return num >= 0
numbers = [-3, -2, -1, 0, 1, 2, 3]
squared_numbers = map(lambda x: x ** 2, numbers)
positive_squares = filter(square_filter, squared_numbers)
sum_of_squares = sum(positive_squares)
print(sum_of_squares)'''


#Q6

'''def func(t):
    if t[0]<t[1]+t[2] and t[1]<t[0]+t[2] and t[2]<t[1]+t[0]:
        return True
from functools import reduce
triangle1=[1,2,3]
triangle2=[1,2,3]
triangle3=[2,3,4]
combined_triangles=list(zip(triangle1,triangle2,triangle3))
print (combined_triangles)
filtered_sides=list(filter(func,combined_triangles))
print(filtered_sides)'''

#Q7**

'''from functools import reduce
list_of_strings=["hello","world","aeiou"]
vowels=['a','e','i','o','u']
def isvowel(s):
    for i in s:
        if(i not in vowels):
            return 0
    return 1

def fil(z):
    if(isvowel(z)):
        return 0
    return 1

ir=list(filter(fil,list_of_strings))
fs=reduce(lambda x,y:x+y,ir)
print(fs)'''

#Q1

'''def read_large_file(sample):
    try:
        with open(sample, 'r') as file:
            for line in file:
                yield line.strip('\n')
    except FileNotFoundError:
        pass

gen=read_large_file("sample.txt")
print(next(gen))'''


#Q2

'''def even_number(num):
    for i in num:
        if i % 2==0:
            yield i
number=[1,2,3,4,5,6]
even_gen=even_number(number)
print(next(even_gen))
print(next(even_gen))
# it=iter(even_gen)
# print(next(it))
# print(next(it))'''


#Q3

#Generator
'''def filt_transform():
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

#Iterator
print("Filtering data by even values(Iterator):")
tr_list = [ i for i in range(1,10)]
ft = list(filter(lambda x:x %2 ==0,tr_list))
iter_ft = iter(ft)
print(next(iter_ft))
print(next(iter_ft))
print(next(iter_ft))
print(next(iter_ft))'''

