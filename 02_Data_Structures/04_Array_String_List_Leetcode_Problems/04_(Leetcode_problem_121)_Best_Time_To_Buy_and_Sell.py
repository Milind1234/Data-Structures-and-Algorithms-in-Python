"""
notes.py
---------
Topic: Best Time to Buy and Sell Stock (LeetCode 121)

Problem:
--------
You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Function Signature:
-------------------
def maxProfit(prices: List[int]) -> int
"""

# ---------------------------------------------------
# Approach 1: Brute Force
# ---------------------------------------------------
# - Try all possible pairs of buy day (i) and sell day (j), where i < j.
# - For each pair, calculate profit = prices[j] - prices[i].
# - Keep track of the maximum profit found.
# - Return that maximum.
class SolutionBruteForce(object):
    def maxProfit(self, prices):
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

"""
Time Complexity:
----------------
- O(n^2), since we check all pairs.

Space Complexity:
-----------------
- O(1), only variables used.

Interview Notes:
----------------
- Brute force is simple but too slow for large n (up to 1e5).
- Useful to explain first, then optimize.
"""


# ---------------------------------------------------
# Approach 2: Optimal (One Pass)
# ---------------------------------------------------
# - Track the minimum price seen so far as a candidate buy day.
# - At each day, compute profit = current_price - min_price_so_far.
# - Update max_profit if this profit is larger.
# - Update min_price_so_far if today’s price is lower than the current min_price.
# - Return max_profit at the end.
class SolutionOptimal(object):
    def maxProfit(self, prices):
        min_price_so_far = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price_so_far:
                min_price_so_far = price
            else:
                profit = price - min_price_so_far
                if profit > max_profit:
                    max_profit = profit
        return max_profit

"""
Detailed Example Walkthrough:
-----------------------------
Input: prices = [7,1,5,3,6,4]

Initial setup
-------------
min_price_so_far = ∞ (very big number, so any real price will be smaller)
max_profit = 0

Iteration 1 → price = 7
Is 7 < ∞? ✅ Yes → update min_price_so_far = 7
Else part skipped
State: min_price_so_far = 7, max_profit = 0

Iteration 2 → price = 1
Is 1 < 7? ✅ Yes → update min_price_so_far = 1
Else part skipped
State: min_price_so_far = 1, max_profit = 0

Iteration 3 → price = 5
Is 5 < 1? ❌ No → go to else part
Profit = 5 - 1 = 4
Is 4 > 0? ✅ Yes → update max_profit = 4
State: min_price_so_far = 1, max_profit = 4

Iteration 4 → price = 3
Is 3 < 1? ❌ No → go to else part
Profit = 3 - 1 = 2
Is 2 > 4? ❌ No → do nothing
State: min_price_so_far = 1, max_profit = 4

Iteration 5 → price = 6
Is 6 < 1? ❌ No → go to else part
Profit = 6 - 1 = 5
Is 5 > 4? ✅ Yes → update max_profit = 5
State: min_price_so_far = 1, max_profit = 5

Iteration 6 → price = 4
Is 4 < 1? ❌ No → go to else part
Profit = 4 - 1 = 3
Is 3 > 5? ❌ No → do nothing
State: min_price_so_far = 1, max_profit = 5

End of loop
-----------
The best profit we could make is 5.
That means buy at 1 (day 2) and sell at 6 (day 5).

✅ Final Output = 5

Complexities:
-------------
- Brute Force:   Time O(n^2), Space O(1)
- Optimal:       Time O(n),   Space O(1)

Interview Notes:
----------------
- Start with brute force to show understanding, then present the optimal one-pass method.
- Key insight for optimal: maintain the minimum price so far and compute profit on the fly.
"""
