# ==========================================================
# Topic: Inserting Elements in Dictionary
# ==========================================================

# Dictionary is mutable → allows adding new key-value pairs
# If the key does not exist → new key-value pair is inserted
# Performed using assignment operator

# ------------------------------
# 1) Basic Insertion (Assignment)
# ------------------------------
my_dict = {"name": "Edy", "age": 26}
my_dict["address"] = "London"
print(my_dict)  
# Output: {'name': 'Edy', 'age': 26, 'address': 'London'}

# Time: O(1), Space: Amortized O(1)

# ------------------------------
# 2) Using update()
# ------------------------------
my_dict.update({"phone": "123456"})
print(my_dict)  
# Output: {'name': 'Edy', 'age': 26, 'address': 'London', 'phone': '123456'}

# Time: O(k), Space: O(1)

# ------------------------------
# 3) Using setdefault()
# ------------------------------
my_dict.setdefault("email", "edy@example.com")
print(my_dict)  
# Output: {'name': 'Edy', 'age': 26, 'address': 'London', 'phone': '123456', 'email': 'edy@example.com'}

# Time: O(1), Space: O(1)

# ------------------------------
# 4) Using Dictionary Unpacking
# ------------------------------
my_dict = {**my_dict, **{"country": "UK"}}
print(my_dict)  
# Output: {'name': 'Edy', 'age': 26, 'address': 'London', 'phone': '123456', 'email': 'edy@example.com', 'country': 'UK'}

# Time: O(n), Space: O(n)

# ------------------------------
# Summary Table
# ------------------------------
# Method            Time Complexity    Space Complexity
# Assignment        O(1)               O(1)
# update()          O(k)               O(1)
# setdefault()      O(1)               O(1)
# Unpacking         O(n)               O(n)
