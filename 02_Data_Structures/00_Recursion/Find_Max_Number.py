# ------------------------------------------------------
# 📘 Recursive Algorithm Analysis Notes
# ✅ Topic: Measuring Recursive Algorithms
# ------------------------------------------------------

"""
📌 Problem Statement:
---------------------
We need to find the **maximum element** in a given array using recursion.

In the previous lecture, we learned to measure the time complexity of **iterative algorithms**
using 5 rules. Now we extend that logic to **recursive algorithms**.

We'll use the same problem — finding the largest number in an array — but
implement it recursively.
"""

# ------------------------------------------------------
# 🧠 Step 1: Recursive Function Definition
# ------------------------------------------------------

def findMaxNumRec(arr, n):
    """
    Recursive function to find the maximum number in an array.
    
    Parameters:
        arr : list of numbers
        n   : size of the array (int)
    
    Logic:
        1️⃣ Base Case: If n == 1 → return arr[0]
        2️⃣ Recursive Case: Compare last element with
            the maximum of the rest of the array (n-1 elements)
    """
    if n == 1:
        return arr[0]
    return max(arr[n - 1], findMaxNumRec(arr, n - 1))


# ------------------------------------------------------
# 🧩 Step 2: Visualization (Example)
# ------------------------------------------------------

"""
Sample Array:
-------------
A = [5, 4, 10, 8, 11, 88, 87, 10]
n = 8

Recursive Calls:
----------------
findMaxNumRec(A, 8)
→ max(A[7], findMaxNumRec(A, 7))
→ max(10, findMaxNumRec(A, 7))

findMaxNumRec(A, 7)
→ max(A[6], findMaxNumRec(A, 6))
→ max(87, findMaxNumRec(A, 6))

findMaxNumRec(A, 6)
→ max(A[5], findMaxNumRec(A, 5))
→ max(88, findMaxNumRec(A, 5))

findMaxNumRec(A, 5)
→ max(A[4], findMaxNumRec(A, 4))
→ max(11, findMaxNumRec(A, 4))

findMaxNumRec(A, 4)
→ max(A[3], findMaxNumRec(A, 3))
→ max(8, findMaxNumRec(A, 3))

findMaxNumRec(A, 3)
→ max(A[2], findMaxNumRec(A, 2))
→ max(10, findMaxNumRec(A, 2))

findMaxNumRec(A, 2)
→ max(A[1], findMaxNumRec(A, 1))
→ max(4, findMaxNumRec(A, 1))

findMaxNumRec(A, 1)
→ Base case reached → returns A[0] = 5


Call Stack Unwinding:
---------------------
max(4, 5) → 5
max(10, 5) → 10
max(8, 10) → 10
max(11, 10) → 11
max(88, 11) → 88
max(87, 88) → 88
max(10, 88) → 88

✅ Final Answer: 88
"""

arr = [5, 4, 10, 8, 11, 88, 87, 10]
print("Maximum element in array:", findMaxNumRec(arr, len(arr)))


# ------------------------------------------------------
# 🧮 Step 3: Time Complexity Analysis
# ------------------------------------------------------

"""
Let's measure this recursive algorithm.

We define:
M(n) = Time complexity of finding max in an array of size n.

From the function:
------------------
M(n) = O(1) + M(n-1)

Explanation:
------------
- The comparison (max) operation → O(1)
- The recursive call → M(n-1)
Thus:
    M(n) = O(1) + M(n-1)

Expanding:
-----------
M(n)   = 1 + M(n-1)
M(n-1) = 1 + M(n-2)
M(n-2) = 1 + M(n-3)
...
M(1)   = O(1)

Substituting backward:
M(n) = 1 + (1 + (1 + ... + O(1)))
     = n * O(1)
     = O(n)

✅ Therefore, Time Complexity = O(n)
-------------------------------------

🔸 Why?
Because the function makes a single recursive call in each step,
and each call performs constant work (one comparison).

If the recursion had **two calls per step** (like Fibonacci),
the recurrence would double → O(2ⁿ).

So in our case:
M(n) = M(n-1) + O(1)
→ Linear recursion → O(n)
"""

# ------------------------------------------------------
# 💾 Step 4: Space Complexity Analysis
# ------------------------------------------------------

"""
In recursion, space complexity = function call stack depth.

Each recursive call waits for the next one to complete.
So, for n elements, recursion depth = n.

Hence:
✅ Space Complexity = O(n)

(Note: Iterative version would be O(1) space.)
"""

# ------------------------------------------------------
# 🧠 Summary
# ------------------------------------------------------

"""
📋 Summary Table:
-----------------
| Operation Type | Complexity | Reason                           |
|----------------|-------------|-----------------------------------|
| Time           | O(n)        | Single recursive call per level   |
| Space          | O(n)        | Stack grows linearly with n       |

🎯 Key Takeaways:
-----------------
1️⃣ Base case returns constant time O(1).
2️⃣ Each recursive call reduces the problem size by 1.
3️⃣ Total of n calls → Linear growth.
4️⃣ Formula: M(n) = O(1) + M(n-1)
5️⃣ Final Complexity: O(n)
"""

# ------------------------------------------------------
# ✅ OUTPUT:
# Maximum element in array: 88
# ------------------------------------------------------
