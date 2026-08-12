class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start_i = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                continue
            else:
                if nums[start_i] == nums[i-1]:
                    res.append(str(nums[i-1]))
                else:
                    res.append(str(nums[start_i]) + '->' + str(nums[i-1]))
                start_i = i
            last = i
        
        if nums[start_i] == nums[len(nums)-1]:
            res.append(str(nums[len(nums)-1]))
        else:
            res.append(str(nums[start_i]) + '->' + str(nums[len(nums)-1]))
            
        return res

