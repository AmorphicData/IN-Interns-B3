#Modules and Packages

#Q1 Calculator

calculator.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a/b
    else:
        try:
            y=a/b
        except ZeroDivisionError:
            print("Can not divide by zero")

import calculator as c
print("Calculate: ")
x=c.add(5,4)
print("Addition of 5 and 4 is: ",x)
y=c.sub(7,3)
print("Subtraction of 7 and 3 is: ",y)
a=c.mul(2,4)
print("Multiplication of 2 and 4 is: ",a)
b=c.div(10,5)
print("Division of 10 by 5 is: ",b)
d=c.div(10,0)
print("Division of 10 by 0 is: ",d)

#Q2 Shapes

area.py

import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length,breadth):
    return length*breadth

perimeter.py

import math

def perimeter_circle(radius):
    return 2*math.pi * radius

def perimeter_rectangle(length,breadth):
    return 2*(length+breadth)

import shapes.area as a, shapes.perimeter as p
c1=a.area_circle(4)
c2=p.perimeter_circle(4)
print(f"Area and Perimeter of Circle is: {c1}, {c2}")
r1=a.area_rectangle(5,7)
r2=p.perimeter_rectangle(5,7)
print(f"Area and Perimeter of Circle is: {r1}, {r2}")

#Q3 Various functionalities of the following modules os, sys, datetime, collections and re.

import os
import sys
import datetime
import collections
from collections import Counter
import re

def os_module_functions():

    # 1. Get the current working directory
    print("Current Working Directory:", os.getcwd())

    # 2. List files and directories in a directory
    print("Files and Directories in Current Directory:")
    print(os.listdir())

    # 3. Create a new directory
    new_dir_name = "learning"
    os.mkdir(new_dir_name)
    print(f"Directory '{new_dir_name}' created successfully")

    # 4. Rename a file or directory
    os.rename(new_dir_name, "renamed_directory")
    print(f"'{new_dir_name}' renamed to 'renamed_directory'")

    # 5. Remove a file or directory
    os.rmdir("renamed_directory")
    print("'renamed_directory' removed successfully")

def sys_module_functions():

    # 1. Get the command line arguments
    print("Command Line Arguments:", sys.argv)

    # 2. Get the Python version
    print("Python Version:", sys.version)

    # 3. Get the platform information, The sys.platform attribute in Python returns a string 
    # identifying the platform (operating system) on which the Python interpreter is executing. 
    print("Platform:", sys.platform)

    # 4. Getting the maximum integer value that can be represented in Python
    print("Maximum integer value in Python:", sys.maxsize)

    # 5. Terminate the program
    sys.exit("Exiting the program...")

def datetime_module_functions():


    # 1. Get the current date and time
    print("Current Date and Time:", datetime.datetime.now())

    # 2. Format a date
    current_date = datetime.datetime.now()
    print("Formatted Date:", current_date.strftime("%d-%m-%Y"))

    # 3. Create a timedelta object: a timedelta object represents a duration, or the difference 
    # between two dates or times. It allows you to perform arithmetic operations on dates and times, 
    # such as addition or subtraction, by specifying a certain duration.

    delta = datetime.timedelta(days=7)
    print("Timedelta Object (7 days):", delta)
    print("Datetime after adding 7 days:", current_date+delta)

    # 4. Get the current year
    print("Current Year:", datetime.datetime.now().year)

    # 5. Get the day of the week
    print("Day of the Week (Monday=0):", datetime.datetime.now().weekday())

def collections_module_functions():

    # 1. use of Counter and Most Common
    # Example: Finding the most common elements in a list
    numbers = [1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 2, 3, 3, 3]
    counter = Counter(numbers)
    # Find the most common elements and their counts
    most_common = counter.most_common(3)#to find the top 3 most common elements
    print("Most common elements:", most_common)

    # 2. Count occurrences of elements in a list
    counter_example = collections.Counter([1, 2, 3, 1, 2, 1])
    print("Counter Example:", counter_example)

    # 3. Create a named tuple
    Point = collections.namedtuple('Point', ['x', 'y']) #defines a new type called Point, 
    #which has two fields named x and y
    p = Point(10, 20)#creates an instance of the Point named tuple with the values with respective values
    print("Named Tuple Example:", p)

    # 4. Create a defaultdict
    defaultdict_example = collections.defaultdict(int)
    print("Defaultdict Example:", defaultdict_example) #defaultdict(<class 'int'>, {})

    # 5. Create an OrderedDict
    #An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
    #OrderedDicts are useful when you need a dictionary that retains the order of insertion.
    ordered_dict_example = collections.OrderedDict({'a': 1, 'b': 2, 'c': 3})
    print("OrderedDict Example:", ordered_dict_example)#It shows the current state of the ordered dict
    

def re_module_functions():

    # 1. Match a pattern in a string
    pattern = r'\bcat\b'
    text = "The cat sat on the mat"
    match = re.search(pattern, text)
    if match:
        print("Pattern found:", match.group())
    else:
        print("Pattern not found")

    # 2. Find all occurrences of a pattern in a string
    matches = re.findall(r'\b\w{4}\b', "This is a sample text with some words.")
    print("All 4-letter words:", matches)

    # 3. Replace occurrences of a pattern in a string
    new_text = re.sub(r'\b\w{4}\b', '****', "This is a sample text with some words.")
    print("Replaced text:", new_text)

    # 4. Split a string based on a pattern
    parts = re.split(r'\s+', "Split this string by spaces")
    print("Split parts:", parts)

    # 5. Compile a regular expression pattern for reusing
    pattern = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
    result = pattern.search("My SSN is 123-45-6789")
    if result:
        print("SSN found:", result.group())
    else:
        print("SSN not found")

if __name__ == "__main__":
    os_module_functions()
    sys_module_functions()
    datetime_module_functions()
    collections_module_functions()
    re_module_functions()


#Files

#Q1 To extract data from multiple CSV files, aggregate the data, and generate a summary report.

import csv

sales1.csv

Product,Sales
Laptop,100
Mouse,200
Keyboard,150

sales2.csv

Product,Sales
Laptop,120
Mouse,180
Keyboard,130


# Function to read data from CSV files and aggregate sales
def aggregate_sales(csv_files):
    product_sales = {}

    for file in csv_files:
        with open(file, 'r') as csvfile:  
            reader = csv.DictReader(csvfile) # read the CSV file as a dictionary, where each row 
            #is represented as a dictionary with keys being the column headers and values 
            #being the corresponding values in that row.
            for row in reader:
                product = row['Product']
                sales = int(row['Sales'])
                if product in product_sales:
                    product_sales[product] += sales
                else:
                    product_sales[product] = sales

    return product_sales

# Function to generate summary report
def generate_report(product_sales):
    print("\nProduct-wise Sales Summary: \n")
    total_sales = 0
    for product, sales in product_sales.items():
        print(f"{product}: ${sales}")
        total_sales += sales
    print("\n")
    print(f"Total Sales: ${total_sales}")


csv_files = ['sales1.csv', 'sales2.csv']

# Aggregate sales data
product_sales = aggregate_sales(csv_files)

# Generate and print report
generate_report(product_sales)

#Q2 To read JSON data, validate it against a schema, and clean the data by removing or modifying invalid entries.

import json

# Define predefined rules for validation
mandatory_keys = {'name', 'age', 'email', 'address', 'phone'}

# Function to validate and clean JSON data
def validate_and_clean_data(json_data):
    cleaned_data = []
    
    for entry in json_data:
        cleaned_entry = {}
        for key in mandatory_keys:
            if key in entry:
                # Convert data to appropriate data types
                if key == 'age':
                    try:
                        cleaned_entry[key] = int(entry[key])
                    except ValueError:
                        print(f"Invalid age value '{entry[key]}' for entry: {entry}")
                        break
                elif key == 'phone':
                    # Remove non-numeric characters from phone number
                    cleaned_entry[key] = ''.join(filter(str.isdigit, entry[key]))
                else:
                    cleaned_entry[key] = entry[key]
            else:
                print(f"Missing mandatory key '{key}' for entry: {entry}")
                break
        
        # If all mandatory keys are present, add the cleaned entry
        if len(cleaned_entry) == len(mandatory_keys):
            cleaned_data.append(cleaned_entry)
    
    return cleaned_data

# Sample JSON data (replace this with your actual JSON data)
json_data = [
    {"name": "Kaustubh", "age": "21", "email": "kaustubh@gmail.com", "address": "Surya Royal Homes Oliva", "phone": "8234567891"},
    {"name": "Yash", "age": "21", "email": "yash@gmail.com", "address": "MG Road"},
    {"name": "Raj", "email": "raj@gmail.com", "address": "Hebbal", "phone": "9234567891"},
    {"name": "Shubham", "age": "35", "email": "shubh@gmail.com", "address": "pune", "phone": "abc-1234"},
    {"name": "Vishesh", "age": "40", "email": "vishesh@gmail.com", "phone": "abc-123124234"},
]

# Validate and clean the data
cleaned_data = validate_and_clean_data(json_data)

# Print cleaned data
print("\nCleaned Data: \n")
print(cleaned_data)


#Databases
#SQL

import sqlite3

# Connect to the database
conn = sqlite3.connect('crud_operations.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
conn.commit()

def create_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

def read_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_user(user_id, new_name, new_email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name, new_email, user_id))
    conn.commit()

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

# Example usage
create_user('Kaustubh Pandey', 'kaustubh@gmail.com')
create_user('Raj', 'raj@gmail.com')
read_users()

update_user(1, 'Yash', 'yash@gmail.com')
read_users()

delete_user(2)
read_users()

# Close connection
conn.close()

#NoSQL

from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)

# Access the database (if it doesn't exist, MongoDB will create it)
db = client['crud_operations']

# Access the collection (if it doesn't exist, MongoDB will create it)
users_collection = db['users']

def create_user(name, email):
    user_data = {'name': name, 'email': email}
    result = users_collection.insert_one(user_data)
    return result.inserted_id

def read_users():
    users = users_collection.find()
    for user in users:
        print(user)

def update_user(user_id, new_name, new_email):
    query = {'_id': user_id}
    new_values = {'$set': {'name': new_name, 'email': new_email}}
    users_collection.update_one(query, new_values)

def delete_user(user_id):
    query = {'_id': user_id}
    users_collection.delete_one(query)

# Example usage
user1_id = create_user('Kaustubh Pandey', 'kaustubh@gmail.com')
user2_id = create_user('Raj', 'raj@gmail.com')
read_users()

update_user(user1_id, 'Yash', 'yash@gmail.com')
read_users()

delete_user(user2_id)
read_users()

# Close the MongoDB connection
client.close()

