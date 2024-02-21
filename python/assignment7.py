#Q1
import calculator
def main():
    number1=int(input("Enter Number1:"))
    number2=int(input("Enter Number2:"))
    operator=input("Mention the Operator You Want to use:")
    if operator=="+":
        ans=calculator.add(number1,number2)
        return ans
    elif operator=="-":
        ans=calculator.diff(number1,number2)
        return ans
    elif operator=="*":
        ans=calculator.multiply(number1,number2)
        return ans
    elif operator=="/":
        try:
            ans=calculator.divide(number1/number2)
            return ans
        except Exception as e:
            print(f"Retry Failed due to {e}")
    else:
        print("Invalid Input")


if __name__=="__main__":
    answer=main()
    print(answer)

#Q2
import shapes.circle as fig1,shapes.rectangle as fig2
def main():
    shape=input("Enter The Shape you want to calculate:")
    if shape=="circle":
        radius=int(input("Enter The Radius:"))
        choice=input("Enter Whether you want area/permiter:")
        if choice=="area":
            ans=fig1.area(radius)
            return ans
        elif choice=="perimeter":
            ans=fig1.perimeter(radius)
        else:
            print("Wrong choice")
    elif shape=="rectangle":
        length=int(input("Enter the length:"))
        width=int(input("Enter your width:"))
        choice=input("Enter Whether you want area/permiter:")
        if choice=="area":
            ans=fig2.area(length,width)
            return ans
        elif choice=="perimter":
            ans=fig2.perimeter(length,width)
            return ans
        else:
            print("Wrong choice")
    else:
        print("Wrong figure")
if __name__=="__main__":
    answer=main()
    print(answer)

#Q3 OS MODULE
import os
#to get the current working directory
current_dir=os.getcwd()
print("Current Directory:",current_dir)

#to List file and directory in the current directory
file_list=os.listdir(current_dir)
print("Files and Directory in current Directory:",file_list)

#Check if the file is there or not
file_path=os.path.join(current_dir,'sample.txt')
if os.path.exists(file_path):
    print("File Exists:",file_path)

#to know the Size of File
file_size=os.path.getsize(file_path)
print("File Size:",file_size,"bytes")

#to Remove the File
os.remove(file_path)
print("File is Removed")

#Q3 SYS module
import sys

# #print the python version
print("Python Version:",sys.version)

# #print platform information
print("Platform Information",sys.platform)

# #Maximum Integer Size
print("Maximum Integer size:",sys.maxsize)


# #Interacting with Interperator
# #Reading standord input
data=sys.stdin.readline()
print("Input:",data)

# #Writing Standor Output
sys.stdout.write("Hello My Name is Rounak\n")

# #Writing Standor Error
sys.stderr.write("Error Please Try Again")

#Memory 

#Getting Memory of The object
print("Memory Size:",sys.getsizeof([1,2,3]))

#Q3 DateTime
import datetime

#to get the current time and date
curr=datetime.datetime.now()
print("Current Time",curr)

#create a date object for a specific date
d=datetime.date(2022,2,16)
print("Specific Date",d)

#create a time object for a specific time
t=datetime.time(12,30,0)
print("Specific Time",t)

#Reprsent duration between  two dates
duration=datetime.timedelta(days=5,seconds=3600)
print("Duration:",duration)

# Parse a string representing a date and time
date_str = "2024-02-20 12:00:00"
parsed_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_datetime)


#Q3 collections Module
from collections import namedtuple,deque,Counter,OrderedDict,defaultdict

#named Tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("Named tuple:", p)
print("Accessing named tuple fields:", p.x, p.y)

# deque
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print("Deque:", d)
print("Deque length:", len(d))
print("Deque pop:", d.pop())
print("Deque pop left:", d.popleft())

# Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)
print("Word counts:", word_counts)
print("Most common word:", word_counts.most_common(1))

# OrderedDict
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("OrderedDict:", d)
print("Keys in OrderedDict:", list(d.keys()))

# defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print("Defaultdict:", d)
print("Accessing key not present in defaultdict:", d['c'])
print("Defaultdict after accessing key not present:", d)

#Q3 re Module
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

#Files
#Q1 CSV
import csv
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

#Q2 JSON ONE
import json
#Define pre defined rules for Validation
needed_keys={'name','age','email','address','phone'}

#now i will create a function to clean and validate json data
def validate(json_data):
    cleaned_data=[]
    for entry in json_data:
        cleaned_entry={}
        for key in needed_keys:
            if key in entry:
                #now i will convert
                if key=='age':
                    try:
                        #now i will convert to appropriate data type
                        cleaned_entry[key]=int(entry[key])
                    except ValueError:
                        print(f"Invalid format of age value '{entry[key]} for enrty:{entry}")
                        break
                elif key=='phone':
                    # Remove non-numeric characters from phone number
                    cleaned_entry[key] = ''.join(filter(str.isdigit, entry[key]))
                else:
                    #Seedha String me convert ho jayega
                    cleaned_entry[key]=entry[key]
            else:
                print(f"Missing mandatory key '{key}' for entry: {entry}")
                break
        
        if len(cleaned_entry) == len(needed_keys):
         cleaned_data.append(cleaned_entry)
    
    return cleaned_data

def main():
    with open('data.json','r')as file:
        data=json.load(file)
    
    # data = json_data
    #print(data)
    cleaned=validate(data)
    for enrty in cleaned:
        print(enrty)
if __name__=="__main__":
    main()


#SQl Database
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
        insert_record(connect,"Rounak Chauhan",22,"rounak@gmail.com")
        insert_record(connect,"tarun",21,"tarun@gmail.com")
        #Read all data matlab Select Statement
        read_data(connect)
        #Update Record
        update_record(connect,1,"Saksham Dhillon",21,"saksham@gmail.com")
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