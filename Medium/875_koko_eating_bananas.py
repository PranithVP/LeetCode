from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a = 1
        b = max(piles)
        min_speed = float('inf')

        while a <= b:
            mid = (a + b) // 2
            curr = self.time_taken(piles, mid)
            if curr > h:
                a = mid + 1
            else:
                min_speed = min(mid, min_speed)
                b = mid - 1

        return min_speed
        
    def time_taken(self, lst, k):
        count = 0
        for elem in lst:
            count += ceil(elem / k)
        return count
