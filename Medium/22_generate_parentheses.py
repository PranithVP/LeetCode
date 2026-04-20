from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(opened, closed):
            if len(curr) == n*2:
                res.append(''.join(curr))
            else:
                if opened < n:
                    curr.append('(')
                    dfs(opened+1, closed)
                    curr.pop()
                if closed < opened:
                    curr.append(')')
                    dfs(opened, closed+1)
                    curr.pop()
        
        dfs(0, 0)
        return res
