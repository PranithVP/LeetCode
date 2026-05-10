class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, sum = 1, 0
        for ch in str(n):
            prod *= int(ch)
            sum += int(ch)
        return prod - sum