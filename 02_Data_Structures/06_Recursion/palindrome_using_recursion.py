def is_palindrome(string, start, end):
    # Base Case: If start crosses or meets end, string is palindrome
    if start >= end:
        return True

    # If mismatch found at any point, string is not a palindrome
    if string[start] != string[end]:
        return False

    # Recursive Case: Move inward and check remaining substring
    return is_palindrome(string, start + 1, end - 1)


# Driver Code
string = 'madam'
print(is_palindrome(string, 0, len(string) - 1))  # Expected Output: True


"""
--- STACK WORKING EXPLANATION FOR "madam" ---

Initial Call: is_palindrome("madam", 0, 4)
1. Compare string[0] = 'm' and string[4] = 'm' → match
   Call is_palindrome("madam", 1, 3)
        | is_palindrome(1,3) |
        | is_palindrome(0,4) |

2. Compare string[1] = 'a' and string[3] = 'a' → match
   Call is_palindrome("madam", 2, 2)
        | is_palindrome(2,2) |
        | is_palindrome(1,3) |
        | is_palindrome(0,4) |

3. Base Case Hit: start = 2, end = 2 → return True

--- UNWINDING (returns back up the stack) ---
- is_palindrome(2,2) returns True → is_palindrome(1,3) returns True → is_palindrome(0,4) returns True

--- FINAL OUTPUT ---
True
"""
