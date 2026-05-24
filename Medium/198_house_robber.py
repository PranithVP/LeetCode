class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                dp[i] = nums[i]
            elif i == len(nums)-2:
                dp[i] = max(nums[i], dp[i+1])
            else:
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])

        return dp[0]