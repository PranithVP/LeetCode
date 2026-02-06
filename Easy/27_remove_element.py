from typing import List

def removeElement(nums: List[int], val: int) -> int:
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] == val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
    
    while nums and nums[-1] == val: nums.pop()

    return j + 1

l = [0,1,2,2,3,0,4,2]
print(removeElement(l, 2))