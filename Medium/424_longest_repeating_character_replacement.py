class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        arr = [0] * 26
        max_replace = 0

        for j in range(len(s)):
            arr[ord(s[j]) - ord('A')] += 1

            while (j - i + 1) - max(arr) > k:
                arr[ord(s[i]) - ord('A')] -= 1
                i += 1

            max_replace = max(j - i + 1, max_replace)
            
        return max_replace