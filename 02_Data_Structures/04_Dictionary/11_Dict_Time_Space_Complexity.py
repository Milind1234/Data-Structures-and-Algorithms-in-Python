# ========================================
# Time & Space Complexity of Dictionary
# ========================================

"""
Operation-wise Time & Space Complexity:

1. Creating a Dictionary:
   - Time Complexity: O(n) (depends on size of dictionary)
   - Space Complexity: O(n)

2. Inserting a Value:
   - Time Complexity: O(1) (average case) 
   - Space Complexity: O(1)

3. Traversing a Dictionary:
   - Time Complexity: O(n) (visits all items)
   - Space Complexity: O(1)

4. Accessing a Given Key:
   - Time Complexity: O(1)
   - Space Complexity: O(1)

5. Searching a Given Value:
   - Time Complexity: O(1) (using 'in') / O(n) (linear search)
   - Space Complexity: O(1)

6. Deleting a Given Value:
   - Time Complexity: O(1)
   - Space Complexity: O(1)
"""

# ================================
# Examples for Each Operation
# ================================

# 1. CREATING A DICTIONARY (O(n))
my_dict = {"a": 1, "b": 2, "c": 3}
print("Created Dictionary:", my_dict)
# Output: Created Dictionary: {'a': 1, 'b': 2, 'c': 3}

# 2. INSERTING A VALUE (O(1))
my_dict["d"] = 4
print("After Insertion:", my_dict)
# Output: After Insertion: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 3. TRAVERSING (O(n))
for key, value in my_dict.items():
    print(f"Key={key}, Value={value}")
# Output (order may vary):
# Key=a, Value=1
# Key=b, Value=2
# Key=c, Value=3
# Key=d, Value=4

# 4. ACCESSING A VALUE (O(1))
print("Value of key 'b':", my_dict["b"])
# Output: Value of key 'b': 2

# 5. SEARCHING A VALUE
# (a) Using key with 'in' operator (O(1))
print("'c' in dictionary?", "c" in my_dict)  # Output: True

# (b) Searching value using loop (O(n))
found = 4 in my_dict.values()
print("Value 4 found:", found)
# Output: Value 4 found: True

# 6. DELETING A VALUE (O(1))
del my_dict["a"]
print("After Deletion:", my_dict)
# Output: After Deletion: {'b': 2, 'c': 3, 'd': 4}

# ===============================
# SUMMARY TABLE (for Quick Look)
# ===============================
# Operation         | Time Complexity | Space Complexity
# -----------------------------------------------------
# Create Dictionary | O(n)            | O(n)
# Insert Key-Value  | O(1) (avg)      | O(1)
# Traverse          | O(n)            | O(1)
# Access by Key     | O(1)            | O(1)
# Search by Key     | O(1) (in) / O(n)| O(1)
# Delete by Key     | O(1)            | O(1)
