class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        set_x, set_y, set_z = set(), set(), set()

        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                set_x.add(a)
                set_y.add(b)
                set_z.add(c)
        
        return x in set_x and y in set_y and z in set_z
