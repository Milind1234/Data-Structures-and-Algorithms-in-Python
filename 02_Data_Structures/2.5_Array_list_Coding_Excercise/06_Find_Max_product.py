"""
🔢 Problem: Max Product of Two Integers in a List

🎯 Goal:
Given a list of positive integers, return the maximum product of any two distinct numbers in the list.

📥 Input  : [1, 7, 3, 4, 9, 5]
📤 Output : 63  # (9 * 7)

──────────────────────────────────────────────
🔍 Approach 1: Brute Force (Check all pairs)

🧠 Steps:
1. Initialize a variable `max_product` to 0.
2. Use two nested loops:
   - Outer loop from index `i = 0` to end.
   - Inner loop from `j = i + 1` to end.
3. For every pair `(i, j)`, calculate the product `arr[i] * arr[j]`.
4. If the product is greater than `max_product`, update it.
5. After checking all pairs, return `max_product`.

⏱ Time Complexity : O(n^2)
🧠 Space Complexity: O(1)
"""

def max_product_brute(arr):
    max_product = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
    return max_product

# ✅ Test Brute Force
arr = [1, 7, 3, 4, 9, 5]
print("Brute Force Result:", max_product_brute(arr))  # Output: 63

"""
⚡ Approach 2: Optimized (Find top 2 largest numbers)

🧠 Steps:
1. Initialize two variables: `max1 = 0`, `max2 = 0`.
2. Traverse through each number in the array:
   - If current number > max1:
     → Assign max2 = max1
     → Assign max1 = current number
   - Else if current number > max2:
     → Assign max2 = current number
3. Return the product `max1 * max2`.

✅ Why this works:
The two largest numbers will always give the maximum product in a list of all positive integers.

⏱ Time Complexity : O(n)
🧠 Space Complexity: O(1)
"""
def max_product_optimized(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization
 
    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment
 
    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication
 
arr = [1, 7, 3, 4, 9, 5]
print(max_product_optimized(arr))  # Output: 63 (9*7)

# ✅ Test Optimized
print("Optimized Result:", max_product_optimized(arr))  # Output: 63

"""
🧾 Summary:
- Brute force checks all pairs and is simple but slow (O(n²)).
- Optimized approach is much faster (O(n)) and best for large arrays.
- Both return the same correct result when the input has ≥2 positive integers.
"""
