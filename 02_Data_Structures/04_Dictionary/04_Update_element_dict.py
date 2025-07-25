# ==========================================================
# Topic: Updating Elements in Dictionary
# ==========================================================

# If key exists → value modified
# If key does not exist → new key-value pair created

# ------------------------------
# 1) Basic Updating (Assignment)
# ------------------------------
my_dict = {"name": "Edy", "age": 26}
my_dict["age"] = 27
print(my_dict)  
# Output: {'name': 'Edy', 'age': 27}

# Time: O(1), Space: O(1)

# ------------------------------
# 2) Using update()
# ------------------------------
my_dict.update({"age": 30, "address": "London"})
print(my_dict)  
# Output: {'name': 'Edy', 'age': 30, 'address': 'London'}

# Time: O(k), Space: O(1)

# ------------------------------
# 3) Using setdefault()
# ------------------------------
my_dict.setdefault("phone", "123456")
print(my_dict)  
# Output: {'name': 'Edy', 'age': 30, 'address': 'London', 'phone': '123456'}

# Time: O(1), Space: O(1)

# ------------------------------
# 4) Dictionary Comprehension (mass update)
# ------------------------------
my_dict = {k: (v.upper() if isinstance(v, str) else v)
           for k, v in my_dict.items()}
print(my_dict)  
# Output: {'name': 'EDY', 'age': 30, 'address': 'LONDON', 'phone': '123456'}

# Time: O(n), Space: O(n)

# ------------------------------
# Summary Table
# ------------------------------
# Method                    Time Complexity    Space Complexity
# Assignment update         O(1)               O(1)
# update()                  O(k)               O(1)
# setdefault()              O(1)               O(1)
# Dictionary comprehension  O(n)               O(n)
