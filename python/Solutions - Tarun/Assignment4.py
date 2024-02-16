#Write a program that reads a string (paragraph) and performs various text analysis 
#tasks such as counting the number of words, counting the frequency of each word, finding the longest word, etc.

print("Enter a paragraph:(use Ctrl+D to stop providing input)")

cont = []
while True:
    try:
        line = input()
    except EOFError:
        break
    cont.append(line)

para = ''.join(cont)
words = para.split()
cnt = 0
dic_word={}
for i in words:
    cnt+=1
    dic_word[i] = dic_word.get(i, 0) + 1
print("Count of words:" , cnt)
print("Count of each word:-")
for word,freq in dic_word.items():
    print(f"{word} : {freq}")

print("Longest word:", max(words, key=len))

# =============================================================================================================
# Write a program that generates random passwords of a given length using uppercase letters, 
# lowercase letters, numbers, and special characters

import string 
import random

pas = ''
l = int(input("Enter the length:"))
all_char = string.ascii_letters + string.digits + string.punctuation

pas += ''.join(random.choice(all_char) for i in range(l))
print("Password:" , pas)

# =============================================================================================================
# Write a program that generates a calendar for a specified month and year.

import calendar

y = int(input("Enter the year: "))
m= int(input("Enter the month (1-12): "))

print("Invalid" if m < 1 or m > 12 else "Generating calender.....\n")

cal = calendar.month(y, m)
print(f"Calendar for {calendar.month_name[m]} {y}:\n")
print(cal)

# =============================================================================================================
# Write a program that generates a random number between 1 and 100 and prompts the user 
# to guess the number. The program should provide feedback on whether the guess is too high 
# or too low and allow the user to continue guessing until they either guess the correct number or exceed a certain number of attempts.

import random

target_number = random.randint(1, 100)
print("Enter a number between 1 and 100. \n")

for attempt in range(10):
    user_guess = int(input("Enter your guess: "))
    if user_guess == target_number:
        print("Correct guess")
        break
    elif user_guess < target_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    if attempt == 9:
        print("Max attempt reached")

# =============================================================================================================
# Create a program that manages inventory for a store. Use loop to continuously prompt the user 
# for actions such as adding, updating, or removing items from the inventory.
        
inventory = {}

def show_inv():
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    print()

def add_item():
    it_name = input("Enter item name: ")
    quant = int(input("Enter quantity: "))
    if it_name in inventory:
        inventory[it_name] += quant
    else:
        inventory[it_name] = quant

def updt_item():
    it_name = input("Enter item name: ")
    if it_name in inventory:
        new_quant = int(input("Enter new quantity: "))
        inventory[it_name] = new_quant
    else:
        print(f"{it_name} not found in inventory.")

def rmv_item():
    it_name = input("Enter item name: ")
    if it_name in inventory:
        del inventory[it_name]
    else:
        print(f"{it_name} not found in inventory.")

while True:
    print("Available Operations:")
    print("1. Show Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        show_inv()
    elif choice == '2':
        add_item()
    elif choice == '3':
        updt_item()
    elif choice == '4':
        rmv_item()
    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice!")