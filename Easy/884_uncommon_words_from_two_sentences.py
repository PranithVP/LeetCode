from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        counts = Counter(s1.split() + s2.split())
        res = []
        
        for elem in counts:
            if counts[elem] == 1:
                res.append(elem)
                
        return res