from bisect import bisect_left
from math import ceil

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        for spell in spells:
            i = bisect_left(potions, ceil(success/spell))
            res.append(len(potions) - i)
        
        return res