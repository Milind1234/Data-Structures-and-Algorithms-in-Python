"""
==========================================================
Dictionary Traversal in Python
==========================================================

🔹 What is Dictionary Traversal?
- Traversing a dictionary means iterating over its keys and values.
- It is often used to access, display, or process all elements.

----------------------------------------------------------
1) Traversal using Keys (Default)
----------------------------------------------------------
"""

my_dict = {'name': 'EDY', 'age': 30, 'address': 'LONDON', 'phone': '123456'}

def traverse_keys(my_dict):
    for key in my_dict:  # Iterates through keys
        print(f"{key} : {my_dict[key]}")  # Fetch value using key

traverse_keys(my_dict)

"""
Output:
name : EDY
age : 30
address : LONDON
phone : 123456
"""

"""
----------------------------------------------------------
2) Traversal using items() (Recommended)
----------------------------------------------------------
"""

def traverse_items(my_dict):
    for key, value in my_dict.items():  # Directly get key and value
        print(f"{key} : {value}")

traverse_items(my_dict)

"""
Output:
name : EDY
age : 30
address : LONDON
phone : 123456
"""

"""
----------------------------------------------------------
3) Traversal using keys() and values() separately
----------------------------------------------------------
"""

def traverse_keys_values(my_dict):
    print("Keys:")
    for key in my_dict.keys():
        print(key)
    
    print("\nValues:")
    for value in my_dict.values():
        print(value)

traverse_keys_values(my_dict)

"""
Output:
Keys:
name
age
address
phone

Values:
EDY
30
LONDON
123456
"""

"""
==========================================================
Time & Space Complexity
==========================================================
- Traversal Time Complexity → O(n) (n = number of items)
- Space Complexity → O(1) (only loop variables used)
==========================================================
Summary:
- Use `items()` when you need both key and value.
- Default traversal gives keys only.
- `keys()` and `values()` help when you need only one part.
==========================================================
"""
