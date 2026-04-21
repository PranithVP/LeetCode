import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr_partition = []

        def dfs(i):
            if i >= len(s):
                res.append(curr_partition[:])
                return 
            for j in range(i, len(s)):
                curr_string = s[i:j+1]
                if self.isPalindrome(curr_string):   
                    curr_partition.append(curr_string)
                    dfs(j+1)
                    curr_partition.pop()
                else:
                    continue

        dfs(0)
        return res

            
    def isPalindrome(self, word):
        if len(word) == 0:
            return True

        i, j = 0, len(word)-1

        while i < j:
            if word[i] == word[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
        