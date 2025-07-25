"""
==========================================================
Searching for an Element in a Dictionary
==========================================================

🔹 Problem:
- Given a dictionary, search for a specific value.
- If found, print its key and value; otherwise, return "Element not found".

----------------------------------------------------------
ASCII Diagram Representation
----------------------------------------------------------

Dictionary Example:
my_dict = {
    'name': 'EDY',
    'age': 30,
    'address': 'LONDON',
    'phone': '123456'
}

Visual Representation (Key → Value):
    name    → 'EDY'
    age     → 30
    address → 'LONDON'
    phone   → '123456'

----------------------------------------------------------
Approach:
----------------------------------------------------------
1. Iterate through all dictionary keys.
2. For each key, check if its value matches the target value.
3. If a match is found → print key and value.
4. If no match is found → return `"Element not found in dict"`.

----------------------------------------------------------
Code Implementation:
----------------------------------------------------------
"""

my_dict = {'name': 'EDY', 'age': 30, 'address': 'LONDON', 'phone': '123456'}

def Search_element(dictionary, value):
    for key in dictionary:              # Iterate through keys
        if dictionary[key] == value:    # Check value
            return f"{key}: {value}"                      
    return "Element not found in dict"  # If not found

# Example Call
print(Search_element(my_dict, 30))


"""
Output:
age: 30
"""

"""
----------------------------------------------------------
Optimized Version:
----------------------------------------------------------
- If we want to return the result instead of just printing:
"""

def search_element_return(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return f"{key}: {val}"
    return "Element not found in dict"

print(search_element_return(my_dict, 30))  
# Output: age: 30

print(search_element_return(my_dict, "DELHI"))  
# Output: Element not found in dict

"""
==========================================================
Time & Space Complexity:
==========================================================
- Time Complexity → O(n) (must check each key-value pair)
- Space Complexity → O(1) (no extra data structures)
==========================================================
Summary:
- Best used for small dictionaries.
- For frequent searches by value, consider reversing dictionary to key lookup.
==========================================================
"""
