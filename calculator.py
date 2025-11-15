"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b

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
