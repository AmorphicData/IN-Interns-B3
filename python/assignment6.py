#Q1
def greet(fx):
    def mfx(*args,**kwargs):
        print(f"Logging: {fx.__name__}() called with args: {args} and kwargs: {kwargs}")
        ans=fx(*args,**kwargs)
        print(f"Function:{fx.__name__}() called is finished and answer is obtained")
        return ans
    return mfx

@greet
def add(x,y):
    return x+y

ans2=add(3,5)
print(ans2)

#Q2
def greet(fx):
    def mfx(*args,**kwargs):
        #attemp=0
        max_attemp=1
        for _ in range(max_attemp):
            try:
                ans=fx(*args,**kwargs)
                return ans
            except Exception as e:
                print(f"Retry failed due to {e} . Retrying ")
    return mfx

@greet
def divide(a,b):
    return a/b

ans2=divide(6,3)
print(ans2)
ans3=divide(6,0)
print(ans3)


#Q3
user_details={"Rounak":"Rounak@123","Nayan":"Nayan@123","Saksham":"Saksham@123"}
allowed_user=['admin','manager']
def greet(fx):
    def mfx(*args,**kwargs):
        user=kwargs.get('user')
        if user in allowed_user:
            return fx(*args,**kwargs)
        else:
            raise PermissionError("Unauthorized user")
    return mfx

@greet
def info(user=None):
    print("Sensitive Information")

if __name__=="__main__":
    try:
        info(user='admin')
        info(user='clerk')
    except PermissionError as e:
        print(e)

#Q4
import time
import functools
curr=0
def greet(fx):
    def mfx(*args,**kwargs):
       max_limit_allowed=5
       global curr #it will refer to global curr and take that value
       if  curr<max_limit_allowed:
           ans=fx(*args,**kwargs)
           curr+=1
           return ans
       else:
           raise Exception("Rate Limit Exceed")
    return mfx

@greet
def fun():
    print("Heavy Tasking Ongoing")

if __name__=="__main__":
    try:
        fun()
        fun()
        fun()
        fun()
        fun()
        fun()
    except Exception as e:
        print(e)

               
#Q4 Appraoch 2
import time
def rate_limit_decorator(fx):
    last_called=[0]#use this list to call mutuable value
    def mfx(*args):
        limit_per_minute=args[0]
        curr_time=time.time()
        if curr_time-last_called[0]>=60/limit_per_minute:
            last_called[0]=curr_time
            return fx(*args)
        else:
            print("Rate Limit Exceed")
    return mfx

@rate_limit_decorator
def fun(limi):
    print("Function Called at",time.strftime("%H:%M:%S"))

if __name__=="__main__":
    limit_per=int(input("Enter Limit Per Minute:"))
    for _ in range(3):
        fun(limit_per)
        time.sleep(5)


#Q5
def input_valid_decorator(fx):
    def mfx(*args,**kwargs):
        num=args[0]
        if 1<=num<=100:
            return fx(*args,**kwargs)
        else:
            raise Exception("Invalid Input")
    return mfx

@input_valid_decorator
def input_validator(user_inp):
    print("Number is Provided to Function",user_inp)
    
if __name__=="__main__":
    try:
        num=int(input("enter a Number between 1 to 100:"))
        input_validator(num)
    except Exception as e:
        print(e)    

#Q6
import functools
def cache(fx):
    cached_result={}#empty dict
    def mfx(*args,**kwargs):
        key=(args,frozenset(kwargs.items()))#Create a unique key based on args and kwargs
        if key not in cached_result:
            #Then Calculate the Result
            cached_result[key]=fx(*args,**kwargs)
        return cached_result[key]
    return mfx

@cache
def fibonaci(n):
    if n<=1:
        return n
    return fibonaci(n-1)+fibonaci(n-2)

if __name__=="__main__":
    print(fibonaci(5))
    print(fibonaci(5))
