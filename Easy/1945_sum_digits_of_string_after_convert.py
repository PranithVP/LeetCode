class Solution:
    def getLucky(self, s: str, k: int) -> int:
        counts = {}
        curr = 1
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            counts[ch] = curr
            curr += 1
            
        digits = ''.join(str(counts[ch]) for ch in s)
         
        for _ in range(k):
            digits = str(sum(int(ch) for ch in digits))
        
        return int(digits)
         