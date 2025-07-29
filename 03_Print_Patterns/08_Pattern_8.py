# note.py
# Pattern to print:
# *********
#  *******
#   *****
#    ***
#     *

# ---------------------------------------------------------
# Version 1: Using Two Loops (spaces and stars separately)
# ---------------------------------------------------------
def pattern():
    n = int(input("Enter the number of rows: "))
    for i in range(n):
        # i -> current row index (starts at 0)
        # For each row:
        #   Spaces = i
        #   Stars  = 2 * (n - i) - 1

        # Print spaces
        print(" " * i, end="")

        # Print stars
        for j in range(2 * (n - i) - 1):
            print("*", end="")

        # Move to the next line after one row
        print()

# ---------------------------------------------------------
# Version 2: Using a single print statement (simplified)
# ---------------------------------------------------------
def pattern_simplified():
    n = int(input("Enter the number of rows: "))
    for i in range(n):
        # Print spaces + stars directly
        print(" " * i + "*" * (2 * (n - i) - 1))

# ---------------------------------------------------------
# Dry Run Example for n = 5
# ---------------------------------------------------------
# Row 0:
#   i = 0 -> spaces = 0, stars = 2*(5-0)-1 = 9
#   Output: "*********"
#
# Row 1:
#   i = 1 -> spaces = 1, stars = 2*(5-1)-1 = 7
#   Output: " *******"
#
# Row 2:
#   i = 2 -> spaces = 2, stars = 2*(5-2)-1 = 5
#   Output: "  *****"
#
# Row 3:
#   i = 3 -> spaces = 3, stars = 2*(5-3)-1 = 3
#   Output: "   ***"
#
# Row 4:
#   i = 4 -> spaces = 4, stars = 2*(5-4)-1 = 1
#   Output: "    *"

# ---------------------------------------------------------
# Call the functions
# ---------------------------------------------------------
pattern()
pattern_simplified()
