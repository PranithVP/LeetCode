class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        res = []
        
        for i in range(len(s)-1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i
        
        i = 0
        
        while i < len(s):
            target = last[s[i]]
            start = i
            
            while i < target:
                i += 1
                target = max(target, last[s[i]])
            
            res.append(i - start + 1)
            i += 1
            
        
        return res