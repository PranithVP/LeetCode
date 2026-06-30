from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        res = []
        freq = Counter(changed)
        changed.sort()

        for x in changed:
            if freq[x] == 0:
                continue
            
            if freq[x*2] == 0:
                return []
            
            res.append(x)
            freq[x] -= 1
            freq[x*2] -= 1

        return res