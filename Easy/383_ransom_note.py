from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for k in r:
            if k in m:
                if r[k] > m[k]:
                    return False
            else:
                return False
        
        return True
