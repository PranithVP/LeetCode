import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        h = [-c for c in counts.values()]
        heapq.heapify(h)
        time = 0

        while h:
            temp = []

            for _ in range(1+n):
                if h:
                    count = (-heapq.heappop(h)) - 1
                    if count > 0:
                        temp.append(count)
            
                time += 1

                if not h and not temp:
                    break
                
            for elem in temp:
                if elem > 0:
                    heapq.heappush(h, -elem)
        
        return time