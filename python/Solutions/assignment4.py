#Write a program that reads a string (paragraph) and performs various text analysis tasks such as counting the number of words, counting the frequency of each word, finding the longest word, etc.

def paragraph(para):
    new_para = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in para)

    words = new_para.split()

    word_count = len(words)
    print(f"Word count: {word_count}")

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    print("Word frequency:", freq)

    longest = max(words, key=len)
    print(f"Longest word: {longest}")

para = "We will try with this code. Code checking. Gonna try it."
paragraph(para)

#Write a program that generates random passwords of a given length using uppercase letters, lowercase letters, numbers, and special characters

import random

def password(length):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    spl_chr = '!@#$%^&*()_-+=<>?'

    all_chr = upper + lower + num + spl_chr

    if length < 8:
        print("Password length should be at least 8 characters. Generating an 8-character password.")
        length = 8

    pwd = ''.join(random.choice(all_chr) for _ in range(length))
    
    return pwd

length = int(input("Desired password length: "))
password = password(length)
print(f"Generated Password: {password}")

#Write a program that generates a random number between 1 and 100 and prompts the user to guess the number. The program should provide feedback on whether the guess is too high or too low and allow the user to continue guessing until they either guess the correct number or exceed a certain number of attempts.

import random

def guess():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = int(input("Enter max number of attemps: "))

    while attempts < max_attempts:
        guess = int(input("Guess the number (1-100): "))
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed the number.")
            break
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    else:
        print(f"Sorry! You exceeded {max_attempts} attempts. The correct number was {number}.")

guess()

#Write a simple calculator program that takes user input for arithmetic operations (+, -, *, /) and performs the calculations. Use loop to continuously prompt the user for input until they choose to exit the program, and include error handling to handle invalid inputs.

def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator: ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                print("Invalid operator. Please enter +, -, *, or /.")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        finally:
            exit = input("Do you want to exit? (yes/no): ").lower()
            if exit == 'yes':
                break

calculator()

#Write a program that generates a calendar for a specified month and year.

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print(cal)

# Write a program that simulates a banking system where users can deposit, withdraw, and transfer funds between accounts. Use loop to continuously prompt the user for actions until they choose to exit.

accounts = {}

def display(acc):
    print(f"Balance for {acc}: ${accounts[acc]}")

while True:
    print("Banking System Menu: \n1. Deposit\n2. Withdraw\n3. Transfer\n4. Display Balance\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        acc = input("Enter account name: ")
        amount = float(input("Enter the deposit amount: "))
        accounts[acc] = accounts.get(acc, 0) + amount
        print(f"Deposited ${amount} to {acc}'s account.")

    elif choice == '2':
        acc = input("Enter account name: ")
        amount = float(input("Enter the withdrawal amount: "))
        if amount <= accounts[acc]:
            accounts[acc] -= amount
            print(f"Withdrew ${amount} from {acc}'s account.")
        else:
            print("Insufficient funds.")

    elif choice == '3':
        from_acc = input("Enter your account name: ")
        to_acc = input("Enter recipient account name: ")
        amount = float(input("Enter the transfer amount: "))
        if amount <= accounts[from_acc]:
            accounts[from_acc] -= amount
            accounts[to_acc] += amount
            print(f"Transferred ${amount} from {from_acc} to {to_acc}.")
        else:
            print("Insufficient funds for the transfer.")

    elif choice == '4':
        acc = input("Enter account name: ")
        display(acc)

    elif choice == '5':
        print("Exiting the Banking System.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
