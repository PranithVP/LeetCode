class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        d = {}

        for ch in chars:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

        for word in words:
            good = True
            d2 = d.copy()

            for ch in word:
                if ch not in d2:
                    good = False
                else:
                    d2[ch] -= 1
                    if d2[ch] < 0:
                        good = False
                        break
            if good: total += len(word)
        return total