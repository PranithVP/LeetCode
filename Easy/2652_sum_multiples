class Solution:
    def sumOfMultiples(self, n: int) -> int:
        r = 0
        for i in range(1, n+1):
            one, five, seven = i % 3 == 0, i % 5 == 0, i % 7 == 0
            if one or five or seven:
                r += i
        return r