"""
===============================================================================
📘 03_InsertString.py — Insert a String into a Trie (4 Cases + Full Explanation)
===============================================================================

Purpose
-------
This file explains **how to insert a string** into a Trie data structure.

It includes:

  ✔ How Trie nodes store characters  
  ✔ How links between characters work  
  ✔ 4 insertion cases explained with diagrams  
  ✔ Why endOfString flag is needed  
  ✔ Full Python implementation (your logic preserved)  
  ✔ Time & Space complexity analysis  

Trie Node Properties
--------------------
Each Trie node contains:
  - children (dict):  Mapping: character → TrieNode  
  - endOfString (bool): Marks the end of a complete string  

-----------------------------------------------------------------------------
Insertion Cases
-----------------------------------------------------------------------------
When inserting a word into a Trie, there are **four major cases**:

Case 1️⃣ — Trie is Empty  
Case 2️⃣ — Prefix is common with another word  
Case 3️⃣ — Prefix itself is already a complete word  
Case 4️⃣ — Word already exists in Trie  
-----------------------------------------------------------------------------
"""


# =============================================================================
#                               TRIE NODE
# =============================================================================
class TrieNode:
    """
    Represents ONE node inside Trie.
    children   : dictionary mapping character → TrieNode
    endOfString: True if this node terminates a valid stored string
    """
    def __init__(self):
        self.children = {}        # Ex: { 'A': TrieNode(), 'B': TrieNode() }
        self.endOfString = False  # Marks final character of a stored word


# =============================================================================
#                               TRIE CLASS
# =============================================================================
class Trie:
    """
    Trie class containing a ROOT node.
    Root contains empty children initially.
    """
    def __init__(self):
        self.rootnode = TrieNode()

    # =========================================================================
    #                           INSERT STRING
    # =========================================================================
    def insertString(self, word):
        """
        Insert a string into the Trie.

        Steps:
        ------
        1) Start at root
        2) For each character:
            → If char exists: reuse node
            → Else: create a new TrieNode and link
        3) After last char: mark endOfString = True

        Complexity:
            Time  = O(m)   where m = length of the word
            Space = O(m)   (worst case: all chars new)

        Prints success message.
        """
        current = self.rootnode

        for char in word:
            node = current.children.get(char)

            # Case: Character NOT found → create new node
            if node is None:
                node = TrieNode()
                current.children.update({char: node})

            # Move forward
            current = node

        # Mark end of this complete word
        current.endOfString = True

        print(f"String '{word}' inserted Successfully")

    # =========================================================================
    #                      Pretty-print / textual tree view
    # =========================================================================
    def __repr__(self):
        return self._repr_trie()

    def __str__(self):
        return self.__repr__()

    def _repr_trie(self):
        """
        Build a multi-line string showing the trie as a readable tree.

        Uses simple box-drawing characters:
          ├─ child (intermediate)
          └─ child (last)
          │  vertical continuation

        Each node shows the character and a ' (*)' marker when endOfString is True.
        Example:
          root
          ├─ A
          │  ├─ p
          │  │  └─ p (*)
          │  └─ i (*)
          └─ B
             └─ a
                └─ t (*)
        """
        lines = []
        lines.append("root")

        # recursively walk children in sorted order for deterministic output
        def walk(node, prefix):
            # sort keys so representation is stable across runs
            keys = sorted(node.children.keys())
            for i, ch in enumerate(keys):
                child = node.children[ch]
                is_last = (i == len(keys) - 1)

                # choose branch drawing chars
                branch = "└─ " if is_last else "├─ "
                line = prefix + branch + ch + (" (*)" if child.endOfString else "")
                lines.append(line)

                # prepare next prefix: if current branch is not last, we must keep a vertical line
                if is_last:
                    new_prefix = prefix + "   "
                else:
                    new_prefix = prefix + "│  "

                # recurse
                walk(child, new_prefix)

        walk(self.rootnode, "")
        return "\n".join(lines)


# =============================================================================
#                         EXAMPLE USAGE (RUN DIRECTLY)
# =============================================================================
if __name__ == "__main__":
    """
    More examples to exercise all insertion cases and branching:
      - Case 1: inserting into a blank trie            -> "App"
      - Case 2: sharing prefix with existing word      -> "Api"
      - Case 3: prefix is already a complete word     -> "Apis" after "Api"
      - Case 4: word already present (duplicate insert)-> "App" again
      - Additional branching words to show tree output -> "Bat", "Bar", "Balm"
    """

    newTrie = Trie()

    # Case 1: Trie is blank -> create nodes for "App"
    newTrie.insertString("App")

    # Case 2: New string shares prefix -> "Api" (A,P exist; add I)
    newTrie.insertString("Api")

    # Case 3: Prefix already a complete word -> insert "Apis" (Api is complete)
    newTrie.insertString("Apis")

    # Duplicate insert (Case 4): insert "App" again (should not break anything)
    newTrie.insertString("App")

    # More branching examples to show structure clearly
    newTrie.insertString("Bat")    # creates B -> a -> t
    newTrie.insertString("Bar")    # shares B -> a, adds r
    newTrie.insertString("Balm")   # B -> a -> l -> m (demonstrates multi-branch)
    newTrie.insertString("Apple")  # extends App -> l -> e (shows extension of existing word)
    newTrie.insertString("Apply")  # App -> l -> y (branch sibling to 'e')

    # Print resulting trie structure
    print("\n--- Trie structure (visual) ---")
    print(newTrie)

    # Also show some single-line info (optional)
    print("\n--- Quick checks ---")
    print("Root children:", sorted(newTrie.rootnode.children.keys()))
    # Show that endOfString flags exist at some nodes by scanning top-level branches
    for ch in sorted(newTrie.rootnode.children.keys()):
        node = newTrie.rootnode.children[ch]
        print(f"Top-level '{ch}' has children: {sorted(node.children.keys())}, endOfString={node.endOfString}")

"""
===============================================================================
Insertion Case-by-Case (ASCII VISUALIZATION)
===============================================================================

CASE 1️⃣ — Trie is Blank  
Insert: APP

 Initially:
      (root)
        |

 Step 1: Insert 'A'
      root
        └── A

 Step 2: Insert 'P'
      A
      └── P

 Step 3: Insert 'P'
      P
      └── P  (endOfString = True)


CASE 2️⃣ — New string shares prefix with previous string  
Insert: API

 Existing Trie:
         A
         └── P
             └── P (end)
 Insert 'I':
             P
             └── I (new) → endOfString = True


CASE 3️⃣ — Prefix already exists as a FULL stored string  
Stored: API  
Insert: APIS

 API exists fully, so only add:
        S → endOfString = True


CASE 4️⃣ — Word is already present  
Insert: APIS (again)
 → No changes (all characters + endOfString already exist)

===============================================================================
TIME & SPACE COMPLEXITY SUMMARY
===============================================================================
Operation                  Time Complexity         Space Complexity
------------------------   ---------------------   ---------------------------
Insert(word of length m)     O(m)                     O(m)
Search                       O(m)                     O(1)
Delete                       O(m)                     O(m)
Creation (root only)         O(1)                     O(1)
===============================================================================
"""
