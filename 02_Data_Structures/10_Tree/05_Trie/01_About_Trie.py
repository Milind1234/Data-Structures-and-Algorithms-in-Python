"""
===============================================================================
📘 Trie_Introduction_Notes.py — What is a Trie? Why we need Trie?
===============================================================================

Purpose
-------
This notes file explains:
  - What a Trie is
  - Why Trie is needed
  - Properties of Trie
  - How strings like AIR, AIT, BAR, BAL, BM are stored (with visual ASCII)
  - Where Trie is used in real-world systems (Spell check, Auto-completion)
  - Why each node keeps “end of string” flag

This file is ONLY THEORY NOTES — no code is implemented here.

===============================================================================
WHAT IS A TRIE?
===============================================================================
A Trie (pronounced “try”) is a **tree-based data structure** that organizes 
information in a **hierarchy**, mainly used for **strings**.

Unlike BST / AVL / Heap, which store entire keys in one node,  
a Trie stores **characters of strings level-by-level**.

It is especially efficient for:
  - Prefix-based searches
  - Auto-completion
  - Dictionary word lookup
  - Spell-check systems

Time efficiency comes from early termination:
Searching “ALGO” ends as soon as a character is missing — not at the end.

===============================================================================
PROPERTIES OF TRIE
===============================================================================

1️⃣ **Used to store and search strings efficiently**  
   - Especially useful when many strings have common prefixes  
     (ex: app, apple, application, apply…)

2️⃣ **A node can store one or multiple NON-REPEATING characters**  
   Example from the diagram:
         Node stores: "AB"
         Node stores: "RT"
         Node stores: "AIM"
   BUT characters **inside one node cannot repeat**  
   → Internal compression is to save space.

3️⃣ **Every node stores links to next possible characters**  
   Structure:
        node.characters = list or map of chars
        node.children   = pointers to next nodes

4️⃣ **Each node has an "end of string" Boolean flag**  
   This marks whether the path from root → this node forms a valid word.

   Example:
       (R) → (●)
   The ● node stores: endOfString = True  
   Meaning: the parent node’s character completes a word.

===============================================================================
VISUAL EXPLANATION OF TRIE (from lecture)
===============================================================================

Example trie from the slides:

                    AB
                   /  \
                  I   AIM
                 |    / | \
                RT   R  L  ●
               /  \
              ●    ●

Here:
- AIR is stored (A → I → R → ●)
- AIT is stored (A → I → RT → T → ●)
- BAR stored (B → A → R → ●)
- BAL stored (B → A → L → ●)
- BM stored  (B → M → ●)

The ● represents a separate blank node whose only purpose is:
      end_of_string = True

===============================================================================
HOW TRIE STORES STRINGS — STEP-BY-STEP
===============================================================================

-------------------------------------------------------------------------------
Example 1: Store "AIR"
-------------------------------------------------------------------------------
Create A → I → R → end node.

ASCII:

        A
        |
        I
        |
        R
        |
        ● (end of string)

-------------------------------------------------------------------------------
Example 2: Insert "AIT"
-------------------------------------------------------------------------------
A exists → I exists → now R ≠ T  
So attach T under I.

ASCII:

        A
        |
        I
       / \
      R   T
      |   |
      ●   ●

-------------------------------------------------------------------------------
Example 3: Insert "BAR"
-------------------------------------------------------------------------------
Root has no B → create B  
B → A → R → ●

ASCII:

        B
        |
        A
        |
        R
        |
        ●

-------------------------------------------------------------------------------
Example 4: Insert "BAL"
-------------------------------------------------------------------------------
B exists  
Under B → A exists  
Under A → child R exists, but we need L  
So create L → ●

ASCII:

        B
        |
        A
       / \
      R   L
      |   |
      ●   ●

-------------------------------------------------------------------------------
Example 5: Insert "BM"
-------------------------------------------------------------------------------
B exists  
Under B: A exists (but we need M) → create M → ●

ASCII:

        B
       / \
      A   M
     / \   |
    R   L  ●
    |   |
    ●   ●

===============================================================================
WHY DO WE NEED TRIE?
===============================================================================

Trie solves many real-world string problems efficiently:

1️⃣ **Spell Checker**  
   Words are stored level-by-level.  
   Compare character-by-character → early mismatch → O(1) stop.

2️⃣ **Auto-completion (Google Search)**  
   When user types "A":
     - Go to node A
     - DFS all children
     - Show suggestions: AIR, AIT, AIM, etc.

3️⃣ **Prefix Searching**  
   Searching all words beginning with “AL” or “BA” is extremely fast.

Compared to arrays or hash tables:
- Hash table can check complete words but NOT prefixes efficiently.
- Trie can check prefixes instantly.

===============================================================================
INTERNAL NODE STRUCTURE
===============================================================================

A real-world Trie node typically has:

    class TrieNode:
        def __init__(self):
            self.children = {}  # char → TrieNode
            self.endOfString = False
            self.charactersStored = ""   # optional compression

Example from lecture node:

    Node:
       characters: "AIM"
       children: { 'R': childRef, 'L': childRef }
       endOfString: False

===============================================================================
SUMMARY
===============================================================================
- Trie is a hierarchical tree for storing strings.
- Each character stored level-by-level.
- Perfect for prefix matching, searching, auto-completion.
- Very useful in dictionary applications and search engines.
- End-of-string indicator is crucial.
- Multiple strings share prefixes: saves memory and improves speed.

===============================================================================
END OF NOTES — Trie Introduction
===============================================================================
"""
