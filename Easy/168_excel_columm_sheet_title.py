class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
       res = ""
       
       while columnNumber > 0:
           columnNumber -= 1
           curr = (columnNumber % 26)
           columnNumber //= 26
           res = chr(ord('A') + curr) + res
       
       return res