class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        encountered = False
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                if not encountered and ((i >= len(nums)-1 or nums[i-1] < nums[i+1]) or (i < 2 or nums[i-2] < nums[i])):
                    encountered = True
                else:
                    return False
        
        return True