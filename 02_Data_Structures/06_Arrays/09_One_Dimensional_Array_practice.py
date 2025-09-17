# one_dimensional_array_practice.py
# Practice problems on 1D array using Python's array module

import array as arr

# 1. Create an array and traverse
# Time: O(n), Space: O(n)
arr_1 = arr.array('i', [1, 2, 3, 4, 5, 6])
def array_traversal(array):
    for i in array:
        print(i, end=" ")
print("\n1. Traversing array:")
array_traversal(arr_1)


# 2. Access individual elements through indexes
# Time: O(1), Space: O(1)
arr_2 = arr.array('i', [1, 2, 3, 4, 5, 6])
print("\n\n2. Access elements by index:")
print(arr_2[0])  # prints 1
print(arr_2[3])  # prints 4
print(arr_2[5])  # prints 6


# 3. Append any value to the array using append() method
# Time: O(1) amortized, Space: O(1)
arr_3 = arr.array('i', [1, 2, 3, 4, 5, 6])
arr_3.append(7)
print("\n3. After append:", arr_3.tolist())


# 4. Insert value in an array using insert() method
# Time: O(n), Space: O(1)
arr_4 = arr.array('i', [1, 2, 3, 4, 5, 6])
arr_4.insert(0, 9)  # Insert 9 at index 0
print("\n4. After insert at 0th index:", arr_4.tolist())


# 5. Extend python array using extend() method
# Time: O(k), Space: O(k), k = number of elements being added
arr_5 = arr.array('i', [1, 2, 3, 4, 5, 6])
arr_5.extend([7, 8])
print("\n5. After extend:", arr_5.tolist())


# 6. Add items from list into array using fromlist() method
# Time: O(k), Space: O(k)
tempList = [6, 7, 8, 9]
arr_6 = arr.array('i', [1, 2, 3, 4, 5])
print("\n6. Before fromlist:", arr_6.tolist())
arr_6.fromlist(tempList)
print("After fromlist:", arr_6.tolist())


# 7. Remove any array element using remove(), pop(), del
# Time: remove() O(n), pop() O(1), del O(n), Space: O(1)
arr_7 = arr.array('i', [1, 2, 3, 4, 5])
arr_7.remove(3)  # Remove first occurrence of 3
print("\n7. After remove(3):", arr_7.tolist())
arr_7.pop(1)  # Remove element at index 1
print("After pop(1):", arr_7.tolist())
arr_7.pop()   # Remove last element
print("After pop():", arr_7.tolist())
del arr_7[1]  # Delete element at index 1
print("After del[1]:", arr_7.tolist())


# 8. Remove last array element using pop() method
# Time: O(1), Space: O(1)
arr_8 = arr.array('i', [1, 2, 3, 4, 5])
arr_8.pop()
print("\n8. After pop():", arr_8.tolist())


# 9. Fetch any element through its index using index() method
# Time: O(n), Space: O(1)
arr_9 = arr.array('i', [1, 2, 3, 4, 5])
arr9_index = arr_9.index(4)
print("\n9. Index of element 4:", arr9_index)


# 10. Reverse a python array using reverse() method
# Time: O(n), Space: O(1)
arr_10 = arr.array('i', [1, 2, 3, 4, 5])
arr_10.reverse()
print("\n10. After reverse:", arr_10.tolist())


# 11. Get array buffer information through buffer_info() method
# Time: O(1), Space: O(1)
arr_11 = arr.array('i', [1, 2, 3, 4, 5, 6])
print("\n11. Buffer info (memory address, length):", arr_11.buffer_info())


# 12. Count number of occurrences of an element
# Time: O(n), Space: O(1)
arr_12 = arr.array('i', [1, 2, 3, 4, 4, 5, 4, 6, 5, 4])
print("\n12. Count of 4:", arr_12.count(4))
print("Count of 5:", arr_12.count(5))
print("Count of 1:", arr_12.count(1))


# 13. Convert array to string using tobytes() method
# .tostring() is deprecated in Python 3.9+, use tobytes() instead
# Time: O(n), Space: O(n)
arr_13 = arr.array('i', [1, 2, 3, 4, 5])
byte_str = arr_13.tobytes()
print("\n13. Byte string (tobytes):", byte_str)


# 14. Convert array to list using tolist() method
# Time: O(n), Space: O(n)
arr_14 = arr.array('i', [1, 2, 3, 4, 5])
print("\n14. Converted to list:", arr_14.tolist())


# 15. Append a string to char array using fromunicode() method
# .fromstring() is deprecated; use fromunicode for 'u' type
# Time: O(k), Space: O(k)
char_arr = arr.array('u', 'Hello')
print("\n15. Char array before append:", char_arr)
char_arr.fromunicode(' World')
print("Char array after append:", char_arr)


# 16. Slice Elements from an array
# Time: O(k), Space: O(k)
arr_16 = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
slice_arr = arr_16[2:9]
print("\n16. Sliced array [2:9]:", slice_arr.tolist())
