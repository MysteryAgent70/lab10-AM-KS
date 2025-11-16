#https://github.com/MysteryAgent70/lab10-AM-KS
#Partner 1: Keshanta Smith
#Partner 2: Angel Moreno

import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take square root of a negative number")
def hypotenuse(a, b):
        return math.hypot(a, b)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Invalid arguments for logarithm")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
