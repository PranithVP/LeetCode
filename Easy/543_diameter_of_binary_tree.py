# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depth = {}

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left not in self.depth:
            self.depth[root.left] = self.maxDepth(root.left)
        if root.right not in self.depth:
            self.depth[root.right] = self.maxDepth(root.right)

        return max(self.depth[root.left] + self.depth[root.right], 
        self.diameterOfBinaryTree(root.left), 
        self.diameterOfBinaryTree(root.right))
    
    def maxDepth(self, root):
        if not root:
            return 0

        if root.left not in self.depth:
            self.depth[root.left] = self.maxDepth(root.left)
        if root.right not in self.depth:
            self.depth[root.right] = self.maxDepth(root.right)
        
        return 1 + max(self.depth[root.left], self.depth[root.right])