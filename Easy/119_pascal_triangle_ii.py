class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        
        for _ in range(rowIndex):
            res = [1] + [res[i] + res[i+1] for i in range(len(res)-1)] + [1]
        
        return res

            