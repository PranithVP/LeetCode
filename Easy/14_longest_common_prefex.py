from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs[1:]:
                if i > len(s) - 1:
                    return pre
                elif s[i] != ch:
                    return pre
            pre += ch
        return pre