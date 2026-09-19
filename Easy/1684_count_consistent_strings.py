class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(ch for ch in allowed)
        count = 0
        
        for word in words:
            for ch in word:
                if ch not in allowed:
                    count -= 1
                    break
            count += 1
        
        return count