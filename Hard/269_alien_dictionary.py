from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        indegree = {}
        for word in words:
            for ch in word:
                if ch not in graph:
                    graph[ch] = set()
                    indegree[ch] = 0

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            equalWords = True

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:  
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    equalWords = False
                    break
            
            if equalWords and len(word1) > len(word2):
                return ""
        
        q = deque()
        path = ""
        
        for elem in indegree:
            if indegree[elem] == 0:
                q.append(elem)
        
        while q:
            curr = q.pop()
            path += curr
            
            for neigh in graph[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        if len(path) != len(indegree):
            return ""
        
        return path