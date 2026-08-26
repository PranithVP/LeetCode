from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        freq = Counter(stones)
        
        for ch in jewels: 
            total += freq[ch]

        return total