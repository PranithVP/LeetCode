class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = len(nums)-1
        i = 0

        while i < j:
            if nums[i] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        
        return nums