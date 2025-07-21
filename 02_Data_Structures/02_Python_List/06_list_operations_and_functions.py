# 📘 Python List Operations and Built-in Functions

# ----------------------------
# 🔗 1. List Concatenation using '+' Operator
# ----------------------------
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("Concatenated list:", c)

# ⏱ Time Complexity: O(n + m) → where n and m are lengths of a and b
# 💾 Space Complexity: O(n + m)

# ----------------------------
# ✨ 2. List Repetition using '*' Operator
# ----------------------------
repeat_list = [0, 1]
repeated = repeat_list * 4
print("Repeated list:", repeated)

# ⏱ Time Complexity: O(n * k)
# 💾 Space Complexity: O(n * k)

# ----------------------------
# 🔢 3. len() → Get number of elements in the list
# ----------------------------
length = len(repeated)
print("Length of repeated list:", length)

# ⏱ Time Complexity: O(1)
# 💾 Space Complexity: O(1)

# ----------------------------
# 📈 4. max() → Get maximum value
# ----------------------------
max_value = max([3, 5, 7, 2])
print("Maximum value:", max_value)

# ⏱ Time Complexity: O(n)
# 💾 Space Complexity: O(1)

# ----------------------------
# 📉 5. min() → Get minimum value
# ----------------------------
min_value = min([3, 5, 7, 2])
print("Minimum value:", min_value)

# ⏱ Time Complexity: O(n)
# 💾 Space Complexity: O(1)

# ----------------------------
# ➕ 6. sum() → Sum of list elements
# ----------------------------
total = sum([3, 5, 7, 2])
print("Sum of elements:", total)

# ⏱ Time Complexity: O(n)
# 💾 Space Complexity: O(1)

# ----------------------------
# 📊 7. Average using sum() and len()
# ----------------------------
numbers = [3, 5, 7, 2]
average = sum(numbers) / len(numbers)
print("Average:", average)

# ⏱ Time Complexity: O(n)
# 💾 Space Complexity: O(1)

# ----------------------------
# 🧪 8. Challenge – Taking Input Until "done" and Calculating Average
#     Original loop rewritten using a list
# ----------------------------

# Uncomment below lines to run in interactive environment
"""
user_inputs = []
while True:
    data = input("Enter a number (or 'done' to finish): ")
    if data.lower() == 'done':
        break
    try:
        num = float(data)
        user_inputs.append(num)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if user_inputs:
    avg = sum(user_inputs) / len(user_inputs)
    print("Average:", avg)
else:
    print("No numbers entered.")
"""

# ⏱ Time Complexity: O(n)
# 💾 Space Complexity: O(n) — for storing input numbers in list

# ------------------------------------------
# 📌 Summary of List Functions & Complexities
# ------------------------------------------
"""
| Function       | Description                           | Time Complexity | Space Complexity |
|----------------|---------------------------------------|------------------|------------------|
| +              | Concatenation                         | O(n + m)         | O(n + m)         |
| *              | Repetition                            | O(n * k)         | O(n * k)         |
| len()          | Get number of elements                | O(1)             | O(1)             |
| max()          | Get max element                       | O(n)             | O(1)             |
| min()          | Get min element                       | O(n)             | O(1)             |
| sum()          | Get sum of elements                   | O(n)             | O(1)             |
| avg            | Combination of sum() / len()          | O(n)             | O(1)             |
"""


my_list = list()

while True:
    a= input("Enter the no. and if not the type done:")
    if a.lower() == "done":break
    value = float(a) 
    my_list.append(value)

avg = sum(my_list) // len(my_list)
print(avg)