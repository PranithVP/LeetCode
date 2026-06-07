class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying: # buying
                dp[(i, True)] = max(dfs(i+1, False) - prices[i], dfs(i+1, True))
            else: # selling
                dp[(i, False)] = max(dfs(i+2, True) + prices[i], dfs(i+1, False))
            return dp[(i, buying)]
        
        return dfs(0, True)