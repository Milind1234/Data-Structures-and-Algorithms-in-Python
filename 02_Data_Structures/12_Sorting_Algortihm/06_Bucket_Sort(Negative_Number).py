"""
===============================================================================
📘 BucketSort_Negative_Numbers_Notes.py — Bucket Sort Handling Negative Numbers
===============================================================================

This file contains:

- Clean explanation of how bucket sort works when negative values exist
- ASCII visualization for bucket distribution
- Flowchart (ASCII)
- Exact implementation provided by you (kept unchanged)
- insertionSort helper
- Dry-run example
- Time & Space complexity notes

===============================================================================
"""

import math

# -----------------------------------------------------------------------------
# INSERTION SORT (used to sort each bucket)
# -----------------------------------------------------------------------------
def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList


# -----------------------------------------------------------------------------
# BUCKET SORT FOR NEGATIVE NUMBERS (CODE EXACTLY AS PROVIDED)
# -----------------------------------------------------------------------------
def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberofBuckets
 
    buckets = [[] for _ in range(numberofBuckets)]
 
    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue) / rangeVal)
            buckets[index_b].append(j)
    
    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = insertionSort(buckets[i])
        sorted_array.extend(buckets[i])
    
    return sorted_array



# -----------------------------------------------------------------------------
# THEORY — Explanation in plain python-note style
# -----------------------------------------------------------------------------
EXPLANATION = """
Bucket Sort With Negative Numbers
---------------------------------
When negative numbers exist, bucket sort must adjust bucket boundaries.

Key idea:
    Before placing values into buckets, shift all values relative to the
    minimum number in the array.

Variables used:
    minValue  → minimum element in the array
    maxValue  → maximum element in the array
    rangeVal  → bucket width = (maxValue - minValue) / numberOfBuckets

Bucket index formula:
    index = floor( (value - minValue) / rangeVal )

This ensures:
    - Negative numbers map to correct buckets
    - Range is normalized from 0 → (maxValue − minValue)
"""


# -----------------------------------------------------------------------------
# ASCII VISUALIZATION FOR NEGATIVE NUMBER BUCKETING
# -----------------------------------------------------------------------------
VISUAL = """
Example:
    customList = [-7, -3, 0, 2, 5, -1, 4]
    n = 7 → numberOfBuckets = round(sqrt(7)) = 3

minValue = -7
maxValue =  5
rangeVal  = (5 - (-7)) / 3 = 12/3 = 4

Bucket Ranges:
    Bucket 0 → [-7  to -3)
    Bucket 1 → [-3  to  1)
    Bucket 2 → [ 1  to  5]

Distribution:
    -7 → bucket 0    ((-7 - (-7))/4 = 0)
    -3 → bucket 1    ((-3 - (-7))/4 = 1)
    -1 → bucket 1
     0 → bucket 1
     2 → bucket 2
     4 → bucket 2
     5 → LAST BUCKET (special case for maxValue)

After sorting each bucket:
    bucket 0: [-7]
    bucket 1: [-3, -1, 0]
    bucket 2: [2, 4, 5]

Final merged result:
    [-7, -3, -1, 0, 2, 4, 5]
"""


# -----------------------------------------------------------------------------
# FLOWCHART (ASCII)
# -----------------------------------------------------------------------------
FLOWCHART = """
            ┌──────────────────────────┐
            │        Start             │
            └─────────────┬────────────┘
                          │
        ┌─────────────────▼─────────────────┐
        │ Compute buckets = round(sqrt(n))  │
        └─────────────────┬─────────────────┘
                          │
        ┌─────────────────▼──────────────────────────────────┐
        │ Find minValue and maxValue                         │
        └─────────────────┬──────────────────────────────────┘
                          │
        ┌─────────────────▼──────────────────────────────────┐
        │ Compute rangeVal = (maxValue - minValue)/buckets   │
        └─────────────────┬──────────────────────────────────┘
                          │
        ┌─────────────────▼──────────────────────────────────┐
        │ Place each element into correct bucket              │
        │ index = floor((value - minValue)/rangeVal)          │
        └─────────────────┬──────────────────────────────────┘
                          │
        ┌─────────────────▼──────────────────────────────────┐
        │ Sort each bucket using insertion sort              │
        └─────────────────┬──────────────────────────────────┘
                          │
        ┌─────────────────▼──────────────────────────────────┐
        │ Merge all buckets into final sorted array           │
        └─────────────────┬──────────────────────────────────┘
                          │
            ┌─────────────▼────────────┐
            │           End            │
            └──────────────────────────┘
"""


# -----------------------------------------------------------------------------
# DRY RUN — Example Demonstration
# -----------------------------------------------------------------------------
def dry_run():
    example = [-7, -3, 0, 2, 5, -1, 4]
    print("\n=== DRY RUN FOR NEGATIVE NUMBER BUCKET SORT ===")
    print("Input:", example)

    n = len(example)
    numberofBuckets = round(math.sqrt(n))
    minValue = min(example)
    maxValue = max(example)
    rangeVal = (maxValue - minValue) / numberofBuckets

    print("\nBuckets =", numberofBuckets)
    print("minValue =", minValue)
    print("maxValue =", maxValue)
    print("rangeVal =", rangeVal)

    buckets = [[] for _ in range(numberofBuckets)]

    print("\n--- Distribution Phase ---")
    for j in example:
        if j == maxValue:
            idx = numberofBuckets - 1
        else:
            idx = math.floor((j - minValue) / rangeVal)
        buckets[idx].append(j)
        print(f"Value {j} → bucket {idx}  →", buckets)

    print("\n--- Sorting Each Bucket ---")
    for i in range(numberofBuckets):
        print(f"bucket[{i}] before:", buckets[i])
        buckets[i] = insertionSort(buckets[i])
        print(f"bucket[{i}] after :", buckets[i])

    print("\n--- Merging Buckets ---")
    result = []
    for b in buckets:
        result.extend(b)
        print("merged:", result)

    print("\nFinal Sorted Output:", result)



# -----------------------------------------------------------------------------
# COMPLEXITY
# -----------------------------------------------------------------------------
COMPLEXITY = """
Time Complexity
---------------
Best / Avg Case (uniform distribution):
    O(N + N * log(N/K))  ≈ O(N)

Worst Case (all elements in one bucket):
    O(N^2)

Space Complexity:
    O(N + K)
    N = number of elements
    K = number of buckets
"""


# -----------------------------------------------------------------------------
# RUN DEMO
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print(EXPLANATION)
    print(VISUAL)
    print(FLOWCHART)
    dry_run()
    print(COMPLEXITY)
