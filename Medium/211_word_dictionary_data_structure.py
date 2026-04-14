class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = WordDictionary()
            curr = curr.children[ch]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(curr, i):
            if i == len(word):
                return curr.end
                    
            ch = word[i]
            if ch == '.':
                return any([dfs(curr.children[elem], i+1) for elem in curr.children])
            else:
                if ch not in curr.children:
                    return False
                return dfs(curr.children[ch], i+1)

        return dfs(self, 0)
