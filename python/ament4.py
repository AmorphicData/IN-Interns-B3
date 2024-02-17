import random
'''def take_paragraph_input():
    print("Enter a paragraph (type 'end' on a new line to finish):")

    paragraph_lines = []
    while True:
        line = input()
        if line.lower() == 'end':
            break
        paragraph_lines.append(line)

    paragraph = '\n'.join(paragraph_lines)
    return paragraph



fre_dict={}
max_word=""
count=0
def traverse(para):
    lines=para.split('\n')
    global count
    
    global max_word
    global fre_dict
    for line_number, line in enumerate(lines, start=1):
       li=line.split()
       
       for i in li:
           j=i.strip('.,!?').lower()
           count=count+1
           if(len(j)>len(max_word)):
               max_word=j
           fre_dict[j]=fre_dict.get(j,0)+1

    return
para = take_paragraph_input()
traverse(para)
print(count)
print(max_word)
for key,value in fre_dict.items():
    print(f"frequency of {key} is {value}")
print(fre_dict)
#random password
s=""
len=int(input())
count=0
while(count<len):
    random_char = chr(random.randint(32, 126))
    s+=random_char
    count+=1
print(s)
pattern=""
s=input()
fre_dict={}
for i in range(1,len(s)):
    lim=len(s)-i
    for j in range(0,lim+1):
        fr=fre_dict.get(s[j:(j+i)],0)
        if(fr>0&len(pattern)<i):
            pattern=s[j:(j+i)]
        fre_dict[s[j:(j+i)]]=fr+1
print(pattern)
year=int(input())
leap=False
if(year%4==0):
      if(year%100==0):
            leap=True if year%400==0 else False
      else:
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
        
co=0
day=1
while(day<=count):
    print(day,"/",month,"/",year,end="     ")
    co=co+1
    if(co==4):
        print("\n")
        co=0
    day=day+1

r_n=random.randint(1,100)

lim=10
c=0
while(c<lim):
     u_n=int(input())
     if(u_n==r_n):
        print("Correct Guess")
        break
     else:
        if(u_n>r_n):
            print("Guess is too high")
            
        else:
            print("Guess is too low")
        c+=1  '''  
         

# l=input().split(',')
# print(l)
        
           

