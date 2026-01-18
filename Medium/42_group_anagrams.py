from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = defaultdict(list)
    for word in strs:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        d[tuple(freq)].append(word)
    
    return list(d.values())