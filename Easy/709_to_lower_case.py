class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([chr(ord(ch) + 32) if ch.isupper() else ch for ch in s])