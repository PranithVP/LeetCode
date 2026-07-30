class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[None] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        for i in range(len(s)):
            dp[i][len(t)] = 1
        
        for i in range(len(t)):
            dp[len(s)][i] = 0
        
        dp[len(s)][len(t)] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                if dp[i][j] is not None:
                    continue
                
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][0]
                    
        