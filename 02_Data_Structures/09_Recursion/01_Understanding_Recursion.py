# ------------------------------------------------------------
# 📘 RECURSION - Complete Notes
# ✅ Topic: Understanding Recursion (with Examples & Code)
# ------------------------------------------------------------
"""
Welcome to this detailed guide on Recursion!

This file is designed for absolute beginners.
By the end, you will understand:
✅ What recursion is
✅ How it works internally (stack mechanism)
✅ Recursion vs Iteration
✅ When to use or avoid recursion
✅ How to write recursive functions in 3 simple steps
✅ Real examples: Factorial & Fibonacci
✅ How to measure recursive algorithm complexity

Let's start!
"""

# ============================================================
# 🧩 1. WHAT IS RECURSION?
# ============================================================

"""
📘 Definition:
Recursion is a method of solving a problem where the solution
depends on solutions to smaller instances of the *same problem*.

In simple words:
👉 A function that calls itself until a base condition is met.

Example:
    def example():
        example()   # This function calls itself (recursive)

But to make recursion work correctly, we MUST have:
1️⃣ A smaller subproblem in each call
2️⃣ A base case to stop recursion
"""

# ============================================================
# 🎯 2. REAL-LIFE EXAMPLE — RUSSIAN NESTING DOLL
# ============================================================

"""
Imagine a set of Russian dolls (Matryoshka dolls):

[ 🪆1 ]  →  [ 🪆2 ]  →  [ 🪆3 ]  →  [ 🪆4 (smallest) ]

Each doll contains a smaller one inside.
Every time you open a doll, you perform the SAME OPERATION
on a smaller version of the same problem.

🧠 Visualization:

Open(🪆1)
 └── Open(🪆2)
      └── Open(🪆3)
           └── Open(🪆4) → (Base case: smallest doll, stop)

This is the essence of recursion — performing the same operation
on smaller inputs until reaching a point where no further action is needed.
"""

# ============================================================
# 🧠 3. MAIN PROPERTIES OF RECURSION
# ============================================================

"""
From the Russian doll example, recursion has three properties:

1️⃣ Same operation repeated with different inputs
   ➤ Each time, we open a smaller doll (input shrinks)

2️⃣ The problem size reduces each step
   ➤ Every recursive call simplifies the problem

3️⃣ Base condition (stopping criteria)
   ➤ When we reach the smallest doll → Stop!
   ➤ Without it → infinite recursion (system crash)

💡 Example of infinite recursion joke:
A programmer’s wife says: "While you’re out, buy some milk."
He never comes back. 🥛 (No base case!)
"""

# ============================================================
# ⚙️ 4. HOW RECURSION WORKS INTERNALLY (STACK MEMORY)
# ============================================================

"""
Every time a function is called, Python stores it in the **Call Stack**.
This stack follows LIFO (Last In, First Out).

🧩 Example with 4 functions:

def first():
    second()
    print("I am first")

def second():
    third()
    print("I am second")

def third():
    fourth()
    print("I am third")

def fourth():
    print("I am fourth")

When you call first():
1️⃣ first() is pushed to stack
2️⃣ first() calls second() → push second()
3️⃣ second() calls third() → push third()
4️⃣ third() calls fourth() → push fourth()

Now stack = [first, second, third, fourth]
➡ Execute fourth() → pop it
➡ Resume third() → pop it
➡ Resume second() → pop it
➡ Resume first() → pop it

🧠 LIFO visualization:
Push: first → second → third → fourth
Pop: fourth → third → second → first
"""

# ============================================================
# 🔁 5. RECURSION vs ITERATION
# ============================================================

"""
Both recursion and iteration can solve similar problems.

| Property        | Recursion                              | Iteration                     |
|-----------------|-----------------------------------------|--------------------------------|
| Memory          | Uses call stack (O(n))                  | Uses single loop variable (O(1)) |
| Speed           | Slower (function call overhead)         | Faster                        |
| Simplicity      | Easier for divide-and-conquer problems  | Easier for repetitive tasks   |
| Readability     | Clean & elegant                         | More manual steps             |
| Example Use     | Trees, Graphs, Divide & Conquer, DP     | Counting, Summation, Loops    |

💡 Conclusion:
- Use recursion for *subdivisible* problems (trees, DFS, etc.)
- Use iteration for performance-critical loops.
"""

# ============================================================
# ⚖️ 6. WHEN TO USE OR AVOID RECURSION
# ============================================================

"""
✅ Use recursion when:
- The problem divides into smaller similar subproblems
- You need elegant code (e.g. tree traversal, factorial)
- You have sufficient memory & time margin

🚫 Avoid recursion when:
- You have strict performance limits
- You’re coding for low-memory environments (mobile, embedded)
- The input is very large (risk of stack overflow)
- Simple loops can do the same work faster
"""

# ============================================================
# 🧭 7. WRITING RECURSIVE FUNCTIONS IN 3 STEPS
# ============================================================

"""
🪄 The 3-Step Recursion Template

Step 1️⃣ — Identify Recursive Case
   - Express the problem in terms of smaller instances.

Step 2️⃣ — Identify Base Case
   - Define stopping condition.

Step 3️⃣ — Handle Unintentional Cases
   - Validate inputs (avoid infinite loops or invalid data)
"""

# ============================================================
# 📗 EXAMPLE 1: FACTORIAL USING RECURSION
# ============================================================

def factorial(n):
    """Return factorial of n using recursion."""
    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer"

    # 🧩 Step 2: Base case
    if n == 0 or n == 1:
        return 1

    # 🔁 Step 1: Recursive case
    return n * factorial(n - 1)


"""
📘 Explanation:
factorial(n) = n * factorial(n-1)

Example:
factorial(4)
= 4 * factorial(3)
= 4 * (3 * factorial(2))
= 4 * (3 * (2 * factorial(1)))
= 4 * 3 * 2 * 1
= 24

🧠 Visualization:
factorial(4)
 ├─ factorial(3)
 │   ├─ factorial(2)
 │   │   ├─ factorial(1)
 │   │   └─ return 1
 │   └─ return 2
 └─ return 24
"""

# ============================================================
# 📘 EXAMPLE 2: FIBONACCI USING RECURSION
# ============================================================

def fibonacci(n):
    """Return nth Fibonacci number using recursion."""
    assert isinstance(n, int) and n >= 0, "Fibonacci number must be positive integer"

    # 🧩 Base case
    if n == 0 or n == 1:
        return n

    # 🔁 Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


"""
📘 Fibonacci Definition:
F(0)=0, F(1)=1
F(n) = F(n-1) + F(n-2)

🧠 Visualization:
fib(4)
 ├─ fib(3)
 │   ├─ fib(2)
 │   │   ├─ fib(1)
 │   │   └─ fib(0)
 │   └─ fib(1)
 └─ fib(2)
     ├─ fib(1)
     └─ fib(0)
= 3

⚙️ Complexity:
- Naive recursive: O(2^n)
- With memoization: O(n)
"""

# ============================================================
# 📉 8. MEASURING RECURSIVE TIME COMPLEXITY
# ============================================================

"""
To find time complexity of recursive algorithms,
we use a recurrence relation.

🧩 Example: Find max element in array recursively
"""

def find_max(arr, n):
    """Return maximum element in array using recursion."""
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max(arr, n - 1))


"""
Example: arr = [11, 4, 12, 7]

find_max(arr, 4)
 → max(arr[3], find_max(arr, 3))
 → max(7, max(12, find_max(arr, 2)))
 → max(7, max(12, max(4, find_max(arr, 1))))
 → max(7, max(12, max(4, 11)))
 = 12

🧠 Recursive Visualization:
find_max(4)
 └── find_max(3)
      └── find_max(2)
           └── find_max(1) → 11

Time complexity analysis:

Let M(n) = time to solve problem of size n

M(n) = O(1) + M(n-1)
M(1) = O(1)

Expanding:
M(n) = O(1) + O(1) + ... (n times)
M(n) = O(n)

✅ So, Time Complexity = O(n)
✅ Space Complexity = O(n) (due to recursive stack)
"""

# ============================================================
# 📊 9. KEY TAKEAWAYS
# ============================================================

"""
⭐ Recursion is breaking down a big problem into smaller subproblems.
⭐ Base case prevents infinite recursion.
⭐ Stack memory keeps track of function calls.
⭐ Recursive functions can be measured using recurrence equations.
⭐ Recursive vs Iterative → readability vs performance tradeoff.
⭐ Factorial & Fibonacci are classic recursion examples.
⭐ Recursion’s space/time complexity depends on call depth & subcalls.
"""

# ============================================================
# 🧩 10. PRACTICE EXERCISES
# ============================================================

"""
1️⃣ Write a recursive function to sum elements of an array.
2️⃣ Write a recursive function to reverse a string.
3️⃣ Implement Fibonacci with memoization (use functools.lru_cache).
4️⃣ Write a recursive function to count digits of a number.
5️⃣ Modify find_max() to also return the index of max element.
"""

# ============================================================
# 🎉 END OF FILE
# ============================================================

"""
Congrats! 🎯
You now understand recursion completely:
- Concept
- Properties
- Internal working
- Comparison
- Examples
- Measuring complexity

Next topics will expand this knowledge to:
👉 Tree & Graph traversals (where recursion shines!)
"""

