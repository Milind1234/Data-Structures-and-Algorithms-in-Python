# note.py
# Pattern to print:
#     *    
#    ***   
#   *****  
#  ******* 
# *********
#  ******* 
#   *****  
#    ***   
#     *

# ----------------------------------------------------------
# Version 1: Your Original Code (with explanations)
# ----------------------------------------------------------
def pattern_original():
    n = int(input("Enter the number of rows: "))
    
    # Upper Pyramid
    for i in range(n):
        # Spaces = n - i - 1, Stars = 2 * i + 1
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
    # Lower Inverted Pyramid
    for j in range(n):
        # Spaces = j + 1, Stars = 2 * (n - j) - 3
        print(" " * (j + 1) + "*" * (2 * (n - j) - 3))

# ----------------------------------------------------------
# Dry Run for n = 5
# ----------------------------------------------------------
# Upper Part:
# i = 0 -> spaces=4, stars=1 -> "    *"
# i = 1 -> spaces=3, stars=3 -> "   ***"
# i = 2 -> spaces=2, stars=5 -> "  *****"
# i = 3 -> spaces=1, stars=7 -> "  *******"
# i = 4 -> spaces=0, stars=9 -> "*********"
#
# Lower Part:
# j = 0 -> spaces=1, stars=7 -> "  *******"
# j = 1 -> spaces=2, stars=5 -> "   *****"
# j = 2 -> spaces=3, stars=3 -> "    ***"
# j = 3 -> spaces=4, stars=1 -> "     *"
# j = 4 -> spaces=5, stars=-1 -> "" (prints nothing)

# ----------------------------------------------------------
# Version 2: Simplified Version (clean & beginner-friendly)
# ----------------------------------------------------------
def pattern_simplified():
    n = int(input("Enter the number of rows: "))

    # Upper Pyramid
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

    # Lower Pyramid (starts from second-last row)
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# ----------------------------------------------------------
# Call the functions
# ----------------------------------------------------------
pattern_original()
pattern_simplified()
