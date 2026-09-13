class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for i in range(low, high+1):
            curr = str(i)
            n = len(curr)
            
            if n % 2 != 0:
                continue
            
            n //= 2
            
            if sum(int(ch) for ch in curr[:n]) == sum(int(ch) for ch in curr[n:]):
                count += 1
        
        return count