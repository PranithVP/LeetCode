class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        chars = set()
        max_len = 0

        while j < len(s):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            chars.add(s[j])
            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len