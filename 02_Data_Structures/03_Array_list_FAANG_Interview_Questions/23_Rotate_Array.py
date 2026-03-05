"""
===============================================================================
📘 note_rotate_array.py — Rotate Array (Brute Force, Extra Array, Reversal, Juggling)
===============================================================================

Problem
-------
Given an array arr[] rotate the array to the LEFT by d positions.
Rotation is circular.

Example
-------
arr = [1,2,3,4,5], d = 2

Step1: [2,3,4,5,1]
Step2: [3,4,5,1,2]

Final Output
------------
[3,4,5,1,2]

Important Concept
-----------------
Array is considered circular.
If d > n we reduce rotations.

Example:
arr = [7,3,9,1]
d = 9
n = 4

Effective rotation:

    d = d % n
    d = 9 % 4 = 1

So rotate only once.

===============================================================================
Approach 1 — Brute Force (Rotate One by One)
===============================================================================

Idea
----
Rotate array d times.
Each rotation shifts elements one step left.

Example
-------
arr = [1,2,3,4,5]

Rotation1
[2,3,4,5,1]

Rotation2
[3,4,5,1,2]

Code
----
"""

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        
        for _ in range(d):
            first = arr[0]
            
            for i in range(1, n):
                arr[i-1] = arr[i]
                
            arr[n-1] = first

"""
Time Complexity
---------------
Each rotation takes O(n)

Total rotations = d

Time = O(n * d)

Worst case
----------
n = 100000

d = 100000

→ Too slow

Space Complexity
----------------
O(1)

Pros
----
✔ Very easy to understand

Cons
----
❌ Very slow for large input

===============================================================================
Dry Run + Visualization (For Each Approach)
===============================================================================

Example used for dry run
------------------------
arr = [1,2,3,4,5]
d = 2

Expected result
---------------
[3,4,5,1,2]


-----------------------------------------------------------------------
Approach 1 Dry Run — Brute Force
-----------------------------------------------------------------------

Initial
[1,2,3,4,5]

Rotation 1
---------
Store first = 1
Shift elements left

2 3 4 5 _

Place first at end

[2,3,4,5,1]

Rotation 2
---------
Store first = 2

3 4 5 1 _

Place 2 at end

[3,4,5,1,2]

Final result achieved after d rotations.


===============================================================================
Approach 2 — Using Extra Array
===============================================================================

Idea
----
Store first d elements temporarily.
Shift remaining elements to front.
Place stored elements at end.

Example
-------
arr = [1,2,3,4,5]
d = 2

Step1: temp = [1,2]

Step2: shift left

[3,4,5,4,5]

Step3: place temp

[3,4,5,1,2]

Code
----
"""

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        
        temp = arr[:d]
        
        for i in range(d, n):
            arr[i-d] = arr[i]
        
        for i in range(d):
            arr[n-d+i] = temp[i]

"""

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(d)

Pros
----
✔ Simple
✔ Fast

Cons
----
❌ Uses extra space

-----------------------------------------------------------------------
Approach 2 Dry Run — Extra Array
-----------------------------------------------------------------------

Initial
[1,2,3,4,5]

Step 1
------
Store first d elements

temp = [1,2]

Step 2
------
Shift remaining elements

arr becomes

[3,4,5,4,5]

Step 3
------
Place temp at end

[3,4,5,1,2]


===============================================================================
Approach 3 — Reversal Algorithm (Most Popular)
===============================================================================

Idea
----
Rotate using 3 reversals.

Example
-------
arr = [1,2,3,4,5]
d = 2

Step1 reverse first d

[2,1,3,4,5]

Step2 reverse remaining

[2,1,5,4,3]

Step3 reverse whole array

[3,4,5,1,2]

Visualization
-------------
Original

1 2 | 3 4 5

Reverse first part

2 1 | 3 4 5

Reverse second part

2 1 | 5 4 3

Reverse whole

3 4 5 | 1 2

Code
----
"""

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        
        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        reverse(0, d-1)
        reverse(d, n-1)
        reverse(0, n-1)

"""

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(1)

Pros
----
✔ No extra space
✔ Very fast
✔ Interview favorite

-----------------------------------------------------------------------
Approach 3 Dry Run — Reversal Algorithm
-----------------------------------------------------------------------

Initial

1 2 | 3 4 5

Step 1 Reverse first d

2 1 | 3 4 5

Step 2 Reverse remaining

2 1 | 5 4 3

Step 3 Reverse whole array

3 4 5 | 1 2

Final

[3,4,5,1,2]


===============================================================================
Approach 4 — Juggling Algorithm (GCD Method)
===============================================================================

Idea
----
Divide array into cycles using GCD.
Move elements within cycles.

Example
-------
arr = [1,2,3,4,5,6]
d = 2

n = 6

gcd(6,2) = 2 cycles

Cycle1
------
1 → 3 → 5 → 1

Cycle2
------
2 → 4 → 6 → 2

Elements shift within cycles.

Code
----
"""

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        g = gcd(n, d)
        
        for i in range(g):
            temp = arr[i]
            j = i
            
            while True:
                k = j + d
                
                if k >= n:
                    k -= n
                    
                if k == i:
                    break
                    
                arr[j] = arr[k]
                j = k
            
            arr[j] = temp

"""

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(1)

Pros
----
✔ No extra space
✔ Efficient

Cons
----
❌ Hard to understand
❌ Rarely asked compared to reversal

===============================================================================
Dry Run + Visualization (For Each Approach)
===============================================================================

Example used for dry run
------------------------
arr = [1,2,3,4,5]
d = 2

Expected result
---------------
[3,4,5,1,2]


-----------------------------------------------------------------------
Approach 4 Dry Run — Juggling Algorithm
-----------------------------------------------------------------------

Example
arr = [1,2,3,4,5]
d = 2
n = 5

Compute

gcd(5,2) = 1

So only ONE cycle

Cycle movement
--------------

Start index = 0

temp = 1

Move elements by d positions

index 0 -> 2
index 2 -> 4
index 4 -> 1
index 1 -> 3
index 3 -> 0

Cycle visualization

1 → 3 → 5 → 2 → 4 → back to 1

Array transformation

Step1 move 3 to index0

[3,2,3,4,5]

Step2 move 5 to index2

[3,2,5,4,5]

Step3 move 2 to index4

[3,2,5,4,2]

Step4 move 4 to index1

[3,4,5,4,2]

Step5 place temp

[3,4,5,1,2]

Final result

[3,4,5,1,2]



===============================================================================
Comparison Table

===============================================================================

Method              | Time Complexity | Space Complexity
--------------------|----------------|-----------------
Brute Force         | O(n*d)         | O(1)
Extra Array         | O(n)           | O(d)
Reversal Algorithm  | O(n)           | O(1)
Juggling Algorithm  | O(n)           | O(1)

===============================================================================
Interview Recommendation
===============================================================================

BEST METHOD
-----------
Reversal Algorithm

Reason
------
✔ O(n) time
✔ O(1) space
✔ Easy to explain
✔ Most commonly expected in interviews

===============================================================================
Demo Execution
===============================================================================

if __name__ == "__main__":

    arr = [1,2,3,4,5]
    d = 2

    print("Original Array:", arr)

    s = Solution()
    s.rotateArr(arr, d)

    print("Rotated Array:", arr)

===============================================================================
"""
