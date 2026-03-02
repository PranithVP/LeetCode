from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        for elem in nums:
            d[elem] = d.get(elem, 0) + 1

        n_pairs = 0
        for key in d.keys():
            complement = k - key
            if complement in d:
                if key == complement:
                    curr = d[key] // 2
                    n_pairs += curr
                    d[key] -= (curr * 2)
                else:
                    curr = min(d[complement], d[key])
                    n_pairs += curr
                    d[key] -= curr
                    d[complement] -= curr
        
        return n_pairs

        