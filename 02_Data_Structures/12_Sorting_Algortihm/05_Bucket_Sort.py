"""
===============================================================================
📘 BucketSort_Notes.py — Bucket Sort (Theory + Visualization + Code + Dry runs)
===============================================================================

Contents:
- Plain-language explanation and the bucket formulas used in these notes
- ASCII visualizations showing how items are distributed into buckets
- ASCII flowchart (high level)
- The Bucket_Sort function exactly as provided (kept unchanged)
- insertionSort helper (kept as in your snippet)
- Verbose trace mode (step-by-step distribution, per-bucket sort, merge)
- Dry-run generator that prints iteration-by-iteration state (notes style)
- Complexity analysis and guidance on when to use / avoid bucket sort

Uploaded image referenced in the materials (local path):
    /mnt/data/WhatsApp Image 2025-11-20 at 14.40.52.jpeg

Run:
    python BucketSort_Notes.py
===============================================================================
"""

from typing import List
import math
import textwrap

# -----------------------------------------------------------------------------
# THEORY — Short Definition
# -----------------------------------------------------------------------------
THEORY = """
Bucket Sort — Short Definition
------------------------------
Bucket sort distributes elements of an array into a number of buckets.
Each bucket is sorted individually (commonly using insertion sort).
Finally, the buckets are concatenated to produce the sorted array.

Two commonly used formulas:
  - number_of_buckets = round(sqrt(n))            # n = len(array)
  - bucket_index = ceil((value * number_of_buckets) / max_value) - 1

Notes:
  - Values are expected to be non-negative and bounded (or normalized).
  - For best performance the input values should be (approximately) uniformly
    distributed across the range.
"""

# -----------------------------------------------------------------------------
# ASCII VISUALIZATION — distribution example
# -----------------------------------------------------------------------------
VISUAL = """
Example distribution (n = 9, buckets = round(sqrt(9)) = 3)

Array: [5, 3, 4, 7, 2, 8, 6, 9, 1]
Max value = 9
Buckets (index formula): idx = ceil((value * 3)/9) - 1

Distribution steps:
  value=5 -> (5*3)/9 = 1.666.. -> ceil -> 2 -> idx=1 (bucket 2)
  value=3 -> (3*3)/9 = 1.      -> ceil -> 1 -> idx=0 (bucket 1)
  value=4 -> (4*3)/9 = 1.333.. -> ceil -> 2 -> idx=1 (bucket 2)
  value=7 -> (7*3)/9 = 2.333.. -> ceil -> 3 -> idx=2 (bucket 3)
  value=2 -> (2*3)/9 = 0.666.. -> ceil -> 1 -> idx=0 (bucket 1)
  value=8 -> (8*3)/9 = 2.666.. -> ceil -> 3 -> idx=2 (bucket 3)
  value=6 -> (6*3)/9 = 2       -> ceil -> 2 -> idx=1 (bucket 2)
  value=9 -> (9*3)/9 = 3       -> ceil -> 3 -> idx=2 (bucket 3)
  value=1 -> (1*3)/9 = 0.333.. -> ceil -> 1 -> idx=0 (bucket 1)

Buckets (before sort):
  bucket 0: [3, 2, 1]
  bucket 1: [5, 4, 6]
  bucket 2: [7, 8, 9]

After sorting each bucket (e.g. insertion sort):
  bucket 0: [1, 2, 3]
  bucket 1: [4, 5, 6]
  bucket 2: [7, 8, 9]

Merge (concatenate buckets): [1,2,3,4,5,6,7,8,9]
"""

# -----------------------------------------------------------------------------
# ASCII FLOWCHART — high-level
# -----------------------------------------------------------------------------
FLOWCHART = """
Bucket Sort — Flowchart (ASCII)
--------------------------------
START
  |
  v
Compute k = round(sqrt(n)) and maxValue
  |
  v
Create k empty buckets: arr = [ [] for _ in range(k) ]
  |
  v
For each value v in input:
  compute index = ceil((v * k) / maxValue) - 1
  arr[index].append(v)
  |
  v
For each bucket in arr:
  sort(bucket)   # use insertion sort (or any efficient sort)
  |
  v
Concatenate buckets into original array
  |
  v
END
"""

# -----------------------------------------------------------------------------
# insertionSort helper (returns list) — kept as in your snippet
# -----------------------------------------------------------------------------
def insertionSort(customList):
    for i in range(1 , len(customList)):
        key = customList[i]
        j = i-1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList

# -----------------------------------------------------------------------------
# Bucket_Sort function — EXACTLY as provided by you (kept unchanged)
# -----------------------------------------------------------------------------
def Bucket_Sort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    
    for j in customList:
        index_bucket = math.ceil((j *  numberOfBuckets) / maxValue) - 1
        arr[index_bucket].append(j)

    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


# -----------------------------------------------------------------------------
# Verbose mode to illustrate each step (distribution, sorting buckets, merge)
# (This wrapper uses your Bucket_Sort logic but prints steps before/after)
# -----------------------------------------------------------------------------
def Bucket_Sort_verbose(customList):
    """
    Verbose runner that prints distribution -> per-bucket contents -> sorted buckets -> merged result.
    The internal bucket sorting is done by your Bucket_Sort implementation.
    """
    print("\n=== BUCKET SORT — VERBOSE TRACE ===")
    print("Input:", customList)
    if not customList:
        print("Empty list — nothing to do.")
        return customList

    n = len(customList)
    k = round(math.sqrt(n))
    if k <= 0:
        k = 1
    maxValue = max(customList)
    print(f"Number of buckets (k) = round(sqrt({n})) = {k}")
    print(f"Max value = {maxValue}\n")

    # Show distribution (recompute same as in your function)
    buckets = [[] for _ in range(k)]
    for v in customList:
        idx = math.ceil((v * k) / maxValue) - 1
        idx = max(0, min(idx, k-1))
        buckets[idx].append(v)
        print(f"  value {v} -> bucket {idx}")

    print("\nBuckets after distribution:")
    for i, b in enumerate(buckets):
        print(f"  bucket[{i}] = {b}")

    # Use your insertionSort to sort each bucket and display
    print("\nSorting each bucket (using insertionSort):")
    for i in range(k):
        print(f"  bucket[{i}] before sort: {buckets[i]}")
        buckets[i] = insertionSort(buckets[i])
        print(f"  bucket[{i}] after  sort: {buckets[i]}")

    # Merge and show final result
    merged = []
    for i in range(k):
        merged.extend(buckets[i])
        print(f"  after adding bucket[{i}]: {merged}")

    # Put merged results back into list using your merge approach
    for i in range(len(merged)):
        customList[i] = merged[i]

    print("\nFinal sorted array:", customList)
    return customList

# -----------------------------------------------------------------------------
# Dry-run function — prints notes-style step-by-step for a chosen example
# -----------------------------------------------------------------------------
def bucket_sort_dry_run(example: List[int]):
    print("\n=== BUCKET SORT — DETAILED DRY RUN ===")
    print("Example input:", example)
    arr = example.copy()
    n = len(arr)
    if n == 0:
        print("Empty array — done.")
        return

    k = round(math.sqrt(n))
    if k <= 0:
        k = 1
    maxValue = max(arr)

    print(f"\nStep 1: Compute k = round(sqrt(n)) = {k}")
    print(f"Step 2: maxValue = {maxValue}")

    buckets = [[] for _ in range(k)]
    print("\nStep 3: Distribute elements into buckets using index = ceil((v*k)/maxValue)-1")

    for v in arr:
        idx = math.ceil((v * k) / maxValue) - 1
        idx = max(0, min(idx, k - 1))
        print(f"  value {v}: (v*k)/maxValue = {(v*k)/maxValue:.4f} -> ceil -> bucket {idx}")
        buckets[idx].append(v)

    print("\nBuckets after distribution (before sorting):")
    for i, b in enumerate(buckets):
        print(f"  bucket[{i}] = {b}")

    print("\nStep 4: Sort each bucket (insertion sort)")
    for i in range(k):
        print(f"  bucket[{i}] before sort: {buckets[i]}")
        buckets[i] = insertionSort(buckets[i])
        print(f"  bucket[{i}] after sort : {buckets[i]}")

    print("\nStep 5: Merge buckets (concatenate)")
    merged = []
    for i in range(k):
        merged.extend(buckets[i])
        print(f"  after bucket[{i}] -> merged: {merged}")

    print("\nDry-run final sorted array:", merged)
    return merged

# -----------------------------------------------------------------------------
# Complexity & When to use
# -----------------------------------------------------------------------------
COMPLEXITY_AND_GUIDANCE = textwrap.dedent("""
Time & Space Complexity (summary)
---------------------------------
- Best case (good distribution, small buckets + use O(n) bucket sort):
    Time: O(n + k + sum(sort(bucket_i))) ~ O(n) if buckets small
- Average case:
    Time: O(n + k + n * t) depending on bucket sort used inside
- Worst case:
    Time: O(n^2)  (if all elements land in one bucket and we use insertion sort)
- Space:
    O(n + k) additional space (buckets list + extra arrays)
    If you count only in-place operations, original array is reused for result
- Important: bucket sort is not in-place because of bucket arrays

When to use Bucket Sort
-----------------------
- Input values are:
    • numeric (or mappable to numeric),
    • from a bounded range (or normalized to a bounded range),
    • and roughly uniformly distributed.
- Use when you can afford O(n) extra space and want near-linear performance.

When to avoid Bucket Sort
-------------------------
- Input distribution is highly skewed (many collisions into a few buckets).
- Memory is tight (bucket arrays increase memory).
- Input contains negative numbers or floats without normalization — handle carefully.
- You need a stable guaranteed O(n log n) behavior (use merge/heap/quick variants instead).
""")

# -----------------------------------------------------------------------------
# If run as a script, demonstrate the functions and traces
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n" + "="*80)
    print("BUCKET SORT — FULL NOTES")
    print("="*80)

    print("\nTHEORY:")
    print(THEORY)

    print("\nEXAMPLE VISUAL:")
    print(VISUAL)

    print("\nFLOWCHART:")
    print(FLOWCHART)

    # Demo: Original implementation (clean) — using your code exactly
    demo = [3, 2, 4, 1, 5, 7, 6, 8]
    print("\n" + "="*40 + " DEMO: Bucket_Sort (clean) " + "="*40)
    print("Input:", demo)
    out = Bucket_Sort(demo.copy())
    print("Sorted:", out)

    # Demo: Verbose trace (uses the wrapper that prints steps)
    demo2 = [5, 3, 4, 7, 2, 8, 6, 9, 1]
    print("\n" + "="*40 + " DEMO: Bucket_Sort_verbose " + "="*40)
    Bucket_Sort_verbose(demo2.copy())

    # Dry run
    print("\n" + "="*40 + " DEMO: bucket_sort_dry_run " + "="*40)
    bucket_sort_dry_run([5, 3, 4, 7, 2, 8, 6, 9, 1])

    # Complexity & Guidance
    print("\n" + "="*40 + " COMPLEXITY & GUIDANCE " + "="*40)
    print(COMPLEXITY_AND_GUIDANCE)

    print("\nUploaded file referenced in materials (local path):")
    print("/mnt/data/WhatsApp Image 2025-11-20 at 14.40.52.jpeg")
    print("\nEnd of BucketSort_Notes.py demo.")
