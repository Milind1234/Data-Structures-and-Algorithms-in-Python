def fibonacci(n):
    # Base Case 1: fibonacci(0) = 0
    if n == 0:
        return 0
    # Base Case 2: fibonacci(1) = 1
    elif n == 1:
        return 1

    # Recursive Case:
    # fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(n-1) + fibonacci(n-2)


# Driver Code
print(fibonacci(5))  # Expected Output: 5


"""
--- STACK WORKING EXPLANATION FOR fibonacci(5) ---

Initial Call: fibonacci(5)
1. fibonacci(5) → fibonacci(4) + fibonacci(3)
        | fibonacci(4) |
        | fibonacci(5) |

2. fibonacci(4) → fibonacci(3) + fibonacci(2)
        | fibonacci(3) |
        | fibonacci(4) |
        | fibonacci(5) |

3. fibonacci(3) → fibonacci(2) + fibonacci(1)
        | fibonacci(2) |
        | fibonacci(3) |
        | fibonacci(4) |
        | fibonacci(5) |

4. fibonacci(2) → fibonacci(1) + fibonacci(0)
        | fibonacci(1) |
        | fibonacci(2) |
        | fibonacci(3) |
        | fibonacci(4) |
        | fibonacci(5) |

5. fibonacci(1) → Base Case → returns 1
6. fibonacci(0) → Base Case → returns 0

--- UNWINDING (Calculations start) ---
- fibonacci(2) = 1 + 0 = 1
- fibonacci(3) = 1 + 1 = 2
- fibonacci(4) = 2 + 1 = 3
- fibonacci(5) = 3 + 2 = 5

--- FINAL OUTPUT ---
5
"""
