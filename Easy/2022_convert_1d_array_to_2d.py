class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        res = []
        
        if m * n != len(original):
            return res
            
        curr = 0
        for i in range(m):
            res.append(original[curr:curr+n])
            curr += n
            
        return res