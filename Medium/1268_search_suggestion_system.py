class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
    
    def insert(self, word):
        curr = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = Trie()
            curr = curr.children[idx]
        curr.end = True
    
    def firstThree(self, word):
        res = []

        def dfs(t, path):
            if len(res) == 3:
                return
            
            if t.end:
                res.append(path)
            
            for i in range(26):
                if t.children[i]:
                    dfs(t.children[i], path + chr(ord('a') + i))

        curr = self
        count = 0
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                break
            curr = curr.children[idx]
            count += 1
        if count == len(word):
            dfs(curr, word)
        return res



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        res = []

        for product in products:
            t.insert(product)
        
        prefix = ""
        for ch in searchWord:
            prefix += ch
            res.append(t.firstThree(prefix))
        
        return res