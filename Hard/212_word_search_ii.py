class Trie:
    def __init__(self):
        self.children = {}
        self.word = None
    
    def insert(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_trie = Trie()
        for word in words:
            word_trie.insert(word)
        
        matches = set()

        def dfs(curr_trie, r, c):
            if not 0 <= r < len(board) or not 0 <= c < len(board[0]) or board[r][c] == '#':
                return
                
            curr_char = board[r][c]
            if curr_char not in curr_trie.children:
                return

            curr_trie = curr_trie.children[curr_char]
            if curr_trie.word:
                matches.add(curr_trie.word)
                curr_trie.word = None
            
            board[r][c] = '#'
            dfs(curr_trie, r+1, c)
            dfs(curr_trie, r, c+1)
            dfs(curr_trie, r-1, c)
            dfs(curr_trie, r, c-1)
            board[r][c] = curr_char
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(word_trie, r, c)

        return list(matches)