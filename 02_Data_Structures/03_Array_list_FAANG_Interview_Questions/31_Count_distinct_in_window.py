"""
===============================================================================
📘 note_count_distinct_in_window.py — Count Distinct Elements in Every Window
===============================================================================

Problem
-------
Given an array arr[] and integer k,
find number of DISTINCT elements in every window of size k.

Example
-------
arr = [1,2,1,3,4,2,3]
k = 4

Output:
[3,4,4,3]

Expected:
Time  → O(n)
Space → O(k)

===============================================================================
Approach 1 — Brute Force (O(n*k))
===============================================================================
"""
class SolutionBrute:
    def countDistinct(self, arr, k):
        """
        Purpose:
        Count distinct elements in every window of size k using brute force.

        Steps:
        1. For each starting index i
        2. Create an empty set
        3. Insert next k elements into the set
        4. Append size of set to result

        🔍 Visualization:

        arr = [1,2,1,3,4,2,3], k = 4

        Window 1 (0-3): [1,2,1,3]
        Set → {1,2,3}
        Distinct = 3

        Window 2 (1-4): [2,1,3,4]
        Set → {2,1,3,4}
        Distinct = 4

        Window 3 (2-5): [1,3,4,2]
        Set → {1,3,4,2}
        Distinct = 4

        Window 4 (3-6): [3,4,2,3]
        Set → {3,4,2}
        Distinct = 3

        ⏱️ Time Complexity: O(n*k)
        ⏱️ Space Complexity: O(k)
        """
        n = len(arr)
        result = []
        
        for i in range(n - k + 1):
            window_set = set()
            for j in range(i, i + k):
                window_set.add(arr[j])
            result.append(len(window_set))
        
        return result
"""
Time → O(n*k)
Space → O(k)

===============================================================================
Approach 2 — Sliding Window + HashMap (Optimal O(n))
===============================================================================
"""
class SolutionSliding:
    def countDistinct(self, arr, k):
        """
        Purpose:
        Count distinct elements efficiently using sliding window technique.

        Core Idea:
        Maintain a frequency dictionary for the current window.

        Steps:
        1. Build frequency map for first window
        2. Append len(freq) to result
        3. Slide window one element at a time:
           - Decrease outgoing element frequency
           - Remove if frequency becomes 0
           - Add incoming element
           - Append len(freq)

        🔍 Detailed Visualization:

        arr = [1,2,1,3,4,2,3]
        k = 4

        ---------------------------------
        First Window: [1,2,1,3]
        freq = {1:2, 2:1, 3:1}
        distinct = 3
        result = [3]

        ---------------------------------
        Slide 1 → add 4, remove 1
        outgoing = 1 → freq becomes {1:1,2:1,3:1}
        incoming = 4 → freq becomes {1:1,2:1,3:1,4:1}
        distinct = 4
        result = [3,4]

        ---------------------------------
        Slide 2 → add 2, remove 2
        outgoing = 2 → freq becomes {1:1,3:1,4:1}
        incoming = 2 → freq becomes {1:1,3:1,4:1,2:1}
        distinct = 4
        result = [3,4,4]

        ---------------------------------
        Slide 3 → add 3, remove 1
        outgoing = 1 → removed completely
        incoming = 3 → freq[3] becomes 2
        freq = {3:2,4:1,2:1}
        distinct = 3
        result = [3,4,4,3]

        Final Output → [3,4,4,3]

        ⏱️ Time Complexity: O(n)
        ⏱️ Space Complexity: O(k)
        """
        n = len(arr)
        freq = {}
        result = []
        
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
        result.append(len(freq))
        
        for i in range(k, n):
            outgoing = arr[i-k]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]
            
            incoming = arr[i]
            freq[incoming] = freq.get(incoming, 0) + 1
            
            result.append(len(freq))
        
        return result
"""
Time → O(n)
Space → O(k)

===============================================================================
Comparison
===============================================================================

Method        | Time     | Space | Recommended
--------------|----------|-------|------------
Brute Force   | O(n*k)   | O(k)  | ❌
Sliding + Map | O(n)     | O(k)  | ⭐ Best

===============================================================================
Demo Execution (Run Both Approaches)
===============================================================================
"""
if __name__ == "__main__":

    arr = [1,2,1,3,4,2,3]
    k = 4

    print("Array:", arr)
    print("k:", k)

    print("\nBrute Force:")
    print(SolutionBrute().countDistinct(arr, k))

    print("\nSliding Window:")
    print(SolutionSliding().countDistinct(arr, k))
"""
===============================================================================
How To Run
===============================================================================

python note_count_distinct_in_window.py

===============================================================================
Interview Cheat Sheet
===============================================================================

Fixed window + distinct count → HashMap + Sliding Window

When sliding:
- Remove outgoing
- Delete if freq = 0
- Add incoming
- Distinct = len(freq)

Time → O(n)
Space → O(k)

===============================================================================
"""
