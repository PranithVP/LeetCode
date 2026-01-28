from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0

        while j < len(prices):
            curr = prices[j] - prices[i]
            if prices[i] < prices[j]:
                max_profit = max(max_profit, curr)
            else:
                i = j
            j += 1
        return max_profit
            
            
