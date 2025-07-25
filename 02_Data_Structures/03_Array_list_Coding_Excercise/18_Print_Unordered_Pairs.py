"""
------------------------------------------------------
Print Unordered Unique Pairs from a List
------------------------------------------------------

🧾 Question:
Write a function to print all **unique unordered pairs** from a given list.  
Unordered pairs mean:
- (1,2) is the same as (2,1) → Only one should be printed.
- No self-pairs like (1,1).

Example:
Input: [1, 2, 3, 4, 5]
Output:
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5

------------------------------------------------------

🧠 Steps to Solve:
1. Loop through the array with index `i` from 0 to n-1.
2. For each element at index `i`, loop from index `i+1` to n-1 (to avoid duplicate and self-pairs).
3. Print the pair `(array[i], array[j])`.

------------------------------------------------------

🕒 Time Complexity:
- Outer loop runs n times.
- Inner loop runs (n-i-1) times.
- Total complexity = O(n²) (since all unique pairs are considered).

💾 Space Complexity:
- O(1) → No additional space used (besides output).

------------------------------------------------------

# ✅ Code
"""

def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(f"{array[i]}  {array[j]}")

# Example Call
printUnorderedPairs([1, 2, 3, 4, 5])

"""
------------------------------------------------------
Note:
- Avoids duplicate commutative pairs like (2,1) if (1,2) is already printed.
- Avoids self-pairs like (1,1).
- Useful for pair-based problems (e.g., 2-sum variations, graph edge pairs).
------------------------------------------------------
"""
