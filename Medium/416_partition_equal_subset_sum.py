class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total / 2
        possible_sums = set([0])

        for num in nums:
            temp = possible_sums.copy()
            for elem in possible_sums: temp.add(elem + num)
            possible_sums = temp
        
        return target in possible_sums
