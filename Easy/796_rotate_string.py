class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s) + 1):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False