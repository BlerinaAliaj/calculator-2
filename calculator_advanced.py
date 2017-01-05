"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic_2 import *


def my_reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('No values to iterate over')

    accum_value = initializer

    for x in it:
        accum_value = function(accum_value, x)
    return accum_value


# Your code goes here

math_function = ""

while math_function != 'q':

    math_function = raw_input(">")

    tokens = math_function.split()  # input will be saved on tokens

    try:
        if tokens[0] == "+":
            sub_total = my_reduce(add, map(int, tokens[2:]))
            print add(int(tokens[1]), sub_total)

        elif tokens[0] == "-":
            print my_reduce(subtract, map(int, tokens[1:]))

        elif tokens[0] == "*":
            print my_reduce(multiply, map(int, tokens[1:]))

        elif tokens[0] == "/":
            if len(tokens) > 3:
                print "You have given me too many numbers for this function. Try again!"
            else:
                print divide(int(tokens[1]), int(tokens[2]))

        elif tokens[0] == "square":
            for item in tokens[1:]:
                print square(int(item))

        elif tokens[0] == "cube":
            for item in tokens[1:]:
                print cube(int(item))

        elif tokens[0] == "pow":
            if len(tokens) > 3:
                print "You have given me too many numbers for this function. Try again!"
            else:
                print power(int(tokens[1]), int(tokens[2]))

        elif tokens[0] == "mod":
            if len(tokens) > 3:
                print "You have given me too many numbers for this function. Try again!"
            else:
                print mod(int(tokens[1]), int(tokens[2]))

        elif tokens[0] == 'q' or tokens[0] == 'quit':
            math_function = 'q'
        else:
            print "I did not understand that. Try again!"
    except ValueError:
        print "You entered incorrect value. Try again!"





# math_function = ""

# while math_function != 'q':

#     math_function = raw_input(">")

#     tokens = math_function.split()

#     token_dictionary = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide", "pow": "power", "mod": "mod", "square": "square", "cube": "cube"}

#     try:
#         if tokens[0] in token_dictionary:
#             operator = eval(token_dictionary[tokens[0]])  # eval() takes an argument and parses it as a Python expression
#             if len(tokens) == 2:
#                 print operator(int(tokens[1]))
#             else:
#                 res = map(int, tokens[2:])
#                 print operator(int(tokens[1]), *res)

#         elif tokens[0] == 'q' or tokens[0] == 'quit':
#             math_function = 'q'
#         else:
#             print "I did not understand that. Try again!"
#     except ValueError:
#         print "You entered incorrect value. Try again!"


