class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chars = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()

        for word in words:
            curr = ""
            for ch in word:
                curr += chars[ord(ch) - ord('a')]
            res.add(curr)

        return len(res)