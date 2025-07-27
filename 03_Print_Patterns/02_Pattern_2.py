# Pattern Printing using Nested Loops
# Goal: Print a right-angled triangle of stars

def print_triangle_pattern():
    # Ask user for number of rows
    n = int(input("Enter number of rows: "))

    # Outer loop → controls rows (1 to n)
    for i in range(n):
        # Inner loop → prints '*' i times
        for j in range(i+1):
            print("*", end=" ")  # print star with space, stay on same line
        print()  # move to the next line after finishing one row


# Function call
print_triangle_pattern()


"""
--- EXPLANATION OF FLOW ---

1. Outer Loop (for rows):
   - Runs 'n' times → i = 1, 2, 3, ..., n
   - Each iteration prints one row of stars.

2. Inner Loop (for columns):
   - Runs 'i' times for each row.
   - On row 1 → prints 1 star
   - On row 2 → prints 2 stars
   - On row 3 → prints 3 stars
   - and so on...

3. print() after inner loop:
   - Moves the cursor to the next line after one row is complete.

--- STEP-BY-STEP EXECUTION (Example: n = 4) ---
- i = 1 → inner loop prints "* " → print() moves to new line
- i = 2 → inner loop prints "* * " → print() moves to new line
- i = 3 → inner loop prints "* * * " → print() moves to new line
- i = 4 → inner loop prints "* * * * " → print() moves to new line

--- FINAL OUTPUT (n = 4) ---
* 
* * 
* * * 
* * * *
"""
