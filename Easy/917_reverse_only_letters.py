class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = ""
        i = 0
        
        order = []
        alpha = []
        other = []
        
        while i < len(s):
            if s[i].isalpha():
                alpha.append(s[i])
                order.append(0)
            else:
                other.append(s[i])
                order.append(1)
            
            i += 1
        
        other = other[::-1]
             
        for elem in order:
            if elem == 0:
                res += alpha.pop()
            else:
                res += other.pop()
        
        return res