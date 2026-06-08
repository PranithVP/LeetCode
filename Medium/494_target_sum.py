class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def dfs(remaining, i):
            if i == len(nums):
                if remaining == 0:
                    return 1
                else: return 0
            if (remaining, i) in dp:
                return dp[(remaining, i)]
            
            total = dfs(remaining + nums[i], i+1) + dfs(remaining - nums[i], i+1)
            dp[(remaining, i)] = total
            return total

        return dfs(target, 0)
