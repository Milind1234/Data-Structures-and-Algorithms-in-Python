# Pattern Printing using Nested Loops
# Goal: Print an inverted right-angled triangle of stars
# Example for n = 5:
# * * * * *
# * * * *
# * * *
# * *
# *

def print_triangle_pattern():
    # Ask user for number of rows
    n = int(input("Enter number of rows: "))

    # Outer loop → controls rows (from 1 to n)
    for i in range(1, n + 1):
        # Inner loop → prints (n - i + 1) stars for each row
        for j in range(n - i + 1):
            print("*", end=" ")  # print star with space, stay on same line
        print()  # move to the next line after finishing one row


# Function call
print_triangle_pattern()


"""
--- EXPLANATION OF FLOW ---

1. Outer Loop (for rows):
   - Runs 'n' times → i = 1, 2, 3, ..., n
   - Each iteration prints one row.

2. Inner Loop (for columns):
   - Prints stars for each row.
   - Row 1 → prints n stars
   - Row 2 → prints n-1 stars
   - Row 3 → prints n-2 stars
   - ...
   - Last row → prints 1 star

3. print() after inner loop:
   - Moves the cursor to the next line after one row is complete.

--- STEP-BY-STEP EXECUTION (Example: n = 5) ---
- i = 1 → prints "* * * * * " → next line
- i = 2 → prints "* * * * " → next line
- i = 3 → prints "* * * " → next line
- i = 4 → prints "* * " → next line
- i = 5 → prints "* " → next line

--- FINAL OUTPUT (n = 5) ---
* * * * *
* * * *
* * *
* *
*
"""
