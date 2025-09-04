# 🔷 Valid Anagram Problem
# --------------------------------------------
# Problem: Check if two strings s and t are anagrams of each other.
# An anagram is formed by rearranging the letters of one string 
# to make another string, using all original letters exactly once.

# Example:
# Input: s = "anagram", t = "nagaram"
# Output: True
# --------------------------------------------

class Solution(object):
    def isAnagram(self, s, t):
        """
        Checks if two strings are anagrams.

        Steps:
        1️⃣ If the lengths are not equal → return False immediately.
        2️⃣ Create a dictionary `count` to store character frequencies from s.
        3️⃣ Loop through s:
            - Increment the count for each character.
        4️⃣ Loop through t:
            - Decrement the count for each character.
        5️⃣ If any value in the dictionary is not 0 → return False.
        6️⃣ If all counts are zero → return True.
        """

        # Step 1: Length check
        if len(s) != len(t):
            return False

        # Step 2: Frequency dictionary
        count = {}

        # Step 3: Count frequency from s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1  # Increment count

        # Step 4: Decrease frequency based on t
        for ch in t:
            count[ch] = count.get(ch, 0) - 1  # Decrement count

        # Step 5: Validate all counts are zero
        for value in count.values():
            if value != 0:
                return False

        # Step 6: Strings are anagrams
        return True


# --------------------------------------------
# 🔹 Example Run:
s = "anagram"
t = "nagaram"
s1 = Solution()
result = s1.isAnagram(s, t)
print(result)  # Expected Output: True
# --------------------------------------------

# 🛠 DETAILED DRY RUN
# Step 1: Length Check → len("anagram") == len("nagaram") → True
# Step 2: Initialize count = {}

# Step 3: Loop through s = "anagram"
# (count.get(ch, 0) means → get the value for ch if it exists, else 0)
# 
# Iteration 1 → ch = 'a': count = {'a': 1}
# Iteration 2 → ch = 'n': count = {'a': 1, 'n': 1}
# Iteration 3 → ch = 'a': count = {'a': 2, 'n': 1}
# Iteration 4 → ch = 'g': count = {'a': 2, 'n': 1, 'g': 1}
# Iteration 5 → ch = 'r': count = {'a': 2, 'n': 1, 'g': 1, 'r': 1}
# Iteration 6 → ch = 'a': count = {'a': 3, 'n': 1, 'g': 1, 'r': 1}
# Iteration 7 → ch = 'm': count = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}

# Step 4: Loop through t = "nagaram"
# (Here we decrement counts)
# Iteration 1 → ch = 'n': count = {'a': 3, 'n': 0, 'g': 1, 'r': 1, 'm': 1}
# Iteration 2 → ch = 'a': count = {'a': 2, 'n': 0, 'g': 1, 'r': 1, 'm': 1}
# Iteration 3 → ch = 'g': count = {'a': 2, 'n': 0, 'g': 0, 'r': 1, 'm': 1}
# Iteration 4 → ch = 'a': count = {'a': 1, 'n': 0, 'g': 0, 'r': 1, 'm': 1}
# Iteration 5 → ch = 'r': count = {'a': 1, 'n': 0, 'g': 0, 'r': 0, 'm': 1}
# Iteration 6 → ch = 'a': count = {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 1}
# Iteration 7 → ch = 'm': count = {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0}

# Step 5: All counts are zero → return True

# --------------------------------------------
# 📊 Time Complexity:
# O(n) → We iterate through both strings once.
# 📊 Space Complexity:
# O(1) → Max 26 keys for lowercase letters (constant space).

# --------------------------------------------
# 📌 How the loops work:
# for ch in s:
#     count[ch] = count.get(ch, 0) + 1
#   - Goes character by character through s
#   - Updates dictionary count[ch] by adding 1
#
# for ch in t:
#     count[ch] = count.get(ch, 0) - 1
#   - Goes character by character through t
#   - Updates dictionary count[ch] by subtracting 1

# --------------------------------------------
# 💡 Possible Interview Questions:
# 1. What if the strings contain Unicode characters instead of only lowercase?
# 2. Can you solve it without using extra space (e.g., by sorting)?
# 3. How would you handle case sensitivity? ("Listen" vs "silent")
# 4. How can you optimize if we know both strings are extremely large?
