#Calculator module
# Create a module named calculator.py with functions to perform basic mathematical operations. Then, create another 
# Python script to import and use these functions.
import calc_mod as c

a,b = input("Enter two numbers:").split()
a = float(a)
b = float(b)
print("Sum:", c.add(a,b))
print("Difference:", c.diff(a,b))
print("Multiply:", c.mul(a,b))
print("Division:", c.div(a,b))

print("==========================================")

# Create a package named shapes with modules for calculating the area and perimeter of geometric shapes such as 
# circles and rectangles. Then, import and use these modules in another Python script.
#Shapes package
import shapes.perimeter as per
import shapes.area as ar

sh = input("Enter a shape:")

if sh == 'circle':
    rad = int(input("Radius : "))
    print("Perimeter:", per.circleP(rad))
    print("Area:", ar.circleA(rad))
elif sh == 'triangle':
    a,b,c = map(int,input("Sides : ").split())
    print("Perimeter:", per.triangleP(a,b,c))
    print("Area:", ar.triangleA(a,b,c))
elif sh == 'square':
    side = int(input("Side : "))
    print("Perimeter:", per.squareP(side))
    print("Area:", ar.squareA(side))
elif sh == 'rectangle':
    l,b = map(int,input("Length and Breadth : ").split())
    print("Perimeter:", per.rectangleP(l,b))
    print("Area:", ar.rectangleA(l,b))
else:
    print("Shape not available.")

print("==========================================")

# Explore various functionalities of the following modules os, sys, datetime, collections and re. (Min 5 methods in each module)


import os 
#Print current device operating system details
print(os.uname())
#Print current working directory
print(os.getcwd())
#Create a directory given name as an argument
os.mkdir("test")
#Removes a file passed as argument can be relative path or absolute
os.remove('test.txt')
#Return the number of cpu cores present
print(os.cpu_count())

import sys
#Get input from command line directly. Functions in the similar way as a input
for i in sys.stdin:
    if "exit" == i.rstrip():
        break
    print("Typed: ", i)

#Display output directly to console. Print functionality is implemented this way      
sys.stdout.write("This will be directly printed similar to print.")

#Display number of arguments passed
print("Arguments:", len(sys.argv))      #pass arguments like bash

#Display path to all namespaces where modules are located at
print(sys.path)
print("-------------------------------------")
print(sys.modules)

print("==========================================")

import datetime

#Print current timestamp
print(datetime.datetime.now())

#Print an exact date
dt = datetime.date(2005,8,18)
print(dt)

#Get date in string format
st = datetime.date.isoformat(dt)
print(type(st), st)

#Printing date in a specific format
now = datetime.datetime.now()
stfmt=now.strftime("%A %m %-Y")
print("Date in format(Day of Week Month Year):-  ", stfmt)

#Finding difference between date(timedelta)
t1 = datetime.date(year = 2024, month = 2, day = 20)
t2 = datetime.date(year = 2010, month = 1, day = 1)
t3 = t1-t2
print("DIfference between 20 Feb 2024 and 1 January 2010:  ", t3)
print("Type of t3(difference) =", type(t3))

print("==========================================")

#Counts the frequency of occurence
from collections import Counter
print(Counter(['B','C','A','B','C','A','B', 'B','A','C','A','V','V','C','A','V'])) 

#Ordered dicts remember the order in which keys are inserted
from collections import OrderedDict
od = OrderedDict()  
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
    
print('Before Deleting') 
for key, value in od.items():  
    print(key, value)  
od.pop('a')     #Deletion
od['a'] = 1     #Re-insertion
print('\nAfter re-inserting') 
for key, value in od.items():  
    print(key, value)


#Default dict do not need to use .get method. Each key has default value of zero
from collections import defaultdict  
     
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]  
for i in L:
    d[i] += 1
print(d)

#ChainMap : Useful for encapsulating many dictionaries into one
from collections import ChainMap  
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
c = ChainMap(d1, d2, d3)  
     
print(c)

#Double ended queue or Deque
from collections import deque 
de = deque([2,6,7])  
    
print("Original queue:", de)
de.append(4)  
print ("The deque after appending at right is : ")  
print (de)  

de.appendleft(6)
print ("The deque after appending at left is : ")  
print (de)

print("==========================================")

import re

cont = '''This text will be checked for some patterns so this will be a useful example 
            to understand this functionality of Re'''
#Print all occurence of a substring or pattern
x = re.findall("this",cont)
print(x)

#Search helps to search for a substring or a pattern and if multiple found it owuld only return its first occurence
sear = re.search("\s", cont)
print("The first white-space character is located in position:", sear.start())

#sub function to replace the match with some string
under = re.sub("\s","_",cont)
print(under)

#split function returns are list after splitting the content based on some pattern
lt= re.split("this", cont)
print(lt)

print("==========================================")

# Write a Python script to extract data from multiple CSV files, aggregate the data, and generate a 
# summary report. For example, you could extract sales data from multiple CSV files, calculate total sales for 
# each product, and generate a report with product-wise sales.

import os
import pandas as pd

def extract(csv_file):
    df = pd.read_csv(csv_file)
    return df

def aggregate_dat(dataframes):
    agg_data = pd.concat(dataframes, ignore_index=True)
    return agg_data.groupby('Product')['Sales'].sum().reset_index()

def gen_report(agg_data):
    summary_report = agg_data.sort_values(by='Sales', ascending=False)
    return summary_report

def proc_csv(csv_directory):
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]
    dataframes = []
    for csv_file in csv_files:
        file_path = os.path.join(csv_directory, csv_file)
        dataframes.append(extract(file_path))

    agg_data = aggregate_dat(dataframes)
    summary_report = gen_report(agg_data)
    return summary_report

dir = 'sample_data'
res = proc_csv(dir)
print(res)

print("==========================================")

# To read JSON data, validate it against a schema, and clean the data by removing or modifying invalid entries. 
# For example, you could validate user data against predefined rules and generate a clean dataset. File contains 
# 10 key value pairs, out of which we need only 5 mandatory key-value pairs and we have to convert the values to appropriate datatypes.

imp_keys = {'name', 'age', 'grades', 'address'}
def validate(df):
    cleaned_data = []
    for index, row in df.iterrows():
        clean_entry = {}
        for key in imp_keys:
            if key in row:
                if key == 'age':
                    try:
                        clean_entry[key] = int(row[key])
                    except ValueError:
                        print(f"Invalid age value '{row[key]}' for entry at index {index}")
                        break
                elif key == 'grades':
                    if isinstance(row[key], list):
                        clean_entry[key] = row[key]
                    else:
                        print(f"Invalid 'grades' value '{row[key]}' for entry at index {index}")
                        break
                else:
                    clean_entry[key] = row[key]
            else:
                print(f"Missing mandatory key '{key}' for entry at index {index}")
                break
            if len(clean_entry) == len(imp_keys):
                print(clean_entry)
                cleaned_data.append(clean_entry)
    return cleaned_data

df = pd.read_json("sample.json")
print(df)
cleaned_data = validate(df)

print("\nCleaned Data: \n")
print(cleaned_data)

print("==========================================")

# Write a python script to do basic CRUD operations for both SQL and NoSQL databases

import sqlite3
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
conn.commit()

def create(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
def read():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("--------------------------------")
def update(user_id, new_name, new_email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name, new_email, user_id))
    conn.commit()
def delete(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

create('John Doe', 'jhon12@gmail.com')
create('Jack Reacher', 'jakakaka@gmail.com')
create('Obadiah Stian', 'staiener@gmail.com')
read()

update(1, 'J Jonah Jamerson', 'jjj12341@gmail.com')
read()

delete(3)
read()

conn.close()

print("==========================================")