class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {order[i]: i for i in range(len(order))}

        for i in range(len(words)-1):
            first, second = words[i], words[i+1]
            decided = False
            for j in range(min(len(first), len(second))):
                if d[first[j]] < d[second[j]]:
                    decided = True
                    break
                elif d[first[j]] > d[second[j]]:
                    return False
            if not decided and len(first) > len(second):
                return False
        
        return True