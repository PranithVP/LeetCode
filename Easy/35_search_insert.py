from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums)-1

        while a < b:
            m = (a + b) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                a = m + 1
            else:
                b = m
        
        while a < len(nums) and nums[a] < target:
            a += 1
        return a
