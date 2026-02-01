class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        encounteredSegments = 0
        encounteredOne = False

        for ch in s:
            if ch == '0':
                encounteredOne = False
            else:
                if encounteredOne:
                    continue
                else:
                    encounteredOne = True
                    encounteredSegments += 1
        
        return encounteredSegments <= 1
