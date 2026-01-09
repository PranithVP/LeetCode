from typing import List

def longestConsecutive(nums: List[int]) -> int:
    elems = set(nums)
    
    max_seq = 0
    for elem in elems:
        curr = 0
        if elem - 1 not in elems:
            while elem in elems:
                curr += 1
                elem += 1
        if curr > max_seq:
            max_seq = curr
    
    return max_seq