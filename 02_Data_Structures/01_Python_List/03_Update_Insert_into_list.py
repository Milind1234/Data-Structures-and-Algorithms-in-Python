# 📘 Python Lists: Insert & Update Methods

# ✅ Updating Elements in a List
"""
Updating an element in a list means changing the value at a specific index.
"""

L1 = [1, 2, 3, 4, 5, 6]
print("Original List:", L1)

# 🔄 Update index 2
L1[2] = 22
print("Updated List (index 2 → 22):", L1)

# Time Complexity: O(1)
# Space Complexity: O(1)

# -----------------------------------------------------
# ✅ Inserting Elements into a List

# 🔹 Method 1: insert(index, value)
"""
Inserts an element at a specific position.
Shifts elements to the right.
"""

l2 = [1, 2, 3, 4, 5]
print("\nOriginal List:", l2)

# Insert 15 at index 1
l2.insert(1, 15)
print("After insert(1, 15):", l2)

# Time Complexity: O(n) → due to shifting elements
# Space Complexity: O(1)

# 🔹 Method 2: append(value)
"""
Appends an element at the end of the list.
"""

l3 = [1, 2, 3, 4, 5]
print("\nOriginal List:", l3)

l3.append(6)
print("After append(6):", l3)

# Time Complexity: O(1) (amortized)
# Space Complexity: O(1)

# 🔹 Method 3: extend(iterable)
"""
Adds elements from another list (or iterable) to the end.
"""

l4 = [6, 7, 8, 9]
l5 = [10, 11, 12, 13, 14, 15]
print("\nList to Extend:", l4)
print("Original Base List:", l5)

l5.extend(l4)
print("After extend(l4):", l5)

# Time Complexity: O(k) → k = len(l4)
# Space Complexity: O(k)

# -----------------------------------------------------
# ✅ Additional Insertion Methods

# 🔹 Method 4: Using slicing for insertion
"""
Insert multiple values without using extend().
"""

l6 = [1, 2, 3, 4]
l6[2:2] = [100, 200]
print("\nUsing Slicing Insertion at index 2:", l6)

# Time Complexity: O(n + m) → n is original list size, m is inserted slice
# Space Complexity: O(m)

# 🔹 Method 5: Insert using '+' operator (creates new list)
"""
Concatenates two lists and returns a new one.
"""

a = [1, 2, 3]
b = [4, 5]
c = a + b
print("\nUsing '+' Operator:", c)

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

# 🔹 Method 6: insert multiple using loop
"""
Manually insert elements using loop and insert().
"""

l7 = [10, 20, 30]
to_insert = [99, 88]
for item in to_insert[::-1]:
    l7.insert(1, item)

print("\nManual Insert multiple items at index 1:", l7)

# Time Complexity: O(n * m)
# Space Complexity: O(1)

# -----------------------------------------------------
# ✅ Summary Table (as comment):

"""
| Method            | Description                         | Time Complexity   | Space Complexity |
|------------------ |-------------------------------------|-------------------|------------------|
| list[index] = val | Update at index                     | O(1)              | O(1)             |
| list.insert()     | Insert at specific index            | O(n)              | O(1)             |
| list.append()     | Add at end                          | O(1) (amortized)  | O(1)             |
| list.extend()     | Add all elements from iterable      | O(k)              | O(k)             |
| list[i:i] = vals  | Insert using slicing                | O(n + m)          | O(m)             |
| list + list       | Combine lists (new list)            | O(n + m)          | O(n + m)         |
| insert in loop    | Multiple insert with insert()       | O(n * m)          | O(1)             |
"""
