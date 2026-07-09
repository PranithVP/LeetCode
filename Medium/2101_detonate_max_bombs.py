from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        max_count = 0
        graph = defaultdict(list)

        for i in range(len(bombs)):
            bombs[i] = tuple(bombs[i])

        for i in range(len(bombs)):
            x1, y1, r = bombs[i]
            for j in range(len(bombs)):
                if j != i:
                    x2, y2, _ = bombs[j]
                    if ((x2-x1)**2) + ((y2-y1)**2) <= (r**2):
                        graph[i].append(j) 
        
        for i in range(len(bombs)):
            s = [i]
            visited = {i}
            count = 1
            while s:
                curr = s.pop()
                for neigh in graph[curr]:
                    if neigh not in visited:
                        s.append(neigh)
                        visited.add(neigh)
                        count += 1
            
            max_count = max(max_count, count)
        
        return max_count


