# ================================
# Diagonal Extraction from Tuple of Tuples
# ================================

# --- Problem Statement ---
# Create a function that takes a tuple of tuples (like a matrix)
# and returns a tuple containing only the diagonal elements.

# Example:
# input_tuple = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
# )
# output_tuple = get_diagonal(input_tuple)
# Expected output: (1, 5, 9)

# --- Approach 1: Using Loop and List Conversion ---
def get_diagonal(input_tuple):
    temp_list = []
    for i in range(len(input_tuple)):
        temp_list.append(input_tuple[i][i])  # Selecting diagonal element
    return tuple(temp_list)  # Converting list to tuple

# --- Approach 2: Using Generator Expression ---
def get_diagonal_optimized(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

# --- Example Run ---
input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Output: (1, 5, 9)

# --- Time and Space Complexity ---
# 1) Iteration over 'n' elements -> O(n) time
# 2) Tuple creation of 'n' elements -> O(n) space
# Overall:
# Time Complexity -> O(n)
# Space Complexity -> O(n)
