#Q1 Logging

def logging(fx):
    def modifying_func(*args):
        print(f"Logging: {fx.__name__}() called with args: {args}")
        ans=fx(*args)
        return ans
    return modifying_func
@logging
def multiply(x,y):
    return x*y
ans2=multiply(1,7)
print(ans2)

#Q2 Retry Mechanism

def dec(fx):
    def mfx(*args,**kwargs):
        #attemp=0
        max_attemp=4
        for _ in range(max_attemp):
            try:
                ans=fx(*args,**kwargs)
                return ans
            except Exception as e:
                print(f"Retry failed due to {e} . Retrying ")
    return mfx
@dec
def divide(a,b):
    return a/b
ans2=divide(9,3)
print(ans2)


#Q3 Authorization

allowed_user=['admin','manager']
def dec(fx):
    def mfx(**kwargs):
        user=kwargs.get('user')
        if user in allowed_user:
            return fx(**kwargs)
        else:
            raise PermissionError("Unauthorized user")
    return mfx
@dec
def info(user=None):
    print("Sensitive Information")
if __name__=="__main__":
    try:
        info(user='admin')
        info(user='clerk')
    except PermissionError as e:
        print(e)

#Q4 Rate Limiting (Limit the number of times function being called)

curr=0
def dec(fx):
    def mfx(*args,**kwargs):
       max_limit_allowed=5
       global curr
       if  curr<max_limit_allowed:
           ans=fx(*args,**kwargs)
           curr+=1
           return ans
       else:
           raise Exception("Rate Limit Exceed")
    return mfx

@dec
def fun():
    print("all fine  within limit")

if __name__=="__main__":
    try:
        fun()
        fun()
        fun()
        fun()
        fun()
        #fun()
    except Exception as e:
        print(e)       


#Q5 Input Validation
        
def input_decorator(fx):
    def mfx(*args,**kwargs):
        num=args[0]
        if 1<=num<=10:
            return fx(*args,**kwargs)
        else:
            raise Exception("Invalid Input")
    return mfx

@input_decorator
def input_validator(user_inp):
    print("Number valid",user_inp)
    
if __name__=="__main__":
    try:
        num=int(input("enter a Number between 1 to 10:"))
        input_validator(num)
    except Exception as e:
        print(e) 

#Q6 Caching function results
        
import functools

def cache(fx):
    cached_result = {}  # empty dictionary to store cached results
    
    @functools.wraps(fx)
    def mfx(*args, **kwargs):
        key = args  # unique key based on args only, since factorial doesn't take kwargs
        if key not in cached_result:
            # Calculate the result if not already cached
            cached_result[key] = fx(*args, **kwargs)
        return cached_result[key]
    
    return mfx

@cache
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(5))  # Output: 120 (calculated and cached)
    print(factorial(5))  # Output: 120 (retrieved from cache)
