# 📘 Array Creation in Python (Array vs NumPy)

"""
This note explains how to create arrays in Python using the built-in `array` module and the external `NumPy` library
"""

# 🧰 Using `array` Module
import array

# Creating an empty integer array
my_array = array.array('i')
print(my_array)  # Output: array('i') → O(1) space & time complexity

# Creating an array with elements
my_array1 = array.array('i', [1, 2, 3, 4])
print(my_array1)  # Output: array('i', [1, 2, 3, 4]) → O(N)

"""
✅ When you create an **empty array** using `array`, a minimal block of memory is allocated.
✅ When you initialize with values, memory is allocated proportionally to the number of elements (O(N)).
🚫 Only basic homogeneous types are supported.
"""

# 🧮 Using NumPy (Recommended for Advanced Use)
import numpy as np

# Creating an empty numpy array of integers
dtype = int
np_array = np.array([], dtype=dtype)
print(np_array)  # Output: [] → O(1)

# Creating a NumPy array with values
np_array1 = np.array([1, 2, 3, 4])
print(np_array1)  # Output: [1 2 3 4] → O(N)

"""
✅ NumPy offers high performance and supports advanced numerical operations.
✅ Supports multi-dimensional arrays and a wide range of data types.
❗ Requires external installation: `pip install numpy`
"""

# 🧠 Complexity Summary
"""
Time Complexity:
- Creating empty array (array / NumPy) → O(1)
- Creating array with N elements → O(N)

Space Complexity:
- Empty array → O(1)
- Array with N elements → O(N)
"""

# 📌 Key Takeaways
"""
- Use `array` for simple static arrays with basic types.
- Use `NumPy` for scientific computing, larger datasets, and multidimensional support.
"""

# 🔗 References
"""
- GeeksforGeeks: https://www.geeksforgeeks.org/python-arrays/
- NumPy Docs: 
https://numpy.org/doc/
"""
