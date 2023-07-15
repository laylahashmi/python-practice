# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
input = [1, 2, 3]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

# def halve_the_list(list):
#     half = len(list)//2
#     return [list[:half], list[half:]]

def halve_the_list(input):
    return (
        input[0:len(input) // 2 + (len(input) % 2)],
        input[len(input) // 2 + (len(input) % 2):],
    )

# def halve_the_list(input):
#     first_list = []
#     second_list = []
#     first_list_len = len(input) // 2 + (len(input) % 2)
#     for i in range(first_list_len):
#         first_list.append(input[i])
#     for i in range(len(input) // 2):
#         index = i + first_list_len
#         second_list.append(input[index])
#     return first_list, second_list



print(halve_the_list(input))
