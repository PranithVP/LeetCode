class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        bobTotal = sum(bobSizes)
        aliceTotal = sum(aliceSizes)
        
        aliceSizes = set(aliceSizes)
        target = (aliceTotal - bobTotal) // 2
        
        for elem in bobSizes:
            if elem+target in aliceSizes:
                return [elem + target, elem]
            
            