#!/usr/bin/env python3

#Custom functions
#Write python program to illustrate the usage of custom functions to replace the built-in functions (Min 10 custom functions). Minimize using any built-in functions while trying to program the custom functions.

#len function
a = [1, 2, 3, 4, 5]
count = 0
for i in a:
    count += 1
print(count)

#abs function
a = -5
print(-(a)) if a < 0 else a

#min function
a = 6
b = 7
c = 8
min = a
if b<a and b<c: min = b
elif c<a and c<b: min = c
else: min = a
print(min)

#max function
a = 6
b = 7
c = 8
max = a
if b>a and b>c: max = b
elif c>a and c>b: max = c
else: max = a
print(max)

#isupper function
s = 'ANANYA'
for char in s:
    # Check if the character is an uppercase letter
    if ord('A') <= ord(char) <= ord('Z'):
        continue
    else:
        print('False')
    print('True')

#avg function
arr = [3, 66, 88, 34, 10]
avg = 0
for i in arr:
    avg += i/len(arr)
print(avg)

#sqrt function
a = 144
print(a**(1/2))

#sum function
sum = 0
for i in arr:
    sum +=i
print(sum)

#split
string = 'Hi, I am Ananya'
s = ''
arr = []
for i in string:
    if i == ' ':
        s = ''
    else:
        arr.append(s)
        s = s+i
print(arr)  

#replace
k = ''
sentence = 'Hi, I am Ananya'
char1 = input()
char2 = input()

for i in sentence:
    if i == char1:
        k = k + char2
    else:
        k = k + i

print(k)

#strip
input_string = input()
start = 0
end = len(input_string) - 1

while start <= end:
  if input_string[start] not in " \t\n":
    break
  start += 1

while end >= start:
  if input_string[end] not in " \t\n":
    break
  end -= 1

stripped = input_string[start:end + 1]
print(stripped)


#Built-in functions
#Write python program to illustrate the usage of different built-in functions (Min 25 built-in functions). Avoid repeating the frequently discussed/used built-in functions.

# isspace()
text = "  Hello"
print(text.isspace())  # True

# isalpha()
text = "Hello"
print(text.isalpha())  # True

# isalnum()
text = "Hello123"
print(text.isalnum())  # True

# casefold()
text = "Hello"
print(text.casefold())  # hello

# endswith()
text = "Hello"
print(text.endswith("lo"))  # True

# encode()
text = "Hello"
encoded_text = text.encode("utf-8")
print(encoded_text)  # b'Hello'

# center()
text = "Hello"
centered_text = text.center(10, "*")
print(centered_text)  # **Hello***

# isascii()
text = "Hello"
print(text.isascii())  # True

# isdecimal()
text = "12345"
print(text.isdecimal())  # True

# isnumeric()
text = "12345"
print(text.isnumeric())  # True

# lstrip()
text = "   Hello"
print(text.lstrip())  # 'Hello'

# rstrip()
text = "Hello   "
print(text.rstrip())  # 'Hello'

# swapcase()
text = "HeLLo"
print(text.swapcase())  # 'hEllO'

# startswith()
text = "Hello"
print(text.startswith("He"))  # True

# chr()
print(chr(65))  # 'A'

# ord()
print(ord('A'))  # 65

# zfill()
text = "42"
print(text.zfill(5))  # '00042'

#divmod
x = divmod(5, 2)
print(x)  # 2, 1

# partition()
text = "Hello World"
print(text.partition(" "))  # ('Hello', ' ', 'World')

# rpartition()
text = "Hello World"
print(text.rpartition(" "))  # ('Hello', ' ', 'World')

# rsplit()
text = "Hello World"
print(text.rsplit(" "))  # ['Hello', 'World']

# splitline()
text = "Hello\nWorld"
print(text.splitlines())  # ['Hello', 'World']

# rjust()
text = "Hello"
print(text.rjust(10, "*"))  # '*****Hello'

# title()
text = "hello world"
print(text.title())  # 'Hello World'

# expandtabs()
text = "Hello\tWorld"
print(text.expandtabs(4))  # 'Hello   World'

# isdigit()
text = "123"
print(text.isdigit())  # True

# index()
text = "Hello"
print(text.index("e"))  # 1

# issuperset()
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # True

# isdisjoint()
set1 = {1, 2, 3}
set2 = {4, 5}
print(set1.isdisjoint(set2))  # True

# isidentifier()
text = "my_variable"
print(text.isidentifier())  # True
