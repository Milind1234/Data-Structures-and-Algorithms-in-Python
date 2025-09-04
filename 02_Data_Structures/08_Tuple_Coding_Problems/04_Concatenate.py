# Concatenate Strings from Tuple
# ---------------------------------------
# Question:
# Write a function that takes a tuple of strings and concatenates them,
# separating each string with a space.
#
# Example:
# input_tuple = ('Hello', 'World', 'from', 'Python')
# output_string = concatenate_strings(input_tuple)
# print(output_string)  # Expected output: 'Hello World from Python'


# Approach 1: Convert tuple to list and join (less optimal)
def concatenate_strings_v1(input_tuple):
    l1 = list(input_tuple)             # Convert tuple to list
    return " ".join(l1)                # Join elements with a space


# Approach 2: Directly join tuple elements (optimal)
def concatenate_strings_v2(input_tuple):
    return " ".join(input_tuple)       # Direct join (no conversion needed)


# Example Run
input_tuple = ('Hello', 'World', 'from', 'Python')
print(concatenate_strings_v1(input_tuple))  # Output: Hello World from Python
print(concatenate_strings_v2(input_tuple))  # Output: Hello World from Python


# ---------------------------------------
# Explanation:
# - The join() method efficiently concatenates iterable elements into a single string
#   with the specified separator (in this case, a space " ").
# - In Approach 1, we first convert the tuple to a list (extra step).
# - In Approach 2, we directly use the tuple (preferred and optimal).

# ---------------------------------------
# Time & Space Complexity:
# - Time Complexity: O(n)
#   (Iterates through all n strings in the tuple and concatenates them)
# - Space Complexity: O(n)
#   (Creates a new string whose size is equal to the sum of lengths of all strings + spaces)
