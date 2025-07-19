# -------------------------------------------------------
# 📚 Topic: Conditional List Comprehension in Python
# -------------------------------------------------------

# ✅ Simple Filtering with if in List Comprehension

my_list = [0, -1, -3, 5, 6, 7, -10, -4, -8, 9, 8]
print("Original list:", my_list)

# ➤ Keep only non-negative numbers
new_list = [i for i in my_list if i >= 0]
print("Only non-negative numbers:", new_list)
# Output: [0, 5, 6, 7, 9, 8]


# ✅ Transforming Data with if in List Comprehension

# ➤ Get square of only the negative numbers
new_list = [i * i for i in my_list if i <= 0]
print("Squares of negative numbers:", new_list)
# Output: [0, 1, 9, 100, 16, 64]


# ✅ Using a Helper Function to Filter Data (Consonants Only)

# ➤ Sentence to filter consonants from
sentence = "himynameismilind"

# ➤ Function to check if a character is a consonant
def is_consonant(letter):
    vowels = 'aeiou'
    letter = letter.lower()
    return letter.isalpha() and letter not in vowels

# ➤ List comprehension using the helper function
consonants = [i for i in sentence if is_consonant(i)]
print("Consonants in sentence:", consonants)
# Output: ['h', 'm', 'y', 'n', 'm', 's', 'm', 'l', 'n', 'd']


# ✅ List Comprehension with if-else Condition

# ➤ Replace negative numbers with 0, keep positive as is
new_list = [i if i > 0 else 0 for i in my_list]
print("Replace negative numbers with 0:", new_list)
# Output: [0, 0, 0, 5, 6, 7, 0, 0, 0, 9, 8]

# ➤ Replace negative numbers with 'negative no.'
new_list = [i if i > 0 else 'negative no.' for i in my_list]
print("Label negative numbers:", new_list)
# Output: ['negative no.', 'negative no.', 'negative no.', 5, 6, 7, 'negative no.', 'negative no.', 'negative no.', 9, 8]


# ✅ Using a Function to Handle Complex Conditional Logic

# ➤ Define a function to encapsulate the condition
def get_number(i):
    if i > 0:
        return i
    else:
        return 'negative no.'

# ➤ Use the function inside list comprehension
new_list = [get_number(i) for i in my_list]
print("Using get_number function:", new_list)
# Output: ['negative no.', 'negative no.', 'negative no.', 5, 6, 7, 'negative no.', 'negative no.', 'negative no.', 9, 8]

# -------------------------------------------------------
# 🧠 Summary:
# - Use `if` in list comprehension to filter elements.
# - Use `if-else` inside to transform elements conditionally.
# - You can call helper functions inside the comprehension.
# - Helps keep code compact and readable.
# -------------------------------------------------------
