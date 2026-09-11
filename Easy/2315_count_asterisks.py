class Solution:
    def countAsterisks(self, s: str) -> int:
        i = 0
        n = len(s)
        
        res = 0
        
        while i < n:
            if s[i] == '|':
                j = i + 1
                while j < n and s[j] != '|':
                    j += 1
                i = j + 1
            else:
                if s[i] == '*':
                    res += 1
                i += 1
        
        return res