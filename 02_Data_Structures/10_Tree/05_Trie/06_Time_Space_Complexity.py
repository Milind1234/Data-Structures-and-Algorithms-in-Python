"""
===============================================================================
📘 05_Trie_Time_Complexity.py — Time & Space Complexity of Trie Operations
===============================================================================

Purpose
-------
This file explains the **time and space complexity analysis** of ALL major Trie
operations:

    ✔ Creating a Trie
    ✔ Inserting a Word
    ✔ Searching for a Word
    ✔ Deleting a Word
    ✔ Space usage of the entire Trie

All complexities are given using:
    m → length of the word
    n → number of words stored in the Trie

===============================================================================
🔷 1. Creation of Trie
===============================================================================

Operation:
    newTrie = Trie()

Explanation:
    Creating a Trie only initializes:
      - one empty TrieNode
      - with an empty dictionary {}
      - and endOfString = False

TIME COMPLEXITY:
    O(1)
SPACE COMPLEXITY:
    O(1)

Reason:
    Only a single node is allocated. No loops, no recursion.

===============================================================================
🔷 2. Insert a String into Trie
===============================================================================

Operation:
    trie.insertString(word)

Process:
    - For each of the m characters:
        → check if child exists (dict lookup O(1))
        → if not, create new TrieNode
        → move to the next node
    - Mark endOfString = True

TIME COMPLEXITY:
    O(m)

Why?
    We visit each character exactly once.

SPACE COMPLEXITY:
    O(m)

Worst case:
    Every character of the new word creates a new node.

Best case:
    Word already exists → O(1) extra space.

===============================================================================
🔷 3. Search for a String
===============================================================================

Operation:
    trie.searchString(word)

Process:
    - Traverse through characters one by one
    - If path breaks → return False
    - At end, check endOfString flag

TIME COMPLEXITY:
    O(m)

Because:
    One traversal through characters.

SPACE COMPLEXITY:
    O(1)

Because:
    No additional memory allocated (iterating, no recursion).

===============================================================================
🔷 4. Delete a String
===============================================================================

Operation:
    deleteString(root, word, 0)

Process:
    - Recursively traverse down (depth = m)
    - On returning upward:
        → delete nodes ONLY if no other child depends on them

TIME COMPLEXITY:
    O(m)

Explanation:
    - Each character is visited once on the way down.
    - Each character is visited once on the way up.
    But 2 * m is still O(m).

SPACE COMPLEXITY:
    O(m)

Because:
    - Function is recursive
    - Recursion depth = length of word m
    - Stack frames stored = m

===============================================================================
🔷 5. Space Complexity of the Entire Trie
===============================================================================

Let:
    n = number of words inserted
    m = average length of each word

Worst-case space usage:
    O(n * m)

Why?
    - Every character creates a new node.
    - No prefix-sharing.

Typical / average case:
    Much smaller than O(nm) because:
      - Prefixes are shared between words.
      - English language words share many common roots/prefixes.

Example:
    Words: "APP", "API", "APIS", "APPLE"
    Instead of 4×4 = 16 nodes
    Trie uses ~7 nodes total due to prefix sharing.

===============================================================================
SUMMARY TABLE
===============================================================================

Operation                Time Complexity    Space Complexity
----------------------   ----------------   ----------------
Create Trie                  O(1)                O(1)
Insert(word)                 O(m)                O(m)
Search(word)                 O(m)                O(1)
Delete(word)                 O(m)                O(m)
Whole Trie (n words)         ---                 O(n * m)

===============================================================================
BIG PICTURE NOTES
===============================================================================

✔ Trie operations depend on **length of word**, NOT number of words  
✔ All operations are **much faster** for prefix problems than BST / Hash Table  
✔ Trie deletion is the only recursive operation  
✔ Insert/Search scale almost linearly with characters  

===============================================================================
"""
