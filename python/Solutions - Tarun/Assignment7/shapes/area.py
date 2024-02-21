import math

def circleA(r):
    return math.pi*(r**2)

def squareA(s):
    return s**2

def triangleA(a,b,c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def rectangleA(l,b):
    return l*b