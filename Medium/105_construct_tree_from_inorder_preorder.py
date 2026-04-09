# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {v: i for i, v in enumerate(inorder)}
        self.pre_i = 0

        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_i]
            self.pre_i += 1

            root = TreeNode(root_val)
            pivot = d[root_val]

            root.left = dfs(left, pivot-1)
            root.right = dfs(pivot+1, right)

            return root
        
        return dfs(0, len(inorder)-1)

