from typing import List

def longestConsecutive(nums: List[int]) -> int:
    elems = set(nums)
    if len(nums) == 0: return 0
    minimum = min(nums)
    maximum = max(nums)

    max_seq = 0
    curr = 0
    for i in range(minimum, maximum+1):
        if i in elems:
            curr += 1
            if curr > max_seq:
                max_seq = curr
        else:
            curr = 0
    
    return max_seq
