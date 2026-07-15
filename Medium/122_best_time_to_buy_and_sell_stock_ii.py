class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, can_buy):
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]
            
            if i == len(prices):
                return 0
            
            max_profit = dfs(i+1, can_buy)

            if can_buy:
                buy = dfs(i+1, False) 
                max_profit = max(max_profit, buy - prices[i])
            else:
                sell = dfs(i+1, True)
                max_profit = max(max_profit, sell + prices[i])
            
            dp[(i, can_buy)] = max_profit
            return max_profit
                
        return dfs(0, True)