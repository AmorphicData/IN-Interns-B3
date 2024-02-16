#Q1
def operation_para(para):
    #count the number of words
    words=para.split()#split hamesha list me daalega and iska default argument is space
    number_of_words=len(words)
    print(number_of_words)
    #find the longest word
    longest_word_len=max(words,key=len)#this will find the maximum by using length as key
    print(longest_word_len)
    ##{} yeh dict hai 
    #word freq
    word_freq={}
    for word in words:
        word_freq[word]=word_freq.get(word,0)+1
    for word,freq in word_freq.items():
        print(f"{word},{freq}")
    #most common word
    most_common_word=max(word_freq,key=word_freq.get)
    print(most_common_word)

input("Enter your Paragraph Press Enter to go to next Line")
lines=[]
while True:
    line=input()
    if not line:
        break
    lines.append(line)
    paragraph=' '.join(lines)

print(paragraph)
operation_para(paragraph)

#Q8
def display(inventory):
    print("Current Inventory")
    for item,quant in inventory.items():
        print(f"{item},{quant}")
def add(inventory):
    item=input("Enter the item you want to add")
    quant=int(input("Enter the quantity you want to add"))
    inventory[item]=inventory.get(item,0)+quant
    print(f"{quant},{item}(s) are added")
def remove(inventory):
    item=input("Enter the item you want to remove")
    if item in inventory:
        del inventory[item]
        print(f"{item} is deleted")
    else:
        print("Item does not exists")
def update(inventory):
    item=input("Enter the item you want to update")
    if item in inventory:
        quant=int(input("Enter the quantity you want to update"))
        inventory[item]=quant
        print(f"Inventory updated: {item} quantity set to {quant}.")
    else:
        print("Item not found in directory")
def main():
    inventory={}
    while True:
        print("\nOpions Avaialbe")
        print("1. Display Inventory")
        print("2. Add element in Inventory")
        print("3. Removing Element from Inventory")
        print("4. Update Item")
        print("5. Exit")

        choice=int(input("Enter your choice (1-5)"))
        if choice==1:
            display(inventory)
        elif choice==2:
            add(inventory)
        elif choice==3:
            remove(inventory)
        elif choice==4:
            update(inventory)
        elif choice==5:
            print("Exiting program")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()

#Q7
class BankAccount:
    def __init__(self,account_number,balance=0):
        self.account_number=account_number
        self.balance=balance #In Python, self is a reference to the current instance of the class.
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited ${amount}. New Balance ${self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdraw ${amount}. New Balance ${self.balance}")
        else:
            print("insufficient Funds")
    def transfer(self,amount,reciever):
        if amount<=self.balance:
            self.balance-=amount
            reciever.balance+=amount
            print(f"Transferred ${amount} to account {reciever.account_number}. Your balance: ${self.balance}")
        else:
            print("Insufficient Funds")
    def get_balance(self):
        return self.balance
def main():
    account1=BankAccount(account_number=1234,balance=10000)
    account2=BankAccount(account_number=4567,balance=20000)
    while True:
        print("\Options")
        print("1. Deposit")
        print("2. WithDraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Exist")
        choice=int(input("Enter your Choice: "))
        if choice==1:
            amount=float(input("Enter the amount you want to add"))
            account1.deposit(amount)
        elif choice==2:
            amount=float(input("Enter the amount you want to Withdraw"))
            account1.withdraw(amount)
        elif choice==3:
            amount=float(input("Enter the amount you want to transfer"))
            reciever_account_no=int(input("Enter the Reciever account number"))
            reciever=account2 if reciever_account_no==account2.account_number else account1
            account1.transfer(amount,reciever)
        elif choice==4:
            print(f"your balance: ${account1.get_balance}")
        elif choice==5:
            print("Existing Program")
            break
        else:
            print("Invalid Choice")

if __name__=="__main__":
    main()


#Q6
def find_answer(number1,opr,number2):
    if opr=='+':
        return number1+number2
    elif opr=='-':
        return number1-number2
    elif opr=='*':
        return number1*number2
    elif opr=='/':
        if number2!=0:
            return number1/number2
        else:
            print("Zero Division Error")
    else:
        print("Inavlid Operator")
def main():
    while True:
        try:
            expression=input("Enter Valid Experssion e.g 5+3: ")
            if expression.lower()=='exit':
                print("Existing Program")
                break
            number1,operator,number2=expression.split()
            number1=float(number1)
            number2=float(number2)
            ans=find_answer(number1,operator,number2)
            print("Answer: ",ans)
        except ValueError:
            print("Error Inavlid Input")
        except ZeroDivisionError:
            print("Error Cannot Divide by Zero")
        except Exception as e:
            print("Error Occoured")

if __name__=="__main__":
    main()

#Q5
import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            break
        
        attempts += 1
    if attempts == max_attempts:
        print(f"Sorry, you have used up all your attempts. The correct number was {secret_number}.")

guess_the_number()


#Q3
import calendar

def generate_calendar(year, month):
    # Generate the calendar for the specified month and year
    cal = calendar.month(year, month)
    return cal

year = int(input("Enter the year (e.g., 2022): "))
month = int(input("Enter the month (1-12): "))

if 1 <= month <= 12:
    calendar_output = generate_calendar(year, month)
    print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
    print(calendar_output)
else:
    print("Invalid month. Please enter a number between 1 and 12.")


