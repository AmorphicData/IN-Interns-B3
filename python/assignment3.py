#Built-in functions

#abs() -1 
print(abs(-8))

#any() -2
print(any([1,False,None]))

#all() -3
print(all([0,1,None]))

#bin() -4
print(bin(7))

#exec() -5
x = 8  
exec('print(x==8)')  
exec('print(x+4)')  

#format() -6
print(format(123,"d"))
print(format(12,"b"))

#complex() -7
print(complex(7,2))

#enumerate() -8 
l=enumerate([1,2,3,4,5])
print(list(l))

#hex() -9
print(hex(13))
print(hex(6))

#oct() -10
print(oct(10))
print(oct(64))

#pow() -11  
print(pow(4,2))

#round() -12
print(round(10.5))
print(round(25.8))

#zip() -13
l=["hani","kittu"]
l1=["1","2"]
l2=zip(l,l1)
print(list(l2))

#chr() -14
print(chr(65))
print(chr(112))


#map() -15
n=[1,2,3,4,5]
def square(x):
    return x**2
sq_num=map(square,n)
print(list(sq_num))

#divmod() -16
print(divmod(17,4))

#reversed() -17

str_1='hellobanglore'
print(list(reversed(str_1)))

#getattr() -18

class student:
    name='hani'
    age=20
print(getattr(student,'name'))

#hasattr() -19
print(hasattr(student,'age'))
print(hasattr(student,'gender'))

#isinstance() -20

print(isinstance(5,float))

#next() -21
l=iter([1,2,3,4])
print(next(l))


#setattr() -22

print(setattr(student,'age',25))
print(getattr(student,'age'))
      
#slice() -23

a=[1,2,3,4,5,6,7,8,9,10]
x=slice(0,8,3)
print(a[x])

#sorted() -24

n=["k","w","p","d"]
print(sorted(n))

#open() -25
f=open("demo.txt","r")
print(f.read())



#Custom functions

numbers = [5, 2, 8, 3, 1, 7, 9]

#sum

def sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result
print("Sum:", sum(numbers))

#max

def max(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum
print("Max:", max(numbers))

#min

def min(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum
print("Min:", min(numbers))

#len

def length(numbers):
    count = 0
    for i in numbers:
        count += 1
    return count
print("Len:", length(numbers))


#avg

def average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    if count == 0:
        return 0 
    return total / count

print("Average:", average(numbers))

#pow

def pow(base, exponent):
    result = 1
    i=0
    while i <exponent:
        result *= base
        i+=1
    return result

print("Power:", pow(2,3))


#abs
def abs(num):
    return -num if num < 0 else num
print("Absolute Value:", abs(-9))
      
#reverse
def reverse(input_str):
    return input_str[::-1]
print("Reverse String:", reverse('harshinibollineni'))

#isalpha

def isalpha(s):
    for char in s:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            return False
    return True
print("Is a alphabet:", isalpha('B'))
print("Is a alphabet:", isalpha('$'))


#isdigit

def isdigit(s):
    for char in s:
        if '0' <= char <= '9':
            return True
    return False

print("Is a digit:", isdigit("1234"))
print("Is a digit:", isdigit("12.8"))
print("Is a digit:", isdigit("hanii"))



