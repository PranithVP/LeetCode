from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1

    while i < j:
        summed = numbers[i] + numbers[j]
        if summed == target:
            return [i + 1, j + 1]
        elif summed < target:
            i += 1
        else:
            j -= 1
        
    