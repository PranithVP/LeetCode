class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        arr1, arr2 = [0] * 200, [0] * 200
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if arr1[ord(s[i])] != arr2[ord(t[i])]:
                return False

            arr1[ord(s[i])] = i + 1
            arr2[ord(t[i])] = i + 1
        
        return True