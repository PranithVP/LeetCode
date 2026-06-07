class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(remaining, i):
            if remaining == 0:
                return 1
            if remaining < 0 or i == len(coins):
                return 0
            if (remaining, i) in dp:
                return dp[(remaining, i)]
            else:
                total = dfs(remaining - coins[i], i) + dfs(remaining, i+1)

                dp[(remaining, i)] = total
                return total
                    
        
        return dfs(amount, 0)