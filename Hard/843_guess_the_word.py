# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def num_match(w1, w2):
            count = 0
            for i in range(6):
                if w1[i] == w2[i]:
                    count += 1
            return count
        
        def most_common_word():
            freq = [[0] * 26 for _ in range(6)]
            for w in words:
                for i in range(len(w)):
                    freq[i][ord(w[i]) - ord('a')] += 1
            
            max_score_word = ""
            max_score = float('-inf')

            for w in words:
                score = 0
                for i in range(len(w)):
                    score += freq[i][ord(w[i]) - ord('a')]
                if score > max_score:
                    max_score_word = w
                    max_score = score
            
            return max_score_word

            
        def remove_invalid(lst, guess, expected_match):
            updated = []
            for word in lst:
                if num_match(word, guess) == expected_match:
                    updated.append(word)
            
            return updated

        while True:
            curr_word = most_common_word()
            curr_matches = master.guess(curr_word)
            
            if curr_matches == 6:
                return curr_word
            
            words = remove_invalid(words, curr_word, curr_matches)

            