from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace('.', ' ')
        paragraph = paragraph.replace(',', ' ')
        paragraph = "".join(a for a in paragraph if a.isalnum() or a == ' ').lower()
        words = [a for a in paragraph.split() if a not in banned]
        count = Counter(words)
        return max(count.items(), key=lambda x: x[1])[0]