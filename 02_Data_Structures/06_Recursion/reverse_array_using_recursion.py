def reverse_array(arr, start, end):
    # Base Case: stop when start crosses or meets end (middle reached)
    if start >= end:
        return arr

    # Swap elements at positions start and end
    arr[start], arr[end] = arr[end], arr[start]

    # Recursive call for the inner part of the array
    return reverse_array(arr, start + 1, end - 1)


# Driver Code
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr, 0, len(arr) - 1))  # Expected output: [5, 4, 3, 2, 1]


"""
--- STACK WORKING EXPLANATION FOR reverse_array([1,2,3,4,5], 0, 4) ---

1. Initial Call: reverse_array(arr, 0, 4)
   Swap arr[0] & arr[4] → [5, 2, 3, 4, 1]
   Calls reverse_array(arr, 1, 3)
        | reverse_array(1,3) |
        | reverse_array(0,4) |

2. Second Call: reverse_array(arr, 1, 3)
   Swap arr[1] & arr[3] → [5, 4, 3, 2, 1]
   Calls reverse_array(arr, 2, 2)
        | reverse_array(2,2) |
        | reverse_array(1,3) |
        | reverse_array(0,4) |

3. Third Call: reverse_array(arr, 2, 2)
   Base Case hit (start >= end) → return array

--- UNWINDING (stack returns back) ---
- reverse_array(2,2) returns → reverse_array(1,3) returns → reverse_array(0,4) returns

--- FINAL OUTPUT ---
[5, 4, 3, 2, 1]
"""
