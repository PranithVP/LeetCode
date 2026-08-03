class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
            n = -n
        
        def helper(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n % 2 == 0:
                return helper(x*x, n // 2)
            else:
                return x * helper(x, n-1)
        
        return helper(x, n)