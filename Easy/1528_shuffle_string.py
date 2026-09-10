class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        arr = [None] * len(s)
        
        for i in range(len(s)):
            arr[indices[i]] = s[i]
        
        return ''.join(arr)