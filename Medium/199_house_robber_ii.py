class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def process(lst):
            dp = [0 for _ in range(len(lst))]
            
            for i in range(len(lst)-1, -1, -1):
                if i == len(lst)-1:
                    dp[i] = lst[i]
                elif i == len(lst)-2:
                    dp[i] = max(lst[i], dp[i+1])
                else:
                    dp[i] = max(lst[i] + dp[i+2], dp[i+1])

            return dp[0]
        
        return max(process(nums[:-1]), process(nums[1:])) 