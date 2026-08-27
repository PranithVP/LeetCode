class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = 0
        found = False

        if len(nums) <= 2:
            return True
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            
            if not found:
                if nums[i-1] < nums[i]:
                    direction = 1
                else:
                    direction = -1

                found = True
                continue
            
            if direction == 1 and nums[i-1] > nums[i]:
                return False
            if direction == -1 and nums[i-1] < nums[i]:
                return False
    
        return True