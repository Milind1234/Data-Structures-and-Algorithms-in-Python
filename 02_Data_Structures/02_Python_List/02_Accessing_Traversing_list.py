# 📘 Python List: Traversing & Accessing Elements

# 📌 Sample List
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# -----------------------------------------------------
# 🔍 Accessing Elements (Using Indexing)

# Access first element
print(fruits[0])   # Output: apple

# Access last element
print(fruits[-1])  # Output: elderberry

# Access middle element
print(fruits[2])   # Output: cherry

# ❌ Accessing out of range index throws IndexError
# print(fruits[10])  # Uncommenting this will raise an error

# -----------------------------------------------------
# 🔁 Traversing a List
print("Traversing a List")
# ✅ 1. Using For Loop
for fruit in fruits:
    print(fruit)
print("............................................")

print("Using Index-based For Loop")
# ✅ 2. Using Index-based For Loop
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

print("............................................")

print("Using While Loop")
# ✅ 3. Using While Loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

print("............................................")

# ✅ 4. Using List Comprehension
[print(fruit.upper()) for fruit in fruits]

print("............................................")

# ✅ 5. Using Enumerate (Accessing Index & Value)
for idx, fruit in enumerate(fruits):
    print(f"Element at index {idx} is {fruit}")

print("............................................")

# ✅ 6. Using Map Function (read-only operation)
def to_upper(item):
    return item.upper()

print(list(map(to_upper, fruits)))

print("............................................")

# -----------------------------------------------------
# ⚙️ Time and Space Complexity

"""
🔸 Accessing an element: O(1) time — done directly via indexing.
🔸 Traversing the list: O(n) time — where n is the length of the list.
🔸 Space Complexity: O(1) for traversal (if not storing new values), O(n) if creating a new list.
"""

# Example: Access in O(1)
print(fruits[3])  # Accessing is constant time.

# Example: Traversal in O(n)
for item in fruits:
    print(item)   # Visits all n elements → O(n)

# Example: Creating a new list while traversing
capitalized_fruits = [fruit.capitalize() for fruit in fruits]  # O(n) time and O(n) space
print(capitalized_fruits)

# -----------------------------------------------------
# 📎 Bonus: Safe Access Using Try-Except
try:
    print(fruits[10])
except IndexError:
    print("Index out of range!")

# ✅ Summary:
"""
- Use indexing for direct access (fast and efficient).
- Use loops (for, while) or comprehensions for traversal.
- Use enumerate when you need both index and value.
- Access: O(1), Traversal: O(n)
- Be cautious of index out-of-bound errors!
"""
