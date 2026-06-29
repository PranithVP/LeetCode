from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        hand.sort()

        for i in range(len(hand)):
            if hand[i] not in freq:
                continue
            
            start = hand[i]
            freq[hand[i]] -= 1
            if freq[hand[i]] == 0:
                del freq[hand[i]]

            for j in range(1, groupSize):
                if hand[i] + j in freq:
                    freq[hand[i] + j] -= 1
                    if freq[hand[i] + j] == 0:
                        del freq[hand[i] + j]
                else:
                    return False

        return True
            

