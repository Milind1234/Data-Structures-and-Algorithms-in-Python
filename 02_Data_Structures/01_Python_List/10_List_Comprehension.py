    # -----------------------------
# Topic: List Comprehension in Python
# -----------------------------

# 💡 What is List Comprehension?
# List comprehension is a concise way to create new lists by applying an expression to each item 
# in an iterable (like list, string, range, etc.).
# It reduces the amount of code and is generally more readable.

# Syntax:
# new_list = [new_item for item in iterable]

# Traditional for-loop way:
prev_list = [1, 2, 3]
new_list = []
for i in prev_list:
    multiply_2 = i * 2
    new_list.append(multiply_2)

print("Using for loop:", new_list)  # Output: [2, 4, 6]

# Equivalent List Comprehension:
prev_list = [1, 2, 3]
new_list = [i * 2 for i in prev_list]

print("Using list comprehension:", new_list)  # Output: [2, 4, 6]


# --------------------------------
# 🔁 How to write list comprehension step-by-step
# --------------------------------

# Template: [new_item for item in iterable]

# Example 1: Multiply each element by 2
numbers = [1, 2, 3]
result = [num * 2 for num in numbers]
print("Example 1:", result)  # Output: [2, 4, 6]

# Example 2: Square each number in a range
squares = [x**2 for x in range(5)]
print("Example 2:", squares)  # Output: [0, 1, 4, 9, 16]

# Example 3: Convert string to list of characters
language = "Python"
char_list = [letter for letter in language]
print("Example 3:", char_list)  # Output: ['P', 'y', 't', 'h', 'o', 'n']


# --------------------------------
# 📚 Python Sequences Supported by List Comprehension
# --------------------------------
# You can use list comprehension on these Python sequences:
# 1. List
# 2. Range
# 3. String
# 4. Tuple

# Example 4: Using tuple
tuple_data = (10, 20, 30)
new_tuple_list = [t + 5 for t in tuple_data]
print("Example 4:", new_tuple_list)  # Output: [15, 25, 35]

# Example 5: Using range
even_numbers = [n for n in range(10) if n % 2 == 0]
print("Example 5:", even_numbers)  # Output: [0, 2, 4, 6, 8]

# Example 6: Uppercasing characters in a string
word = "hello"
upper_word = [ch.upper() for ch in word]
print("Example 6:", upper_word)  # Output: ['H', 'E', 'L', 'L', 'O']
