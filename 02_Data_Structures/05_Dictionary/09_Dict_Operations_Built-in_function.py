# ================================
# Dictionary Operations & Built-in Functions
# ================================

# Sample dictionary for demonstration
my_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}


# 1. 'in' Operator (Checks KEYS only)
print(3 in my_dict)       # True → Key 3 exists
print(10 in my_dict)      # False → Key 10 does not exist

# 'in' for VALUES (use .values())
print("three" in my_dict) # False → does not search for values
print("three" in my_dict.values())  # True → Value exists

# 'not in' Operator
print(10 not in my_dict)  # True → Key 10 is NOT in dictionary
print(3 not in my_dict)   # False → Key 3 exists


# ---------------------------------------

# 2. len() → Number of key-value pairs
print(len(my_dict))  
# Output: 6  (Each key-value pair counts as one element)

# ---------------------------------------

# 3. all() → Returns True if ALL KEYS are "truthy"
dict_all_true = {1: "A", 2: "B", 3: "C"}
dict_some_false = {0: "A", False: "B"}
print(all(dict_all_true))     # True → All keys are non-zero and True
print(all(dict_some_false))   # False → Key 0 & False are considered False

# ---------------------------------------

# 4. any() → Returns True if ANY KEY is "truthy"
dict_all_false = {0: "A", False: "B"}
dict_one_true = {0: "A", 1: "B"}
print(any(dict_all_false))    # False → All keys are False
print(any(dict_one_true))     # True → One key (1) is True

# ---------------------------------------

# 5. sorted() → Returns sorted list of KEYS
print(sorted(my_dict))  
# Output: [1, 2, 3, 4, 5, 6] → Sorted order of keys

# ---------------------------------------
# END OF NOTES
# ---------------------------------------
