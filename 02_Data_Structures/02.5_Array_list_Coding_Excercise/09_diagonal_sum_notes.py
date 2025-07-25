# 🧾 Question:
# Given a 2D list (matrix), write a function to calculate:
# 1. Primary diagonal sum (top-left to bottom-right)
# 2. Secondary diagonal sum (top-right to bottom-left)
# Return both sums only if the matrix is square.

# 🧠 Steps to Solve:
# 1. Define a function that accepts a 2D list as input.
# 2. Check if the matrix is square: number of rows == number of columns.
# 3. If not square, return an appropriate message.
# 4. Initialize variables for primary and secondary diagonal sums.
# 5. Loop through the matrix using the index:
#    - For primary diagonal, add matrix[i][i]
#    - For secondary diagonal, add matrix[i][n - 1 - i]
# 6. Return both sums as a dictionary.

# ✅ Code:

def diagonal_sums(matrix):
    rows = len(matrix)
    
    # Check for empty matrix or inconsistent row sizes
    if rows == 0 or any(len(row) != rows for row in matrix):
        return "Error: Matrix is not square."

    primary_sum = 0
    secondary_sum = 0

    for i in range(rows):
        primary_sum += matrix[i][i]
        secondary_sum += matrix[i][rows - 1 - i]

    return {
        "primary_diagonal_sum": primary_sum,
        "secondary_diagonal_sum": secondary_sum
    }

# 🧪 Test Cases:

# Case 1: Square matrix
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sums(matrix1))  # {'primary_diagonal_sum': 15, 'secondary_diagonal_sum': 15}

# Case 2: Non-square matrix
matrix2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(diagonal_sums(matrix2))  # Error: Matrix is not square.

# 🕒 Time Complexity: O(n)
# → One pass through the diagonals of the square matrix.

# 💾 Space Complexity: O(1)
# → Only two variables used, independent of input size.
