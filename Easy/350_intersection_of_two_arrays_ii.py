from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1, freq2 = Counter(nums1), Counter(nums2)
        
        res = []
        
        for k in freq1:
            if k in freq2:
                res.extend([k] * min(freq1[k], freq2[k]))
        
        return res