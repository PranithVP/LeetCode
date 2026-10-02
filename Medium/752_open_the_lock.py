from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        neighbours = {}

        for i in range(1, 9):
            neighbours[str(i)] = [str(i+1), str(i-1)]
        
        neighbours['0'] = ['1', '9']
        neighbours['9'] = ['0', '8']

        deadends = set(deadends)

        if '0000' in deadends:
            return 0 if target == '0000' else -1

        visited = set(['0000'])
        q = deque([('0000', 0)])

        while q:
            curr, count = q.popleft()

            if curr == target:
                return count

            for i in range(len(curr)):
                for neigh in neighbours[curr[i]]:
                    neigh_str = curr[:i] + neigh + curr[i+1:]

                    if neigh_str not in visited and neigh_str not in deadends:
                        q.append((neigh_str, count + 1))
                        visited.add(neigh_str)

        return -1

                