# Pattern to print:
#      *     
#     ***    
#    *****   
#   *******  
#  ********* 
# ***********

# ----------------------------------------------------------
# Simplified Version
# ----------------------------------------------------------

def pattern():
    n = int(input("Enter the number of rows: "))

    # Outer loop -> controls the number of rows
    for i in range(n):
        # Explanation:
        # i = current row number (starting from 0)
        # For each row:
        #   Spaces = (n - i - 1)
        #   Stars  = (2 * i + 1)
        #
        # Example for n=6:
        # Row 0 -> spaces=5, stars=1  -> "     *"
        # Row 1 -> spaces=4, stars=3  -> "    ***"
        # Row 2 -> spaces=3, stars=5  -> "   *****"
        # Row 3 -> spaces=2, stars=7  -> "  *******"
        # Row 4 -> spaces=1, stars=9  -> " *********"
        # Row 5 -> spaces=0, stars=11 -> "***********"

        # Print spaces and stars together
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

        # Each iteration ends with moving to the next line automatically
        # because print() by default adds a newline

# Dry Run for n = 6:
# i = 0 -> spaces=5, stars=1  -> "     *"
# i = 1 -> spaces=4, stars=3  -> "    ***"
# i = 2 -> spaces=3, stars=5  -> "   *****"
# i = 3 -> spaces=2, stars=7  -> "  *******"
# i = 4 -> spaces=1, stars=9  -> " *********"
# i = 5 -> spaces=0, stars=11 -> "***********"

pattern()

# Pattern to print:
#      *     
#     ***    
#    *****   
#   *******  
#  ********* 
# ***********

# ----------------------------------------------------------
# Original Code with Explanation
# ----------------------------------------------------------
def pattern():
    n = int(input("Enter the number of rows: "))
    
    # Outer loop controls rows
    for i in range(n):
        # For each row:
        #   Spaces = (n - i - 1)
        #   Stars  = (2 * i + 1)
        
        # Inner loop to print spaces
        print(" " * (n - i - 1), end="")  # end="" -> stay on same line
        
        # Inner loop to print stars
        for j in range(2 * i + 1):
            print("*", end="")
        
        # Move to next line
        print()

# ----------------------------------------------------------
# Dry Run Example (n = 6)
# ----------------------------------------------------------
# i = 0:
#   spaces = n - i - 1 = 6 - 0 - 1 = 5 -> "     "
#   stars  = 2 * i + 1 = 2 * 0 + 1 = 1 -> "*"
#   Output: "     *"
#
# i = 1:
#   spaces = 4 -> "    "
#   stars  = 3 -> "***"
#   Output: "    ***"
#
# i = 2:
#   spaces = 3 -> "   "
#   stars  = 5 -> "*****"
#   Output: "   *****"
#
# i = 3:
#   spaces = 2 -> "  "
#   stars  = 7 -> "*******"
#   Output: "  *******"
#
# i = 4:
#   spaces = 1 -> " "
#   stars  = 9 -> "*********"
#   Output: " *********"
#
# i = 5:
#   spaces = 0 -> ""
#   stars  = 11 -> "***********"
#   Output: "***********"

# ----------------------------------------------------------
# Calling the function
# ----------------------------------------------------------
pattern()
