import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return [b for _, b in sorted([(b, a) for a, b in freq.items()], key=lambda x:(-x[0], x[1]))][:k]
