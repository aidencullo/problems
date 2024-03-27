"""
This script demonstrates the error that occurs when trying to modify a variable in a nested function.
"""


def f1():
    x = 5
    def f2():
         x+=1
    f2()
    print(x)

f1() # UnboundLocalError: local variable 'x' referenced before assignment
