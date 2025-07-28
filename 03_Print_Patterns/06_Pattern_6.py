# Pattern Printing using Nested Loops
# Goal: Print numbers in decreasing order per row
# Example for n = 5:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def pattern():
    # Ask user for number of rows
    n = int(input("Enter the number of rows: "))
    
    # Outer loop → controls rows (1 to n)
    for i in range(1, n + 1):
        # Inner loop → prints numbers from 1 to (n - i + 1)
        for j in range(1, n - i + 2):
            print(j, end=" ")  # print number with space, stay on same line
        print()  # move to the next line after finishing one row


# Function call
pattern()


"""
--- EXPLANATION OF FLOW ---

1. Outer Loop (for rows):
   - Runs 'n' times → i = 1, 2, 3, ..., n
   - Each iteration prints one row.

2. Inner Loop (for columns):
   - Prints numbers from 1 up to (n - i + 1).
   - Row 1 → prints numbers from 1 to n
   - Row 2 → prints numbers from 1 to n-1
   - Row 3 → prints numbers from 1 to n-2
   - ...
   - Last row → prints only 1

3. print() after inner loop:
   - Moves the cursor to the next line after one row is complete.

--- STEP-BY-STEP EXECUTION (Example: n = 5) ---
- i = 1 → inner loop prints "1 2 3 4 5" → next line
- i = 2 → inner loop prints "1 2 3 4" → next line
- i = 3 → inner loop prints "1 2 3" → next line
- i = 4 → inner loop prints "1 2" → next line
- i = 5 → inner loop prints "1" → next line

--- FINAL OUTPUT (n = 5) ---
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
