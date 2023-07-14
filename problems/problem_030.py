# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
    if len(values)==0 or len(values)==1:
        return None
    values.sort()
    return values[-2]

print(find_second_largest([4, 3, 23, 12, 89]))
