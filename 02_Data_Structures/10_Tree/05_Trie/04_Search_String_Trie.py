"""
===============================================================================
📘 03_SearchString.py — Search for a String in a Trie (3 Cases + Full Notes)
===============================================================================

Purpose
-------
This file explains how **searching** works in a Trie.

We cover:

  ✔ 3 possible search outcomes  
  ✔ Why matching characters is NOT enough  
  ✔ Why endOfString flag is crucial  
  ✔ Python implementation (your logic preserved)  
  ✔ Many test examples  
  ✔ Time & Space complexity  

Trie Recap
----------
Each Trie node contains:
  - children (dict): char → TrieNode
  - endOfString (bool): marks end of a valid complete word

===============================================================================
SEARCH CASES
===============================================================================

When searching a word in a Trie, **3 outcomes** are possible.

-------------------------------------------------------------------------------
CASE 1️⃣ — String does NOT exist  
-------------------------------------------------------------------------------

Search:  "BCD"

Trie only has:  A → P → P → (end)

Steps:
  • Compare first char 'B' with root's children: root only has 'A'
  • 'B' not found → return FALSE immediately

Diagram:

  root
    └── A
         └── P
             └── P (*)

Search for “B”:
  B ✗ (not present anywhere)
  → String does NOT exist.


-------------------------------------------------------------------------------
CASE 2️⃣ — String exists COMPLETELY  
-------------------------------------------------------------------------------

Search: "API"

Trie:
  A → P → I (*)

Steps:
  • 'A' found → go deeper  
  • 'P' found → go deeper  
  • 'I' found → now check endOfString  
  • endOfString == TRUE → valid stored string → return TRUE

IMPORTANT:
  Matching characters alone is NOT enough.
  Final node must have endOfString = True.


-------------------------------------------------------------------------------
CASE 3️⃣ — Word is only a PREFIX (NOT a complete stored word)
-------------------------------------------------------------------------------

Search: "AP"

Trie:
  A → P → I (*)

Steps:
  • 'A' found  
  • 'P' found  
  • endOfString == FALSE → means "AP" is just a prefix  
  • NOT a complete string → return FALSE

Diagram:

  A
   └── P
        └── I (*)

AP = prefix  
API = valid stored word  
So AP does NOT exist as a complete string.

===============================================================================
Python Implementation
===============================================================================
"""

# =============================================================================
#                               TRIE NODE
# =============================================================================
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


# =============================================================================
#                               TRIE CLASS
# =============================================================================
class Trie:
    def __init__(self):
        self.rootnode = TrieNode()

    # =========================================================================
    #                             INSERT STRING
    # =========================================================================
    def insertString(self, word):
        current = self.rootnode
        for ch in word.lower():
            node = current.children.get(ch)

            # Create node if missing
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})

            current = node

        current.endOfString = True
        print(f"String '{word}' inserted Successfully")

    # =========================================================================
    #                             SEARCH STRING
    # =========================================================================
    def searchString(self, word):
        """
        Search the Trie for an exact word match.

        Returns:
            True  → if full word exists AND endOfString == True
            False → otherwise (not found OR only prefix)

        Three possible outcomes:
            1. Character missing       → FALSE
            2. Characters found + EOS  → TRUE
            3. Characters found but EOS FALSE → prefix → FALSE

        Time Complexity:  O(m)
        Space Complexity: O(1)
        """
        currentNode = self.rootnode

        # Traverse character by character
        for ch in word.lower():
            node = currentNode.children.get(ch)
            if node is None:
                return False  # Character path does not exist
            currentNode = node

        # Word only valid if final node marks end-of-string
        return currentNode.endOfString


# =============================================================================
#                         EXAMPLE USAGE (RUN DIRECTLY)
# =============================================================================
if __name__ == "__main__":
    newTrie = Trie()

    # Insert example strings
    newTrie.insertString("App")
    newTrie.insertString("Apis")

    print("\n--- SEARCH RESULTS ---")
    print("APP  →", newTrie.searchString("APP"))     # True
    print("APIs →", newTrie.searchString("APIs"))    # True
    print("API  →", newTrie.searchString("API"))     # False (prefix only)
    print("DACk →", newTrie.searchString("DACk"))    # False (not present)"


"""
===============================================================================
ASCII VISUALIZATION OF SEARCH LOGIC
===============================================================================

Given Trie:

root
 └─ a
     └─ p
         ├─ p (*)
         └─ i (*)

Search "APP":
  a ✓
  p ✓
  p ✓ → endOfString=TRUE → VALID

Search "API":
  a ✓
  p ✓
  i ✓ → endOfString=TRUE → VALID

Search "AP":
  a ✓
  p ✓
  reached end but endOfString=FALSE → prefix → INVALID

Search "BCD":
  b ✗ → INVALID

===============================================================================
TIME & SPACE COMPLEXITY SUMMARY
===============================================================================

Operation                    Time Complexity      Space Complexity
------------------------     ----------------     ----------------
Insert(word of length m)        O(m)                   O(m)
Search(word of length m)        O(m)                   O(1)
Delete(word of length m)        O(m)                   O(m)
Create empty trie               O(1)                   O(1)

===============================================================================
"""
