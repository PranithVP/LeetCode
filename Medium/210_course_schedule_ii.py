from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}


        for course, prereq in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        order = []
        
        while q:
            
            curr = q.popleft()
            order.append(curr)

            for neigh in graph[curr]:
                indegree[neigh] -= 1
                
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        
        if len(order) == numCourses:
            return order
        return []