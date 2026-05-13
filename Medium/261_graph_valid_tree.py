class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        
        def dfs(curr, parent):
            visited.add(curr)
            for neigh in graph[curr]:
                if neigh not in visited:
                    if dfs(neigh, curr): return True
                elif neigh != parent:
                    return True
            return False
        
        if dfs(0, None):
            return False
            
        return len(visited) == n