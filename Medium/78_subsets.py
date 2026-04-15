class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        elif len(nums) == 1:
            return [nums, []]
        else:
            res = self.subsets(nums[1:])
            return [[nums[0]] + elem for elem in res] + res  
