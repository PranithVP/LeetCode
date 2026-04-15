class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr_target, curr_combo):
            if curr_target == 0:
                res.append(curr_combo[:])
                return
            elif curr_target < 0 or i >= len(candidates):
                return
            else:
                curr_combo.append(candidates[i])
                dfs(i, curr_target-candidates[i],curr_combo)
                curr_combo.pop()
                dfs(i+1, curr_target, curr_combo)


        dfs(0, target, [])
        return res