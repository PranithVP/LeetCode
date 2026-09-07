class Solution:
    def reverseByType(self, s: str) -> str:
        res = ""
        i = 0
        
        order = []
        alpha = []
        special = []
        
        while i < len(s):
            if s[i].isalpha():
                alpha.append(s[i])
                order.append(0)
            else:
                special.append(s[i])
                order.append(1)
            
            i += 1
             
        for elem in order:
            if elem == 0:
                res += alpha.pop()
            else:
                res += special.pop()
        
        return res