# Pattern Printing using Nested Loops
# Goal: Print a square of stars (4x4)

for i in range(0, 4):            # Outer loop → controls number of rows (4 rows)
    for j in range(0, 4):        # Inner loop → controls number of columns (4 columns)
        print("*", end="")       # Print star on the same line (end="" avoids new line)
    print()                      # Move to next line after printing one full row


"""
--- EXPLANATION OF FLOW ---

1. Outer Loop (for rows):
   - Runs 4 times → i = 0, 1, 2, 3
   - Each iteration prints one row of stars.

2. Inner Loop (for columns):
   - Runs 4 times for each row → j = 0, 1, 2, 3
   - Prints "*" without moving to the next line because of end=""

3. print() after inner loop:
   - Moves the cursor to the next line after one row is complete.

--- STEP-BY-STEP EXECUTION ---
- i = 0 → inner loop prints **** → print() moves to new line
- i = 1 → inner loop prints **** → print() moves to new line
- i = 2 → inner loop prints **** → print() moves to new line
- i = 3 → inner loop prints **** → print() moves to new line

--- FINAL OUTPUT ---
****
****
****
****
"""
