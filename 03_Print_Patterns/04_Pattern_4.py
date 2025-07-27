# Pattern Printing using Nested Loops
# Goal: Print numbers in a right-angled triangle
# Each row contains the same number repeated equal to its row number
# Example for n = 5:
# 1
# 22
# 333
# 4444
# 55555

def pattern():
    # Ask user for number of rows
    n = int(input("Enter number of rows: "))
    
    # Outer loop → controls number of rows
    for i in range(1, n + 1):
        # Inner loop → prints the row number 'i' exactly 'i' times
        for j in range(1, i + 1):
            print(i, end=" ")   # print row number with space, stay on same line
        print()  # move to the next line after finishing one row


# Function call
pattern()


"""
--- EXPLANATION OF FLOW ---

1. Outer Loop (for rows):
   - Runs 'n' times → i = 1, 2, 3, ..., n
   - Each iteration prints one row.

2. Inner Loop (for columns):
   - Runs 'i' times for each row.
   - Prints the current row number 'i' for all positions in that row.
   - Row 1 → prints: 1
   - Row 2 → prints: 2 2
   - Row 3 → prints: 3 3 3
   - Row 4 → prints: 4 4 4 4
   - Row 5 → prints: 5 5 5 5 5

3. print() after inner loop:
   - Moves the cursor to the next line after one row is complete.

--- STEP-BY-STEP EXECUTION (Example: n = 5) ---
- i = 1 → inner loop prints "1" → next line
- i = 2 → inner loop prints "2 2" → next line
- i = 3 → inner loop prints "3 3 3" → next line
- i = 4 → inner loop prints "4 4 4 4" → next line
- i = 5 → inner loop prints "5 5 5 5 5" → next line

--- FINAL OUTPUT (n = 5) ---
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
