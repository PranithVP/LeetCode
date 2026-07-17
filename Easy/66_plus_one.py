class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOver = 1

        for i in range(len(digits)-1, -1, -1):
            total = digits[i] + carryOver
            digits[i] = total % 10
            carryOver = total // 10

            if carryOver == 0:
                break

        if carryOver > 0:
            digits.insert(0, carryOver)

        return digits