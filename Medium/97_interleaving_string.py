class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        n1, n2 = len(s1), len(s2)
        
        if len(s3) != n1 + n2:
            return False

        def dfs(i1, i2):
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            if i1 == n1 and i2 == n2:
                return True
            if i1 == n1:
                res = s3[i1+i2:] == s2[i2:]
                dp[(i1, i2)] = res
                return res
            if i2 == n2:
                res = s3[i1+i2:] == s1[i1:]
                dp[(i1, i2)] = res
                return res
            
            res1, res2 = False, False
            if s1[i1] == s3[i1+i2]:
                res1 = dfs(i1+1, i2)
            if s2[i2] == s3[i1+i2]:
                res2 = dfs(i1, i2+1)
            
            res = res1 or res2
            dp[(i1, i2)] = res
            return res

        return dfs(0, 0)
            