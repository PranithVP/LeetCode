from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        one = []
        two = []

        for elem in nums:
            total += elem
            if elem % 3 == 1:
                one.append(elem)
            elif elem % 3 == 2:
                two.append(elem)
        
        one = sorted(one, reverse=True)
        two = sorted(two, reverse=True)

        if total % 3 != 0:
            if total % 3 == 1:
                if len(two) < 2:
                    total -= one.pop()
                elif len(one) < 1 or (two[-1] + two[-2]) < one[-1]:
                    total -= two.pop()
                    total -= two.pop()
                else:
                    total -= one.pop()
            else:
                if len(one) < 2:
                    total -= two.pop()
                elif len(two) < 1 or (one[-1] + one[-2]) < two[-1]:
                    total -= one.pop()
                    total -= one.pop()
                else:
                    total -= two.pop()
        
        return total
