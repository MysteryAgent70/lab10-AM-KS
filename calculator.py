"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#Partner 1: Keshanta Smith
#Partner 2: Angel Moreno

import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a * b

def fiv(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Invalid arguments for logarithm")
    return math.log(b, a)
def exp(a, b):
    return a ** b


