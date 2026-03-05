class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(' ')
        d = {}
        d2 = {}

        if len(pattern) != len(arr):
            return False

        for i in range(len(pattern)):
            print(d, d2)
            if pattern[i] in d:
                if d[pattern[i]] != arr[i]:
                    return False
            if arr[i] in d2:
                if d2[arr[i]] != pattern[i]:
                    return False
            else:
                d[pattern[i]] = arr[i]
                d2[arr[i]] = pattern[i]

        return True 
            