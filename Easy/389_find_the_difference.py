from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sd = Counter(s)
        td = Counter(t)

        for k in td:
            if k not in sd:
                return k
            elif td[k] != sd[k]:
                return k