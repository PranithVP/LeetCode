class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides = [0, 0, 0, 0]

        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total // 4
        matchsticks.sort(reverse=True)

        def dfs(i):
            seen = set()

            if i == len(matchsticks):
                return target == sides[0] == sides[1] == sides[2] == sides[3]
            
            for s in range(4):
                if sides[s] in seen:
                    continue
                seen.add(sides[s])

                if sides[s] + matchsticks[i] <= target:
                    sides[s] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[s] -= matchsticks[i]

            return False
        
        return dfs(0)
