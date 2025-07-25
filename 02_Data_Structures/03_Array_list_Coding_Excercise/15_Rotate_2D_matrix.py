"""
LeetCode 48 – Rotate Image (90 degrees clockwise)

📌 Problem:
Given an n x n 2D matrix representing an image, rotate the image by 90 degrees clockwise **in-place**.
You are not allowed to allocate another matrix for the rotation.

🧠 Idea:
Rotation of a matrix by 90° clockwise can be achieved in 2 main steps:
1. Transpose the matrix (swap matrix[i][j] with matrix[j][i])
2. Reverse each row

----------------------------------------------------------
🔁 Step 1: Transpose the Matrix
----------------------------------------------------------
- Transposing means converting rows into columns and columns into rows.
- We only need to swap elements where column index > row index (i.e., j > i)
  to avoid swapping the same elements twice.

For example:
Original:
1 2 3
4 5 6
7 8 9

After Transposing (swap i,j with j,i):
1 4 7
2 5 8
3 6 9

----------------------------------------------------------
🔁 Step 2: Reverse Each Row
----------------------------------------------------------
- Reversing each row after transposing results in the final rotated matrix.

After reversing each row:
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]

➡️ Which is the desired 90° rotated output.

----------------------------------------------------------
⏱️ Time Complexity:
----------------------------------------------------------
- Transposing: O(n²) because we visit half the matrix.
- Reversing: O(n) per row ⇒ O(n²) total.
- Hence, total time complexity = O(n²)

🧠 Space Complexity: O(1)
- Done in-place; no extra space is used.

"""

def rotate(matrix):
    # Step 1: Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
    
    return matrix


# ✅ Example usage
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
