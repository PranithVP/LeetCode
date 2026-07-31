class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        dp = [[None]*len(nums) for _ in range(len(nums))]
        
        def dfs(left, right):
            if dp[left][right] is not None:
                return dp[left][right]
            
            dp[left][right] = 0        
            for i in range(left+1, right):
                dp[left][right] = max(dp[left][right], dfs(left, i) + dfs(i, right) + nums[left]*nums[i]*nums[right])
    
                 
            return dp[left][right]
        
        return dfs(0, len(nums)-1)