from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse=True)

        for a, b in tickets:
            graph[a].append(b)

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            res.append(node)

        res = []
        dfs("JFK")

        return res[::-1]