from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = 0
        odd_found = False
        d = Counter(s)

        for k in d.keys():
            if d[k] >= 2:
                l += (d[k] - (d[k] % 2))
                d[k] %= 2
            if not odd_found and d[k] == 1:
                odd_found = True
        
        if odd_found: l += 1
        
        return l

