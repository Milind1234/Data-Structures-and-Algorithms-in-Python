"""
------------------------------------------------------
Print All Pairs from a List
------------------------------------------------------

🧾 Question:
Write a function to print all possible pairs from a given array/list.

Example:
Input: [1, 2, 3]
Output:
1 , 1
1 , 2
1 , 3
2 , 1
2 , 2
2 , 3
3 , 1
3 , 2
3 , 3

------------------------------------------------------

🧠 Steps to Solve:
1. Loop through every element in the array using a nested loop.
2. For each element i in the outer loop, pair it with every element j in the inner loop.
3. Print or store each pair.

------------------------------------------------------

🕒 Time Complexity:
- Outer loop runs n times.
- Inner loop runs n times for each element.
- Total complexity = O(n²)

💾 Space Complexity:
- O(1) → No additional space (besides output).

------------------------------------------------------

# ✅ Code
"""

def Print_Pairs(array):
    for i in array:
        for j in array:
            print(f"{i} , {j}")

# Example Call
Print_Pairs([1, 2, 3, 4, 5, 6])

"""
------------------------------------------------------
Note:
- This approach prints **all pairs**, including self-pairs (x,x) 
  and commutative duplicates (1,2) & (2,1).
- If only unique unordered pairs are required, logic needs modification.
------------------------------------------------------
"""
