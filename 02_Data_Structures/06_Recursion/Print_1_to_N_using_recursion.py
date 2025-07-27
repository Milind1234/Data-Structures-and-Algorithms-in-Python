def print_numbers(current, n):
    # Base Case: Stop recursion when current > n
    if current > n:
        return
    
    # Print the current number
    print(current)
    
    # Recursive call: Ask the function to handle the next number
    print_numbers(current + 1, n)


# Driver code to start printing from 1 to n
n = 5
print_numbers(1, n)


"""
--- STACK WORKING EXPLANATION ---
1. Initial Call: print_numbers(1, 5)
   -> Adds print_numbers(1,5) to stack

2. print_numbers(1,5) calls print_numbers(2,5)
   -> Stack grows:
        | print_numbers(2,5) |
        | print_numbers(1,5) |

3. print_numbers(2,5) calls print_numbers(3,5)
   -> Stack grows:
        | print_numbers(3,5) |
        | print_numbers(2,5) |
        | print_numbers(1,5) |

4. Similarly it calls print_numbers(4,5) then print_numbers(5,5)
   -> Stack at max:
        | print_numbers(5,5) |
        | print_numbers(4,5) |
        | print_numbers(3,5) |
        | print_numbers(2,5) |
        | print_numbers(1,5) |

5. print_numbers(5,5) calls print_numbers(6,5)
   -> Base case hit (6 > 5), return back

6. Now stack starts UNWINDING (functions finish one by one):
        print_numbers(6,5) removed
        print_numbers(5,5) removed
        print_numbers(4,5) removed
        print_numbers(3,5) removed
        print_numbers(2,5) removed
        print_numbers(1,5) removed

--- OUTPUT SEEN ON SCREEN ---
1
2
3
4
5
"""
