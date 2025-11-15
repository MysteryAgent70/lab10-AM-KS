"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
#Partner 1: Keshanta Smith
#Partner 2: Angel Moreno

import math
def square_root(a):
    try:
        return math.sqrt(a)f
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
=======
# First example
import math

def add(a, b): 
    return a + b
>>>>>>> 18e873bca20e072f879c5cf07ef0e9240577faba

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError("ZeroDivisionError")
        else:
            return b / a
    except ZeroDivisionError as error:
        return str(error)

def log(a, b):
    try:
        if a == 1 or a <= 0 or b <= 0:
            raise ValueError("ValueError")
        else:
            return math.log(b, a)
    except ValueError as error:
        return str(error)

def exp(a, b):
    return math.pow(a, b)
