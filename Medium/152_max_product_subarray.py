class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = nums[-1], nums[-1]
        largestMax = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            curr = nums[i]
            currMin, currMax = (
                min(curr * currMax, curr * currMin, curr), 
                max(curr * currMax, curr * currMin, curr)
            )

            largestMax = max(largestMax, currMax)
            
        return largestMax