class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fixed_dict = dict()

        for ch in s1:
            fixed_dict[ch] = fixed_dict.get(ch, 0) + 1

        d = fixed_dict.copy()

        i = 0
        missing = len(fixed_dict)
        for j in range(len(s2)):
            if s2[j] in d:
                d[s2[j]] -= 1
                while d[s2[j]] < 0:
                    d[s2[i]] += 1
                    if d[s2[i]] == 1:
                        missing += 1
                    i += 1
                if d[s2[j]] == 0:
                    missing -= 1
                if (missing <= 0) and ((j - i + 1) == len(s1)):
                    return True
            else:
                i = j + 1
                d = fixed_dict.copy()
                missing = len(fixed_dict)
        return False
            
