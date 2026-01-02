def isAnagram(self, s: str, t: str) -> bool:
    d = dict()

    if len(s) != len(t):
        return False

    for a, b in zip(s, t):
        d[a] = d.get(a, 0) + 1
        d[b] = d.get(b, 0) - 1
    
    for k in d:
        if d[k] != 0:
            return False
    return True