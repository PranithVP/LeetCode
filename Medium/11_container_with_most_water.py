from typing import List

def maxArea(height: List[int]) -> int:
    curr_max = 0

    i = 0
    j = len(height) - 1

    while i < j:
        curr = min(height[i], height[j])*(j-i)
        max(curr_max = curr)
        if height[i] < height[j]: i += 1
        elif height[j] < height[i]: j-= 1
        else: i += 1
    
    return curr_max