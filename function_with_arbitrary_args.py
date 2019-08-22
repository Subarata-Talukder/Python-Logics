# @Author Subarata Chandra Talukder

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def zero_or_more_var_agrs(*names):
    print("All students names are: ")
    for std in names:
        print(std)

zero_or_more_var_agrs('Rajib','Subarata','Rimpi')

print(list(range(3, 6))) # normal call with separate arguments
args = [3, 6]
print(list(range(*args))) # call with arguments unpacked from a list