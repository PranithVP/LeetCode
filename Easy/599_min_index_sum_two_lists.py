class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}

        for i in range(len(list1)):
            if list1[i] not in d:
                d[list1[i]] = i
        
        curr_min = float('inf')
        res = []

        for i in range(len(list2)):
            if list2[i] in d:
                if d[list2[i]] + i < curr_min:
                    curr_min = d[list2[i]] + i
                    res = [list2[i]]
                elif d[list2[i]] + i == curr_min:
                    res.append(list2[i])
                
        return res

