from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0
    
    for i in range(len(heights)):
        popped = False
        if i == 0:
            stack.append((heights[i], i))
        else:
            while stack and heights[i] < stack[-1][0]:
                last_popped = stack.pop()
                height, start = last_popped
                max_area = max(max_area, height * (i - start))
                popped = True
            start_index = last_popped[1] if popped else i
            stack.append((heights[i], start_index))

    while stack:
        height, start = stack.pop()
        max_area = max(max_area, height * (len(heights) - start))

    return max_area