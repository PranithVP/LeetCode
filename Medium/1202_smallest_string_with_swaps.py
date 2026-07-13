from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return
        
        self.parent[py] = px
            


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        d = defaultdict(list)
        n = len(s)
        uf = UnionFind(n)
        res = ""

        for i1, i2 in pairs:
            uf.union(i1, i2)
        
        for i in range(n):
            d[uf.find(i)].append(s[i])
        
        for k in d:
            d[k].sort(reverse=True)
        
        for i in range(n):
            res += d[uf.find(i)].pop()

        return res