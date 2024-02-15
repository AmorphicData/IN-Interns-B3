#The max Function

# L=[1,2,3,4,5]
# max_num=-1
# for i in L:
#     if i>max_num:
#         max_num=i
# print(max_num)

#The min Function

# L=[7,3,4,5]
# min_num=L[0]
# for i in L:
#     if i<min_num:
#         min_num=i
# print(min_num)

#The len function

# def length(L):
#     count=0
#     for i in L:
#         count=count+1
#     return count

# L=[1,5,6,7,8]
# print(length(L))

#the sum function

# numbers=input("enter nums to find sum of:")
# sum=0
# for i in numbers:
#     sum=sum+int(i)
# print(sum)

#the average function 

# L=[1,2,3,4,5]
# sum=0
# for i in L:
#     sum=sum+int(i)
# print(sum)

# count=0
# for j in L:
#     count=count+1
# print(count)

# print(sum/count)


#power function

# def power(base, exponent):
#     if exponent==0:
#         return 1
#     elif exponent==1:
#         return base
#     else:
#         return base*power(base, exponent-1)
    
# print(power(2,5))


# absolute function
# def abs(n):
#     if(n>0):
#         return n
#     n=(-1)*n
#     return n

# print(abs(5))



# the square root function

# number=int(input("please enter number to find aquare root of:"))
# for i in range(1,number):
#         if(i*i>number):
#          print(i-1)
#          break

# the range function

# def custom_range(start,stop=None,step=1):
#    #agar stop nahi de rakha hai toh start hi stop hoga
#    if stop==None:
#       stop=start
#       start=0
#    ans=[]
#    if step>0:
#       #badti hue range hai
#       while start<stop:
#          ans.append(start)
#          start+=step
#    elif step<0:
#       #decrease vaali range
#      while start>stop:
#             ans.append(start)
#             start += step
#    return ans
# print(custom_range(5))
# print(custom_range(1,5))
# print(custom_range(1,5,2))

#25 built-in functions

#hex
# num = 3456
# hex_num = hex(num)
# print(hex_num)

#all, any

# ls =[True,False,True,False,False,True,True,True]
# print(ls)
# print("All:" , all(ls))                  
# print("Any:" , any(ls))                  

#bin

# num = -10
# binary_representation = bin(num)
# print(binary_representation)

# # Using bytes to get bytes object for a int
# print("Byte obejct of int 9" , bytes(9))
# #Using evaluate
# print("Evaluating 7 times 7" , eval("7*7"))
# #Using execute
# exec('print("Sum of 64 and 42 is", (64+42))')
# #octal conversion
# print("Octal value of 1111: ",oct(1111))
# #Using ord to get ascii value of a char(10)
# print("ASCII value of A: ", ord('A'))
# #Using round to round off
# print("Rounding off 68.6952",round(68.6952))
# #Returns the type of an object
# print(type(5)) 
# #Converts a value to a Boolean
# print(bool(0)) 
# #power
# print(pow(2, 3)) 
# #absolute
# print(abs(-5))
# #to check the type 
# x = 10
# print(isinstance(x, int))
# #to print hash value
# print(hash("hello"))
# #to printlen
# l = [1, 2, 3, 4, 5]
# print(len(l))  
# #max num
# print(max(l))
# #min num
# print(min(l))
# #sum
# print(sum(l))
#help function
# help(print)

# locals(): Returns a dictionary representing the current local symbol table.
def my_func():
    x = 10
    print(locals())

my_func()

# getattr(): Returns the value of the named attribute of an object.
class MyClass:
    x = 10

obj = MyClass()
print(getattr(obj, 'x'))  # Output: 10


