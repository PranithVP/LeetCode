from typing import List
import heapq

# Hashmap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for elem in nums:
            d[elem] = d.get(elem, 0) + 1
        
        sorted_items = sorted([(b, a) for a, b in d.items()], reverse=True)
        return [b for _, b in sorted_items[:k]]

# Heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for elem in nums:
            d[elem] = d.get(elem, 0) + 1
        
        l = [(b, a) for a, b in d.items()]
        return [b for _, b in heapq.nlargest(k, l)]


# Bucket sort
def topKFrequent(nums: List[int], k: int) -> List[int]:
    d = {}
    for elem in nums:
        d[elem] = d.get(elem, 0) + 1

    
    buckets = [[] for _ in range(len(nums))]
    
    for key in d:
        buckets[d[key]-1].append(key)

    res = []
    
    for i in range(len(buckets)-1, -1, -1):
        res.extend(buckets[i])
        if len(res) >= k:
            return res[:k]