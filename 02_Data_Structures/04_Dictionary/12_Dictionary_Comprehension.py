# ========================================
# DICTIONARY COMPREHENSION IN PYTHON
# ========================================

"""
Dictionary comprehension is a short and efficient way to create dictionaries from:
- Lists
- Other Dictionaries
- Any Iterable (e.g., range, string)

-----------------------------------
General Syntax:
-----------------------------------
new_dict = { new_key: new_value for item in iterable }

With condition:
new_dict = { new_key: new_value for item in iterable if condition }

For existing dictionary:
new_dict = { key: value for key, value in old_dict.items() if condition }
"""

# ----------------------------------------
# 1) Create Dictionary from List
# ----------------------------------------

import random

# List of cities
cities = ["Paris", "London", "Berlin", "Madrid", "Rome"]

# Syntax:
# new_dict = { key: value for key in list }
# Example: Generate random temperature (20 - 30) for each city

city_temps = {city: random.randint(20, 30) for city in cities}
print("City Temperatures:", city_temps)
# Output Example: {'Paris': 22, 'London': 28, 'Berlin': 25, 'Madrid': 21, 'Rome': 30}


# ----------------------------------------
# 2) Create Dictionary from Dictionary
# ----------------------------------------

# Syntax:
# new_dict = { key: value for key, value in old_dict.items() }
# Example: Copy city_temps dictionary into a new one

copy_temps = {city: temp for city, temp in city_temps.items()}
print("Copied Dictionary:", copy_temps)
# Output Example: {'Paris': 22, 'London': 28, 'Berlin': 25, 'Madrid': 21, 'Rome': 30}


# ----------------------------------------
# 3) Dictionary Comprehension with Condition
# ----------------------------------------

# Syntax:
# new_dict = { key: value for key, value in old_dict.items() if condition }
# Example: Select only cities where temperature > 25

temps_above_25 = {city: temp for city, temp in city_temps.items() if temp > 25}
print("Cities with Temperature > 25:", temps_above_25)
# Output Example: {'London': 28, 'Rome': 30}


# ----------------------------------------
# 4) Dictionary Comprehension with range() + condition
# ----------------------------------------

# Syntax:
# new_dict = { key_expr: value_expr for item in range(n) if condition }
# Example: Square numbers for only even numbers

squares_even = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Squares of Even Numbers (1-10):", squares_even)
# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# ========================================
# QUICK SUMMARY TABLE (SYNTAX + PURPOSE)
# ========================================
"""
1) From List:
   new_dict = { key_expr: value_expr for item in iterable }
   -> Example: city_temps = {city: random.randint(20, 30) for city in cities}

2) From Dictionary:
   new_dict = { key_expr: value_expr for key, value in old_dict.items() }
   -> Example: copy_dict = {k: v for k, v in old_dict.items()}

3) With Condition:
   new_dict = { key_expr: value_expr for key, value in old_dict.items() if condition }
   -> Example: temps_above_25 = {c: t for c, t in city_temps.items() if t > 25}

4) From range() + Condition:
   new_dict = { key_expr: value_expr for item in range(n) if condition }
   -> Example: squares_even = {x: x**2 for x in range(1, 11) if x % 2 == 0}
"""
