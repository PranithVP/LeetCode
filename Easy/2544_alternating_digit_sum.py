class Solution:
    def alternateDigitSum(self, n: int) -> int:
        temp = n
        digits = 0

        while temp > 0:
            leftover = temp % 10
            temp //= 10
            digits += 1

        sign = -1 if digits % 2 == 0 else 1
        total = 0

        while n > 0:
            leftover = n % 10
            n //= 10
            total += sign * leftover
            sign *= -1
        
        return total