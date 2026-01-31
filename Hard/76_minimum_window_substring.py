class Solution:
    def minWindow(self, s: str, t: str) -> str:
        curr, curr_len = "", float("inf")
        d = dict()

        for ch in t:
            d[ch] = d.get(ch, 0) + 1

        missing, i = len(d), 0

        for j in range(len(s)):
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    missing -= 1

                if missing <= 0:
                    while i <= j:
                        if s[i] not in d:
                            i += 1
                        elif d[s[i]] < 0:
                            d[s[i]] += 1
                            i += 1
                        else:
                            break
                    if (j - i + 1) < curr_len:
                        curr, curr_len = s[i:j+1], (j - i + 1)
        return curr