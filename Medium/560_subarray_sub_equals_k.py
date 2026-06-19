from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1

        for i in range(len(nums)):
            prefix += nums[i]
            count += freq[prefix - k]

            freq[prefix] += 1

        return count