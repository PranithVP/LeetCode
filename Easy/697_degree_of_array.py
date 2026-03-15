from collections import Counter
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.items(), key=lambda x: x[1])[1]
        max_freq_nums = [k for k in count if count[k] == max_freq]
        diff = float('inf')
        
        for max_freq_num in max_freq_nums:
            first, last = -1, -1

            for i in range(len(nums)):
                if nums[i] == max_freq_num:
                    first = i
                    break
            
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == max_freq_num:
                    last = i
                    break
            
            curr_diff = last - first + 1
            if curr_diff < diff:
                diff = curr_diff
        
        return diff
        
        