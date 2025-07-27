# Pattern Printing using Nested Loops
# Goal: Print a square of stars (4x4)
def print_square_pattern():  
    # Ask user for number of rows
    n = int(input("Enter number of rows: "))
    
    # Outer loop → controls rows
    for i in range(n):
        # Inner loop → controls columns
        for j in range(n):
            print("*", end="")  # Print star on same line
        print()  # Move to next line after one row


# Function call
print_square_pattern()
print_square_pattern()

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
