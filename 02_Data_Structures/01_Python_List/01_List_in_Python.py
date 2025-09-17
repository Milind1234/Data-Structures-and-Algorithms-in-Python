# 📘 Python List Notes

## 🧠 What is a List in Python?
"""
A **list** is a built-in data structure in Python that stores an **ordered collection** of items.
It can hold **elements of different data types** (unlike arrays).

It is **mutable**, which means its elements can be changed after creation.
Lists are enclosed in **square brackets** `[]`, and items are separated by commas `,`.

Other built-in data structures include: `tuple`, `set`, and `dictionary`.
"""


## 📋 Creating Lists in python
# List of integers
int_list = [1, 2, 3, 4]

# List of strings
shopping_list = ["milk", "cheese", "butter"]

# List with mixed data types
mixed_list = [10, 3.14, "spam"]

# Nested list
nested_list = [1, 2, 3, ["a", "b"], 4.5]

# Empty list
empty_list = []



## 🧪 Accessing List Elements python

print(shopping_list[0])  # Output: milk
print(nested_list[3])    # Output: ["a", "b"]
print(nested_list[3][1]) # Output: b



## 🛠️ Common List Methods in Python

# | Method                 | Description                                  |
# |------------------------|----------------------------------------------|
# | `append(x)`            | Adds element `x` to the end of the list      |
# | `insert(i, x)`         | Inserts `x` at position `i`                  |
# | `extend(iterable)`     | Appends elements from another list           |
# | `remove(x)`            | Removes first occurrence of `x`              |
# | `pop([i])`             | Removes and returns item at `i` (or last)    |
# | `clear()`              | Removes all elements                         |
# | `index(x)`             | Returns index of first `x`                   |
# | `count(x)`             | Returns count of `x` in the list             |
# | `sort()`               | Sorts the list in ascending order            |
# | `reverse()`            | Reverses the elements of the list            |
# | `copy()`               | Returns a shallow copy of the list           |


## 🔁 Looping Through a List 
# python
for item in shopping_list:
    print(item)



## 🧪 Example Practice

# python
# Append and pop
fruits = []
fruits.append("apple")
fruits.append("banana")
print(fruits)     # ['apple', 'banana']
fruits.pop()
print(fruits)     # ['apple']

# Insertion
nums = [1, 2, 4, 5]
nums.insert(2, 3)
print(nums)       # [1, 2, 3, 4, 5]

# Sorting
letters = ['d', 'a', 'c', 'b']
letters.sort()
print(letters)    # ['a', 'b', 'c', 'd']

# Nested list access
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Output: 6

## 📌 Key Properties of Lists
# - **Ordered**: Items maintain insertion order
# - **Mutable**: Can change items
# - **Heterogeneous**: Items can be of different types
# - **Dynamic size**: Can grow or shrink during execution


# 🔗 References
# - [GeeksforGeeks - Python List](https://www.geeksforgeeks.org/python-list/)
# - [W3Schools - List Methods](https://www.w3schools.com/python/python_ref_list.asp)

# ✅ *This section introduces you to the powerful list data structure in Python. Learn it well—it’s used everywhere!*
