class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        elem_to_index = {}
        for i, elem in enumerate(sorted(score, reverse=True)):
            elem_to_index[elem] = i
        
        for i in range(len(score)):
            score[i] = str(elem_to_index[score[i]] + 1)
            if score[i] == "1": score[i] = "Gold Medal"
            if score[i] == "2": score[i] = "Silver Medal"
            if score[i] == "3": score[i] = "Bronze Medal"

        return score


