from math import *


# def add(num1, *args):
#     return num1 + int(sum(args))

def add(*args):
    addition = sum(args)
    return addition


def subtract(num1, *args):
    subtraction = num1 - sum(args)
    return subtraction


def multiply(*args):
    multiplication = 1
    for arg in args:
        multiplication *= arg
    return multiplication


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2)


def square(*num1):
    # Needs only one argument
    squared = []
    for num in num1:
        squared += [num ** 2]   # return num1 * num1
    return squared


def cube(*num1):
    # Needs only one argument
    cubed = []
    for num in num1:
        cubed += [num ** 3]
    return cubed


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
