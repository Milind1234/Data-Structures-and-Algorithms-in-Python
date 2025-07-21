"""
Title: Diagonal Sum of 2D List

Problem:
Given a 2D square list (matrix), write a function that calculates the sum of the primary diagonal elements.
The primary diagonal elements are those where the row index and column index are the same.

Example:
Input:  [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
Output: 15  (because 1 + 5 + 9 = 15)

------------------------------------------------

Steps to Solve:

1. Initialize a variable `total` to 0 to keep track of the diagonal sum.
2. Loop through the matrix using a single loop from index 0 to len(matrix) - 1.
3. In each iteration, add the element at the diagonal position (i.e., matrix[i][i]) to `total`.
4. After the loop ends, return the `total`.

------------------------------------------------

Time Complexity: O(n)
- We traverse the diagonal once, where `n` is the number of rows (or columns) in the square matrix.

Space Complexity: O(1)
- We use only a constant amount of space (`total`) regardless of the input size.

------------------------------------------------

Code:
"""

def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

# Example usage
myList2D = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

print(diagonal_sum(myList2D))  # Output: 15
