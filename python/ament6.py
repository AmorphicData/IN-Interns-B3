import datetime
import time

'''def log(di):
 def dec(fun):
    def wrapper(*args,**kwargs):
        st=datetime.datetime.now()
        r=fun(*args)
        en=datetime.datetime.now()
        ex=en-st
        l=[]
        name=fun.__name__
        l.append(f"Function {name} Details-")
        l.append(f"Start time={st}")
        l.append(f"End time={en}")
        l.append(f"exec time={ex}")
        l.append(f"Result was={r}")
        di[f"{name}"]=l
        p=[]
        lis=[]
        for key,value in di.items():
             lis.append(f"{key}:{value}")
             lis.append("#########################################")
        p='\n'.join(lis)
        return p
    return wrapper
 return dec

di={}  
@log(di)
def s_h():
    return "Hello" 

@log(di)
def h_f():
      return "hello"

@log(di)
def add(*args):
      sum=0
      for i in args:
            sum+=i
      return sum

r=add(1,2,4)
print(s_h())
print(h_f())
print(r)'''
#Q-2 RE-TRY
# def dec(max_attempt):
#  def greet(fx):
#     def d2(*args,**kwargs):
#         #attemp=0
#         max_a=max_attempt
#         for _ in range(max_a):
#             try:
#                 ans=fx(*args,**kwargs)
#                 return ans
#             except Exception as e:
#                 print(f"Retry failed due to {e} . Retrying ")
#     return d2
#  return greet
# @dec(4)
# def divide(a,b):
#     return a/b
# ans2=divide(6,3)
# print(ans2)
#Q-3
# def dec(di):
#     def auth(fun):
#         def wr(*args,**kwargs):
#                 nam=kwargs.get('name')
#                 pas=kwargs.get('pasw')
#                 ps=di.get(nam)
#                 # print(nam)
#                 # print(pas)
#                 # print(ps)
#                 if(ps==pas):
#                      return fun(*args,**kwargs)
#                 else:
#                      raise PermissionError('Unauthorised User')
#         return wr
#     return auth
# di={}
# di['Raj']='1234**'
# di['Ram']='*&^%12'
# @dec(di)
# def auth(**kwargs):
#      try:
#          return "Successfuly loggedin"
#      except PermissionError as e:
#            print(e)
# try:
#  d=auth(name='Raj',pasw='123**')
#  print(d)
# except Exception as e:
#  print(e)
#Q-4
# till=0
# l=0
# r=0
# def d1(lim):
#   ls=[0]
#  def d2(fun):
    
    
#     def d3(*args):
#         limit=lim
        
#         cr=time.time()
#         if(cr-ls[0]>=(60/limit)):
#             ls[0]=cr
#             return fun(*args)
#         else:
#             return "Error"
#     return d3
#  return d2
# @d1(6)
# def fun(lim=None):
#     return ("Fun called at" ,time.strftime("%H:%M;%S"))
# d=fun()

# d1=fun()
# print(d)
# print(d1)
##################################################
#Q-4 Approach 2
# till=0
# l=0
# r=0
# def d1(lim):
#  def d2(fun):
    
#     ls=[0]
#     def d3(*args):
#         global till
#         global l
#         global r
#         if(till==lim):
#           cur=time.time()
#           at=ls[l]+60
#           print("Stopped for now")
#           while(cur<at):
#             cur=time.time()
#             time.sleep(1)
#           ls.append(time.time())
#           r+=1
#           return fun(*args)


#         else:
#             cur=time.time()
              
#             if(cur-ls[l]>=60):
#                 l+=1
#                 till-=1
#             ls.append(cur)
#             r+=1
#             till+=1
#             return fun(*args)

#     return d3
#  return d2
# @d1(6)
# def fun(lim=None):
#     return ("Fun called at" ,time.strftime("%H:%M;%S"))
# d=fun()

# d1=fun()
# for i in range(1,8):
#    print(fun())
#    time.sleep(1)

#Q-6
# def d1(di):
#     def d2(fun):
#         def d3(n):
#             if(di.get(n,0)!=0):
#                 print(f"Got {n} and its cached value {di[n]}")
#                 return di[n]
#             else:
#                  di[n]= fun(n)
#                  return di[n]
#         return d3
#     return d2
# di={}
# @d1(di)
# def fac(n):
#     if(n==0):
#         return 1
#     return n*fac(n-1)

# print(fac(6))
# print(fac(7))
#Q-5
# def d1(fx):
#     def d2(*args):
#         num=args[0]
#         if (num>=1&num<=100):
#             return fx(*args)
#         else:
#             raise  Exception("Invalid Input")
#     return d2

# @d1
# def i_v(user_inp):
# try:
#     return ("Input Number",user_inp)
# except Exception as e:
#       return e   

# try:
#         num=int(input("enter a Number between 1 to 100:"))
#         print(i_v(num)) 
# except Exception as e:
#         print(e) 


          





