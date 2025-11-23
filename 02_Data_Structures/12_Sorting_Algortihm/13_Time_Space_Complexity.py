"""
===============================================================================
📘 Sorting Algorithms Comparison — Time, Space, Stability (Detailed Notes)
===============================================================================

Purpose
-------
This notes section summarizes how to choose the correct sorting algorithm based on:
    • Time Complexity
    • Space Complexity
    • Stability
It also explains how the choice changes depending on system requirements.

===============================================================================
1) THREE CRITERIA TO CHOOSE A SORTING ALGORITHM
===============================================================================

When deciding which sorting algorithm to use, you must consider:

    1. Time Complexity      → How fast the algorithm runs as input grows
    2. Space Complexity     → How much extra memory the algorithm requires
    3. Stability            → Whether equal-valued elements keep their original order


===============================================================================
2) WHEN SPACE IS THE MAIN CONCERN (Embedded Systems, Low-memory devices)
===============================================================================

If your environment has very little RAM (like embedded systems, microcontrollers),
you MUST choose algorithms that use **O(1) space**.

These algorithms use constant extra memory:

    ✔ Bubble Sort       O(1) space  (stable)
    ✔ Selection Sort    O(1) space  (not stable)
    ✔ Insertion Sort    O(1) space  (stable)
    ✔ Heap Sort         O(1) space  (not stable)

Use these when memory consumption is the priority.


===============================================================================
3) WHEN TIME COMPLEXITY IS THE MAIN CONCERN (Large data, performance-critical)
===============================================================================

If you need **fast sorting**, choose algorithms with **O(n log n)** running time:

    ✔ Bucket Sort       O(n log n) avg   (stable)
    ✔ Merge Sort        O(n log n)       (stable)
    ✔ Quick Sort        O(n log n) avg   (not stable)
    ✔ Heap Sort         O(n log n)       (not stable)

These are widely used in high-performance systems.

NOTE:
 - QuickSort is generally the fastest in practice (good cache usage),
   but it is NOT stable.
 - MergeSort is stable but needs O(n) extra space.
 - HeapSort is time-efficient + O(1) space, but not stable.


===============================================================================
4) WHEN STABILITY IS IMPORTANT (Databases, Records, Sorting by multiple fields)
===============================================================================

An algorithm is stable if:
    "Equal-valued elements remain in the same relative order after sorting."

Stability is required when:
    • sorting employee records by salary but maintaining alphabetical order
    • sorting objects with multiple attributes
    • sorting strings where equal prefixes matter

Stable sorting algorithms:

    ✔ Bubble Sort      (Stable)
    ✔ Insertion Sort   (Stable)
    ✔ Bucket Sort      (Stable)
    ✔ Merge Sort       (Stable)

Unstable algorithms:
    ✘ Selection Sort
    ✘ Quick Sort
    ✘ Heap Sort


===============================================================================
5) THE BIG PICTURE — SORTING ALGORITHM TABLE
===============================================================================

Name              Time Complexity     Space Complexity     Stable?
-----------------------------------------------------------------------
Bubble Sort       O(n²)               O(1)                 Yes
Selection Sort    O(n²)               O(1)                 No
Insertion Sort    O(n²)               O(1)                 Yes
Bucket Sort       O(n log n)          O(n)                 Yes
Merge Sort        O(n log n)          O(n)                 Yes
Quick Sort        O(n log n) avg      O(n) / O(log n)      No
Heap Sort         O(n log n)          O(1)                 No
-----------------------------------------------------------------------


===============================================================================
6) HOW TO CHOOSE THE RIGHT SORT?
===============================================================================

Case 1 — LIMITED MEMORY (microcontrollers, embedded)
    → Use: Bubble, Selection, Insertion, Heap Sort (O(1) space)

Case 2 — NEED FAST PERFORMANCE
    → Use: QuickSort / MergeSort / HeapSort / Bucket Sort

Case 3 — STABILITY REQUIRED
    → Use: MergeSort, Insertion Sort, Bubble Sort, Bucket Sort

Case 4 — GENERAL PURPOSE (most programming languages default)
    → Python uses Timsort (Hybrid: Merge + Insertion)
       • O(n log n)
       • Stable
       • Excellent real-world performance

===============================================================================
7) FINAL SUMMARY
===============================================================================

Sorting algorithm choice depends on:
    ✔ memory limits
    ✔ speed requirements
    ✔ whether stability is needed

There is NO universally best sorting algorithm.
Each algorithm shines in different scenarios.

===============================================================================
"""
