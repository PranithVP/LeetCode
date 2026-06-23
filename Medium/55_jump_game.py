class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        if len(nums) == 1:
            return True

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
        return goal == 0