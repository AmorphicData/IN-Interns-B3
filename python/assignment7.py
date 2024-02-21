#Modules and Packages

#Create a module named calculator.py with functions to perform basic mathematical operations. Then, create another Python script to import and use these functions.

#calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is undefined"


#main.py 
    
import calculator as cal
a = cal.add(5, 3)
s = cal.subtract(10, 4)
m = cal.multiply(2, 6)
d = cal.divide(8, 2)
div=cal.divide(2,0)

print(f"Addition: {a}")
print(f"Subtraction: {s}")
print(f"Multiplication: {m}")
print(f"Division: {d}")
print(f"Division: {div}")


#Create a package named shapes with modules for calculating the area and perimeter of geometric shapes such as circles and rectangles. Then, import and use these modules in another Python script.

#circle.py

import math
def area(radius):
    return math.pi*radius**2
def perimeter(radius):
    return 2*math.pi*radius

#rect.py

def area(length,width):
    return length*width
def perimeter(length,width):
    return 2*(length+width)

#main.py

import shapes.circle as c , shapes.rect as rectangle
radius=5
c_a=c.area(radius)
c_p=c.perimeter(radius)

print(f"Circle Area: {c_a}")
print(f"Circle Perimeter: {c_p}")

length=5
width=6
r_a=rectangle.area(length,width)
r_p=rectangle.perimeter(length,width)

print(f"Rectangle Area: {r_a}")
print(f"Rectangle Perimeter: {r_p}")

#Explore various functionalities of the following modules os, sys, datetime, collections and re. (Min 5 methods in each module)

#os module 

import os

# 1. Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# 2. List files in a directory
files_in_directory = os.listdir('.')
print(f"Files in Current Directory: {files_in_directory}")

# 3. Check if a file exists
file_exists = os.path.exists('demo.txt')
print(f"Does File exist? {file_exists}")

# 4. Create a new directory
os.mkdir('new_directory')

# 5. Remove a directory
os.rmdir('new_directory')

#sys module 

import sys

# 1. Get the command line arguments
command_line_arguments = sys.argv
print(f"Command Line Arguments: {command_line_arguments}")

# 2. Get the Python version
python_version = sys.version
print(f"Python Version: {python_version}")

# 3. Get the maximum integer value
print(f"Maximum Integer Value: {sys.maxsize}")

# 4. Get the path of the Python interpreter
python_interpreter_path = sys.executable
print(f"Python Interpreter Path: {python_interpreter_path}")

# # 5. Exit the program with an error message
# sys.exit("Exiting the program with an error message")

#datetime module 

from datetime import datetime

# 1. Get the current date and time
current_datetime = datetime.now()
print(f"Current Date and Time: {current_datetime}")

# 2. Format a date as a string
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# 3. Get the current date
current_date = current_datetime.date()
print(f"Current Date: {current_date}")

# 4. Get the current time
current_time = current_datetime.time()
print(f"Current Time: {current_time}")

# 5. Get the day of the week
day_of_week = current_datetime.strftime("%A")
print(f"Day of the Week: {day_of_week}")

#collections module 

from collections import Counter, namedtuple, deque 

# 1. Count occurrences of elements in a list
elements_count = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(f"Element Count: {elements_count}")

# 2. Counter with strings
text = "hello hani"
char_count = Counter(text)
print(f"Character Count: {char_count}")

# 3. Create a named tuple
Person = namedtuple('Person', ['name', 'age'])
person = Person(name='John', age=30)
person2=Person(name='Hani',age=20)
print(f"Named Tuple: {person}")
print(f"Named Tuple: {person2}")
# 4. Create a deque (double-ended queue)
deque_example = deque([1, 2, 3])
deque_example.append(4)
deque_example.appendleft(0)
print(f"Deque: {deque_example}")

# 5. Chain multiple iterables together
import collections 
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
  
# initializing ChainMap 
chain = collections.ChainMap(dic1, dic2) 
  
# printing chainMap using maps 
print ("All the ChainMap contents are : ") 
print (chain.maps) 
  
# printing keys using keys() 
print ("All keys of ChainMap are : ") 
print (list(chain.keys())) 
  
# printing keys using keys() 
print ("All values of ChainMap are : ") 
print (list(chain.values())) 


#re module

import re

# 1. Match a pattern at the beginning of a string
pattern = re.compile(r'^\d+')
match_result = pattern.match('123abc')
print(f"Match Result: {match_result.group()}")

# 2. Search for a pattern anywhere in a string
search_result = re.search(r'\d+', 'abc123')
print(f"Search Result: {search_result.group()}")

# 3. Find all occurrences of a pattern in a string
findall_result = re.findall(r'\d+', '123abc456def789')
print(f"Findall Result: {findall_result}")

# 4. Replace matches in a string
replace_result = re.sub(r'\d+', 'X', 'abc123def456')
print(f"Replace Result: {replace_result}")

# 5. Split a string based on a pattern
split_result = re.split(r'\d+', 'a1b2c3d4')
print(f"Split Result: {split_result}")



#Files

#To extract data from multiple CSV files, aggregate the data, and generate a summary report. For example, you could extract sales data from multiple CSV files, calculate total sales for each product, and generate a report with product-wise sales.

import os
import csv

# Step 1: Get the current working directory
script_directory = os.getcwd()

# Step 2: Create an empty dictionary to store aggregated data
aggregated_data = {}

# Step 3: Loop through each CSV file in the script directory
for filename in os.listdir(script_directory):
    if filename.endswith(".csv"):
        # Step 4: Open and read the CSV file
        with open(os.path.join(script_directory, filename), 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Step 5: Process each row in the CSV file
            for row in csv_reader:
                product = row['Product']
                sales = float(row['Sales'])

                # Step 6: Aggregate data in the dictionary
                if product in aggregated_data:
                    aggregated_data[product] += sales
                else:
                    aggregated_data[product] = sales

# Step 7: Generate a summary report
print("Product-wise Sales Summary:")
for product, total_sales in aggregated_data.items():
    print(f"{product}: ${total_sales:.2f}")


#To read JSON data, validate it against a schema, and clean the data by removing or modifying invalid entries. For example, you could validate user data against predefined rules and generate a clean dataset. File contains 10 key value pairs, out of which we need only 5 mandatory key-value pairs and we have to convert the values to appropriate datatypes.
    
#data.json
# {
#     "name": "Hanisha",
#     "age": 20,
#     "email": "hani@example.com",
#     "address": "731 Main St",
#     "city": "Banglore",
#     "country":"India",
#     "is_student": True,
#     "grades": [85, 92, 78],
#     "phone": "9876504321",
#     "is_employed": False
# }

import json

# Define the schema with 5 mandatory key-value pairs and their data types
schema = {
    "name": str,
    "age": int,
    "email": str,
    "address": str,
    "is_student": bool
}

# Read JSON data from file
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)

# Validate and clean the JSON data against the schema
cleaned_data = {}
for key, data_type in schema.items():
    if key in json_data and isinstance(json_data[key], data_type):
        cleaned_data[key] = json_data[key]

# Display the cleaned data
print("Cleaned Data:")
print(json.dumps(cleaned_data, indent=2))



#Databases

#CURD Operation for both sql and nosql database

#sql - using sqlite3 module

import sqlite3

# Connect to SQLite database (creates a new database if not exists)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        age INTEGER
    )
''')
conn.commit()

# Create (INSERT)
cursor.execute("INSERT INTO users (username, age) VALUES (?, ?)", ('harshini', 20))
conn.commit()

# Read (SELECT)
cursor.execute("SELECT * FROM users")
print("Read:")
print(cursor.fetchall())

# Update (UPDATE)
cursor.execute("UPDATE users SET age=? WHERE username=?", (25, 'harshini'))
conn.commit()

# Read after update
cursor.execute("SELECT * FROM users")
print("Read after Update:")
print(cursor.fetchall())

# Delete (DELETE)
cursor.execute("DELETE FROM users WHERE username=?", ('harshini',))
conn.commit()

# Read after delete
cursor.execute("SELECT * FROM users")
print("Read after Delete:")
print(cursor.fetchall())

# Close SQLite connection
conn.close()

#nosql - using dict


#Create a Python dictionary as a NoSQL database
db_nosql = {}

# Create
db_nosql['user1'] = {'name': 'Hani', 'age': 20}

# Read
print("NoSQL (Python Dictionary) Read:")
print(db_nosql)

# Update
db_nosql['user1']['age'] = 25

# Read after update
print("NoSQL (Python Dictionary) Read after Update:")
print(db_nosql)

# Delete
del db_nosql['user1']

# Read after delete
print("NoSQL (Python Dictionary) Read after Delete:")
print(db_nosql)



