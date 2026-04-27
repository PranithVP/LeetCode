import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for elem in nums:
            heapq.heappush(h, elem)
            if len(h) > k:
                heapq.heappop(h)
        
        
        return heapq.heappop(h)