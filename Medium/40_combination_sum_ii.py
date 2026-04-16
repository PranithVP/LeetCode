class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr_target, curr_combination):
            if curr_target == 0:
                res.append(curr_combination[:])
                return
            elif curr_target < 0 or i == len(candidates):
                return
            else:
                curr_combination.append(candidates[i])
                dfs(i+1, curr_target-candidates[i], curr_combination)
                curr_combination.pop()
                
                while i < len(candidates) - 1 and candidates[i+1] == candidates[i]:
                    i += 1

                dfs(i+1, curr_target, curr_combination)
        
        dfs(0, target, [])
        return res