from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        q = deque([0])
        
        while q:
            curr = q.pop()
            
            if curr in visited:
                continue
            
            visited.add(curr)
            
            for neigh in rooms[curr]:
                if neigh not in visited:
                    q.append(neigh)
                    
        if len(visited) == len(rooms):
            return True
        return False