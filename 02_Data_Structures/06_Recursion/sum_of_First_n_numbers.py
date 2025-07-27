def sum(n):
    # Base Case: if n becomes 0, stop recursion and return 0
    if n == 0:
        return 0

    # Recursive Case:
    # sum(n) = n + sum(n-1)
    return sum(n - 1) + n


# Driver Code
print(sum(5))  # Expected output: 15


"""
--- STACK WORKING EXPLANATION FOR sum(5) ---
1. Initial call: sum(5)
   -> Needs sum(4), so stack grows

2. sum(5) waits for sum(4):
        | sum(4) |
        | sum(5) |

3. sum(4) waits for sum(3):
        | sum(3) |
        | sum(4) |
        | sum(5) |

4. sum(3) waits for sum(2):
        | sum(2) |
        | sum(3) |
        | sum(4) |
        | sum(5) |

5. sum(2) waits for sum(1):
        | sum(1) |
        | sum(2) |
        | sum(3) |
        | sum(4) |
        | sum(5) |

6. sum(1) waits for sum(0):
        | sum(0) |
        | sum(1) |
        | sum(2) |
        | sum(3) |
        | sum(4) |
        | sum(5) |

7. sum(0) returns 0 → stack starts UNWINDING:
   - sum(1) = 0 + 1 = 1
   - sum(2) = 1 + 2 = 3
   - sum(3) = 3 + 3 = 6
   - sum(4) = 6 + 4 = 10
   - sum(5) = 10 + 5 = 15

--- FINAL OUTPUT ---
15
"""
