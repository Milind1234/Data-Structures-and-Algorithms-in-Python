# -----------------------------------------------------------
# 🧠 Understanding O(log n) Time Complexity - Beginner Friendly
# -----------------------------------------------------------

"""
O(log n) means the number of steps grows slowly even if the input grows fast.
We divide the problem into half each time — this is called **Divide and Conquer**.

Let’s understand it with an example.
Suppose we have a sorted array of 8 elements like this:
"""

# 👁️ Visual representation of the array:
print("""
  ________________________________________________
 |     |     |     |     |     |     |     |     |
 |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
 |_____|_____|_____|_____|_____|_____|_____|_____|
""")

# 📌 We want to find number 1 by dividing the array again and again.

arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 1

# Simulating how many times we divide the array to find the target
low = 0
high = len(arr) - 1
steps = 0

while low <= high:
    steps += 1
    mid = (low + high) // 2
    print(f"Step {steps}: Checking element {arr[mid]} at index {mid}")

    if arr[mid] == target:
        print(f"\n✅ Found {target} at index {mid} in {steps} steps.\n")
        break
    elif arr[mid] > target:
        high = mid - 1
    else:
        low = mid + 1

# 🔍 Explanation of log₂(8) = 3

"""
We had 8 elements.
Each time we divided the array by 2.

Step 1: 8 → 4 elements
Step 2: 4 → 2 elements
Step 3: 2 → 1 element

So in 3 steps, we reached the target.

That’s because:

   2^3 = 8   →  log₂(8) = 3

We ask: "2 to the power of what gives 8?" → the answer is 3

So if we had 1 million elements, log₂(1,000,000) ≈ 20 steps only!
That's the power of O(log n)!
"""