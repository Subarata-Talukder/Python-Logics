# @Author Subarata Chandra Talukder

#Define functions with a variable number of arguments have three forms
# 1 Default Argument Values
# 2 Keyword Arguments
# 3 Arbitrary Argument Lists

## Keyword Arguments ##

"""Functions can also be called using keyword arguments of the form kwarg=value."""

# One required argument (voltage) and
# Three optional arguments (state, action, and type)
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


#parrot(1000) # 1 positional argument
#parrot(voltage=1000) # 1 keyword argument
#parrot(voltage=1000000, action='VOOOOOM') # 2 keyword arguments
#parrot(action='VOOOOOM', voltage=1000000) # 2 keyword arguments
#parrot('a million', 'bereft of life', 'jump') # 3 positional arguments
#parrot('a thousand', state='pushing up the daisies') # 1 positional, 1 keyword

d = {"voltage": "four million(400000 V)", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)



