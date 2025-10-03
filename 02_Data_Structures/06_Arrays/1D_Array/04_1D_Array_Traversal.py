# -------------------------------------
# 📘 Array Traversal in Python
# -------------------------------------

# Importing array module
import array as arr

# Creating an array of integers
arr_1 = arr.array('i', [1, 2, 3, 4, 5])

# ✅ Function to traverse and print each element of the array
def array_traversal(array):
    print("Traversing the array:") 
    for i in array: # ............................O(n)
        print(i, end=" ") # ......................O(1)   
    print()  # For clean newline

# Call the traversal function
array_traversal(arr_1)

# -------------------------------------
# 🧠 Time and Space Complexity
# -------------------------------------

# Time Complexity: O(n)
# - We visit each element exactly once.

# Space Complexity: O(1)
# - No extra space is used apart from a few variables (constant space).
