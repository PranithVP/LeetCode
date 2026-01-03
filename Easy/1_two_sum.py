from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in d:
            return [i, d[complement]]
        d[nums[i]] = i