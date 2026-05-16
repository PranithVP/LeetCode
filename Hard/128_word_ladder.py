from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        wordList.add(beginWord)

        if endWord not in wordList:
            return 0
        
        queue = deque()
        visited = set()
        visited.add(beginWord)
        queue.append((1, beginWord))

        while queue:
            dist, curr = queue.popleft()

            if curr == endWord:
                return dist

            for i in range(len(curr)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    neigh = curr[:i] + ch + curr[i+1:]
                    if neigh in wordList and neigh != curr and neigh != beginWord:
                        if not neigh in visited: 
                            visited.add(neigh)
                            queue.append((dist+1, neigh))  
        
        return 0
            
                