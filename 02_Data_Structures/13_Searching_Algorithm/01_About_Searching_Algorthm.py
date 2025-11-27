"""
===============================================================================
📘 Searching Algorithms — Introduction, Purpose, Real-World Use Cases
===============================================================================

Purpose
-------
This note introduces the concept of searching algorithms.
We cover:
    • Why searching algorithms are needed
    • Real-world cases where searching happens behind the scenes
    • Difference between simple searches (Linear / Binary) and complex systems
    • Examples from real applications (usernames, login systems, databases)

These notes prepare us for the two main searching algorithms:
    1. Linear Search
    2. Binary Search

===============================================================================
1) WHAT IS A SEARCHING ALGORITHM?
===============================================================================

A searching algorithm is a method used to *find* something inside a data structure,
such as:
    • an element in a list
    • a value in an array
    • a record in a database
    • a text in a document

Whenever your application needs to answer the question:

        "Does this item exist?"

you are using a searching algorithm — intentionally or behind the scenes.

Examples:
    • Searching for a username in the system
    • Searching for a product in an e-commerce database
    • Searching for contacts inside your phone
    • Searching for files in an operating system
    • Searching for elements in a sorted array (Binary Search)


===============================================================================
2) "SEARCH" IN REAL LIFE (Google vs Algorithm Basics)
===============================================================================

When most people hear "search", they think of Google.

But:
    🔹 Google Search algorithms are extremely complex.
    🔹 They consider:
         - browsing history
         - personalization
         - click patterns
         - device type
         - location
         - search frequency
         - ranking signals (over 200+ parameters)

We are NOT building Google Search here.

Instead, we learn the **fundamental searching algorithms** used inside
applications, interview problems, and many data structures.

Our algorithms:
    ✔ simple
    ✔ efficient for their purpose
    ✔ used in all programming tasks
    ✔ required for coding interviews


===============================================================================
3) WHY DO WE NEED SEARCHING ALGORITHMS?
===============================================================================

Searching is required in almost EVERY application.

Let’s take a simple example:

-----------------------------------
📌 Example: User Registration System
-----------------------------------

Suppose users choose a username when registering.

Requirement:
    • All usernames must be UNIQUE.

Process:
    1. User enters a username (e.g., "Elshad")
    2. System searches the list of existing usernames
    3. If found → reject: “Username already taken”
    4. If NOT found → insert it and confirm registration

Without searching, this system cannot function.

Similar real-world examples:
    ✔ login verification (check if email exists)
    ✔ banking apps (verify account number)
    ✔ gaming platform (check if nickname is available)
    ✔ e-commerce (find product by ID)
    ✔ dictionary apps (search for a word)
    ✔ phone contacts search


===============================================================================
4) TYPES OF SEARCHING ALGORITHMS WE WILL LEARN
===============================================================================

In this section we will study:

---------------------------------------------------
1) LINEAR SEARCH (Simple, works on unsorted lists)
---------------------------------------------------
    • Checks elements one-by-one from left to right.
    • Works on ANY list (sorted or unsorted).
    • Used internally in many small lists.

Real-world use:
    ✔ searching your name in classroom attendance list
    ✔ scanning items in a grocery bill
    ✔ finding a file manually in a folder


---------------------------------------------------
2) BINARY SEARCH (Fastest for sorted data)
---------------------------------------------------
    • Works ONLY on sorted lists.
    • Uses divide-and-conquer:
         - check the middle
         - eliminate half the list each step
    • Very efficient → O(log n)

Real-world use:
    ✔ searching in a phonebook sorted by name
    ✔ searching dictionary words (A-Z)
    ✔ searching ordered numerical datasets
    ✔ internal use in many programming libraries


===============================================================================
5) WHY WE STUDY SEARCHING ALGORITHMS BEFORE TREES & HASH TABLES?
===============================================================================

Because:
    • searching inside arrays teaches the cost of naive search
    • helps understand WHY binary search trees exist
    • explains WHY hashing was invented
    • forms the foundation for:
            – Binary Search Trees (BST)
            – AVL Trees
            – Red/Black Trees
            – Hash Tables
            – Databases indexing


===============================================================================
6) ADDITIONAL REAL WORLD EXAMPLES OF SEARCHING
===============================================================================

✔ Checking if an item is in a shopping cart  
✔ Searching for messages inside WhatsApp chat  
✔ Searching for songs by name in music apps  
✔ Searching inside logs for error messages  
✔ Searching for substring inside a document (Ctrl + F)  
✔ Searching for open tabs in a browser  
✔ Searching transaction ID in a long list of orders  


===============================================================================
7) SUMMARY
===============================================================================

• Searching algorithms are fundamental to ALL software applications.
• They help us find whether data exists and where it is located.
• Two most important algorithms:
        - Linear Search → works on ANY list
        - Binary Search → requires sorted list, but extremely fast
• Real-world apps constantly rely on searching for performance and correctness.

Next steps:
    → We will learn Linear Search with diagrams and dry runs.
    → Then Binary Search with midpoint visualization and recursive approach.

===============================================================================
"""
