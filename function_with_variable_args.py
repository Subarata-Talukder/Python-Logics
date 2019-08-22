# @Author Subarata Chandra Talukder

#Define functions with a variable number of arguments have three forms
# 1 Default Argument Values
# 2 Keyword Arguments
# 3 Arbitrary Argument Lists

## Default Argument Values ##

# Default value for one or more arguments
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt) #Take user input
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask_ok("Enter some value\n")

# The default values are evaluated at the point of
... # function definition in the defining scope
i = 5
def f(arg=i):
    print(arg)

i = 6
f()


# The default value is evaluated only once. This makes a difference
... # when the default is a mutable object such as a list, dictionary,
... # or instances of most classes

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print('\n=========================================\n')
# Don’t want the default to be shared between subsequent calls
def f(a, L=None):
    if L is None:
        L = []
        L.append(a)
        return L

print(f(1))
print(f(2))
print(f(3))