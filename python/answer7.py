import calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /) or 'exit' to quit: ")
if operator == 'exit':
    print("Exit Pressed")
result = calculator.cal(num1, num2, operator)
print("Result:", result)

import shapes.circles,shapes.rectangles

ask=input("circle or rectangle ")
if ask == 'circle':
    radius=float(input('input a value for radius of the circle '))
    ask2=input("area or perimeter ")
    if ask2 == 'area':
        ans=shapes.circles.circle_area(radius)
        print(ans)
    elif ask2 == 'perimeter':
        ans=shapes.circles.circle_perimeter(radius)
        print(ans)
elif ask == 'rectangle':
    l=float(input("enter length "))
    b=float(input("enter breadth "))
    ask2=input("area or perimeter ")
    if ask2 == 'area':
        ans=shapes.rectangles.rectangle_area(l,b)
        print(ans)
    elif ask2 == 'perimeter':
        ans=shapes.rectangles.rectangle_perimeter(l,b)
        print(ans)
        

import os
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

files_and_dirs = os.listdir()
print("Files and Directories:", files_and_dirs)

os.mkdir("Agam")

os.rmdir("Agam")

os.remove("text.txt")

import sys
print(sys.version)

print("Command-line arguments:", sys.argv)

print("Platform:", sys.platform)

sys.stdout.write("Hello, world!\n")

sys.exit(0)

from datetime import datetime
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

date_string = "2024-02-20"
formatted_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Formatted Date:", formatted_date)

from datetime import timedelta
duration = timedelta(days=5, hours=3)
print("Duration:", duration)

current_datetime = datetime.now()
day_of_week = current_datetime.weekday()
print("Day of the Week (0=Monday, 1=Tuesday, ...):", day_of_week)

from collections import Counter
word_counts = Counter(["apple", "banana", "apple", "orange", "banana"])
print("Word Counts:", word_counts)

from collections import defaultdict
fruit_inventory = defaultdict(int)
fruit_inventory["apple"] = 10
print("Fruit Inventory:", fruit_inventory)

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print("Point:", p)

from collections import deque
queue = deque([1, 2, 3], maxlen=3)
print("Queue:", queue)

import re
#re Modules in Python provide Support for working with Regular Expression which is PowerFul tool for Pattern Matching and Text Processing
pattern=r'hello'
string='hello world'
match=re.match(pattern,string)
if match:
    print("Matches Found")
else:
    print("Match Not Found")
#for Search
pattern=r'world'
string='hello world'
match=re.search(pattern,string)
if match:
    print("Yes Pattern is found in String")
else:
    print("No Pattern is Not found")
#non overlapping string
pattern = r'hello'
string = 'hello hello world'
matches = re.findall(pattern, string)
print("All matches:", matches)
#re.sub(pattern, replacement, string): Replaces occurrences of the pattern in the string with the replacement.
pattern = r'\d+'
string = 'Today is 2024-02-20'
replacement = 'YYYY-MM-DD'
new_string = re.sub(pattern, replacement, string)
print("New string:", new_string)
#re.compile(pattern): Compiles a regular expression pattern into a pattern object, which can be used for matching.
pattern = re.compile(r'hello')
string = 'hello world'
match = pattern.match(string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import csv
def aggregate_sales(csv_files):
    product_sales={}
    for file in csv_files:
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = row['Product']
                sales = int(row['Sales'])
                if product in product_sales:
                    product_sales[product] += sales
                else:
                    product_sales[product] = sales
    return product_sales
def generate_report(product_sales):
    print("\nProduct-wise Sales Summary, no. of products sold: \n")
    total_sales = 0
    for product, sales in product_sales.items():
        print(f"{product}: {sales}")
        total_sales += sales
    print("\n")
    print(f"Total Sales in number: {total_sales}")
csv_files = ['product1.csv', 'product2.csv']
product_sales = aggregate_sales(csv_files)
generate_report(product_sales)

import json
#for Validation
needed_keys={'name','age','email','address','phone'}
#function to clean and validate json data
def validate(json_data):
    cleaned_data=[]
    for entry in json_data:
        cleaned_entry={}
        for key in needed_keys:
            if key in entry:
                
                if key=='age':
                    try:
                        
                        cleaned_entry[key]=int(entry[key])
                    except ValueError:
                        print(f"Invalid format of age value '{entry[key]} for enrty:{entry}")
                        break
                elif key=='phone':
                    # Remove non-numeric characters from phone number
                    cleaned_entry[key] = ''.join(filter(str.isdigit, entry[key]))
                else:
                    
                    cleaned_entry[key]=entry[key]
            else:
                print(f"Missing mandatory key '{key}' for entry: {entry}")
                break
        if len(cleaned_entry) == len(needed_keys):
         cleaned_data.append(cleaned_entry)
    return cleaned_data
def main():
    with open('haha.json','r')as file:
        data=json.load(file)
    
    cleaned=validate(data)
    for enrty in cleaned:
        print(enrty)
if __name__=="__main__":
    main()



import sqlite3
#to Set up the connection
def create_connection(database):
    conn=None
    try:
        conn=sqlite3.connect(database)
        print("Connected to Data Base")
    except sqlite3.Error as e:
        print(e)
    return conn
#now i have to create Table
def create_table(conn):
    try:
        cursor=conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT
            )
        ''')
        print("Table Created")
    except sqlite3.Error as e:
        print(e)
def insert_record(conn,name,age,email):
    try:
        cursor=conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, age, email) VALUES (?, ?, ?)
        ''', (name, age, email))
        conn.commit()
        print("Record Inserted Successfully")
    except sqlite3.Error as e:
        print(e)
def read_data(conn):
    try:
        cursor=conn.cursor()
        cursor.execute('Select * From users')
        rows=cursor.fetchall()
        print("Records")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
def update_record(conn, user_id, name, age, email):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users SET name=?, age=?, email=? WHERE id=?
        ''', (name, age, email, user_id))
        conn.commit()
        print("Record updated successfully")
    except sqlite3.Error as e:
        print(e)
def delete_record(conn,user_id):
    try:
        cursor=conn.cursor()
        cursor.execute('''
            DELETE FROM users WHERE id=?
        ''', (user_id,))
        conn.commit()
        print("Deleted success")
    except sqlite3.Error as e:
        print(e)
def main():
    database="sample.db"
    connect=create_connection(database)
    if connect is not None:
        create_table(connect)
        #now if i want to insert a record
        insert_record(connect,"agam kapoor",22,"sandesh4agamaagaaz@gmail.com")
        insert_record(connect,"maddy",21,"madhavan@gmail.com")
        #Read all data matlab Select Statement
        read_data(connect)
        #Update Record
        update_record(connect,1,"himani",21,"himani@gmail.com")
        #read data
        read_data(connect)
        #delete Record
        delete_record(connect,1)
        #Read Data
        read_data(connect)
        connect.close()
        print("Connection Closed")
if __name__=="__main__":
    main()