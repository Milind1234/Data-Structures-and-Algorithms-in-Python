"""
===============================================================================
📘 04_DeleteString.py — Delete a String from a Trie (Detailed Notes + Diagrams)
===============================================================================

Purpose
-------
This file explains **how deletion works in a Trie** using your implementation.

It includes:

  ✔ All 4 deletion cases explained  
  ✔ Why deletion must ALWAYS start from leaf → root  
  ✔ How “dependencies” between words are handled  
  ✔ Full Python implementation (your original logic preserved exactly)  
  ✔ Step-by-step explanation of your deleteString() recursion  
  ✔ Time & Space complexity  

Remember:  
Trie deletion is tricky because a node may be shared among *multiple* words.  
We can delete a node ONLY if **no other word depends on it**.

===============================================================================
TRIE NODE & TRIE CLASS (Insert + Search)
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
        """
        Insert a string character-by-character.
        If character path doesn't exist → create a new TrieNode.

        Time Complexity  : O(m)
        Space Complexity : O(m)
        """
        current = self.rootnode
        for ch in word:
            node = current.children.get(ch)

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
        Search behavior:
        ----------------
        RETRUNS TRUE  → characters exist AND endOfString == True
        RETURNS FALSE → path missing OR only prefix

        Time Complexity  : O(m)
        Space Complexity : O(1)
        """
        currentNode = self.rootnode

        for ch in word:
            node = currentNode.children.get(ch)
            if node is None:    # no path → not found
                return False
            currentNode = node

        return currentNode.endOfString



"""
===============================================================================
DELETE STRING (Your Original Implementation + Full Explanation)
===============================================================================
"""

def deleteString(rootnode, word, index):
    """
    Delete word from Trie based on 4 deletion cases.

    IMPORTANT:
        ✔ Deletion ALWAYS starts from leaf node.
        ✔ We recursively go down and then DELETE while coming UP.
        ✔ A node can be deleted ONLY IF:
              - It has no children AND
              - It is NOT endOfString for another word.

    Parameters:
        rootnode : current TrieNode
        word     : string to delete
        index    : character position

    Returns:
        True  → this node can be deleted from its parent
        False → node must be preserved
    """

    # Character to process
    ch = word[index]
    currentNode = rootnode.children.get(ch)

    # If path doesn't exist, nothing to delete
    if currentNode is None:
        return False

    canThisNodeBeDeleted = False

    # -------------------------------------------------------------------------
    # CASE 1 — Node has multiple children → shared branch → DO NOT delete
    # -------------------------------------------------------------------------

    """
    CASE 1 — Word shares prefix with another word
    ---------------------------------------------
    Deleting "APP" when "APPLE" exists:

    A
     └─ P
         └─ P  (endOfString=True)
             └─ L ─ E
    We unmark 'P' but cannot delete it.
    """

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False     # cannot delete this node


    # -------------------------------------------------------------------------
    # CASE 2 — We reached LAST CHARACTER of the word
    # -------------------------------------------------------------------------
    """
    CASE 2 — Word is a PREFIX of another word
    -----------------------------------------
    Stored: API, APIS  
    Delete: API

    We only unmark:

        A → P → I (endOfString=False now)
                        \
                          S (endOfString=True)

    """

    if index == (len(word) - 1):

        # Case 2A: node has children → word is PREFIX of another word
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False   # unmark only
            return False

        # Case 2B: LEAF node → safe to delete
        else:
            rootnode.children.pop(ch)
            return True


    # -------------------------------------------------------------------------
    # CASE 3 — Another word ENDS here → cannot delete this node
    # -------------------------------------------------------------------------
    """
    CASE 3 — Another word is PREFIX of this word
    --------------------------------------------
    Stored: API  
    Delete: APIS

    We delete S → delete blank EOS → stop at I because API ends there.

    """

    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False


    # -------------------------------------------------------------------------
    # CASE 4 — Default case → recurse deeper and check deletability
    # -------------------------------------------------------------------------
    """
        CASE 4 — Word is isolated
    -------------------------
    Stored: K
    
    Delete K → whole branch removed.
    """

    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)

    # If child can be deleted, remove it from dictionary
    if canThisNodeBeDeleted == True:
        rootnode.children.pop(ch)
        return True
    else:
        return False



"""
===============================================================================
ASCII DIAGRAMS — ALL FOUR CASES
===============================================================================

Let the Trie contain: APP, APIS, APPLE, K, KITE

CASE 1 — Word shares prefix with another word
---------------------------------------------
Deleting "APP" when "APPLE" exists:

    A
     └─ P
         └─ P  (endOfString=True)
             └─ L ─ E

We unmark 'P' but cannot delete it.


CASE 2 — Word is a PREFIX of another word
-----------------------------------------
Stored: API, APIS  
Delete: API

We only unmark:

    A → P → I (endOfString=False now)
                    \
                      S (endOfString=True)


CASE 3 — Another word is PREFIX of this word
--------------------------------------------
Stored: API  
Delete: APIS

We delete S → delete blank EOS → stop at I because API ends there.


CASE 4 — Word is isolated
-------------------------
Stored: K

Delete K → whole branch removed.


===============================================================================
TIME & SPACE COMPLEXITY
===============================================================================

Operation            Time Complexity         Space Complexity
----------------------------------------------------------------
Insert(m)              O(m)                      O(m)
Search(m)              O(m)                      O(1)
Delete(m)              O(m)                      O(m)
                      (recursion depth)       (stack frames)

===============================================================================
"""


# =============================================================================
#                         EXAMPLE USAGE (RUN DIRECTLY)
# =============================================================================
if __name__ == "__main__":
    newTrie = Trie()

    newTrie.insertString("App")
    newTrie.insertString("Apis")

    print("\n--- SEARCH RESULTS ---")
    print("App  →", newTrie.searchString("App"))
    print("Apis →", newTrie.searchString("Apis"))
    print("Api  →", newTrie.searchString("Api"))
    print("Dack →", newTrie.searchString("Dack"))

    # Delete example
    deleteString(newTrie.rootnode, "App", 0)
    print("\nAfter Delete 'App':")
    print(newTrie.searchString("App"))
