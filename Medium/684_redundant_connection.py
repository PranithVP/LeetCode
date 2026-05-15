from collections import defaultdict
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()

        def dfs(u, v):
            visited.add(u)
            if u in graph:
                for neigh in graph[u]:
                    if neigh == v:
                        return True
                    elif neigh not in visited:
                        if dfs(neigh, v):
                            return True
            return False

        for u,v in edges:
            if u in graph and v in graph:
                visited = set()
                if dfs(u,v):
                    return [u,v]

            graph[u].append(v)
            graph[v].append(u)
        
