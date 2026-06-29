class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        min_length = float('inf')
        j = 0

        for i in range(len(nums)):
            curr += nums[i]

            while curr >= target and j <= i:
               min_length = min(i - j + 1, min_length)
               curr -= nums[j]
               j += 1
        
        if min_length == float('inf'):
            return 0

        return min_length


