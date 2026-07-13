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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        d = defaultdict(int)

        for u, v in edges:
            uf.union(u, v)
        
        for i in range(n):
            d[uf.find(i)] += 1
        
        ans = 0
        seen = 0

        for v in d.values():
            ans += seen * v
            seen += v
        
        return ans
