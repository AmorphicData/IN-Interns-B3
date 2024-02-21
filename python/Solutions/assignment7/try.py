# sentence = "Hello, how are you doing today?"
# print(sentence.split(' ')) 
# print(sentence.rsplit(' ', 3))

# s = "hello, world. Today is a nice day, right?"
# print(s.partition(','))
# print(s.rpartition(','))


# a1 = "Hello, 你好"
# a2 = "Hello, world!"
# a3 = "©"
# a4 = "?"

# print(a1.isascii())  
# print(a2.isascii())
# print(a3.isascii())
# print(a4.isascii())

# # l = [2, 3, 4, 5]
# # i = iter(l)
# # j = iter(l)

# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(j))
# # print(next(i))
# # print(next(j))

# # class SequenceIterator:
# #     def __init__(self, sequence):
# #         self._sequence = sequence
# #         self._index = 0

# #     def __iter__(self):
# #         return self

# #     def __next__(self):
# #         if self._index < len(self._sequence):
# #             item = self._sequence[self._index]
# #             self._index += 1
# #             return item * item
# #         else:
# #             raise StopIteration
        
# # s = SequenceIterator([1, 2, 3, 4])
# # l = iter(s)
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))


# # def sqr(x):
# #     return x*x

# # print(list(map(sqr, [4, 5, 6, 7])))

# # def sqr(y):
# #     for i in range(len(y)):
# #         if i == 2:
# #             yield y[i]*y[i]

# # s = sqr([30, 4, 5, 6])

# # print(next(s))

# # def sqr(y):
# #     for i in range(len(y)):
# #         if i == 2:
# #             return y[i]*y[i]

# # s = sqr([30, 4, 5, 6])

# # print(s)

# def func(n, z):
#     y = 5
#     return lambda a: n*a + y - z
# a = func(6, 5)
# b = func(5, 9)
# print(a(3))
# print(b(10))

# def sq(x):
#     global y
#     y = x * x

# def minus(s, y):
#     return y

# s = sq(4)
# m = minus(s, y)
# print(m)

# def outer(t):
#     def inner(t):
#         return t+5
#     return inner(t)

# a = outer(5)
# print(a)

# t = 8
# def outer():
#     pass
#     def inner():
#         pass
#         def f():
#             pass
#         f()
#     inner()

# a = outer()
# print(a)

# def upper_d(function):
#     # def wrapper():
#     func = function()
#     u = func.upper()
#     return u
#     # return wrapper()

# @upper_d
# def say_hello():
#     return 'Hello world'

# print(say_hello)

# # u = upper_d(say_hello)
# # print(u)


# from datetime import datetime

# def time(function):
#     def wrapper(x):
#         start_time = datetime.now()
#         s = start_time.strftime("%H:%M:%S")
#         result = function(x)
#         return result, s
#     return wrapper(3)

# @time
# def calc(x):
#     return x*x

# print(calc)


# import folder.rough as r

# r.main()
# r.add()
# r.main()
# r.s()

# with open('file.txt', 'r') as f:
#     data = f.read()
#     print(data)

# with open('file.txt', 'w+') as f:
#     f.write('1\n')
#     f.write('2\n')
#     f.write('3\n')

# with open('file.txt', 'a+') as f:
#     f.write('a\n')
#     f.write('b\n')
#     f.write('c\n')

# # with open('file.txt', 'w+') as f:
# #     pass

# with open('file.txt', 'r') as f, open('file2.txt', 'w+') as f2:
#     data = f.read()
#     f2.write(data)

# import sys

# add = 0.0
# n = len(sys.argv) 
# for i in range(1, n): 
#     add += float(sys.argv[i]) 
# print("the sum is :", add) 

# class Car:
#     def __init__(self, color, wheels):
#         self.color = 'Red'
#         self.wheels = 4

#     def __str__(self):
#         return f'{self.color}, {self.wheels}'
    
#     def move():
#         return 'Im moving'
    
# class Airplane:
#     def __init__(self, color, milage, wheels):
#         self.color = 'Blue'
#         self.milage = '4000'

#     def __str__(self):
#         return f'{self.color}, {self.milage}'
    
#     def fly():
#         return "I'm Flying"
    
# class ABC(Car, Airplane):
#     def __init__(self, color, wheels, milage, speed):
#         super().__init__(color, wheels)
#         self.speed = 80

#     def __str__(self):
#         return f'{self.wheels, self.color}'

# t = ABC('Green', 4, 3000, 60)
# print(t)
    

# class Car:
#     def __init__(self, color, __wheels):
#         self.color = color
#         self.__wheels = __wheels

#     def __str__(self):
#         return f'{self.color}, {self.__wheels}'

# class ABC(Car):
#     def __init__(self, color, __wheels):
#         super().__init__(color, __wheels)
#         self.speed = 80

#     def __str__(self):
#         return f'{self._Car__wheels} wheels, {self.color}, {self.speed} speed'

# c = ABC('Blue', 4)
# print(c)

