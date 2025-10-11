"""
# Problem: Product and Sum of Array Elements
Given an array of integers, calculate:
1. Sum of all elements
2. Product of all elements

Example:
Input: [1, 2, 3, 4, 5, 6]
Output: Sum = 21, Product = 720

-------------------------------------------------------------
Steps to Solve:
1. Initialize two variables:
   - total_sum = 0
   - total_product = 1
2. Loop through each element in the array:
   - Add it to total_sum
   - Multiply it with total_product
3. Print or return both results.

-------------------------------------------------------------
Time Complexity:
- O(n) → Because we iterate through the list once.
Space Complexity:
- O(1) → No extra data structures used, only two variables.
"""

def product_sum(array):
    # Initialize sum and product
    total_sum = 0
    total_product = 1

    # Loop once to compute sum and product
    for i in array:
        total_sum += i
        total_product *= i

    print(f"Sum of numbers in array: {total_sum} and product of numbers: {total_product}")


# Example usage
product_sum([1, 2, 3, 4, 5, 6])  # Output: Sum = 21, Product = 720
