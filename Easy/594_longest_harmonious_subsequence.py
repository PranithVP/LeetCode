from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        curr_max = 0

        for k in counts.keys():
            if k+1 not in counts or counts.get(k, 0) == 0 or counts.get(k+1, 0) == 0:
                continue

            curr = counts.get(k, 0) + counts.get(k + 1, 0)
            if curr > curr_max: curr_max = curr
        
        return curr_max