# @Author Subarata Chandra Talukder

"""Small anonymous functions can be created with the lambda keyword. Lambda functions can be used wherever function objects are required. They are syntactically
restricted to a single expression. Lambda functions can reference variables from the containing scope:"""

#This function takes formal agrgument input to the 'n' variable
... # The X lambda variable takes lambda input and add with 'n'

#01. Lambda function variation
def make_incrementor(n):
    return lambda x: x + n

#Positional argument
l_fun = make_incrementor(0)

#Lambdata argument
print(l_fun(50))

#02. Lambda function variation

# This function has no formal argument but
# 'a' and 'b' lambda variables take lambda input

def add_two_multi():
    return lambda a,b: (a + b) * b

l_fun1 = add_two_multi()
#Lambdata argument
print(l_fun1(50, 50))

#03. Lambda function variation

# This function has formal string argument, which concatted with
# 'a' lambda variable

def welcome_me(name):
    return lambda a: a +' developed by ' +name

l_fun2 = welcome_me('Subarata Talukder')
#Lambdata argument
print(l_fun2('Python programming'))