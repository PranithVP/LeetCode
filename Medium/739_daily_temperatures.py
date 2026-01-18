from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    s = []
    for i in range(len(temperatures)):
        
        while len(s) > 0 and s[-1][0] < temperatures[i]:
            a, b = s.pop()
            result[b] = i - b

        s.append((temperatures[i], i))
    return result


