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




===============================================================================
When d > n (Important Visualization)
===============================================================================

Sometimes the rotation value is larger than array size.

Example
-------
arr = [7,3,9,1]
d = 9

Array size
n = 4

Instead of rotating 9 times we compute:

    d = d % n

So

    d = 9 % 4
    d = 1

Meaning rotating 9 times is SAME as rotating 1 time.

Visualization
-------------

Rotation1 → [3,9,1,7]
Rotation2 → [9,1,7,3]
Rotation3 → [1,7,3,9]
Rotation4 → [7,3,9,1]

Array repeats every 4 rotations.

So 9 rotations = 1 rotation.

===============================================================================
Left Rotation vs Right Rotation
===============================================================================

Left Rotation
-------------
Elements move toward LEFT.

Example

[1,2,3,4,5] rotate left by 2

Result

[3,4,5,1,2]

Visualization

1 2 | 3 4 5

Right Rotation
--------------
Elements move toward RIGHT.

Example

[1,2,3,4,5] rotate right by 2

Result

[4,5,1,2,3]

Visualization

1 2 3 | 4 5

Relationship
------------

Right rotation by d = Left rotation by (n-d)

Example

Right rotate by 2

= Left rotate by 5-2 = 3

===============================================================================
How Interviewers Ask This Problem
===============================================================================

Common Variations
-----------------

1) Rotate array left by d

2) Rotate array right by k

3) Rotate array using O(1) space

4) Rotate array where d > n

5) Rotate array using reversal algorithm

6) Rotate array using cyclic replacement (juggling)

Typical Interview Flow
----------------------

Step1
Candidate explains brute force solution.

Step2
Interviewer asks to improve time complexity.

Step3
Candidate suggests extra array solution.

Step4
Interviewer asks for O(1) space solution.

Step5
Candidate explains reversal algorithm.

Best Answer in Interviews
-------------------------

Reversal Algorithm

Because

✔ O(n) time
✔ O(1) space
✔ Easy to implement

===============================================================================
LeetCode vs GFG Difference
===============================================================================

GFG Version
-----------
Function modifies array in-place.

Example

def rotateArr(arr, d):
    # modify arr

Return value usually not required.

LeetCode Version
----------------

Function signature

    def rotate(self, nums, k):

But LeetCode usually asks for RIGHT rotation.

Example

Input
nums = [1,2,3,4,5,6,7]
k = 3

Output
[5,6,7,1,2,3,4]

Solution
--------
Use reversal algorithm

reverse whole array
reverse first k
reverse remaining

===============================================================================
Quick Revision (Interview Cheat Sheet)
===============================================================================

If interviewer asks rotation problem remember:

Step1
Reduce rotations

    d = d % n

Step2
Best algorithm

Reversal Algorithm

Step3
3 reversals

reverse(0 , d-1)
reverse(d , n-1)
reverse(0 , n-1)

Time Complexity

O(n)

Space Complexity

O(1)

===============================================================================

"""
