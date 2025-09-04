def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(1,len(prices)):
            Profit = prices[j] - prices[i]
            if Profit > max_profit:
                max_profit = Profit
    return max_profit
prices = [7,1,5,3,6,4]
print(maxProfit(prices))