"""
=========================================================
Count Word Frequency - Multiple Approaches (with Notes)
=========================================================

Problem:
--------
Given a list of words, count how many times each word occurs.

Example:
--------
Input:  ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
Output: {'apple': 3, 'orange': 2, 'banana': 1}

=========================================================
1. Basic Approach (Manual Dictionary Counting)
=========================================================
Steps:
1. Create an empty dictionary
2. Iterate through the list
3. If word exists in dictionary → increment count
4. Else → set count to 1

Time Complexity: O(n)  (n = number of words)
Space Complexity: O(k) (k = number of unique words)

Pros:
- Very intuitive and easy to explain in interviews
- Shows understanding of hash tables

Cons:
- Need to handle key existence manually
"""

def count_frequency_basic(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


"""
=========================================================
2. Using list.count() Method
=========================================================
Steps:
1. Convert list to set() to get unique words
2. For each unique word → use list.count() to find frequency

Time Complexity: O(n²) worst case (count() scans full list for each unique word)
Space Complexity: O(k) (for result dictionary)

Pros:
- Easy to write
Cons:
- Very slow for large data
"""

def count_frequency_using_count(words):
    return {word: words.count(word) for word in set(words)}


"""
=========================================================
3. Using collections.defaultdict (or Counter Logic)
=========================================================
Steps:
1. Use defaultdict(int) which initializes keys automatically
2. Loop and increment counts directly

Time Complexity: O(n)
Space Complexity: O(k)

Pros:
- Clean and efficient
- Pythonic
Cons:
- Slightly advanced for beginners
"""

from collections import defaultdict

def count_frequency_defaultdict(words):
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1
    return dict(freq)


"""
=========================================================
4. Sorting + Grouping (itertools.groupby)
=========================================================
Steps:
1. Sort the list (O(n log n))
2. Group identical items using groupby
3. Count group sizes

Time Complexity: O(n log n)
Space Complexity: O(1) extra (if sorted in place)

Pros:
- Useful if output needs sorted order
Cons:
- Slower than hash-based methods for counting
"""

from itertools import groupby

def count_frequency_sorting(words):
    words.sort()
    freq = {key: len(list(group)) for key, group in groupby(words)}
    return freq


"""
=========================================================
5. Functional / MapReduce Style
=========================================================
Steps:
1. Map each word to (word, 1)
2. Reduce by summing frequencies

Time Complexity: O(n)
Space Complexity: O(k)

Pros:
- Good for advanced (Big Data / ML) interviews
Cons:
- Overkill for small problems
"""

from functools import reduce

def count_frequency_mapreduce(words):
    mapped = [(word, 1) for word in words]
    freq = {}
    for word, value in mapped:
        freq[word] = freq.get(word, 0) + value
    return freq


"""
=========================================================
SUMMARY OF APPROACHES
=========================================================
Approach                Time Complexity    Space Complexity
----------------------------------------------------------
1. Basic Dictionary     O(n)              O(k)
2. list.count()         O(n²)             O(k)
3. defaultdict/Counter  O(n)              O(k)
4. Sorting + Grouping   O(n log n)        O(1) extra
5. MapReduce Style      O(n)              O(k)

Best Choice for Interviews:
- Approach 1 (Basic Dictionary)
- Approach 3 (defaultdict / Counter)
"""

# =============================
# Example Test
# =============================
if __name__ == "__main__":
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']

    print("Basic Approach:", count_frequency_basic(words))
    print("Using count():", count_frequency_using_count(words))
    print("Defaultdict:", count_frequency_defaultdict(words))
    print("Sorting + Grouping:", count_frequency_sorting(words.copy()))
    print("MapReduce Style:", count_frequency_mapreduce(words))
