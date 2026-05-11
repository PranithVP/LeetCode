from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course)

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            count += 1
            curr = q.popleft()
            
            for neigh in graph[curr]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return count == numCourses