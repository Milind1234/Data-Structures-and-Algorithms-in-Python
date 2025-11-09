"""
==========================================================
Deleting Elements from Dictionary
==========================================================

🔹 Problem:
- Remove elements from a dictionary using various built-in methods.
- Understand how each deletion method works and its time/space complexity.

----------------------------------------------------------
Dictionary Example:
----------------------------------------------------------
my_dict = {'name': 'EDY', 'age': 30, 'address': 'LONDON', 'phone': '123456'}

==========================================================
1) Using `del` Statement
==========================================================
- Removes an element by specifying its key.
- If the key does not exist → raises KeyError.
"""
# Code:
my_dict = {'name': 'EDY', 'age': 30, 'address': 'LONDON', 'phone': '123456'}
del my_dict['age']
print(my_dict)

# Output:
{'name': 'EDY', 'address': 'LONDON', 'phone': '123456'}

# Complexity:
# - Time: O(1)
# - Space: O(1)

"""
==========================================================
2) Using `pop()` Method
==========================================================
- Removes the key-value pair for the specified key and returns the value.
- If the key is not found → KeyError unless a default value is provided.

Code:
"""
my_dict = {'name': 'EDY', 'age': 30, 'address': 'LONDON', 'phone': '123456'}
removed_element = my_dict.pop('name')
print(removed_element)   # EDY
print(my_dict)

# Handling KeyError using default value
removed_element = my_dict.pop('nam', None)
print(removed_element)   # None
print(my_dict)

# Output:
# EDY
{'age': 30, 'address': 'LONDON', 'phone': '123456'}
None
{'age': 30, 'address': 'LONDON', 'phone': '123456'}

# Complexity:
# - Time: O(1)
# - Space: O(1)

"""=========================================================
3) Using `popitem()` Method
==========================================================
- Removes and returns the **last inserted** key-value pair (from Python 3.7+).
- Before Python 3.7, it removed random elements.

Code:
"""
my_dict = {'name': 'EDY', 'age': 30, 'address': 'LONDON', 'phone': '123456'}
removed_element = my_dict.popitem()
print(removed_element)
print(my_dict)

# Output:
('phone', '123456')
{'name': 'EDY', 'age': 30, 'address': 'LONDON'}

# Complexity:
# - Time: O(1)
# - Space: O(1)

"""==========================================================
4) Using `clear()` Method
==========================================================
- Removes all elements, leaving an empty dictionary.

Code:"""

my_dict = {'name': 'EDY', 'age': 30, 'address': 'LONDON', 'phone': '123456'}
my_dict.clear()
print(my_dict)

"""Output:
{}

Complexity:
- Time: O(n) → Removes all elements
- Space: O(1)

==========================================================
Summary Table
==========================================================
Method       | Returns            | Time Complexity | Space Complexity
-------------|--------------------|-----------------|-----------------
del          | None               | O(1)            | O(1)
pop(key)     | value              | O(1)            | O(1)
popitem()    | (key, value) tuple | O(1)            | O(1)
clear()      | None               | O(n)            | O(1)
==========================================================
"""
