# 📘 Python List Slicing & Deletion Notes

# ----------------------------------------
# ✂️ LIST SLICING
# ----------------------------------------

"""
Slicing is a way to extract a portion of a list using the format:
list[start:stop:step]

- start: index to begin (inclusive)
- stop: index to end (exclusive)
- step: the interval (default is 1)
"""

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🔹 Basic Slicing
print(nums[2:6])       # [2, 3, 4, 5]

# 🔹 Omitting start or end
print(nums[:5])        # [0, 1, 2, 3, 4]
print(nums[5:])        # [5, 6, 7, 8, 9]

# 🔹 With step
print(nums[1:9:2])     # [1, 3, 5, 7]

# 🔹 Reverse a list
print(nums[::-1])      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 🔹 Copying the whole list
copy_nums = nums[:]
print(copy_nums)       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🔹 Negative indexing with slicing
print(nums[-5:-2])     # [5, 6, 7]

"""
⏱ Time Complexity of Slicing:
- O(k), where k is the size of the slice
🧠 Space Complexity:
- O(k), since a new list is created for the slice
"""

# ----------------------------------------
# ❌ DELETION IN LISTS
# ----------------------------------------

# 1️⃣ del keyword — deletes by index or slice
data = [10, 20, 30, 40, 50]
del data[2]             # removes 30
print(data)             # [10, 20, 40, 50]

# Deleting a slice
del data[1:3]           # removes 20 and 40
print(data)             # [10, 50]

"""
⏱ Time Complexity:
- Deleting an element: O(n)
- Deleting a slice of size k: O(n)
🧠 Space Complexity: O(1)
"""

# 2️⃣ pop() method — removes and returns an element by index
lst = ['a', 'b', 'c', 'd']
removed = lst.pop(1)    # removes 'b'
print(removed)          # b
print(lst)              # ['a', 'c', 'd']

# pop() without index removes last element
last = lst.pop()
print(last)             # d
print(lst)              # ['a', 'c']

"""
⏱ Time Complexity:
- pop(index): O(n)
- pop() [from end]: O(1)
🧠 Space Complexity: O(1)
"""

# 3️⃣ remove() method — deletes by value (first occurrence)
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')  # removes the first 'banana'
print(fruits)            # ['apple', 'cherry', 'banana']

"""
⏱ Time Complexity: O(n) — has to search the item
🧠 Space Complexity: O(1)
"""

# 4️⃣ clear() — removes all elements
nums = [1, 2, 3, 4]
nums.clear()
print(nums)              # []

"""
⏱ Time Complexity: O(n)
🧠 Space Complexity: O(1)
"""

# 5️⃣ List Slicing for Deletion
marks = [91, 92, 93, 94, 95, 96]
marks[1:4] = []          # removes 92, 93, 94
print(marks)             # [91, 95, 96]

"""
⏱ Time Complexity: O(n)
🧠 Space Complexity: O(1)
"""

# --------------------------
# 🔄 Summary of Methods
# --------------------------
"""
1. del list[index]       — by index or range
2. list.pop(index)       — by index (returns item)
3. list.pop()            — removes last item
4. list.remove(value)    — removes first matching value
5. list.clear()          — removes all items
6. list[start:end] = []  — slice deletion
"""

# ----------------------------------------
# ✅ Recap
# ----------------------------------------
"""
Slicing is used for reading/copying sublists.
Deletion is used to modify the list by removing data.
Each method has different use cases based on:
- Whether you know the index or value
- Whether you want to return the value
- Performance needs
"""
