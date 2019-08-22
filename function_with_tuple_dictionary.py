# @Author Subarata Chandra Talukder

#Define functions with a variable number of arguments have three forms
# 1 Default Argument Values
# 2 Keyword Arguments
# 3 Arbitrary Argument Lists

## Keyword Arguments ##

"""The formal parameter of the form **name is present, it receives a dictionary containing all
keyword arguments except for those corresponding to a formal parameter. This may be combined
with a formal parameter of the form *name which receives a tuple containing the positional arguments
beyond the formal parameter list. (*name must occur before **name.)"""

def student(class_name, *description, **profile):
    print("Are you ", class_name, " class student ?")
    print("Yes, I am ", class_name,'\n')

    # Receives a tuple
    print("*" * 40)
    for dsc in description:
        print(dsc)
        print("*" * 40)

    # Receives a dictionary
    print("\n")
    for p in profile:
        print(p, ":", profile[p])


student("TEN",'Sir I am Subarata Talukder', "I live in dhaka",
"My father is a farmer",
roll=102,
dept="Science")