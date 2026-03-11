from collections import Counter
from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        mapping = set(candyType)
        return min(len(mapping), len(candyType) // 2)