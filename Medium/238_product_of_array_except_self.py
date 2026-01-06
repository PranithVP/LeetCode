from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n

    for i in range(1, n):
        res[i] = res[i-1] * nums[i-1]
    
    curr_right = 1
    for j in range(n-2, -1, -1):
        curr_right *= nums[j+1]
        res[j] *= curr_right
    
    return res