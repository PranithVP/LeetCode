class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        count = 0
        for ch in columnTitle[::-1]:
            curr = ord(ch) - ord('A') + 1
            res += curr * 26**count
            count += 1
        return int(res)
