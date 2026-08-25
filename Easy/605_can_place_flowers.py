class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        count = 0

        for i in range(len(flowerbed)):
            prev = 0
            nxt = 0
            curr = flowerbed[i]

            if i >= 1: prev = flowerbed[i-1]
            if i < len(flowerbed)-1: nxt = flowerbed[i+1]

            if not prev and not nxt and not curr: 
                count += 1
                flowerbed[i] = 1
            

            if count == n:
                return True

        return False