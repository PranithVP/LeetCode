from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d1 = defaultdict(list)
        d2 = defaultdict(list)

        for elem in trust:
            d1[elem[0]].append(elem[1])
            d2[elem[1]].append(elem[0])

        for i in range(1, n+1):
            if len(d1[i]) == 0 and len(d2[i]) == n-1:
                return i
        
        return -1
