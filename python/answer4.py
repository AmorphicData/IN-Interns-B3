def para_ops(para):
    
    words=para.split()
    number_of_words=len(words)
    print(number_of_words)
    
    longest_word_len=max(words,key=len)
    print(longest_word_len)
    
    word_freq={}
    for word in words:
        word_freq[word]=word_freq.get(word,0)+1
    for word,freq in word_freq.items():
        print(f"{word},{freq}")

input("Enter your Paragraph Press Enter to go to next Line")
lines=[]
while True:
    line=input()
    if not line:
        break
    lines.append(line)
    paragraph=' '.join(lines)
para_ops(paragraph)



year=int(input("enter year:"))
if(year%4==0|year%400):
    leap=True
m31=[1,3,5,7,8,10,12]
m30=[4,6,9,11]
month=int(input())
count=28
if(month in m31):
    count=31
if(month in m30):
    count=30
if(month==2):
    if(leap):
        count=29

day=1 
while (day<=count):
    print(day,"/", month,"/",end="    ")
    day=day+1


def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

def main():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /) or 'exit' to quit: ")
        if operator == 'exit':
            print("Exit Pressed")
            break
        result = calculator(num1, num2, operator)
        print("Result:", result)


main()

import random
final_pass=""
count=0
lenght_of_pass=int(input())
while(count<lenght_of_pass):
    random_char=chr(random.randint(32, 126))
    final_pass+=random_char
    count+=1
print(final_pass)


import random
def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = -1
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
        print(f"Sorry, you have used up all your attempts.")
guess_the_number()

