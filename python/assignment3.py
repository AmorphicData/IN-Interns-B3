#CUSTOM FUNCTIONS

'''
1. #Max
l = [99,2,3,4,6,5,2,311,33]
a=l[0]
for i in l:
    if i > a:
        a=i
print(a)

2. #Min
l = [9,2,3,4,6,5,2,311,33]
a=l[0]
for i in l:
    if i < a:
        a=i
print(a)

3. #sum
l = [9,2,3,4,6,5,2,311,33,1]
sum=0
for i in l:
    sum+=i
print(sum)

4. #length
l = [9,2,3,4,6,5,2,311,33,1]
count=0
for i in l:
    count+=1
print(count)


5. # Statistics Mean
l = [9,2,3,4,6,5,2,311,33,1]
avg=0
count=0
for i in l:
    count+=1
print(count)
for i in l:
    sum+=i
    avg=sum/count
print(avg)


6. #count
key=int(input())
l = [9,2,3,4,6,5,2,311,33,1,3,3,3,3,3]
count = 0
for i in l:
    if i == key:
        count += 1
print(count)

7. #absolute
a = int(input())
if a<0:
    print (-a)
else:
    print (a)


8. #reverse

l = 9,2,3,4,6,5,2,311,33,1,3,3,3,3,3
rev = l[::-1]
print(rev)


9. #Upper
l=['a','b','c','D','E','f']
result = ""
for char in l:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32) + " "
    else: 
        result += char + " "
print (result)

10. #Lower
l=['a','b','c','D','E','f']
result = ""
for char in l:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32) + " "
    else: 
        result += char + " "
print (result)


#11. power
n = int(input())
power=int(input())
print(n**power)
'''
'''
#BUILD IN FUNCTIONS
#1 sorted
l2=[3, 1, 4, 1, 5, 9, 2]
print(sorted(l2))
#2 format
name = "Nayan"
age = 21
print("My name is {} and I am {} years old.".format(name, age))
#3 round
print(round(3.14159, 2))
#4 any
l3 = [0, False, None, 1]
print(any(l3)) 
#5 all
l4 = [1, True, "hello"] 
print(all(l4))  
#6 enum
l5=["abc",2,3 ]
for index, value in enumerate(l5): 
    print(index, value)

#7 slice
7 = [1, 2, 3, 4, 5]
m = slice(2)
print(l7[m]) 

#8 bool
print(bool(0)) 
result = eval("4 + 7 * 8") #Evaluates a Python expression given as a string and returns the result
print(result)

#9 exec
exec("x = 9\ny = 10\nprint(x * y)") 
#10 isinstance
print(isinstance("abc", str))
#11 hash
print(hash("hello"))
#12 pow
print(pow(2, 3)) 
#13 abs
print(abs(-33))

#14 type
print(type(5))
#15 callable
def func():
    return True
print(callable(func))  
#16 id
l6 = [1, 2, 3]
print(id(l6))
#17 bin
print(bin(21)) 
#18 hex
print(hex(245)) 
#19 oct
print(oct(8))
#20chr
print(chr(65))
#21 ord
print(ord('A')) 

#22 range
for i in range(1,3):
    print(i)

#23 avg
    import statistics
a = [1,2,3,4,5]
print(statistics.mean(a))
import math
#24 sqrt
a=24
print(math.sqrt(a))

#25 islower
a="acbd"
print(a.islower())

#26 isupper
a="aCbd"
print(a.isupper())
'''
#count
a=[1,2,3,2,1,4,2,1]
print(a.count(2))
