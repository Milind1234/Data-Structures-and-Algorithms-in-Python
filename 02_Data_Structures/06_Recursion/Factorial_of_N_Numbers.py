def fact(n):
    # Base Case: If n becomes 1, stop recursion and return 1
    # (Since factorial of 1 is 1)
    if n == 1:
        return 1

    # Recursive Case:
    # fact(n) = n * fact(n-1)
    return fact(n - 1) * n


# Driver Code
print(fact(4))  # Expected output: 24


"""
--- STACK WORKING EXPLANATION FOR fact(4) ---
1. Initial call: fact(4)
   -> Needs fact(3), so stack grows

2. fact(4) waits for fact(3):
        | fact(3) |
        | fact(4) |

3. fact(3) waits for fact(2):
        | fact(2) |
        | fact(3) |
        | fact(4) |

4. fact(2) waits for fact(1):
        | fact(1) |
        | fact(2) |
        | fact(3) |
        | fact(4) |

5. fact(1) hits base case → returns 1

--- UNWINDING (calculations start) ---
- fact(2) = fact(1) * 2 = 1 * 2 = 2
- fact(3) = fact(2) * 3 = 2 * 3 = 6
- fact(4) = fact(3) * 4 = 6 * 4 = 24

--- FINAL OUTPUT ---
24
"""
