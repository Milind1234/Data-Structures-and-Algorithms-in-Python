# ---------------------------------------------
# 🔡 1. Convert String to List of Characters
# ---------------------------------------------
name = "Milind"
char_list = list(name)  # Converts each character into a list element
print("List of characters:", char_list)

# Accessing characters using index
print("First character:", char_list[0])  # Output: 'M'
print("Second character:", char_list[1])  # Output: 'i'

# ⏱ Time Complexity: O(n)
# 💾 Space Complexity: O(n)

# ---------------------------------------------
# 🧩 2. Split String into List of Words
# ---------------------------------------------
sentence = "Python is fun and powerful"
word_list = sentence.split()  # Default delimiter is whitespace
print("List of words:", word_list)

# Accessing specific words
print("Third word:", word_list[2])  # Output: 'fun'

# ⏱ Time Complexity: O(n)
# 💾 Space Complexity: O(k), where k = number of split words

# ---------------------------------------------
# 🧵 3. Split String using Custom Delimiter
# ---------------------------------------------
data = "apple,banana,grapes,kiwi"
split_fruits = data.split(",")
print("Split fruits:", split_fruits)

# Another example with a different delimiter
record = "CS101|AI|A+"
fields = record.split("|")
print("Split record fields:", fields)

# ⏱ Time Complexity: O(n)
# 💾 Space Complexity: O(k)

# ---------------------------------------------
# 🔄 4. Convert List to String using join()
# ---------------------------------------------
items = ['notebook', 'pen', 'eraser']
shopping_line = ", ".join(items)
print("Shopping line:", shopping_line)  # Output: 'notebook, pen, eraser'

# Joining characters to make a word
letters = ['H', 'e', 'l', 'l', 'o']
word = "".join(letters)
print("Joined word:", word)  # Output: 'Hello'

# ⏱ Time Complexity: O(n)
# 💾 Space Complexity: O(n)

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
"""
📌 Summary of String and List Conversion Methods

1. list(str)
   - Converts string to list of characters
   - Example: list("Milind") → ['M', 'i', 'l', 'i', 'n', 'd']

2. str.split([delimiter])
   - Splits a string into a list of substrings
   - Default delimiter is whitespace
   - Example: "Python is fun".split() → ['Python', 'is', 'fun']
   - Example: "apple,banana".split(',') → ['apple', 'banana']

3. str.join(list)
   - Joins list elements into a single string
   - Delimiter is placed between elements
   - Example: ", ".join(['pen', 'pencil']) → 'pen, pencil'

🕒 Time Complexity:
- All of the above operations are O(n), where n is the total number of characters.

💾 Space Complexity:
- O(n), since each conversion creates a new string or list.
"""
