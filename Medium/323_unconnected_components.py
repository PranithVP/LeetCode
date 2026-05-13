class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        visited = set()
        count = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if not neigh in visited:
                    dfs(neigh)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count