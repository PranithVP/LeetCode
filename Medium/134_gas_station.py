class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        start = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(n):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start = i + 1
            
        return start
