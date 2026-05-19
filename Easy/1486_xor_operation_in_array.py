class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        curr = 0
        for i in range(n):
            curr ^= start+2*i
        return curr
        
        