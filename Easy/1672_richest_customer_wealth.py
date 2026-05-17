class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        curr_max = float('-inf')
        for i in range(len(accounts)):
            curr = 0
            for j in range(len(accounts[i])):
                curr += accounts[i][j]
            if curr > curr_max:
                curr_max = curr
        
        return curr_max