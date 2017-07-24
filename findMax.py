# Find maximum value from an arrray
# @Author Subarata Chandra Talukder
def max(valueList):
    max = valueList[0]
    for value in valueList:
        if value > max:
            max = value
    return max

# Test the result by giving this array
print(max([10, 20, 60 ,25]))