from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        seen = set()

        for i in nums:
            if i in seen:
                res.append(i)
            seen.add(i)

        for i in range(1, len(nums)+1):
            if i not in seen:
                res.append(i)
                break
    
        return res
        