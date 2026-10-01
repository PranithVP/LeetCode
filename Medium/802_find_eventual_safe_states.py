from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        outdegree = [None] * n
        reverse = defaultdict(list)

        for i in range(n):
            outdegree[i] = len(graph[i])

            for elem in graph[i]:
                reverse[elem].append(i)
        
        starting_nodes = []

        for i in range(n):
            if outdegree[i] == 0:
                starting_nodes.append(i)

        q = deque(starting_nodes)

        while q:
            curr = q.popleft()
            for neigh in reverse[curr]:
                outdegree[neigh] -= 1
                if outdegree[neigh] == 0:
                    q.append(neigh)
        
        return [i for i in range(n) if outdegree[i] == 0]