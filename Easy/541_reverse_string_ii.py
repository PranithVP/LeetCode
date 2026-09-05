class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        
        for i in range(0, len(s), k):
            print(i)
            if (i / k) % 2 == 0:
                res += s[i:i+k][::-1]
            else:
                res += s[i:i+k]
                
        return res