# Sum and Product of Tuple Elements
"""
Problem:
--------
Write a function that calculates:
1. Sum of all elements in a tuple
2. Product of all elements in a tuple

Example:
--------
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
Output: 10, 24
"""

def sum_product(t):
    # Initialize sum and product
    sum_result = 0
    product_result = 1

    # Traverse each element in the tuple
    for num in t:
        sum_result += num        # Add element to sum
        product_result *= num    # Multiply element to product

    # Return both results as a tuple
    return sum_result, product_result


# Example usage
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10 24


"""
Time Complexity:
----------------
O(n) → because we iterate through all n elements once.

Space Complexity:
-----------------
O(1) → no extra space used apart from variables.
"""
