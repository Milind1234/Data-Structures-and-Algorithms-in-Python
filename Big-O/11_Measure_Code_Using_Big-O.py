# How to Measure the Codes Using Big O
# -------------------------------------

# RULES TO FOLLOW FOR BIG O MEASUREMENT:
#  |----------|------------------------------------------------------------------------------------|----------------|
#  |  Rule 1: | Any assignment statements and if statements that are executed once                 |                |
#  |          | regardless of the size of the problem take                                         |       O(1).    |
#  |  Rule 2: | A simple for loop from 0 to n (with no internal loops) takes                       |       O(n).    |
#  |  Rule 3: | A nested loop of the same type takes quadratic time:                               |       O(n^2).  |
#  |  Rule 4: | A loop in which the controlling parameter is divided by two at each step takes     |       O(log n).|
#  |  Rule 5: | When dealing with multiple statements, just add them up.                           |                |
#  |----------|------------------------------------------------------------------------------------|----------------|

# ---------------------------------------------------------------
# Example: Finding the Biggest Number in a Given Array

sampleArray = [5, 4, 10, 8, 11, 68, 87]  # assume n elements

# Applying rules to find time complexity step by step

def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]#....................................................................................Rule 1: O(1)
    
    for index in range(1, len(sampleArray)):#..................................................... Rule 2: O(n)..}
                                                                                                                #_______}    : O(n)
        if sampleArray[index] > biggestNumber:  # Rule 1 inside loop: O(1)_______}_______________________: O(1)..}
            biggestNumber = sampleArray[index]  # Rule 1 inside loop: O(1)_______} 

    print(biggestNumber) # ........................................................................................... Rule 1: O(1)

# Time Complexity Calculation:
# -----------------------------
# Line 1 → O(1)
# Loop → O(n)
# Inside loop:
#    - if condition → O(1)
#    - assignment → O(1)
#    → These are inside loop, so O(n) total
# Print → O(1)

# Total time complexity:
#   = O(1) + O(n) + O(1)  → Drop constants and non-dominant terms
#   = O(n)

findBiggestNumber(sampleArray)

# ----------------------------------------------------------------
# Final Conclusion:
# Use the given rules to break down any block of code and then
# apply addition/multiplication rules (based on structure).
# Remember:
#   - If parts of code run independently → Add time: O(A) + O(B)
#   - If parts of code are nested         → Multiply time: O(A * B)
