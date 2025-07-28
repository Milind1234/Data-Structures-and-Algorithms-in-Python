# ================================
# Dictionary Methods in Python
# ================================

# 1. clear()
# ----------------------------
# Removes all items from the dictionary.
# Syntax: dict.clear()
my_dict = {"a": 1, "b": 2}
my_dict.clear()
print("clear():", my_dict)  
# Output: {}

# ---------------------------------

# 2. copy()
# ----------------------------
# Returns a shallow copy of the dictionary.
# Syntax: dict.copy()
original = {"x": 10, "y": 20}
copied = original.copy()
print("copy():", copied)
# Output: {'x': 10, 'y': 20}

# ---------------------------------

# 3. fromkeys()
# ----------------------------
# Creates a dictionary from given keys and sets all values to a specified value.
# Syntax: dict.fromkeys(sequence, value)
keys = [1, 2, 3]
new_dict = dict.fromkeys(keys, 0)
print("fromkeys():", new_dict)
# Output: {1: 0, 2: 0, 3: 0}

# ---------------------------------

# 4. get()
# ----------------------------
# Returns the value for a key if present, else returns default value or None.
# Syntax: dict.get(key, default_value)
student = {"name": "John", "age": 22}
print("get():", student.get("age"))        # Output: 22
print("get() with default:", student.get("city", "Unknown"))  # Output: Unknown

# ---------------------------------

# 5. items()
# ----------------------------
# Returns key-value pairs as tuples.
# Syntax: dict.items()
info = {"a": 1, "b": 2}
print("items():", info.items())
# Output: dict_items([('a', 1), ('b', 2)])

# ---------------------------------

# 6. keys()
# ----------------------------
# Returns all keys in the dictionary.
# Syntax: dict.keys()
print("keys():", info.keys())
# Output: dict_keys(['a', 'b'])

# ---------------------------------

# 7. popitem()
# ----------------------------
# Removes and returns the last inserted (key, value) pair.
# Syntax: dict.popitem()
temp = {"x": 1, "y": 2}
print("popitem():", temp.popitem())  
print("Dictionary after popitem:", temp)
# Output (example): ('y', 2) then {'x': 1}

# ---------------------------------

# 8. setdefault()
# ----------------------------
# Returns value of the key if it exists, else inserts the key with default value.
# Syntax: dict.setdefault(key, default_value)
sample = {"name": "Alex"}
print("setdefault() existing:", sample.setdefault("name", "John"))
print("setdefault() new key:", sample.setdefault("age", 25))
print("Dictionary after setdefault:", sample)
# Output:
# setdefault() existing: Alex
# setdefault() new key: 25
# Dictionary after setdefault: {'name': 'Alex', 'age': 25}

# ---------------------------------

# 9. pop()
# ----------------------------
# Removes and returns value for given key.
# Syntax: dict.pop(key, default_value)
marks = {"Math": 90, "Science": 85}
print("pop() existing:", marks.pop("Math"))
print("pop() not existing:", marks.pop("English", "No Record"))
print("Dictionary after pop:", marks)
# Output:
# pop() existing: 90
# pop() not existing: No Record
# Dictionary after pop: {'Science': 85}

# ---------------------------------

# 10. values()
# ----------------------------
# Returns all values of the dictionary.
# Syntax: dict.values()
print("values():", marks.values())
# Output: dict_values([85])

# ---------------------------------

# 11. update()
# ----------------------------
# Updates dictionary with another dictionary or key-value pairs.
# Syntax: dict.update(other_dict)
person = {"name": "John"}
person.update({"age": 30, "city": "London"})
print("update():", person)
# Output: {'name': 'John', 'age': 30, 'city': 'London'}

# ========================================
# END OF NOTES
# ========================================
