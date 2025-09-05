"""
Problem: Plus One (LeetCode 66)

You are given a large integer represented as an integer array `digits`,
where each digits[i] is the ith digit of the integer. The digits are 
ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example:
Input:  [1,2,3]
Output: [1,2,4]
"""

# ---------------------------------------------------------------
# Brute Force Approach (Convert to Number and Back)
# ---------------------------------------------------------------
"""
Idea:
1. Convert the array of digits into a number.
2. Add 1 to this number.
3. Convert the number back into an array of digits.

Time Complexity: O(n)   (building number + converting back)
Space Complexity: O(n)  (extra array for result)

⚠️ Downside: Will break in some languages with very large numbers 
(but Python can handle big integers).
"""

class BruteForceSolution(object):
    def plusOne(self, digits):
        num = 0
        # Step 1: convert array to number
        for digit in digits:
            num = num * 10 + digit
        # Step 2: add one
        num += 1
        # Step 3: convert back to array
        result = []
        while num > 0:
            result.append(num % 10)
            num //= 10
        return result[::-1]


# ---------------------------------------------------------------
# Optimized Approach (Digit-by-Digit Carry Handling)
# ---------------------------------------------------------------
"""
Idea:
Work directly on the digits (like manual addition):
1. Start from the last digit.
2. Add 1 to it.
3. If digit < 10 → return immediately (done).
4. If digit == 10 → set to 0 and carry = 1 → move left.
5. If the loop ends, it means all digits were 9 → prepend 1.

Time Complexity: O(n)   (at most one pass through digits)
Space Complexity: O(1)  (in-place, except final prepend if needed)
"""

class OptimalSolution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:   # no carry, done
                return digits
            digits[i] = 0        # carry → set digit to 0
        # if all were 9, add 1 at the front
        return [1] + digits


# ---------------------------------------------------------------
# Step-by-Step Example Explanations
# ---------------------------------------------------------------
"""
📝 Example 1: Input = [1, 2, 3]

Start: digits = [1, 2, 3]

Iteration 1: i = 2 (last digit = 3)
digits[2] += 1 → [1, 2, 4]
digits[2] < 10 → True → return [1, 2, 4]

✅ Output: [1, 2, 4]
(No further iterations needed because we return immediately.)


📝 Example 2: Input = [1, 2, 9]

Start: digits = [1, 2, 9]

Iteration 1: i = 2 (last digit = 9)
digits[2] += 1 → [1, 2, 10]
digits[2] < 10 → False
So set digits[2] = 0 → [1, 2, 0]

Iteration 2: i = 1 (digit = 2)
digits[1] += 1 → [1, 3, 0]
digits[1] < 10 → True → return [1, 3, 0]

✅ Output: [1, 3, 0]


📝 Example 3: Input = [9, 9, 9]

Start: digits = [9, 9, 9]

Iteration 1: i = 2 (last digit = 9)
digits[2] += 1 → [9, 9, 10]
digits[2] < 10 → False → set to 0 → [9, 9, 0]

Iteration 2: i = 1 (digit = 9)
digits[1] += 1 → [9, 10, 0]
digits[1] < 10 → False → set to 0 → [9, 0, 0]

Iteration 3: i = 0 (digit = 9)
digits[0] += 1 → [10, 0, 0]
digits[0] < 10 → False → set to 0 → [0, 0, 0]

Loop ends → all digits turned into 0’s.

Final Step:
Return [1] + digits → [1, 0, 0, 0]

✅ Output: [1, 0, 0, 0]


🎯 Summary
- The loop goes from last digit to first digit.
- At each step:
  • Add 1
  • If digit < 10 → return immediately (done).
  • If digit == 10 → set to 0 and let carry move left.
- If the loop finishes, it means all digits were 9 → prepend [1].
"""


# ---------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],   # normal case
        [1, 2, 9],   # carry in the last digit
        [9, 9, 9],   # all digits are 9
        [0],         # smallest case
    ]

    print("Testing Brute Force Solution:")
    brute = BruteForceSolution()
    for digits in test_cases:
        print(f"Input: {digits} → Output: {brute.plusOne(list(digits))}")

    print("\nTesting Optimized Solution:")
    optimal = OptimalSolution()
    for digits in test_cases:
        print(f"Input: {digits} → Output: {optimal.plusOne(list(digits))}")
