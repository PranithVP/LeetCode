class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionary = set(dictionary)
        res = []
        words = sentence.split()
        for elem in words:
            found = False
            curr = ""
            for ch in elem:
                curr += ch
                if curr in dictionary:
                    res.append(curr)
                    found = True
                    break
            if not found:
                res.append(curr)
        
        return ' '.join(res)