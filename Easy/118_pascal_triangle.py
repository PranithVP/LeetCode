class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            if i == 0:
                curr = [1]
            elif i == 1:
                curr = [1, 1]
            else:
                curr = [1]
                for i in range(i-1):
                    curr.append(res[-1][i] + res[-1][i+1])
                curr.append(1)
            
            res.append(curr)
        
        return res
