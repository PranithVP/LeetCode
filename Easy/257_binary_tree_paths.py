# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(curr, path):
            if not curr:
                return

            if len(path) > 0:
                path += '->' + str(curr.val)
            else:
                path = str(curr.val)

            if not curr.left and not curr.right:
                res.append(path)
                return
            
            dfs(curr.left, path)
            dfs(curr.right, path)
            
        dfs(root, "")
        return res
