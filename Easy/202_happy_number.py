class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            total = 0
            for ch in str(n):
                ch = int(ch)
                total += ch ** 2
            n = int(total)
            if n == 1:
                return True
        return False