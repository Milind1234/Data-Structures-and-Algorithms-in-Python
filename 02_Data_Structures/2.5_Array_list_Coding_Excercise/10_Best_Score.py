# 🧾 Question:
# Given a list of scores, write a function to get the first and second best (highest) scores.
# The list may contain duplicates. Return the top two distinct scores.

# 🧠 Steps to Solve:
# 1. Define a function that takes a list as input.
# 2. Initialize two variables max1 and max2 to negative infinity.
# 3. Loop through each number in the list:
#     - If the number is greater than max1:
#         - Set max2 = max1
#         - Set max1 = number
#     - Else if the number is greater than max2 and not equal to max1:
#         - Set max2 = number
# 4. Return max1 and max2

# ✅ Code:
def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max1, max2

# 🧪 Test Case:
myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(myList))  # ➞ (90, 87)

# 🕒 Time Complexity: O(n)
# → Single pass through the list to find two best scores.

# 💾 Space Complexity: O(1)
# → Only two variables used to store max values.
