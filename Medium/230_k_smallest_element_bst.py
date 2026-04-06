# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, count):
            if count >= k:
                return (node, count)
            if count < k and node.left:
                res, count = dfs(node.left, count)
            if count < k and node:
                res, count = node, count+1
            if count < k and node.right:
                res, count = dfs(node.right, count)
            return (res, count)
        
        
        return dfs(root, 0)[0].val
