class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        buckets = [0] * k
        target = sum(nums) // k
        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return buckets == [target] * k

            for j in range(len(buckets)):
                if buckets[j] + nums[i] <= target:
                    buckets[j] += nums[i]

                    if dfs(i+1) is True:
                        return True

                    buckets[j] -= nums[i]

                    if buckets[j] == 0:
                        break
        
            return False

        return dfs(0)