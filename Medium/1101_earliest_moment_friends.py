class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.components = n

            def find(self, i):
                if self.parent[i] != i:
                    self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, x, y):
                px, py = self.find(x), self.find(y)

                if px != py:
                    self.parent[py] = px
                    self.components -= 1

        logs.sort()

        uf = UnionFind(n)

        for timestamp, a, b in logs:
            uf.union(a, b)

            if uf.components == 1:
                return timestamp

        return -1