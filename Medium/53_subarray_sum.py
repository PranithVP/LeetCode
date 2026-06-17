class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float('-inf')
        curr_max = curr
        
        for i in range(len(nums)):
            if curr < 0:
                curr = nums[i]
            else:
                curr += nums[i]
            
            curr_max = max(curr_max, curr)
        
        return curr_max