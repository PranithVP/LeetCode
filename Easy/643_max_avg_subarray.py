class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        start = 0
        max_sum = curr
        for i in range(k, len(nums)):
            curr -= nums[start]
            start += 1
            curr += nums[i]
            if curr > max_sum:
                max_sum = curr

        return max_sum / k 