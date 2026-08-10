class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        
        for elem in nums:
            if elem == first or elem == second or elem == third:
                continue
                
            if elem > first:
                first, second, third = elem, first, second
            elif elem > second:
                second, third = elem, second
            elif elem > third:
                third = elem
        
        if third != float('-inf'):
            return third
        return first