class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for s in words:
            i, j = 0, len(s)-1
            pal = True

            while i < j:
                if s[i] != s[j]:
                    pal = False
                    break
                i += 1
                j -= 1

            if pal:
                return s
            else: continue
        return ""