class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[len(s)] = True
        print(dp)

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if s[i:i+len(word)] == word and dp[i+len(word)]:
                    dp[i] = True
        
        return dp[0]

        