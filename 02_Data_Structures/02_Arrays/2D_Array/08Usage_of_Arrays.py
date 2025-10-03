# array_usage_notes.py
# -----------------------------------------------------
# FINAL NOTES: When to Use and Avoid Arrays in Python
# -----------------------------------------------------

"""
✅ WHEN TO USE ARRAYS:

1. When you want to store multiple values of the same data type:
   - Arrays help in managing collections of homogeneous data efficiently.
   - Instead of declaring thousands of individual variables, store them in one array.
   - Example:
       arr = array('i', [1, 2, 3, ..., 1000])

2. When you need fast random access to elements:
   - Arrays provide O(1) time complexity for accessing any element by index.
   - Ideal when performance is critical, e.g., fetching mid-array values.
   - Compared to other structures like lists or linked lists that may require O(n) access.

-----------------------------------------------
🚫 WHEN TO AVOID ARRAYS:

1. When you need to store different data types:
   - Traditional arrays (e.g., using array module in Python or C/C++) support only one data type.
   - Mixed types require using other structures like lists or objects.

2. Fixed size limitation:
   - Arrays require pre-defining size or reallocation.
   - When array size grows beyond initial capacity, a new larger memory block must be allocated and data copied.
   - This results in performance degradation.

3. Inefficient for frequent insertions/deletions:
   - Inserting or deleting from the beginning/middle involves shifting elements.
   - This results in O(n) time complexity, which can be costly for large arrays.

------------------------------------------------
💡 INTERVIEW TIP:

- Use arrays when:
    ✔ You need fast indexed access (O(1))
    ✔ Data is of uniform type and known size

- Avoid arrays when:
    ❌ You need flexibility in size or mixed data types
    ❌ Your program frequently grows/shrinks the data structure

- For Python, prefer `list` or `numpy.array` for flexible or mathematical operations.

"""
