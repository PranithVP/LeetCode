class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = dict()
        words = set(words)

        def dfs(s):
            if s in dp:
                return dp[s]

            largest = 1
            for i in range(len(s)):
                removed = s[:i] + s[i+1:]
                if removed in words:
                    largest = max(largest, 1 + dfs(removed))
                
            dp[s] = largest
            return largest
        
        for elem in sorted(list(words), key= lambda x:len(x)):
            dfs(elem)
        
        return max(dp.values())


