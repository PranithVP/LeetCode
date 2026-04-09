# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        curr_max = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            nonlocal curr_max
            left_path = max(0, dfs(node.left))
            right_path = max(0, dfs(node.right))

            curr_max = max(curr_max, left_path + node.val + right_path)
            return max(node.val + left_path, node.val + right_path)
        
        dfs(root)
        return curr_max