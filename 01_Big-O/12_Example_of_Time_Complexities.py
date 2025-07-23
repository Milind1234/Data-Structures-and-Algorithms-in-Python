"""
==========================================================
Interview Question - 7:
Which of the following are equivalent to O(N)? Why?
==========================================================

1) O(N + P), where P < N/2 → O(N)   ✅
2) O(2N) → O(N)                     ✅
3) O(N + logN) → O(N)               ✅
4) O(N + NlogN) → O(NlogN)          ❌ (Dominant term is NlogN)
5) O(N + M) → Depends on M          ❌ (Only O(N) if M is constant or O(N), 
                                        otherwise consider both variables)

----------------------------------------------------------
Explanation:
1) **O(N + P)** 
   - If P is always less than N/2, 
     N dominates → O(N).

2) **O(2N)** 
   - Constant multiplier 2 is ignored in Big-O → O(N).

3) **O(N + logN)** 
   - N grows faster than logN → O(N).

4) **O(N + NlogN)**
   - NlogN dominates → Overall O(NlogN).

5) **O(N + M)**
   - If M is independent of N, we must keep both variables → O(N + M).
   - Only if M = O(N) (e.g., M ≤ kN), then O(N).

----------------------------------------------------------
ASCII Graph of Complexity
----------------------------------------------------------
Operations (Y-axis)
^
|         /0(2^n)          / 0(n^2)                  /................0(n log n)           
|        /         /                         /            
|       /        /                     /                       
|      /       /                    /                  / ..........0(n)
|     /      /                /                  / 
|    /     /              /              /
|   /    /           /          /
|  /   /        /      /  
| /  /   /      /   
|/ /_____/_______________________________________________............0(log n)
|/|____________________________________________________............0(1) 
+-----------------------------------------------------> Elements (X-axis)

----------------------------------------------------------
Key Notes:
- Big-O ignores constants & lower order terms.
- We keep only the fastest-growing term as n → ∞.
==========================================================
"""
