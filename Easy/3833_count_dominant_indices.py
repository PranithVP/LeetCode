class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0
        
        for i in range(len(nums)-1):
            remaining = len(nums)-(i+1)
            total -= nums[i]
            
            if nums[i] > total/remaining:
                count += 1
            
        return count