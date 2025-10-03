# ===================================================================
# 🧠 PYTHON LIST & FUNCTION BEHAVIOR — MCQ STYLE EXPLANATIONS
# ===================================================================

# 🔹 QUESTION 1: Function Arguments and Mutability
def f(value, values):
    v = 1
    values[0] = 44

t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])  # ✅ Output: 3 44

"""
✔️ Explanation:
- Lists are mutable → changes inside the function affect the original list.
- 't' is passed by value (int is immutable), so it remains 3.
"""

# -------------------------------------------------------------------

# 🔹 QUESTION 2: List Slicing with Negative Step
a = [1, 2, 3, 4, 5]
print(a[3:0:-1])  # ✅ Output: [4, 3, 2]

"""
✔️ Explanation:
a[start:stop:step] → from index 3 to index 0 (exclusive), in reverse.
Picks: a[3]=4, a[2]=3, a[1]=2 → [4, 3, 2]
"""

# -------------------------------------------------------------------

# 🔹 QUESTION 3: List References vs Copies
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1              # Same reference
fruit_list3 = fruit_list1[:]           # Shallow copy

fruit_list2[0] = 'Guava'               # Affects fruit_list1
fruit_list3[1] = 'Kiwi'                # Only affects fruit_list3

print(fruit_list1)  # ['Guava', 'Berry', 'Cherry', 'Papaya']
print(fruit_list2)  # ['Guava', 'Berry', 'Cherry', 'Papaya']
print(fruit_list3)  # ['Apple', 'Kiwi', 'Cherry', 'Papaya']

# Count Guava/Kiwi
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)  # ✅ Output: 22

"""
✔️ Explanation:
- 2 lists have Guava at index 0 → +2
- 1 list has Kiwi at index 1 → +20
→ 2 + 20 = 22
"""

# -------------------------------------------------------------------

# 🔹 QUESTION 4: Shifting Elements Left in a List
arr = [1, 2, 3, 4, 5, 6]

for i in range(1, 6):
    arr[i - 1] = arr[i]

for i in range(0, 6):
    print(arr[i], end=" ")  # ✅ Output: 2 3 4 5 6 6

"""
✔️ Explanation:
- Each element shifts left by one
- Last element is duplicated
"""

# -------------------------------------------------------------------

# 🔹 QUESTION 5: Popping from Sub-Lists
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]

for i in range(0, 4):
    print(arr[i].pop())  # ✅ Output: 4 7 11 15

"""
✔️ Explanation:
- pop() removes the last element of each sublist.
"""

# -------------------------------------------------------------------

# 🔹 QUESTION 6: Shuffle a List Correctly
import random

fruit = ['apple', 'banana', 'papaya', 'cherry']
random.shuffle(fruit)  # ✅ Correct

"""
✔️ Explanation:
- Only `random.shuffle(list)` works.
- fruit.shuffle() → ❌ invalid
- random.shuffleList() → ❌ not a function
"""

# -------------------------------------------------------------------

# 🔹 QUESTION 7: Slice Assignment with Mismatched Sizes
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[::2] = 10, 20, 30, 40, 50, 60  # ❌ ValueError

"""
❌ ERROR:
- a[::2] targets 5 elements (indexes 0,2,4,6,8)
- Right-hand side has 6 elements → mismatch
→ Raises: ValueError
"""

# -------------------------------------------------------------------

# 🔹 QUESTION 8: Basic List Slicing with Step
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])  # ✅ Output: [1, 3, 5, 7, 9]

"""
✔️ Explanation:
- Every 2nd element from start to end → step = 2
"""

# -------------------------------------------------------------------

# 🔹 QUESTION 9: Max Value in 2D List
data = [[[1, 2], [3, 4]],
        [[5, 6], [7, 8]]]

def fun(m):
    v = m[0][0]
    for row in m:
        for element in row:
            if v < element:
                v = element
    return v

print(fun(data[0]))  # ✅ Output: 4

"""
✔️ Explanation:
- fun(data[0]) → processes: [[1, 2], [3, 4]]
- Finds max value → 4
"""

# ===================================================================
# ✅ End of Notes
# ===================================================================
