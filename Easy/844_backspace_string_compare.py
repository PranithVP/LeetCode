class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = ""
        b = ""

        for ch in s:
            if ch == '#':
                a = a[:-1]
            else:
                a += ch

        for ch in t:
            if ch == '#':
                b = b[:-1]
            else:
                b += ch
        
        return a == b