class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        reach = 0
        explored = 0

        while reach < len(nums)-1:
            temp = reach
            for i in range(explored, temp+1):
                reach = max(reach, i+nums[i])
            
            explored = temp + 1
            jumps += 1
        
        return jumps
