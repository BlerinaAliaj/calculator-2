"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

math_function = ""

while math_function != 'q':

    math_function = raw_input(">")

    tokens = math_function.split()

    token_dictionary = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide", "pow": "power", "mod": "mod", "square": "square", "cube": "cube"}

    try:
        if tokens[0] in token_dictionary:
            operator = eval(token_dictionary[tokens[0]])  # eval() takes an argument and parses it as a Python expression
            if len(tokens) == 2:
                print operator(int(tokens[1]))
            else:
                res = map(int, tokens[2:])
                print operator(int(tokens[1]), *res)

        elif tokens[0] == 'q' or tokens[0] == 'quit':
            math_function = 'q'
        else:
            print "I did not understand that. Try again!"
    except ValueError:
        print "You entered incorrect value. Try again!"
