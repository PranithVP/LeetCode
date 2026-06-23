class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        curr_sum_max = float('-inf')
        curr_max = float('-inf')

        curr_sum_min = float('inf')
        curr_min = float('inf')
        
        i = 0

        while i < len(nums):
            curr_sum_max = max(curr_sum_max + nums[i], nums[i])
            curr_sum_min = min(curr_sum_min + nums[i], nums[i])

            curr_max = max(curr_sum_max, curr_max)
            curr_min = min(curr_sum_min, curr_min)

            i += 1
        
        if curr_max < 0:
            return curr_max
        
        return max(curr_max, sum(nums) - curr_min)


        