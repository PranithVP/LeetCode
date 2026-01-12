from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                summed = nums[i] + nums[j] + nums[k]

                if summed == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j, k = j + 1, k - 1

                elif summed < 0:
                    j += 1
                else:
                    k -= 1
        return res