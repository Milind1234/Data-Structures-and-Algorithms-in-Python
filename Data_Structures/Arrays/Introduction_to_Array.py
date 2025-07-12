# 📘 Arrays Detailed Notes

---

## 🧠 What is an Array?
"""
An **array** is a linear data structure that stores elements of the **same data type** in **contiguous memory locations**. Arrays allow **random access** of elements using indices.

> 🗞 **Definition (GeeksforGeeks):** An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.

### 🔍 Why Use Arrays?
- To avoid declaring multiple variables.
- To group similar types of data.
- To optimize memory usage.
- Fast access using index (O(1) time complexity).
"""

"""
## 🍡 Real-Life Analogy
Imagine a box of **macarons**:
- Only macarons can fit (homogeneous type)
- All are placed next to each other (contiguous)
- Each has a fixed position (indexed)

Just like an array!
"""

---

## 🔢 Types of Arrays

"""
### 1️⃣ One-Dimensional Array
- A linear collection with one index.
- Syntax: `a[i]` → `i` is between 0 and n−1.
"""

# 📦 Example:
a = [5, 4, 10, 11, 8, 11, 68, 87, 12]
print(a[2])  # Output: 10

"""
### 2️⃣ Two-Dimensional Array
- Tabular structure (matrix-like).
- Syntax: `a[i][j]` where `i` is row index, `j` is column index.
"""

# 📦 Example:
a = [
    [1, 33, 55, 91, 20, 51, 62, 74, 13],
    [5, 4, 10, 11, 8, 11, 68, 87, 12],
    [24, 50, 37, 40, 48, 30, 59, 81, 93]
]
print(a[2][5])  # Output: 30

"""
### 3️⃣ Three-Dimensional Array
- Array of 2D arrays → represented like a cube.
- Syntax: `a[i][j][k]`
"""

# 📦 Example:
a = [
  [[0, 1, 2], [3, 4, 5]],
  [[6, 7, 8], [9, 10, 11]],
  [[12, 13, 14], [15, 16, 17]]
]
print(a[2][0][2])  # Output: 14

---

## 🧼 Arrays in Memory (RAM)

"""
✅ One-Dimensional Array:
- Stored in contiguous memory.
- Compiler allocates memory blocks next to each other.

✅ Two-Dimensional Array:
- Also stored linearly in memory (row-wise by default).
- Compiler flattens the 2D structure → row0 + row1 + row2...

✅ Three-Dimensional Array:
- Flattened like 2D: All slices are laid out row-wise one after another.

📜 **Note:** All elements of an array (1D/2D/3D) are stored contiguously in memory.
"""

---

## 📚 Summary Table

"""
| Array Type | Indexing Format | Structure Description         |
|------------|------------------|-------------------------------|
| 1D         | a[i]             | Single row                   |
| 2D         | a[i][j]          | Rows and columns (matrix)    |
| 3D         | a[i][j][k]       | Multiple 2D arrays (cube)    |
"""

---

## 🔧 Operations on Arrays

"""
| Operation        | Time Complexity |
|------------------|-----------------|
| Access           | O(1)            |
| Insertion (end)  | O(1) (amortized)|
| Insertion (mid)  | O(n)            |
| Deletion         | O(n)            |
| Search           | O(n) or O(log n)|
"""

---

## 📌 Key Properties
"""
- Homogeneous elements (same data type)
- Fixed size (in static arrays)
- Elements are indexed
- Stored in contiguous memory
"""

---

## 🧰 Python Tip: Array Modules
"""
- Python uses **lists** by default, which are dynamic arrays.
- Use `array` module (for static, type-specific arrays):
"""
from array import array
a = array('i', [1, 2, 3, 4])

"""
- Use `numpy` for powerful numerical operations:
"""
import numpy as np
a = np.array([[1, 2], [3, 4]])

---

## 📌 References
"""
- GeeksforGeeks - Arrays: https://www.geeksforgeeks.org/array-data-structure/
- W3Schools - Python Arrays: https://www.w3schools.com/python/python_arrays.asp
"""

---

"""
✅ *This section gives you complete clarity on arrays from theory to code to memory layout.*
"""
