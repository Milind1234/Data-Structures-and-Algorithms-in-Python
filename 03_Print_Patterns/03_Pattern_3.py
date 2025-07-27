# Pattern Printing using Nested Loops
# Goal: Print increasing numbers in a right-angled triangle
# Example for n = 5:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

def print_triangle_pattern():
    # Ask user for number of rows
    n = int(input("Enter number of rows: "))

    # Outer loop → controls rows (1 to n)
    for i in range(1, n + 1):
        # Inner loop → prints numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=" ")  # print number with space, stay on same line
        print()  # move to the next line after finishing one row


# Function call
print_triangle_pattern()


"""
--- EXPLANATION OF FLOW ---

1. Outer Loop (for rows):
   - Runs 'n' times → i = 1, 2, 3, ..., n
   - Each iteration prints one row of numbers.

2. Inner Loop (for columns):
   - Prints numbers from 1 up to the current row number 'i'.
   - Row 1 → prints: 1
   - Row 2 → prints: 1 2
   - Row 3 → prints: 1 2 3
   - Row 4 → prints: 1 2 3 4
   - and so on...

3. print() after inner loop:
   - Moves the cursor to the next line after one row is complete.

--- STEP-BY-STEP EXECUTION (Example: n = 5) ---
- i = 1 → prints "1" → next line
- i = 2 → prints "1 2" → next line
- i = 3 → prints "1 2 3" → next line
- i = 4 → prints "1 2 3 4" → next line
- i = 5 → prints "1 2 3 4 5" → next line

--- FINAL OUTPUT (n = 5) ---
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
