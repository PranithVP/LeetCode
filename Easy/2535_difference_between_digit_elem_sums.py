class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit, element = 0, 0

        for num in nums:
            element += num
            while num != 0:
                digit += num % 10
                num //= 10
        
        return abs(digit - element)