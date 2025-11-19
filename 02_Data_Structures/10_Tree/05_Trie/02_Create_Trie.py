"""
===============================================================================
📘 Trie_Create_Notes.py — Creation of Trie Data Structure
===============================================================================

Purpose
-------
This notes file explains:
  - Common operations available on a Trie
  - How Trie creation works internally
  - Structure of TrieNode and Trie classes
  - Why children are stored as a dictionary
  - End-of-string marker
  - Time & Space Complexity of creation

This is ONLY THEORY NOTES — code below is basic structure, not full trie logic.

===============================================================================
COMMON OPERATIONS ON TRIE
===============================================================================

The four fundamental operations performed on a Trie are:

1️⃣ Creation of Trie  
2️⃣ Insertion of a string  
3️⃣ Searching for a string  
4️⃣ Deletion of a string  

In this lecture, we only cover the **creation** part.

===============================================================================
1. CREATION OF A TRIE — CONCEPT
===============================================================================

Creating a Trie is extremely simple:

- We only create **one empty root node**.
- This root node has:
      - children = {}      (dictionary to store links to next characters)
      - endOfString = False  (root does NOT represent any character)

⚠ The root node does NOT store any character.  
It is an empty starting point for all words.

===============================================================================
2. INTERNAL STRUCTURE OF A TRIE NODE
===============================================================================

Physically, each Trie node contains:

    1. children — a dictionary  
          key   → character  
          value → reference to next TrieNode  

    2. endOfString — boolean  
          True  → this node represents end of a valid string  
          False → path continues  

Why dictionary?
---------------
Because:
- children may contain many characters  
- lookup for next character becomes O(1)
- easy to dynamically add/remove keys

Example of a logical node:

    Node {
        children = { 'A': ref1, 'R': ref2, 'T': ref3 }
        endOfString = False
    }

===============================================================================
3. PYTHON CLASSES FOR TRIE CREATION
===============================================================================

We define two classes:

(1) TrieNode  → represents a node  
(2) Trie      → manages root + all operations

"""

# ----------------------- TRIE NODE ----------------------- #
class TrieNode:
    def __init__(self):
        # Stores links to children (character → TrieNode)
        self.children = {}

        # Boolean: True if this node marks the end of a string
        self.endOfString = False


# ------------------------- TRIE -------------------------- #
class Trie:
    def __init__(self):
        # Root node is always a blank TrieNode
        self.root = TrieNode()


# Creating a new Trie
newTrie = Trie()


"""
===============================================================================
4. TIME & SPACE COMPLEXITY OF TRIE CREATION
===============================================================================

Time Complexity:   O(1)
    - Only one root node is created.

Space Complexity:  O(1)
    - Only a single TrieNode object is stored.

===============================================================================
SUMMARY
===============================================================================
✔ A Trie is created by initializing ONE empty root node  
✔ TrieNode stores:
      - children (as dictionary)
      - endOfString flag  
✔ Trie creation is O(1) time and O(1) space  
✔ This is the foundation for further operations:
      - insertion
      - search
      - deletion

===============================================================================
END OF NOTES — Trie Creation
===============================================================================
"""
