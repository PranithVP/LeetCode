class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        largest = 0
        curr, prev = 0, float('-inf')

        for i in range(len(nums)):
            if nums[i] > prev:
                curr += 1
                prev = nums[i]
                if largest < curr:
                    largest = curr
            else:
                curr, prev = 1, nums[i]
        
        return largest