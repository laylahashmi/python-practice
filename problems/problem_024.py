# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    count = 0
    for value in values:
        count += value
    return count/len(values)

print(calculate_average([6, 7, 8, 1]))
