from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []

        row1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        row2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        row3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])

        for word in words:
            og = word
            word = word.lower()
            row_num = 0
            if word[0] in row1:
                row_num = 1
            if word[0] in row2:
                row_num = 2
            if word[0] in row3:
                row_num = 3

            invalid = False
            for ch in word[1:]:
                if row_num == 1:
                    if ch not in row1:
                        invalid = True
                        break
                if row_num == 2:
                    if ch not in row2:
                        invalid = True
                        break
                if row_num == 3:
                    if ch not in row3:
                        invalid = True
                        break
            if not invalid: res.append(og)
        
        return res
