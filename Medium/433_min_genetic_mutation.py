from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        visited = set()

        if endGene not in bank:
            return -1
        
        q = deque()
        q.append(startGene)
        visited.add(startGene)

        count = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == endGene:
                    return count

                for ch in 'ACGT':
                    for i in range(8):
                        neighbour = curr[:i] + ch + curr[i+1:]
                        if neighbour in bank and neighbour not in visited:
                            q.append(neighbour)
                            visited.add(neighbour)

            count += 1

        return -1