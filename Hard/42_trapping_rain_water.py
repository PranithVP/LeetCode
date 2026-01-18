from typing import List

def trap(height: List[int]) -> int:
    n = len(height)
    right_max = [0] * n
    curr = 0
    water = 0

    for i in range(n-2, -1, -1):
        right_max[i] = max(height[i+1], right_max[i+1])
    
    for i in range(n):
        if i > 0:
            curr = max(curr, height[i-1])
        water += max(0, min(curr, right_max[i]) - height[i])
    
    return water


def trap(height: List[int]) -> int:
    i, j = 0, len(height) - 1
    i_max, j_max = 0, 0
    water = 0

    while i < j:
        i_max, j_max = max(height[i], i_max), max(height[j], j_max)
        if i_max < j_max:
            water += i_max - height[i]
            i += 1
        else:
            water += j_max - height[j]
            j -= 1
        
    return water