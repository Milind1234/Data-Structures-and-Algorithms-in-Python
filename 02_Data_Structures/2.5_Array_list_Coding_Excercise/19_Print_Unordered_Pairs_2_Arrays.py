"""
------------------------------------------------------
Print Unordered Pairs from Two Different Arrays
------------------------------------------------------

🧾 Question:
Write a function to print all **pairs** formed by taking one element from `array1` 
and one element from `array2`.

Example:
Input:
    array1 = [1, 2, 3, 4, 5]
    array2 = [6, 7, 8, 9, 10]
Output:
    1 6
    1 7
    1 8
    1 9
    1 10
    2 6
    ...
    5 10

------------------------------------------------------

🧠 Steps to Solve:
1. Loop through every element of `array1` using index `i`.
2. For each element in `array1`, loop through every element of `array2` using index `j`.
3. Print each pair `(array1[i], array2[j])`.

------------------------------------------------------

🕒 Time Complexity:
- Outer loop runs `len(array1)` times.
- Inner loop runs `len(array2)` times for each element of array1.
- Total complexity = O(n × m), 
  where n = length of array1 and m = length of array2.

💾 Space Complexity:
- O(1) → No extra space used except for loop variables.

------------------------------------------------------

# ✅ Code
"""

def printUnorderedPairs_2_Arrays(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            print(f"{array1[i]}  {array2[j]}")

# Example Call
printUnorderedPairs_2_Arrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])

"""
------------------------------------------------------
Note:
- All possible pair combinations are printed.
- Since arrays are different, no duplicate checking is needed.
------------------------------------------------------
"""
