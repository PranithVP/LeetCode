class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "." + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        num = ""
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num += s[i]
                i += 1
            elif s[i] == '.':
                i += 1
                num = int(num)
                res.append(s[i:i+num])
                i += num
                num = ""
        
        return res
